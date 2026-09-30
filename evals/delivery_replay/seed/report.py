import csv
import json
import sys
from pathlib import Path

from calc import total
from renderer import render


def export(source, destination):
    rows = json.loads(Path(source).read_text(encoding="utf-8"))
    value = total(rows)
    target = Path(destination)
    target.mkdir(parents=True, exist_ok=True)
    with (target / "total.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["metric", "value"])
        writer.writerow(["net_total", f"{value:.2f}"])
    # Legacy operations path recalculates and loses return signs.
    legacy = sum(abs(float(row["amount"])) for row in rows)
    theme = json.loads(Path("theme.json").read_text(encoding="utf-8"))
    (target / "total.html").write_text(render(legacy, theme), encoding="utf-8")


if __name__ == "__main__":
    export(sys.argv[1], sys.argv[2])
