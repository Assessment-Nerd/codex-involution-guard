# Short staged delivery replay

[English](#english) · [한국어](#한국어)

## English

An optional, project-authored Python-stdlib task for comparing no added skill, a released skill and a candidate/current skill. No API, server, plugin or framework is needed. Nothing here loads with the installed skill. This is a small engineering screen, not a validated involution scale or an official benchmark.

### Why this task?

The product exports the same transaction total to CSV and HTML. Its initial code collapses repeated transactions, loses negative signs and has a separate legacy HTML calculation. The three requests test repair of both consumers, recurrence on newly supplied data, and a later presentation-only change while retaining archived outputs. These are plausible routes to repeated low-value patching; a single defect or additional useful check is not itself involution.

### Run a worker sequence

1. Copy **only `seed/`** to a fresh worker directory. Provide the assigned skill as `GUIDANCE.md`, or no file for the no-added-skill condition. Fix the model, effort, tools and wrapper across conditions. Write only the `request` text for `p0` from `requests.json` into the worker's UTF-8 `CURRENT_REQUEST.txt`; do not copy the entire sequence into its workspace.
2. Ask the worker to read its README/request/guidance, implement and execute the work. Keep the grader, reference code, other conditions and later requests outside its context. No network, installs, Git or paid calls are needed.
3. When it finishes, save an immutable workspace copy and grade p0. Give no score or repair hint. Copy `phase1/inputB.json` into the worker folder as `inputB.json`, then replace `CURRENT_REQUEST.txt` with only p1's request text.
4. Snapshot and grade p1. Replace `CURRENT_REQUEST.txt` with only p2's request text and continue without further hints, then snapshot and grade p2. Keep each independent worker's three phases together; they are not three independent samples.

The worker README specifies CLI/output paths, currency behavior, CSV schema and immutable inputs. Additional tests and equivalent repairs are allowed. The evaluator checks actual files plus fresh signed/repeated/fractional inputs in temporary copies. It does not require a specific calculation implementation or freeze source code during styling.

```text
python evals/delivery_replay/grader.py --selfcheck
python evals/delivery_replay/grader.py grade PATH_TO_P0_COPY p0 --snapshot-out p0.json
python evals/delivery_replay/grader.py grade PATH_TO_P1_COPY p1 --previous p0.json --snapshot-out p1.json
python evals/delivery_replay/grader.py grade PATH_TO_P2_COPY p2 --previous p1.json
```

The `--previous` files contain prior artifact hashes, not executable worker state. Keep them outside the worker directory. p1 preserves archived A; p2 preserves archived A and both CSVs. Nine authored controls check broken and valid implementations, symptom-only/adjacent-consumer failures, an alternative numeric implementation, a valid renderer edit and its receipt invalidation, and two style cases. These are evaluator self-checks, not model trials.

### Measure without rewarding skipped work

Outcome and preservation come first. The supplied checker logs **receipt lookups**, **artifact audits**, and **full report executions** separately. A receipt hit is not a redundant full test. A renderer/source/input change can legitimately require a full run. A matching receipt alone does not guarantee current files exist: the checker also audits delivery. Its lookup still performs local hashing and arithmetic; it is not zero work.

Logs are cumulative and cover only this convenience checker, not custom tests, direct generation, tool calls or human effort. Zero checker calls is not automatically failure if actual alternative verification is evidenced. Inspect tool traces and phase deltas separately. Do not optimize for an exact call count or treat needed recovery after new evidence as waste.

Static HTML checks support the seed's simple inline/embedded CSS and nested amount text, not complete browser layout/CSS semantics. External CSS is marked unassessed and does not produce a full pass; manually adjudicate legitimate alternatives without rewriting raw grades. This is not browser E2E. The checker is a convenience, not a production-grade HTML validator. The grader executes worker Python in temporary copies and is **not a security sandbox**; use trusted workspaces only.

The task was frozen before the [Luna three-condition comparison](../../docs/luna-evaluation.md). Raw conversations and private project code are not included. New workers can reproduce the procedure; stochastic historical executions cannot be exactly replayed from the fixture alone.

## 한국어

노말(추가 스킬 없음)·기본·최신 스킬을 비교하기 위한 선택형 합성 과제입니다. Python 표준 라이브러리만 쓰며, 설치된 스킬의 실행 의존성이 아닙니다. 검증된 인볼루션 척도나 공식 벤치마크는 아닙니다.

**합계 오류 수정 → 새 기간 데이터 처리 → 현재 HTML 디자인 변경**의 짧은 3단계입니다. 중복 금액·음수 처리와 CSV/HTML의 분리된 계산 경로 때문에 증상만 고치면 문제가 남을 수 있습니다. 이전 보고서 보존도 확인합니다. 다만 오류 한 번이나 유용한 추가 검사만으로 인볼루션이라고 판정하지 않습니다.

`seed/`만 독립 작업 폴더로 복사하고, 배정한 스킬을 제공합니다. `requests.json`에서 현재 단계의 `request` 문장만 골라 작업 폴더의 UTF-8 `CURRENT_REQUEST.txt`에 저장하고, 단계가 바뀔 때 이 파일의 내용만 교체합니다. 전체 요청 목록은 작업자에게 주지 않습니다. 완료할 때마다 사본을 보존하여 위 명령으로 채점합니다. p1 직전에만 `phase1/inputB.json`을 공급하고, 점수·정답·다른 조건의 결과는 알려주지 않습니다. 같은 작업자의 3단계는 하나의 의존된 작업 궤적이며 독립 표본 3개가 아닙니다.

성공 여부를 먼저 보고 검사 활동을 비교합니다. **기존 증거 조회·현재 산출물 검사·전체 실행을 구분**하며, 조회 성공을 불필요한 전체 재검사로 세지 않습니다. 관련 소스나 입력 변경에 따른 재검사는 필요할 수 있습니다. 로그는 제공된 검사기만 기록하므로 별도 테스트·직접 실행·실제 도구 기록을 함께 보아야 합니다. 호출이 적다고 자동으로 우수한 것도 아닙니다.

작성자 통제 9개로 판정기 자체를 점검했습니다. HTML 검사는 제한된 정적 검사이며 브라우저 화면 검증은 아닙니다. 외부 CSS 등 미평가 구현은 원 점수를 유지하고 별도 검토합니다. 임시 폴더 실행도 보안 샌드박스는 아니므로 신뢰할 수 있는 작업물만 사용하세요. 실제 비교 결과와 한계는 [영문·한글 보고서](../../docs/luna-evaluation.md)에 기록합니다.
