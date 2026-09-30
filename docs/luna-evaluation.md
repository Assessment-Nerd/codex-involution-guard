# Fast three-condition Luna evaluation

[English](#english) · [한국어](#한국어) · [Structured results](../evals/luna_results.json)

## English

### Outcome first

**The latest skill did not demonstrate an advantage.** Twelve independently started Luna workers compared no added skill, released v0.2.1, and the current 610-word skill. All repaired the short integration task's behavior. In a three-stage report task, no-skill and basic each completed both trajectories, while latest completed one of two: one worker restyled an archived report outside the current request. The other latest worker preserved it.

This is a small descriptive engineering screen, not evidence of general inferiority/superiority, equivalence or a causal psychological mechanism. The archive failure is real scope overreach, but one event does not establish involution or repeated self-reinforcing burden. **No new runtime wording, plugin or release was installed.** The improvement delivered by this cycle is a reusable fast-feedback test, clearer evaluation contracts and a preserved failure case—not a proven skill-performance improvement.

### Fixed comparison

| Condition | Supplied instructions |
| --- | --- |
| Normal / none | No added Involution Guard body; no `GUIDANCE.md` |
| Basic | Last tagged release, `v0.2.1` |
| Latest | Published source at `5054be8`, same 610-word runtime as `41b7bed` |

The rejected 652-word exploratory candidate from the previous cycle was **not** substituted for latest. Guidance hashes and individual outcomes are in the result file. Actual session metadata for all 12 workers records `PRO/gpt-6-luna` / `high`. Each initial worker had a fresh, non-inherited conversation. Followups stayed with that worker. The exact serving backend is unknown.

There were two preallocated repetitions per condition in each of two families. Order was fixed and rotated, not randomized: contract latest/none/basic then basic/latest/none; delivery none/basic/latest then latest/none/basic. Up to three workers ran concurrently. No outcome-driven replacements, repair hints or selective reruns were used. The second repetition was allocated before the first results. Tasks, guidance and evaluators were frozen before their respective workers; the report task received preflight corrections before any delivery worker started.

Shared default instructions, the available skill catalog and platform policies remained in all arms. This is not a policy-free control or a test of natural skill discovery. Tool traces and guidance-file hashes were checked; no outside installed-skill-body read was observed. Directory boundaries were instructions, not an enforced security sandbox.

### Two short tasks

1. **Integration recovery:** reuse the [contract replay](../evals/contract_replay/README.md). The initial program answers correctly only after recovering information omitted earlier. Workers must reduce this repeated recovery without losing requested outputs, source attribution, clarification or meaningful review. Seven behavioral probes include a registered neighboring capability and necessary fault recovery. Deterministic substitute-service calls are not live LLM cost or agent iteration counts.
2. **Repair → new data → presentation-only request:** build the [staged delivery replay](../evals/delivery_replay/README.md). CSV and HTML have duplicate/sign-related calculation defects and separate producer paths. P0 repairs and produces A; P1 supplies new B data while archiving A; P2 changes only current B's presentation. Fresh-input regeneration rejects symptom-only patches. Archived A and both CSVs must survive P2. There is no arbitrary retry/token cutoff or hidden requirement to use one implementation.

The report fixture's nine authored preflight controls accept complete and alternative repairs while rejecting raw/symptom-only/adjacent-consumer defects. They also cover renderer-source changes and basic style alternatives. The root reviewed outcome, developer and user-QC concerns before implementation; a separate Luna authored the fixture. This development review was not blinded.

### Observed effectiveness and time

| Condition | Contract behavioral success | Full report trajectories | Median contract time | Median report time, 3 phases |
| --- | --- | --- | --- | --- |
| None | 2/2 | 2/2 | 120.2 s | 176.9 s |
| Basic | 2/2 | 2/2 | 165.6 s | 210.1 s |
| Latest | 2/2 | 1/2 | 124.7 s | 256.0 s |

Contract raw composite scores differ from behavioral success; see the adjudication below. Report success means every phase's artifact/preservation checks passed, not perfect adherence to all experimental boundaries. Two non-product protocol deviations are listed separately.

Times are measured from each turn's start to its final response, summed across a report trajectory, excluding orchestration gaps between turns. They include tool and scheduling delays, not just inference. Actual contract runs took 117–178 seconds; report trajectories took 152–285 seconds, and the final presentation turn took 37–91 seconds. These support the feasibility of a short feedback cycle, **not a reliable model/skill speed ranking**. Two repetitions are insufficient for a stable estimate. Parent design, review and publication time are excluded.

All six contract workers achieved four substitute-service calls / zero avoidable service recoveries across two supported requests, retaining all seven behavioral controls. No-skill did this too; the code improvement cannot be attributed to the skill.

All six report workers repaired both producers and handled the new data. All had two successful full executions through the supplied checker across P0–P1 and zero additional full checker executions in P2. Receipt-hit counts across entire trajectories varied: none 3/1, basic 5/1, latest 2/3. A receipt lookup is **not** a full rerun and was not scored as wasted validation. Initial missing-artifact audits followed by successful generation are also not failed agent repairs.

These logs omit direct report runs and any other checks. Some workers generated first and then invoked a checker which regenerated on a missing receipt; others used the checker to generate directly. The trace audit retained that distinction. All directly regenerated B for styling; the failing worker also regenerated A. Thus zero full checker executions in P2 does not mean zero computation, zero unnecessary work, or automatic scope compliance.

### Failures, adjudication and boundary deviations

**Contract test-file ambiguity:** the frozen evaluator required byte-identical `tests.py`, while workers were told to preserve original tests and could add their own. Only c01 left that file byte-identical. Raw composite passes remain none 0/2, basic 0/2, latest 1/2. All seven product probes nevertheless passed for all six workers. Independent Luna inspection confirmed every original setup, assertion sequence and main guard remained. c02–c03 added separate methods; c04–c06 also appended assertions to an original method. A clear authority violation is not established by that ambiguous wording. Raw scores are not silently converted to passes. The public seed README now explicitly requires a separate file for additions **for future trials**; the grader code and historical scores are unchanged.

**Archived-output overreach:** d03/latest P2 changed A's HTML from gray/left to blue/right as well as updating B. It preserved numerical values and CSVs, but A was already archived and the request referred to the current report. A separate Luna reviewer, without condition mapping or guidance, inspected the requests, README and before/after artifacts and upheld the scope failure. This is substantive content change, not merely a hash-formatting discrepancy. The same worker had correctly preserved A at P1; its P2 handoff broadened the objective to both reports. That observation suggests a scope-state maintenance hypothesis, not proof that handoffs or this skill caused the mistake.

**Protocol deviations:** c04/basic ran one forbidden read-only `git status` command. d02/basic made an unnecessary read-only app artifact-inventory request outside the file task; it returned an empty list, exposing no peer artifacts. These are reported rather than hidden or equated with product failure. No worker network/API/install, peer-task read or paid call was observed in the audited tool calls. Other harmless missing-directory inspections and local checker activity remain in private traces; a successful artifact score does not mean every intermediate action was useful.

### What changed, and what did not

- Added the optional staged fixture with stateless snapshot grading, fresh-input probes and separate receipt/artifact/full-execution measures.
- Made the old contract fixture's byte-protection rule explicit prospectively.
- Published sanitized outcomes, configuration/hashes, cumulative session token counters and measured turn times. Counters include repeated/cached input and are not an API bill or initial context size. No new metered API calls were made; subscription consumption is not assumed free, and actual monetary cost is unknown.
- Kept the installed 610-word skill unchanged. The predeclared gate required a repeated valid failure before adding another candidate; archive overreach occurred once, not twice. No further task hunting or post-hoc candidate promotion was used.

The next narrowly testable hypothesis is **preserving active-versus-archived scope when the request changes**, not adding a general checklist. Before promoting a new instruction, reproduce that failure across predeclared variants and test a compact scope-boundary change against the unchanged skill on separate variants. Necessary broad propagation remains a control: a truly global request should still update all authorized consumers. A helper/plugin is justified only if an observed information or enforcement need exceeds what instructions can supply; this cycle did not establish that need.

### Reproduction and limits

Use the fixture READMEs and the frozen allocation/hashes in [results](../evals/luna_results.json). Hashes refer to the actual trial bytes; checkout line-ending conversion can change them without changing behavior. The delivery root README was rewritten for publication, but worker seed/code/inputs match the frozen files. The shared worker wrapper was the following, with only workspace/runtime paths substituted:

> Complete a bounded local coding task. Your sole workspace is WORKSPACE. Do not read/write other workspace files, parent history, installed skill files, other agents' work, evaluators or reference solutions. A supplied executable outside the workspace is allowed: PYTHON (use -X utf8 -B). No network, installs, Git, extra agents or paid calls. Read README.md and CURRENT_REQUEST.txt; if GUIDANCE.md exists, read and apply it unchanged; if absent, complete the task normally without adding skill instructions. Preserve supplied source/request/tests as instructed; add your own tests if useful. Implement and execute the requested work, not just a proposal. Maintain only the existing/local .codex-shared/HANDOFF.md if required for continuity. At completion report actual changes, checks and limitations; report any additional mandatory instruction/skill read that conflicted with the assigned-directory boundary. Do not explore parent directories to discover instructions.

Each delivery followup said to continue under the same boundaries, read the updated current request, use any new input in the workspace, and report changes/checks/limits. It supplied no score, archive reminder or corrective hint. Immutable copies were graded before the next request. Fresh grader checks run outside worker context.

This procedure follows the task/outcome distinction in [OpenAI's skill-evaluation guidance](https://developers.openai.com/blog/eval-skills); [Luna documentation](https://developers.openai.com/api/docs/models/gpt-6-luna) informed the requested model setup. No upstream framework, code or benchmark dataset was imported. Private conversation history, machine paths, account identifiers and worker handoffs are not published. Historical stochastic runs cannot be exactly reconstructed from the public fixture alone. Static markup checks are not browser E2E, and no human study, long-running project burden, generalized cost saving or construct validity was measured.

## 한국어

### 결론

**최신 스킬의 우위는 확인되지 않았습니다.** Luna 작업자 12개를 독립적으로 시작하여 노말·기본 v0.2.1·최신 610단어 스킬을 비교했습니다. 단일 통합 과제는 세 조건 모두 기능 개선에 성공했습니다. 3단계 보고서 과제는 노말 2/2, 기본 2/2, 최신 1/2였습니다. 최신 한 작업자가 현재 B 보고서의 디자인을 바꾸면서 보관된 A까지 다시 만든 것이 실패 원인입니다. 다른 최신 작업자에서는 재현되지 않았습니다.

작은 기술 시험이므로 최신이 일반적으로 나쁘다거나, 스킬 때문에 오류가 났다고 단정할 수 없습니다. 범위 초과는 확인했지만 이것 하나만으로 지속적 인볼루션을 입증한 것도 아닙니다. 이번 성과는 **짧게 반복할 수 있는 평가 과제와 실제 실패 사례 확보**이지, 입증된 성능 도약이 아닙니다. 실행 스킬·플러그인·릴리스는 추가하지 않았습니다.

### 무엇을 어떻게 비교했나

기본은 마지막 공개 태그 v0.2.1, 최신은 비교 시작 시 저장소의 610단어 버전입니다. 이전에 기각한 652단어 후보는 제외했습니다. 실제 세션 설정은 모두 `PRO/gpt-6-luna / high`였고, 최초 문맥을 공유하지 않았습니다. 각 과제·조건당 두 번을 미리 배정했으며, 결과를 본 뒤 성공 사례만 다시 뽑지 않았습니다. 노말도 플랫폼 기본 지침과 스킬 목록은 유지하므로 완전히 무지침인 모델은 아닙니다.

- **반복 복구 과제:** 처음부터 최종 답은 맞지만 빠진 정보를 반복 복구하던 코드를 고칩니다. 세 조건 모두 필요한 검토를 유지하면서 대체 서비스 호출 10→4, 불필요한 서비스 복구 4→0을 달성했습니다. 노말도 같았으므로 이를 스킬 효과라고 할 수 없습니다.
- **3단계 보고서 과제:** 합계 오류 수정 → 새로운 기간 데이터 → 현재 HTML 디자인 변경입니다. CSV와 HTML의 누락, 새 입력에서의 재발, 이전 보고서 보존을 검사합니다. 과제 코드는 합성이며 비공개 프로젝트를 공개한 것이 아닙니다.

첫 과제는 작업당 약 **2–3분**, 보고서 3단계 합계는 약 **2.5–4.7분**, 마지막 디자인 요청은 약 **37–91초**였습니다. 턴 시작부터 종료까지의 실제 시간이며 단계 사이 대기·부모의 설계/검토 시간은 제외했습니다. 병렬 실행과 도구 지연이 섞여 있어 정밀한 속도 우열의 근거는 아닙니다. 단계·검사항목 수를 독립 표본 수로 부풀리지 않았습니다.

### 재검사와 실패는 구분했다

제공된 검사기의 전체 실행은 모든 보고서 작업자에서 처음 두 단계 합계 2회, 디자인 단계 추가 0회였습니다. 그러나 **기존 증거 조회는 전체 재검사가 아니며**, 직접 보고서 재생성도 별도 작업입니다. 실제로 최신의 실패 작업자는 검사기 전체 실행 없이도 이전 보고서를 다시 만들었습니다. 호출 수 하나만 보면 이 오류를 놓칩니다. 검사 로그·실제 명령·최종 산출물을 함께 확인했습니다.

기존 통합 과제의 채점기는 테스트 파일 바이트가 같아야 한다고 요구했지만 지시문은 ‘원래 테스트 보존’이라고만 했습니다. 5개 작업자가 원 검사를 유지하며 같은 파일에 검사를 추가했습니다. 따라서 원 종합 점수는 노말 0/2·기본 0/2·최신 1/2로 그대로 남기고, 세 조건 모두 기능 검사 2/2였다는 결과와 분리했습니다. 별도 Luna 검토로 원 assertion 보존을 확인했으며, 미래 시험에만 추가 검사 파일을 분리하라는 규칙을 명시했습니다.

반면 최신의 이전 보고서 수정은 별도 검토에서도 실제 범위 위반으로 확인됐습니다. 단순 해시 차이가 아니라 보관본의 색상·정렬을 바꿨습니다. 기본 조건의 읽기 전용 Git 상태 조회 1회와 불필요한 앱 첨부목록 조회 1회도 실험 경계 이탈로 기록했습니다. 후자는 빈 목록이었으며 다른 작업자의 결과를 노출하지 않았습니다.

### 다음 개선 방향

이번에는 선택형 [빠른 평가 과제](../evals/delivery_replay/README.md), 명확한 채점 계약, [조건별 결과](../evals/luna_results.json)를 추가했습니다. 스킬 본문은 유지했습니다. 미리 정한 ‘반복 확인된 실패 후 후보 개발’ 조건을 한 번의 범위 초과가 충족하지 않았기 때문입니다.

다음 가설은 **요청이 바뀔 때 현재 작업 대상과 보관·완료 대상을 구분해 유지하는가**입니다. 미리 정한 변형 과제에서 실패를 재현한 뒤, 짧은 범위 보존 지침을 별도 과제로 비교하는 것이 적절합니다. 정말 전체 변경을 요청했을 때 필요한 전파를 막지 않는 대조 과제도 있어야 합니다. 이번 결과만으로 장문의 규칙이나 플러그인이 필요하다고 판단하지 않았습니다.

토큰은 반복·캐시 입력을 포함한 세션 누적치이며 API 청구액이 아닙니다. 신규 종량제 API 호출은 없었지만 구독 사용량이 무료라고 가정하지 않았습니다. 실제 비용·인간 개입 시간·장기 프로젝트 부담·심리적 구성개념 타당성은 측정하지 않았습니다. 영어 설명을 먼저 두고, 원 실패와 평가 한계를 함께 공개합니다.
