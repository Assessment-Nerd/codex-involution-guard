# Learning from actual work

[English](#english) · [한국어](#한국어)

## English

### Decision — 2026-09-30

The bounded development cycle is complete. **No incremental skill benefit was demonstrated.** Keep the 610-word skill at commit 41b7bed. The exploratory 652-word candidate is not installed. No plugin, background collector, new runtime dependency, paid API trial or release was added.

What did improve is the evaluation: actual-use traces became executable tasks with delayed follow-ups, source-protection controls and independent review. A reproducible code repair reduced substitute-service calls from 10 to 4 across two requests while retaining necessary review. That is an improvement to task code by the **existing** skill, not evidence that the new instructions improve agents.

[Machine-readable record](../evals/trajectory_results.json) · [Public offline fixture](../evals/contract_replay/README.md) · [Actual worker patch](../evals/contract_replay/observed-worker.patch).

### What the usage records taught us

The [earlier workflow pilot](workflow-evaluation.md) explicitly told workers much of the desired repair strategy. It remains a regression test, not a strong test of discovering drift. This cycle used targeted private records from development, research/learning and literature work. It is not a representative audit of all use.

Three recurring candidates were separated:

- An accepted obligation disappears between the original request, a plan, implementation and handoff.
- Information is lost between an existing capability registry, the compact request representation and independent review. Repeated downstream recovery can produce a correct final answer while leaving this cause intact.
- Evidence or item identity changes at a boundary: a stale view is certified as current, or search hits and access states are confused with unique works and stronger evidence.

These are observable engineering hypotheses, not newly validated psychological constructs. A useful later bug fix is not automatically involution. Counts of fixes, files or tests do not decide whether the project progressed.

One historical interpretation was corrected: research lessons and web work were explicitly authorized **in parallel**. Starting web was not a forbidden phase transition. The concern was the uncancelled lesson obligation disappearing from a next-step plan, not proof of permanent final omission.

### Design, intervention and controls

We reconstructed pre-correction states, checked authored reference solutions, then ran the current skill. All three compact discovery families were ceilings. Rather than hide successes, invent harder traps or lower the model, an independent methods review recommended one bounded richer-context comparison.

This explicitly amended the initial gate requiring a reproduced baseline failure before any new candidate: the candidate was **exploratory**, based on historical evidence, not an already-supported intervention.

It added a parallel-work clarification and replaced one shared-cause paragraph with a bounded instruction to trace an obligation through representation, execution, review and delivery, find its first loss, repair the existing owner, and check changed/unchanged cases. It preserved safety and authority boundaries. Exact wording and hashes are in the result record.

The richer pair received the same 44 chronological user/assistant messages available before the revealing correction, the same accepted plan, task, Python surrogate and tools. Candidate started first, baseline second: fixed order, not randomized or counterbalanced. It is not a full-session replay of the original R application.

A different literature case was prepared independently and kept unseen by the implementer until candidate freeze. It used fictional sources, a delayed source update, then an explicit request to stop expanding scope. Outputs were frozen at each stage. A reviewer scored condition-masked copies with guidance and private reports removed, without being told the mapping. This reduces direct label bias; prose can still reveal cues. The reviewer and workers were AI agents using the same nominal model, not independent human raters.

### Results

| Task family | Execution and observation | Interpretation |
| --- | --- | --- |
| Historical review → save → output | Two current-skill runs each met 8/8 frozen checks at initial and neutral-follow-up stages. Fresh-context continuations made no product edits and qualified their evidence. | Existing skill already passes; two trajectories, not 16 independent samples. |
| Compact research + teaching → web | Current skill delivered both obligations; HTTP/process-restart checks passed. One separate Chrome smoke path confirmed pending work, help attribution and cached redisplay. | Successful baseline; not a new-skill or human-learning effect. |
| Interpretation → execution → review | Current-skill worker retained all 7 quality/control cases; supported substitute calls 10→4 and avoidable recoveries 4→0. Wrong-target injection still required repair and re-review. | Actual code improvement; not live-model speed, money or incremental skill gain. |
| Richer chronological context, A/B | Both delivered web and teaching. The frozen grader failed both; independent post-run diagnostics found implementation-specific grader defects, described below. | No observed advantage on inspected semantic requirements; not a clean preregistered passing A/B. |
| Separate literature continuation, A/B | Both met artifact criteria at collection, delayed update/synthesis and explicit narrowing. Both preserved the 3 earlier outputs byte-for-byte in the narrow phase. Candidate had one minor “5 studies” wording slip despite correctly cataloging 4 papers + 1 vendor source. | No primary artifact separation; retain the candidate's prose defect rather than call both flawless. |

The field continuations found additional useful repairs (no-op save/retry behavior, cancelled-candidate output and receipt identity). Those were not failures of the original acceptance checks, and their additional tests are not automatically waste. Fresh-context workers ran 8 versus 22 tests on different evolved artifacts; this is not comparable efficiency evidence.

The literature reviewer assessed artifacts, not withheld final messages or tool behavior. A separate trace audit confirmed execution boundaries; the implementer inspected saved completion reports and found appropriately limited claims. Do not merge these into a wholly blinded full-trajectory assessment.

#### Frozen grader failures, preserved

| Rich-context arm | Original web result | Original lesson result | Subsequent diagnosis |
| --- | --- | --- | --- |
| A: existing skill | Pass | Fail | Valid variation/application steps did not use the grader's preferred kind vocabulary. |
| B: candidate | Fail | Fail | Same vocabulary issue; restore also renewed only an opaque approval ID, breaking exact-dictionary equality. |

The task did not prescribe those kind values or an immutable approval ID. Independent dynamic checks confirmed substantive state preservation, valid lesson references, retained help history and one research calculation after approval. B rejected an explicit stale token and accepted the current one. Those are legitimate alternatives, not missing user outcomes. Both richer-arm browser render/click journeys remain unverified.

The original grader and scores were not overwritten. The diagnostic checks were created **after** seeing the failure and are reported as adjudication, not a second set of successful model trials. Workers received no targeted repair hints, and were not asked to rename valid steps merely to satisfy the evaluator. No further neutral continuation was sent after the original scope was found delivered.

### What is reusable now

The [public fixture](../evals/contract_replay/README.md) contains only project-authored synthetic code, a deidentified request, an evaluator, authored controls and the observed worker patch. It accepts a legitimate full-representation-first repair and rejects a symptom-only patch that fails a newly registered neighboring capability. That neighbor is a prospective probe, not an extra historical incident. Necessary review and ambiguity controls are retained.

The public evaluator was also improved **after** the model trial. Its original injected-fault rule required a particular service-repair path. Revision v2 accepts local correction when an actual clean review covers the full original request and evidence, and checks protected request/tests separately from runtime file stability. Ten authored controls pass their expected acceptance/rejection, including valid local correction and invalid ignored review. Rescoring the same worker/patch retains 4 calls / 0 service recoveries; no new model A/B was run. Original frozen hashes and scores remain in the result record. Counts exclude local computation and evaluator-only audits; they are not total work.

The original private application, conversations and reference-rich history packets are not redistributed. Thus the full historical trials cannot be reproduced solely from the public repository. Separate directories and read restrictions are experimental instructions, **not a security sandbox**. The fixture is optional development tooling, not loaded by the installed skill.

Development principles were informed by the [OpenAI agent improvement loop](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop), [Anthropic agent-evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [tau2-bench](https://github.com/sierra-research/tau2-bench) and [SWE-bench](https://github.com/SWE-bench/SWE-bench): trace-derived tasks, separation of inputs/interaction/grading, and executable outcome checks. No upstream code, benchmark dataset, paid evaluation service or framework was imported or executed.

### Limits and next decision

Eight initial workers were used across these families, plus two fresh field continuations. Subchecks and dependent phases are not additional independent samples. Recorded primary worker metadata was gpt-6-astra / ultra; provider and exact backend revision were unavailable. No new metered API calls were made; subscription usage is not assumed free. Tokens, comparable elapsed time, cost and real human rescue effort were not measured.

Workers were explicitly required to read their assigned skill and relevant context. These trials do **not** test natural skill discovery, timely invocation or recovery of missing context. Successful reconstruction does not establish that a skill would have prevented the original event, nor that the original event was caused by low shared cognition. Historical focal turns also used the same nominal model/effort, not necessarily the same backend or working conditions.

Failed attempts are retained: both rich-context workers initially had rejected handoff patches; candidate also corrected a test indentation error. Evaluator setup hit an unusable Python alias, an expired worker preview process, and a patch command that skipped a nested path; actual runtime/output checks exposed these and they were corrected. None is scored as a skill advantage. No general superiority, equivalence, construct validity, cost saving or “quantum leap” is established.

The next useful hypothesis is **information availability at the decision boundary**, not another unconditional checklist. A future authorized local test should compare existing handoff access with on-demand retrieval of one accepted obligation and its applicable evidence on the same observed failure. First establish whether context was unavailable, not retrieved, or retrieved but ignored. A retrieval helper targets the first two; the third could call for instructions, interface changes or enforceable checks. None of those tool needs was established here. This is a next-test proposal, not a proven diagnosis or an installed background monitor.

The bounded cycle stops here rather than searching indefinitely for a favorable result. Keep the short runtime, the negative result, the reusable task and the improved evaluation discipline.

## 한국어

### 결론 — 2026-09-30

이번 한정된 개발·평가 사이클은 마쳤습니다. **새 스킬의 추가 성능 향상은 입증하지 못했습니다.** 현재 610단어 스킬은 유지하고, 652단어 실험 후보는 설치하지 않았습니다. 플러그인·백그라운드 수집기·필수 실행 의존성·새 유료 API 시험·릴리스도 추가하지 않았습니다.

발전한 것은 평가 방식입니다. 실제 사용 기록을 실행 가능한 과제로 바꾸고, 후속 요청·범위 축소·보호 자료·독립 검토를 시험했습니다. 코드에서는 두 요청의 대체 서비스 호출을 10회에서 4회로 줄이고 필요한 검토를 유지했습니다. 다만 **기존 스킬도 해낸 코드 개선**이므로 새 스킬의 효과라고 부르지 않습니다.

[결과 원장](../evals/trajectory_results.json) · [직접 실행할 합성 과제](../evals/contract_replay/README.md) · [실제 작업자 수정 패치](../evals/contract_replay/observed-worker.patch).

### 사용 기록에서 배운 것

앞선 과제들은 고쳐야 할 전략을 너무 직접 알려주었습니다. 이번에는 개발·연구 및 학습·문헌 정리 기록에서 나중의 지적이 나오기 전 상태를 복원했습니다. 모든 사용 기록을 대표하는 표본은 아닙니다.

중요한 후보는 세 가지였습니다.

- 원래 합의한 요구가 계획·구현·인계 중간에서 사라진다.
- 지원 기능과 금지 조건, 선택한 분석의 근거가 중간 표현에서 빠져 뒷 단계가 반복 복구한다. 최종 답이 맞아도 공통 원인이 남을 수 있다.
- 자료·증거의 정체성이 경계에서 바뀐다. 오래된 화면을 현재 검토로 인증하거나 검색 건수·초록·전문을 혼동한다.

이는 관찰 가능한 공학적 가설이지 검증된 심리적 구성개념은 아닙니다. 나중에 유용한 버그를 더 고쳤다는 이유만으로 인볼루션으로 세지 않았습니다.

이전 해석도 바로잡았습니다. 원래 사용자는 수업과 웹의 **병렬 진행을 승인**했습니다. 웹을 시작한 것이 순서 위반은 아니었습니다. 검토 대상은 다음 계획에서 취소되지 않은 수업 의무가 빠진 것이며, 최종 결과에서도 반드시 누락됐다는 뜻은 아닙니다.

### 무엇을 개발하고 비교했나

해결 가능한 기준 구현을 먼저 확인한 뒤 현재 스킬을 시험했습니다. 세 가지 짧은 발견 과제는 모두 기존 스킬이 통과했습니다. 성공을 버리거나 억지 함정을 추가하지 않고, 독립 방법론 검토에 따라 실제 시간순 맥락을 더 보존한 비교를 한 번 추가했습니다.

처음의 “재현된 기존 실패가 있어야 후보 개발” 원칙은 이 시점에 명시적으로 수정했습니다. 후보는 이미 효과가 확인된 개입이 아니라 **탐색적 구현**입니다.

후보는 기존 공통 원인 문단 하나를 바꿨습니다. “요구가 표현→실행→검토→전달 중 어디서 처음 빠졌는지 한 경로를 추적하고, 기존 담당 위치를 고치며, 변경·무변경 사례를 확인하라”는 내용입니다. 합의한 병렬 작업에 임의의 선후관계를 강요하지 말라는 문장도 추가했습니다. 안전·권한 제한은 유지했습니다.

실제 사후 지적 전의 메시지 44개, 당시 계획, 동일한 과제·코드·도구를 A/B 모두에게 주었습니다. 후보를 먼저 시작한 고정 순서이며 무작위화·교차배치는 하지 않았습니다. 원래 R 앱과 전체 세션을 그대로 복원한 것은 아닙니다.

별도 문헌 과제는 다른 검토자가 작성하고, 후보 동결 전에는 구현자가 정답·결과를 보지 않았습니다. 최초 수집→새 근거 반영 및 통합 학습자료→명시적 범위 축소 순서로 진행했습니다. 단계마다 결과를 보존하고, 채점자에게 스킬과 A/B 대응을 숨긴 복사본을 줬습니다. 표현으로 조건을 짐작할 가능성은 남으며, 동일 계열 AI 검토이지 독립적인 인간 평가가 아닙니다.

### 실제 결과

| 과제 | 결과 | 해석 |
| --- | --- | --- |
| 검토·저장·출력 | 기존 스킬 두 실행 모두 최초·후속 8/8. 새 문맥 재개에서도 제품 수정 없이 근거에 맞게 설명 | 기존 스킬이 이미 잘함. 검사 16개를 독립 표본으로 세지 않음 |
| 연구·수업·웹 연결 | 기존 스킬이 두 의무를 구현. HTTP·재시작 검사와 별도 Chrome 일부 경로 확인 | 새 스킬이나 실제 학습 효과의 증거는 아님 |
| 해석·실행·검토 연결 | 품질·통제 7항목 유지, 호출 10→4, 불필요한 복구 4→0. 진짜 오류에는 수정·재검토 유지 | 코드 개선. 실제 모델 속도·비용·새 지침 효과와 구분 |
| 실제 시간순 맥락 A/B | 두 버전 모두 웹과 수업 구현. 원 채점기는 둘 다 실패 처리했으나, 독립 사후 검토에서 과도한 구현 방식 제한 확인 | 의미상 요구에서 우월성 관찰 안 됨. 사전 기준으로 깔끔하게 통과한 비교라고 포장하지 않음 |
| 별도 문헌 작업 A/B | 두 버전 모두 최초 정리·근거 갱신·범위 축소 산출물 기준 충족. 마지막에는 기존 결과 3개 해시 유지 | 주요 차이 없음. 후보는 한 문장에서 논문 4개+공급자 자료 1개를 “연구 5개”로 부른 경미한 오류도 남김 |

저장 과제의 후속 작업은 무변경 저장·재시도·취소된 후보·검토 증빙의 추가 문제를 실제로 고쳤습니다. 원래 검사 실패도, 단순한 재검사 낭비도 아닙니다. 새 문맥 작업자가 서로 다른 결과물에 실행한 8개와 22개 시험은 비용 절감 비교로 쓰지 않았습니다.

문헌 블라인드 검토는 산출물만 평가했습니다. 실행 기록은 별도 감사, 저장된 완료 보고는 구현자가 비맹검으로 확인했습니다. 이를 전 과정 블라인드 평가라고 합치지 않습니다.

### 채점기도 검증해야 했다

원점수는 A가 웹 통과·수업 실패, B가 웹·수업 모두 실패였습니다. 하지만 수업 실패는 과제에 지정하지 않은 단계 이름을 채점기가 요구했기 때문이었습니다. B의 웹 실패는 복원할 때 오래된 승인을 무효화하도록 승인 ID만 갱신했는데 상태 전체가 바이트처럼 같아야 한다고 요구했기 때문입니다.

독립 검토자는 실제 HTTP·프로세스 재시작으로 나머지 상태 보존, 수업과 기존 문항 연결, 도움 이력, 승인 후 계산 1회를 확인했습니다. 원 채점기와 실패 결과는 그대로 두고 **사후 판정**을 따로 기록했습니다. 이미 유효한 구현을 채점기에 맞추려고 다시 고치라고 하지 않았습니다. 실제 요구가 이행된 것으로 확인한 뒤 추가 중립 요청을 억지로 보내지도 않았습니다. 두 풍부한 맥락 조건의 브라우저 렌더·클릭 완주는 여전히 미검증입니다.

### 무엇을 남겼고, 다음 도약은 어디서 찾나

공개 합성 과제는 정답이 이미 맞아도 반복 복구하는 문제를 재현합니다. 한 증상만 고친 답은 새 등록 기능에서 실패하고, 필요한 검토를 유지한 다른 정당한 구현은 통과합니다. 원래 비공개 앱·대화·상세 기록은 공개하지 않았으므로 모든 역사적 시험이 공개 자료만으로 재현되는 것은 아닙니다. 개발용 선택 자산이며 스킬 실행 의존성이 아닙니다.

공개 채점기도 모델 시험 후 보완했습니다. 원 판정기의 특정 서비스 복구 경로 강제를 없애고, 실제 검토가 원 요청과 근거 전체에 맞는 올바른 계획을 확인했는지 검사합니다. 로컬 정정은 허용하지만 필요한 검토를 생략한 완료는 거부하며, 원 요청·테스트 보호도 검사합니다. 작성자 통제 10개가 기대한 허용·거부를 모두 충족했고 기존 작업자·패치 사본은 여전히 호출 4회·서비스 복구 0회였습니다. 새 모델 비교 결과가 아니며 원 판정·해시는 보존했습니다. 로컬 연산과 평가자 내부 감사는 이 호출 수에 포함되지 않습니다.

[OpenAI 개선 루프](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop), [Anthropic 평가 지침](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [tau2-bench](https://github.com/sierra-research/tau2-bench), [SWE-bench](https://github.com/SWE-bench/SWE-bench)에서 기록 기반 과제, 상호작용과 채점의 분리, 실행 결과 검증을 참고했습니다. 해당 코드·데이터·프레임워크·유료 서비스를 가져오거나 실행한 것은 아닙니다.

최초 작업자 8명과 저장 과제의 새 문맥 재개 작업자 2명을 사용했습니다. 단계와 검사 항목은 추가 독립 표본이 아닙니다. 기록된 주요 작업자는 gpt-6-astra / ultra였으나 정확한 백엔드는 모릅니다. 새 종량제 API 호출은 없었고, 구독 사용량을 무료라고 가정하지 않습니다. 토큰·비교 가능한 시간·비용·실제 인간 구조 요청량은 측정하지 않았습니다.

중요하게도 작업자에게 스킬과 관련 기록을 **명시적으로 읽게 했습니다.** 실제 업무에서 스킬이 제때 호출되는지, 필요한 기록을 찾아오는지는 시험하지 않았습니다. 따라서 다음 후보는 지침 추가보다 **판단 시점에 필요한 정보가 도착하는가**입니다. 기록이 없었는지, 있는데 찾지 못했는지, 읽고도 따르지 않았는지부터 구분해야 합니다. 앞의 두 문제에는 기존 인수인계에서 요구와 유효한 증거를 필요할 때 가져오는 작은 도구가 후보입니다. 읽고도 무시한다면 지침·화면 설계·실행 시 강제 검사도 검토할 수 있습니다. 이번 시험에서 어느 도구의 필요성도 입증하지 않았고, 확정된 진단이나 설치된 자동 감시기는 아닙니다.

작업자의 패치 실패·시험 코드 오류, 평가 환경의 Python 별칭·종료된 서버·잘못된 패치 적용 경로도 회복 과정과 함께 남겼습니다. 효과가 나올 때까지 시험을 늘리거나, 새 파일·플러그인을 성능 향상으로 부르지 않았습니다. **현재의 짧은 스킬을 유지하면서 재사용할 과제와 부정적 결과를 남기는 것이 이번의 책임 있는 결론입니다.**
