import csv
import hashlib
import json
import re
import subprocess
import sys
from decimal import Decimal
from pathlib import Path


def key(source):
    digest = hashlib.sha256()
    for name in ("calc.py", "report.py", "renderer.py"):
        digest.update(Path(name).read_bytes())
    digest.update(Path(source).read_bytes())
    return digest.hexdigest()


def expected(source):
    rows = json.loads(Path(source).read_text(encoding="utf-8"))
    return sum((Decimal(row["amount"]) for row in rows), Decimal("0"))


def destination(source):
    name = Path(source).stem
    if name.lower().endswith("a"):
        name = "A"
    elif name.lower().endswith("b"):
        name = "B"
    return Path("output") / name


def artifact_ok(target, value):
    try:
        with (target / "total.csv").open(encoding="utf-8", newline="") as stream:
            rows = list(csv.reader(stream))
        html = (target / "total.html").read_text(encoding="utf-8")
        return (rows == [["metric", "value"], ["net_total", f"{value:.2f}"]] and
                re.search(rf"(?<![0-9]){re.escape(f'{value:.2f}')}(?![0-9])", html) is not None)
    except (OSError, ValueError):
        return False


def check(source):
    source = str(source)
    target = destination(source)
    receipt_path, log_path = Path("receipts.json"), Path("checks.jsonl")
    receipts = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.exists() else {}
    current_key = key(source)
    receipt = receipts.get(current_key)
    hit = bool(receipt and Decimal(str(receipt["total"])) == expected(source))
    with log_path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"event": "receipt_lookup", "result": "hit" if hit else "miss", "key": current_key}) + "\n")
    value = expected(source)
    artifacts_ok = artifact_ok(target, value)
    with log_path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"event": "artifact_audit", "result": "pass" if artifacts_ok else "fail", "key": current_key}) + "\n")
    if hit and artifacts_ok:
        print(json.dumps({"event": "receipt_lookup", "result": "hit", "artifact_audit": "pass", "key": current_key}))
        return 0
    reason = "evidence_miss" if not hit else "artifact_repair"
    result = subprocess.run([sys.executable, "report.py", source, str(target)], capture_output=True)
    passed = result.returncode == 0 and artifact_ok(target, value)
    event = {"event": "full_execution", "result": "pass" if passed else "fail", "key": current_key}
    event["reason"] = reason
    with log_path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(event) + "\n")
    if passed and not hit:
        receipts[current_key] = {"input": source, "total": f"{expected(source):.2f}"}
        receipt_path.write_text(json.dumps(receipts, indent=2), encoding="utf-8")
    print(json.dumps(event))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(check(sys.argv[1]))
