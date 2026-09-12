# Codex Involution Guard

[English](#english) · [한국어](#한국어)

## English

A lightweight skill that helps Codex preserve the user's intended outcome when work drifts, repeats ineffective attempts, or accumulates unnecessary process. It supports development, research and learning using relevant instructions and existing project records.

Experimental v0.2.1. No server, API key, background process or required evaluation framework. It guides decisions; it does not enforce behavior or guarantee improved performance or lower cost.

### What it does

| Situation | Intended behavior |
| --- | --- |
| A small fix is mistaken for completion of a larger request | Preserve the original outcome and identify remaining work |
| More tools, rules, documents or reviews are proposed | Consider reuse, consolidation or omission before adding complexity |
| An attempt repeatedly fails | Retry with new evidence or changed conditions; otherwise consider another method |
| Valid checks are about to be repeated | Reuse trustworthy evidence covering the current requirement, artifact version and relevant environment |
| “Efficiency” would remove necessary verification | Retain safety, validity, source and recovery checks |

It does not continuously monitor projects, remember every conversation, collect unrelated histories, automatically route models or impose spending caps. A method can change without silently abandoning the user's goal. Routine edits should not create extra meetings, reports or trackers.

For example, a button fix and passing unit tests do not complete a request for a working onboarding-to-export flow. Conversely, a verified flow need not be rerun merely for reassurance if its evidence still applies.

### Philosophy and psychological principles

**Involution** here means increasing internal complexity without progress toward the intended result—a working description, not a diagnosis or validated AI scale. The framing draws on Clifford Geertz's *Agricultural Involution*, originally about agricultural change in Indonesia. Applying it to AI workflows is an analogy, not validation or implementation of the whole theory. [Publisher information](https://www.ucpress.edu/book/9780520004597/agricultural-involution).

We separate **problem framing → human behavioral evidence → LLM intervention hypotheses → implementation and testing**, rather than ranking disciplines by accuracy.

| Concept | Translation into instructions |
| --- | --- |
| Subtraction neglect / additive bias | Consider reuse, consolidation and omission before adding tools or process |
| Escalation of commitment / sunk costs | Judge continuation by future value, usable assets and switching risks—not irrecoverable effort alone |
| Self-regulation feedback | Compare the intended outcome with current evidence; recognize decision-relevant information as progress |
| Implementation intentions | Specify conditional actions: reuse applicable evidence; check missing, stale or invalidated evidence |

These are design hypotheses informed by human research, **not proof that LLMs have the same psychological mechanisms**. Necessary investigation is not waste simply because it takes time. Counts of files, tests or citations are not substitutes for user value. Keep core instructions short and load optional tool/model guidance only when needed.

[Detailed philosophy, sources and implementation mapping (Korean)](docs/design.md) · [Design/evidence history (English)](docs/evidence.md). Theory documentation is not loaded on every invocation.

### Use it

After installation, ask in your project:

> `$involution-guard Recover the original goal and accepted corrections, check whether work is becoming unnecessarily complex, and proceed with the next useful action.`

For substantial work:

> `$involution-guard Inspect existing implementations first, then plan, review the necessary perspectives and build. Preserve the full request and verify the actual user workflow.`

Reuse existing approvals and project handoffs. Report course corrections briefly instead of creating a competing project ledger.

### Install once, reuse across projects

Clone or download this repository to a stable location. Run the following **from its root**. On Windows, a junction points to the canonical source; it does not create a separate copy. Do not overwrite an existing installation.

```powershell
$skillSource = (Resolve-Path './skills/involution-guard').Path
$skillDirectory = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.agents/skills'
$skillTarget = Join-Path $skillDirectory 'involution-guard'
New-Item -ItemType Directory -Path $skillDirectory -Force | Out-Null
if (Test-Path -LiteralPath $skillTarget) { throw 'An installation already exists; inspect it before changing it.' }
New-Item -ItemType Junction -Path $skillTarget -Target $skillSource
```

On macOS/Linux, from the repository root, run `mkdir -p "$HOME/.agents/skills"`, then `ln -s "$PWD/skills/involution-guard" "$HOME/.agents/skills/involution-guard"` after checking the destination is absent.

If discovery does not refresh, start a new session or restart Codex. Automatic matching is not guaranteed; use explicit invocation when needed. See [official discovery documentation](https://learn.chatgpt.com/docs/build-skills). The local Windows installation has been checked; other platforms and account-specific discovery have not been comprehensively tested.

Keep the source in `skills/involution-guard/`. Moving it requires updating the link. Install separately on other computers. To uninstall, remove **only the installed link**, preserving the source; do not recursively delete the source directory.

### What was reused?

No third-party code, engine or dataset has been copied into or integrated with the skill. Inspiration, development-time use and installed integration are distinct.

| Source | Actual influence or use | Not included |
| --- | --- | --- |
| [OpenAI Plugin Eval](https://github.com/openai/plugins/tree/main/plugins/plugin-eval) | Existing comparison/measurement capabilities informed the decision not to build a duplicate general engine | CLI, metric packs and engine; pilots did not use Plugin Eval |
| [SkillsVote](https://github.com/MemTensor/skills-vote) | Selective exposure of relevant skills informed context discipline | Recommendation service, library and automatic evolution |
| [SkillsBench](https://github.com/benchflow-ai/skillsbench) | Task-based with/without-skill evaluation informed testing | Official benchmark tasks, datasets and harness; our cases are synthetic |
| Local `product-change-review` skill | Planning, review and user-workflow verification practices | Private original instructions; no required installation or permanent multi-agent process |
| Local `skill-creator` skill | Short entry instructions, optional references and development-time validator use | Validator code and development packages as runtime dependencies |

Agent-skill-eval, Promptfoo, agnix and SWE-Skills-Bench were investigated as evaluation options, not integrated or executed for the reported pilots. See [optional tool/model guidance](skills/involution-guard/references/reuse-and-models.md) and [benchmark review (Korean)](docs/evaluation.md).

Our contribution is a small set of outcome-recovery, action-value and evidence-boundary instructions, documentation and synthetic tests—not a new psychological model or automatic detector. An optional project-authored experiment script under `evals/` is not a general framework or skill dependency.

Model descriptions are candidate roles, not fixed rankings or proven superiority. Distinguish supplier claims from local observations; keep the current model unless a specific limitation justifies changing it.

### Changes and evaluation limits

v0.2 clarified three existing questions using behavioral-science-informed design. v0.2.1 refined verification: reuse trustworthy results for the current requirement, version and environment; check missing or invalidated evidence. No mandatory review gate or runtime dependency was added.

Early six-case pilots were mostly short decision scenarios; both conditions passed. They did not demonstrate incremental effectiveness.

A later restricted-action API experiment used four evidence states, three conditions and two repeats: 24 episodes / 40 calls with GPT-5.4 nano. It executed small in-memory CSV/HTML checks, not a full Codex coding workflow.

| Condition | Success | Total checks | Redundant checks |
| --- | --- | --- | --- |
| No skill | 3/8 | 4 | 1 |
| v0.2 | 3/8 | 6 | 2 |
| v0.2.1 candidate | 5/8 | 6 | 1 |

Estimated API cost at uncached published rates was **$0.01189395**, below the $0.30 experiment budget—not an invoice total or total development/subscription cost. Candidate cost was about 1.9% higher than v0.2; total checks did not decline. Three candidate runs still accepted stale or insufficient evidence. **This small experiment does not establish general performance gains, safety or cost savings.**

[Evidence history (English)](docs/evidence.md) · [Full methodology and reproduction (Korean)](docs/evaluation.md) · [Code](evals/recheck_probe.py) · [All synthetic results](evals/recheck_results.json). Only the optional paid experiment requires an API key; **the skill does not**. Rerunning the experiment incurs new charges.

### Feedback, files and license

Share the [repository](https://github.com/Assessment-Nerd/codex-involution-guard) and post in [the feedback issue](https://github.com/Assessment-Nerd/codex-involution-guard/issues/1) or a new issue. Include the original outcome, sanitized reproduction, version/host/model, actual behavior/result, and unnecessary process. Counterexamples—scope shrinkage, excessive review, premature stopping or omitted checks—are especially useful.

Remove credentials, private conversations, personal data and confidential code. Public examples are synthetic; raw personal histories are not distributed. A feedback invitation is not external validation.

- `skills/involution-guard/`: canonical instructions and optional reference.
- `docs/design.md`: philosophy, research and transfer limits (Korean).
- `docs/evidence.md`: decisions and evaluation history (English).
- `docs/evaluation.md`, `evals/`: optional evaluation methodology (Korean), code and synthetic results.
- `.github/ISSUE_TEMPLATE/feedback.md`: feedback template.

MIT licensed. Independent community project; not an official OpenAI product.

---

## 한국어

Codex 작업이 복잡해지기만 하고 원래 목표는 멀어질 때, 다음 행동을 다시 정렬하는 작은 스킬입니다. 개발·연구·학습 프로젝트에서 기존 지시와 작업 기록을 이어받습니다.

모든 프로젝트를 상시 감시하거나 모든 대화를 자동으로 기억하지 않습니다. 자동 모델 배정·비용 상한 강제 기능도 아닙니다. 접근 가능한 관련 맥락을 바탕으로 판단을 돕고, 사용자 목표를 버리지 않은 채 방법을 바꾸도록 안내합니다.

실험 버전 v0.2.1. 서버·API 키·백그라운드 프로세스·평가 프레임워크 없이 사용하는 지침형 스킬입니다. 판단을 돕지만 행동을 강제하거나 성능 향상·비용 절감을 보장하지 않습니다.

### v0.2.1: 필요한 검증은 남기고 유효한 결과는 재사용

현재 요구·파일 버전·관련 환경에 맞는 신뢰할 만한 검사 결과가 있으면, 마무리 확인만을 위해 반복하지 않도록 검증 문단을 보완했습니다. 변경됐거나 범위가 맞지 않는 증거는 재사용하지 않습니다.

추가 API 실험은 24회, 약 **$0.0119**였습니다. 제한된 재검사 과제에서 스킬 없음 3/8, v0.2 3/8, 수정안 5/8 성공을 관찰했지만 일반적 성능 향상은 미확인입니다. 전체 검사 횟수는 줄지 않았고 수정안 비용은 v0.2보다 약 1.9% 늘었습니다. 실패와 비용을 포함한 [과제·기존 벤치마크 검토·전체 결과·재현 방법](docs/evaluation.md)을 공개합니다. 선택적 평가 스크립트만 API 키를 사용하며 **스킬 사용에는 키가 필요 없습니다.**

### v0.2: 철학과 행동과학을 실행 규칙으로

인류학의 인볼루션은 **무엇이 문제인지 보는 관점**, 심리학은 **추가·지속·전환을 판단하는 행동 가설**, 기존 프로젝트는 **구현·평가 방법의 참고 대상**으로 구분했습니다. 인간 연구에서 나온 원리를 LLM에도 입증된 기제라고 주장하지 않습니다.

- 더하기 편향 연구 → 구조를 추가하기 전에 재사용·통합·생략 대안을 고려합니다.
- 몰입 상승 연구 → 이미 쓴 비용만으로 계속하지 않고, 현재 쓸 수 있는 자산과 앞으로의 비용·전환 위험을 비교합니다.
- 자기조절·실행의도 → 목표와 현재 증거의 차이를 확인하고, 특정 상황에서 할 행동을 명확히 합니다.

기존 실행 질문 세 곳만 바꾸었고, 새 점수표·강제 회의·의존성은 없습니다. **필수 검증을 없애거나, 정당한 재시도를 막거나, 사용자 목표를 축소하는 ‘효율화’는 허용하지 않습니다.** [철학 → 연구 근거 → 전이 가설 → 구현 설명](docs/design.md)과 [전후 비교 결과](docs/evidence.md)를 확인하세요. 이론 설명은 매 실행마다 읽히지 않습니다.

### 어떤 문제와 개념에서 출발했나

여기서 **인볼루션(involution)**은 “절차와 내부 정교함은 늘어나는데, 원래 원했던 결과는 진전되지 않는 상태”를 가리키는 작업상 정의입니다. 단순히 작업이 오래 걸리거나 코드가 복잡하다는 뜻은 아닙니다. 어려운 문제에 필요한 연구·검증·복구 작업은 남겨야 합니다.

개념적 배경은 Clifford Geertz의 *Agricultural Involution*으로 대표되는 인류학의 인볼루션 논의입니다. 원래는 인도네시아 농업의 변화에 관한 논의이며, LLM 성능 이론이 아닙니다. 이 프로젝트는 그 문제의식을 AI 작업의 절차 팽창에 **비유적으로 확장**합니다. ‘정체된 복잡성’은 이해를 돕는 표현이지 확립된 AI 진단명이나 측정 척도가 아닙니다. 이론 전체를 검증하거나 소프트웨어로 구현했다는 뜻도 아닙니다. [원저 출판사 안내](https://www.ucpress.edu/book/9780520004597/agricultural-involution).

이를 실제 작업 지침으로 옮길 때는 다음 구분을 사용했습니다. 아래는 이 프로젝트의 설계 원리이며, 별개의 학술 이론을 구현했다는 주장은 아닙니다.

| 차용·채택한 원리 | Codex에서 나타나는 문제 | 스킬에 반영한 행동 |
| --- | --- | --- |
| 결과와 대리지표의 구분 | 파일·테스트·인용 수는 늘지만 요청한 사용 흐름은 미완료 | 먼저 완료 기준과 실제 결과를 확인하고, 그다음 비용을 비교 |
| 추가 작업의 효용 점검 | 같은 실패를 조건 변화 없이 반복하거나 검토를 중복 | 다음 행동이 요구를 충족하거나 중요한 불확실성을 줄이는지 확인 |
| 기존 자산 재사용 | 이미 있는 도구를 조사하고도 비슷한 관리 도구를 새로 제작 | 기존 구현·검토·결정 기록부터 확인하고 부족한 부분만 변경 |
| 점진적 정보 노출 | 모든 스킬·모델 안내를 매 작업에 읽어 맥락 비용 증가 | 핵심 지침만 사용하고 도구·모델 참고자료는 선택 시에만 읽기 |
| 비교 가능한 행동 검증 | 설명이 그럴듯하면 효과가 있다고 판단 | 같은 과제의 스킬 사용/미사용 결과를 비교하고 모르는 비용은 미측정으로 표시 |

예를 들어 “가입부터 결과 확인까지 동작하게 해줘”라는 요청에서 버튼 이름 수정과 단위 테스트만 끝났다면, 완료라고 보고하지 않습니다. 남은 사용자 흐름을 보존하고 다음 검증을 진행합니다. 반대로 단순 오탈자 수정에는 계획서나 검토 회의를 추가하지 않습니다. **일을 줄이는 것 자체가 아니라, 원래 결과를 보존하면서 불필요한 일을 줄이는 것**이 목적입니다.

### 바로 사용하기

설치 후 프로젝트에서 다음처럼 요청하세요.

> `$involution-guard 지금까지의 목표와 수정 요청을 이어받아, 일이 불필요하게 커지고 있는지 확인하고 필요한 다음 작업을 진행해줘.`

새로운 큰 작업에도 사용할 수 있습니다.

> `$involution-guard 기존 구현부터 확인하고 계획 → 필요한 관점 검토 → 제작 순서로 진행해줘. 원래 요구를 축소하지 말고, 검증은 실제 사용 흐름 중심으로 해줘.`

보통은 짧은 내부 점검만 합니다. 오탈자 수정 같은 작은 작업에 회의나 문서를 추가하지 않습니다. 문제를 발견하면 이유와 다음 행동을 짧게 설명합니다. 기존 승인과 프로젝트별 HANDOFF를 사용하며 별도 프로젝트 장부를 만들지 않습니다.

### 한곳에서 관리하고 여러 프로젝트에서 사용하기

이 저장소를 유지할 위치에 한 번 내려받습니다. 아래 PowerShell 명령은 **저장소 루트에서** 실행합니다. 기존 설치가 있으면 덮어쓰지 않습니다. Windows에서는 원본 폴더를 가리키는 junction만 만들어 설치 복사본이 분산되지 않게 합니다.

```powershell
$skillSource = (Resolve-Path './skills/involution-guard').Path
$skillDirectory = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.agents/skills'
$skillTarget = Join-Path $skillDirectory 'involution-guard'
New-Item -ItemType Directory -Path $skillDirectory -Force | Out-Null
if (Test-Path -LiteralPath $skillTarget) { throw 'An installation already exists; inspect it before changing it.' }
New-Item -ItemType Junction -Path $skillTarget -Target $skillSource
```

macOS/Linux: from the repository root, use `mkdir -p "$HOME/.agents/skills"` then `ln -s "$PWD/skills/involution-guard" "$HOME/.agents/skills/involution-guard"` after checking the destination is absent.

Codex supports user-level skills and linked folders. If the skill does not appear, start a new session or restart Codex. Automatic matching is available but not guaranteed; explicit invocation is the reliable fallback. See [official skill discovery documentation](https://learn.chatgpt.com/docs/build-skills).

원본은 `skills/involution-guard/` 한곳에서 수정합니다. 원본 폴더를 이동하면 링크도 갱신해야 합니다. 다른 PC에서는 별도로 설치하며, 앱·계정별 탐색 위치 차이는 확인해야 합니다. 제거할 때는 설치된 **링크 자체만** 제거하고 원본을 보존하세요. 원본 폴더를 재귀 삭제하지 마세요.

### 이미 있는 도구를 어떻게 활용하나

**현재 스킬에는 외부 프로젝트에서 복사한 코드·데이터셋이나 연결된 서비스·평가 하네스가 없습니다.** 아래의 ‘참고’는 설계에 영향을 주었다는 뜻이며, 설치·통합·실행 완료를 뜻하지 않습니다. 외부 도구 위에 만든 래퍼나 해당 프로젝트의 포크도 아닙니다.

| 출처 | 실제로 참고하거나 사용한 부분 | 가져오지 않은 부분 / 현재 상태 |
| --- | --- | --- |
| [OpenAI Plugin Eval](https://github.com/openai/plugins/tree/main/plugins/plugin-eval) | 버전 비교와 확장 가능한 측정 기능을 조사하고, 중복 비교 CLI를 만들지 않기로 결정 | 코드·CLI·metric pack 미포함. 이 저장소의 파일럿은 Plugin Eval로 실행하지 않음 |
| [SkillsVote](https://github.com/MemTensor/skills-vote) | 필요한 스킬을 선별해 노출한다는 접근을 참고해 불필요한 맥락 로딩을 제한 | 추천 엔진·스킬 라이브러리·자동 진화 기능 미포함. 서비스 호출 없음 |
| [SkillsBench](https://github.com/benchflow-ai/skillsbench) | 스킬의 유무에 따른 실제 과제 수행을 비교하는 평가 방향 참고 | 벤치마크 과제·데이터·하네스 미포함. 초기 합성 사례와 별도의 제한된 행동 평가 사용 |
| 개발 환경의 `product-change-review` 스킬 | 계획 → 관점별 검토 → 구현, 사용자 흐름 중심 검증이라는 작업 방식 참고 | 로컬 원문 비공개·미배포. 사용자에게 설치를 요구하지 않으며 매번 다중 에이전트를 실행하지 않음 |
| 개발 환경의 `skill-creator` 스킬 | 짧은 진입 지침과 선택적 참고자료로 구성. 제공된 `quick_validate.py`를 개발 중 구조 검증에 사용 | 검증기 코드·개발용 패키지 미포함. 사용자 실행 의존성 아님 |

`agent-skill-eval`, Promptfoo, agnix는 [선택적 평가 도구 후보](skills/involution-guard/references/reuse-and-models.md)로 조사했습니다. 현재 제품에 통합하거나 이 파일럿에 사용한 도구는 아닙니다. 미래에 실제 문제가 생기면 해당 기능을 먼저 검토한다는 의미입니다.

이 프로젝트에서 새로 작성한 것은 **목표 복원 → 다음 행동의 가치 점검 → 원래 요구를 보존하는 최소 변경 → 증거 수준을 구분한 검증**을 연결하는 지침과, 그 지침을 설명·시험하기 위한 문서 및 합성 사례입니다. 새 알고리즘이나 자동 인볼루션 탐지기는 아닙니다. 기존 개인 작업에서 발견한 실패 양상을 일반화했으며, 개인 대화 원문을 배포하거나 설치 사용자의 다른 프로젝트 기록을 자동 수집하지 않습니다.

따라서 ‘재사용 우선’은 현재 **기존 설계와 검증기를 활용하고 중복 엔진을 만들지 않은 것**까지입니다. 외부 하네스와의 실제 연동까지 끝냈다는 뜻은 아닙니다. 이 스킬이 프로젝트의 기존 검토와 겹치면 그 결과를 재사용합니다.

모델별 장점도 고정 순위 대신 작업별 후보로 관리합니다. 공식 설명과 실제 관측을 구분하고, 현재 모델로 해결되지 않는 구체적 이유가 있을 때 추가 비용을 검토합니다. [선택적으로 읽는 도구·모델 안내](skills/involution-guard/references/reuse-and-models.md).

### 검증과 피드백

[설계 결정·검증 범위](docs/evidence.md)를 확인하세요. 기존 개인 작업에서 발견된 패턴은 일반화한 합성 사례로만 공개합니다. 실제 원문 대화, 연구자료, 로컬 경로, 인증정보는 포함하지 않습니다.

초기 6개 합성 사례에서는 스킬 사용·미사용 모두 기준을 충족했습니다. **추가 효과나 비용 절감은 아직 입증하지 못했습니다.** 현재 공개물은 검증된 최적화 시스템이 아니라, 실사용 반례를 받아 개선하려는 작은 실험적 지침입니다.

Issues에서 “원래 목표 / 스킬이 한 일 / 실제 결과 / 불필요해진 절차”를 알려주세요. 성공담뿐 아니라 목표 축소, 과도한 검토, 잘못된 중단, 필수 검증 생략 같은 반례가 특히 유용합니다. 개인 자료는 제거하고 최소 재현 사례를 보내주세요. 피드백 요청을 게시한 것과 실제 외부 피드백을 받은 것은 구분해 기록합니다.

### 파일 안내

- `skills/involution-guard/`: 유일한 실행 지침과 선택적 참고자료
- `docs/design.md`: 철학·행동과학적 근거·구현과 전이 한계
- `docs/evidence.md`: 계획·검토 결정, 검증과 남은 한계
- `docs/evaluation.md`, `evals/`: 선택적 저비용 평가의 방법·코드·합성 결과 (일상 실행에 로드하지 않음)
- `.github/ISSUE_TEMPLATE/feedback.md`: 공개 피드백 양식

MIT 라이선스입니다. 독립적인 커뮤니티 프로젝트이며 OpenAI 공식 제품이 아닙니다.
