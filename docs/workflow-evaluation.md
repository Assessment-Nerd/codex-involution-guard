# Usage-informed workflow evaluation

## English

This engineering iteration examines recurring defects and verification overhead in the existing skill. It is **not construct validation or a production field experiment**. The runtime remains a portable instruction-only skill; the optional evaluation script is not installed or loaded with it.

### Why these changes

A targeted read-only review of recent private work found three useful patterns after actual skill use, not just catalog mentions. These are observations, not an estimate of failure prevalence or proof that the skill caused them:

- A common-state repair passed its bounded tests, but an adjacent export consumer still used stale state. The lesson is to inspect the affected producer/consumer boundary and a neighboring case, not to dismiss the earlier test or demand a whole-system rewrite.
- Later interpretation/review stages repeatedly recovered information omitted upstream. The claimed latency diagnosis was not independently reproduced. Shared contracts are a cause to investigate, not a proven explanation for every slow run.
- A parallel learning-delivery obligation disappeared from a next-step plan while interface work became the focus; permanent omission from the final deliverable was not established. A later, deeper chronological audit corrected our initial interpretation: the accepted plan allowed lesson and minimum interface work in parallel, and the user authorized proceeding through the interface. Starting it was not itself a phase-order violation. The candidate failure is losing an uncancelled obligation from the plan, not breaking an invented sequential prohibition.

Counterexamples matter: reusing an existing engine with a fresh-process check was useful; read-only diagnosis sometimes correctly led to no migration or deletion. Necessary verification and evidence-supported continuation remain protected. Raw conversations, project names, personal paths and credentials are not published.

The changes target **shared-cause repair, phase prerequisites, and dependency-specific evidence**. Minimum sufficient repair is not always the smallest diff. A file or another assistant's completion sentence is not an execution receipt. Conversely, an unrelated edit need not invalidate every previous check. These are behavioral design hypotheses, not new claims about human or model psychology; the existing [theory mapping](design.md) remains separate.

### Why not a plugin yet?

Observed gaps concerned decisions over already accessible evidence, not an unavailable connector. Packaging the same instructions would not establish enforcement. Official documentation distinguishes [skill guidance from server-backed tools](https://developers.openai.com/plugins/concepts/plugins). A plugin becomes justified if a concrete use case needs opt-in receipt collection, change-to-evidence linking, or deterministic enforcement that cannot be provided by current project tools. No background history collection or extra installation was added.

### Design fixed before execution

The project-authored [workflow_probe.py](../evals/workflow_probe.py) generates small synthetic working directories and grades the resulting files in temporary copies. It does not call a model or network service. No third-party benchmark code or dataset was imported. The existing restricted-action microbenchmark cannot execute arbitrary file repairs, so this bounded companion tests a different evidence level; it is not a general evaluation platform.

- A: existing skill from commit `e417add`, in both rounds. B: first candidate in round 1, revised candidate in round 2. This is an old-versus-new comparison, **not a no-skill comparison**.
- Four actual file/tool tasks per arm: regeneration after recurring defects, full command-line delivery, evidence reuse under irrelevant/relevant change, and authority/contract preservation.
- Two fresh no-parent-history agents per round, assigned opaque A/B labels; identical requests and artifacts within each pair. Launch order was A then B, not randomized. Workers were instructed not to inspect the grader or other arm. Isolation was instructional and directory-based, not an OS sandbox.
- Both rounds' tasks and graders were written and self-tested before round 1. The implementation lead did not inspect the detailed round-2 fixtures before freezing the revised candidate. Recurrence changes from truncation to deduplication, relevant configuration from delimiter/data to scale, irrelevant change from documentation to theme, and diagnosis-only becomes authorized repair. The delivery fixture repeats as a regression control, with different hidden inputs. This is a development holdout, not an external independent benchmark.
- Primary measure: complete task acceptance. Secondary: protected-file violations and verifier calls in the evidence task. Calls are **not total tool use, tokens, latency or cost**. Four tasks in one worker context are one bundled run, not four independent replications.
- Same inherited host settings with no requested override. All four worker `turn_context` records identify model alias `gpt-6-astra`, effort `ultra`; provider and exact backend snapshot are not exposed. Shared host instructions and capable baseline behavior may mask incremental effects. No separate paid API or paid judge was used; subscription usage is not free or measured here.

The grader author checked correct solutions, unmodified failures, task-specific broken fixes and log non-contamination. Diagnosis prose also needs manual inspection; the automatic check is deliberately limited. The implementing agent inspects outcomes, so assessment is not fully blinded.

### Results and iteration

Round 1: both versions passed 4/4 tasks, with zero protected-file violations. Each reused the stable receipt without running its verifier and refreshed the changed receipt once. Both diagnosis explanations were inspected and correct. **No incremental behavioral gain was observed.**

Tool-trace audit confirms that both round-1 workers actually executed the generator, delivery CLI, diagnostic probe and changed verifier, not only wrote plausible outputs. Each had one initial patch context-match failure before a corrected patch succeeded. Those recoveries are retained, not reclassified as first-attempt success. No out-of-arm data, installed guidance or hidden grader reads were found in the audited traces. The audit is not a security guarantee.

The first candidate increased whitespace-delimited instruction length from 679 to 752 words. Because the first run did not demonstrate a gain, the revision added no further workflow rules: it consolidated repeated explanation while retaining the observed-use corrections and authority/safety boundaries. The final candidate is 610 words: 10.2% below baseline and 18.9% below candidate 1. This is text length, not measured token savings or runtime performance. The second A/B tests this compressed candidate against the same old baseline.

| Round | Existing A | Candidate B | Unnecessary verifier runs A / B | Protected-file violations A / B |
| --- | --- | --- | --- | --- |
| 1: first candidate | 4/4 | 4/4 | 0 / 0 | 0 / 0 |
| 2: compressed candidate | 4/4 | 4/4 | 0 / 0 | 0 / 0 |

Each arm in round 2 again refreshed only the affected evidence once. Independent trace review confirmed all four workers' required CLI/probe/verifier executions. Both round-2 arms recovered from one patch context-match failure; A also recovered from two malformed read-only inspection commands. This incidental difference is not evidence of a latency or tool-cost effect. Intentional invalid-input exits were successful negative tests, not unexpected failures.

**Both comparisons tied. No quantum leap, general effectiveness gain, reduced rechecking or cost saving was demonstrated.** The shipped engineering outcome is a shorter, more explicit usage-informed instruction set and a stronger executable regression asset. The three behavior changes remain hypotheses; their separate contributions were not isolated. Stop this cycle here rather than increasing trials until a positive result appears.

[Complete sanitized results](../evals/workflow_results.json) include every arm, frozen guidance text, input/definition hashes, generated source/output artifacts and recovery notes. The definition hash stayed `5cb41b71bba45d39cb3e6151fd859eedbc0ed036b2015c1689593f1f40ca4214` throughout both rounds. Fixture author self-checks: 16 passed; existing microbenchmark self-tests: 4 passed. Structural skill validation passed, and the installed junction matches the final canonical source. Structure checks do not establish behavioral effectiveness.

### Reproduction and limits

```sh
python evals/workflow_probe.py self-test
python evals/workflow_probe.py make --root .codex-shared/new-run/A --round 1 --arm A --guidance-path path/to/frozen-SKILL.md
# Have a fresh agent perform only the generated TASK.md in that arm directory.
python evals/workflow_probe.py grade --root .codex-shared/new-run/A
```

Use new directories and preserve every run, including failures. The grader executes worker-produced Python code: use trusted local fixtures, not untrusted repositories. A temporary copy is not a security sandbox. Receipts/logs are fixture-owned evidence, not signed or tamper-resistant telemetry. Executing the grader alone tests the fixture, not model behavior. Worker execution also requires tool-trace inspection.

No automatic discovery, long-horizon phase transitions, human learning, multi-model transfer, broad cost saving, or psychological mechanism is established. The phase-prerequisite wording is usage-informed but not directly tested as a multi-session transition here. A tie is not proof of equivalence. Strong instructions in the tasks can mask differences between skills. Do not add rules or rerun until a favorable result appears.

The historical [recheck experiment](evaluation.md) changes an environment marker that the renderer does not actually consume. Its environment case therefore tests a hash-matching contract, not realistic causal invalidation. Its old results are preserved, but must not justify rechecking after every unrelated environment edit.

## 한국어

이번 작업은 실제 사용에서 발견한 약점을 바탕으로 기존 스킬을 고치는 개발 실험입니다. **인볼루션 구성개념의 타당화나 실제 운영 프로젝트의 현장 실험은 아닙니다.** 실행 스킬은 지침만 유지하며, 평가 코드는 개발할 때만 사용합니다.

### 무엇을 바꿨나

비공개 기록을 제한적으로 검토한 결과, 공통부 수정 뒤 인접 내보내기 경로가 빠지는 문제, 앞 단계의 누락을 뒷 단계가 반복 복구하는 문제, 화면 작업에 집중하면서 다음 단계 계획에서 병렬로 약속한 수업 자료가 빠지는 문제가 있었습니다. 최종 산출물에서도 영구적으로 누락됐다는 것은 입증하지 않았습니다. 후속 정밀 감사에서 초기 해석을 바로잡았습니다. 당시 합의는 수업 자료와 최소 웹 작업의 병렬 진행을 허용했고, 사용자도 웹까지 진행하도록 승인했습니다. 웹을 시작한 것 자체가 순서 위반은 아니며, 계획에서 취소되지 않은 병렬 의무의 누락이 검토 대상입니다. 스킬의 인과적 실패율을 계산한 것은 아닙니다. 기존 검증이 실제로 통과한 사실과 후속 경로의 누락을 함께 인정합니다. 지연 원인의 세부 설명은 독립 재현하지 않았습니다.

따라서 같은 결함의 생성 원인과 영향을 받는 경로를 좁게 확인하고, 단계 전환의 선행 조건을 지키며, 변경된 의존성과 연결된 검증만 갱신하도록 합니다. 전체 재설계나 모든 테스트 재실행을 요구하지 않습니다. 필요한 재검증과, 측정 결과 아무것도 바꾸지 않는 판단도 보호합니다. 심리학적 기제를 새로 입증했다는 의미가 아닙니다.

현재 관찰된 빈틈은 도구 부재보다 이미 접근 가능한 증거를 적용하는 판단 문제였습니다. 플러그인으로 포장하는 것만으로 해결되지는 않습니다. 자동 증거 수집·변경 영향 연결·결정적 강제가 실제로 필요해질 때 도구화를 검토하며, 이번에는 상시 감시나 추가 설치를 만들지 않았습니다.

### 어떻게 비교했나

기존판 A와 수정판 B에 같은 파일·요청을 주고 실제로 수정·명령 실행을 하게 했습니다. 조건당 4개 과제를 한 에이전트가 수행하며, 라운드마다 새 문맥을 사용합니다. 2차는 사전에 만든 다른 결함·설정·권한 변형을 쓰되, 내보내기 과제는 회귀 확인용으로 유지하고 채점 입력을 바꿨습니다. 완전히 새로운 외부 벤치마크가 아닙니다. 각 라운드 안에서 A/B를 비교해야 하며, 1차와 2차 점수를 단순 전후 향상으로 비교하면 안 됩니다.

정답 판정은 재생성 결과·전체 CLI·보호 파일·검증 영수증으로 합니다. 재검사 횟수는 증거 과제의 특정 검사기 호출만 측정하며, 전체 도구 호출·토큰·시간·비용은 측정하지 않았습니다. 네 실행 기록 모두 모델 별칭 `gpt-6-astra`, 추론 설정 `ultra`이며 공급자와 정확한 백엔드 버전은 노출되지 않았습니다. 별도의 유료 API를 호출하지 않았으며 구독 사용량은 발생합니다.

1차와 2차 모두 기존판·수정판 각각 **4/4 통과, 보호 파일 위반 0건, 불필요 재검사 0회**였습니다. 각 실행은 필요한 변경 검사만 한 번 수행했습니다. 성능 차이는 확인하지 못했습니다. 1차 동률 후 규칙을 더 늘리지 않고 중복 설명을 정리했습니다. 지침은 기존 679단어 → 1차 752단어 → 최종 610단어입니다. 기존보다 10.2% 짧지만, 실제 토큰 비용이나 속도 감소를 측정한 것은 아닙니다.

1차 도구 기록에서 두 실행자의 생성기·내보내기·진단·변경 검사 실행을 확인했습니다. 두 조건 모두 최초 패치가 문맥 불일치로 실패한 뒤 수정해 성공했습니다. 이 실패를 숨기거나 첫 시도 성공으로 세지 않았습니다.

2차도 실제 필수 명령 실행을 확인했습니다. 두 조건 모두 최초 패치 불일치를 복구했고, A에는 읽기 전용 검사 명령의 따옴표 오류 두 건과 복구가 추가로 있었습니다. 이 우연한 차이를 비용·속도 향상으로 해석하지 않습니다. 의도적으로 넣은 비정상 입력의 실패는 정상적인 음성 검사입니다.

따라서 **퀀텀 점프·일반 성능 향상·재검사 감소·비용 절감은 입증하지 못했습니다.** 확인된 개발 성과는 더 짧고 구체적인 지침, 실제 파일/명령을 검사하는 평가 자산, 실패와 한계를 숨기지 않는 기록입니다. 행동 변경들의 독립 효과는 아직 가설입니다. [전체 합성 결과와 동결 지침](../evals/workflow_results.json)에 모든 조건과 복구 기록을 남겼습니다. 평가기 자체검사 16개, 기존 평가기 검사 4개, 스킬 구조 검증을 통과했고 기존 설치 링크에도 최종본이 반영됐습니다.

### 주의할 점

표본이 작고 요청에 단서가 명확한 합성 과제입니다. 동일 에이전트의 네 과제를 독립 반복으로 세지 않습니다. 실행자는 채점기를 보지 않도록 지시받았지만 별도 OS 보안 경계는 아니며, 평가자도 완전히 블라인드하지 않습니다. 채점기는 에이전트가 작성한 코드를 실행하므로 신뢰하는 로컬 과제에만 사용하세요. 영수증·로그도 위변조 방지 시스템이 아닙니다. 실제 명령 실행 여부는 도구 기록도 확인해야 합니다.

동일 점수가 일반적 동등성을 입증하지는 않습니다. 실제 장기 프로젝트·다른 모델·자동 스킬 선택·비용 절감은 별도 검증이 필요합니다. 단계 전환 지침은 사용 기록을 근거로 보완했지만, 이번 짧은 과제로 장기 단계 전환 행동까지 검증하지는 않았습니다.

기존 마이크로벤치마크의 환경 변경은 렌더링에 영향을 주지 않는 표식 변경이었습니다. 과거 결과를 지우지 않되, 이를 모든 환경 변경 후 재검사해야 한다는 근거로 쓰지 않습니다. 개인 기록은 공개하지 않습니다.
