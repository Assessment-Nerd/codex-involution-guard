# Codex Involution Guard

Codex 작업이 복잡해지기만 하고 원래 목표는 멀어질 때, 다음 행동을 다시 정렬하는 작은 스킬입니다. 개발·연구·학습 프로젝트에서 기존 지시와 작업 기록을 이어받습니다.

Experimental v0.1.0. One instruction skill; no server, API key, background process or required evaluation framework. It helps preserve intended outcomes and question unnecessary work. It does not mechanically enforce behavior or guarantee lower cost.

## 어떤 문제와 개념에서 출발했나

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

## 바로 사용하기

설치 후 프로젝트에서 다음처럼 요청하세요.

> `$involution-guard 지금까지의 목표와 수정 요청을 이어받아, 일이 불필요하게 커지고 있는지 확인하고 필요한 다음 작업을 진행해줘.`

새로운 큰 작업에도 사용할 수 있습니다.

> `$involution-guard 기존 구현부터 확인하고 계획 → 필요한 관점 검토 → 제작 순서로 진행해줘. 원래 요구를 축소하지 말고, 검증은 실제 사용 흐름 중심으로 해줘.`

보통은 짧은 내부 점검만 합니다. 오탈자 수정 같은 작은 작업에 회의나 문서를 추가하지 않습니다. 문제를 발견하면 이유와 다음 행동을 짧게 설명합니다. 기존 승인과 프로젝트별 HANDOFF를 사용하며 별도 프로젝트 장부를 만들지 않습니다.

## 한곳에서 관리하고 여러 프로젝트에서 사용하기

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

## 이미 있는 도구를 어떻게 활용하나

**v0.1.0에는 외부 프로젝트에서 복사·수정해 넣은 코드, 가져온 데이터셋, 연결된 서비스나 평가 하네스가 없습니다.** 아래의 ‘참고’는 설계에 영향을 주었다는 뜻이며, 설치·통합·실행 완료를 뜻하지 않습니다. 외부 도구 위에 만든 래퍼나 해당 프로젝트의 포크도 아닙니다.

| 출처 | 실제로 참고하거나 사용한 부분 | 가져오지 않은 부분 / 현재 상태 |
| --- | --- | --- |
| [OpenAI Plugin Eval](https://github.com/openai/plugins/tree/main/plugins/plugin-eval) | 버전 비교와 확장 가능한 측정 기능을 조사하고, 중복 비교 CLI를 만들지 않기로 결정 | 코드·CLI·metric pack 미포함. 이 저장소의 파일럿은 Plugin Eval로 실행하지 않음 |
| [SkillsVote](https://github.com/MemTensor/skills-vote) | 필요한 스킬을 선별해 노출한다는 접근을 참고해 불필요한 맥락 로딩을 제한 | 추천 엔진·스킬 라이브러리·자동 진화 기능 미포함. 서비스 호출 없음 |
| [SkillsBench](https://github.com/benchflow-ai/skillsbench) | 스킬의 유무에 따른 실제 과제 수행을 비교하는 평가 방향 참고 | 벤치마크 과제·데이터·하네스 미포함. 자체 합성 사례 6개만 사용 |
| 개발 환경의 `product-change-review` 스킬 | 계획 → 관점별 검토 → 구현, 사용자 흐름 중심 검증이라는 작업 방식 참고 | 로컬 원문 비공개·미배포. 사용자에게 설치를 요구하지 않으며 매번 다중 에이전트를 실행하지 않음 |
| 개발 환경의 `skill-creator` 스킬 | 짧은 진입 지침과 선택적 참고자료로 구성. 제공된 `quick_validate.py`를 개발 중 구조 검증에 사용 | 검증기 코드·개발용 패키지 미포함. 사용자 실행 의존성 아님 |

`agent-skill-eval`, Promptfoo, agnix는 [선택적 평가 도구 후보](skills/involution-guard/references/reuse-and-models.md)로 조사했습니다. 현재 제품에 통합하거나 이 파일럿에 사용한 도구는 아닙니다. 미래에 실제 문제가 생기면 해당 기능을 먼저 검토한다는 의미입니다.

이 프로젝트에서 새로 작성한 것은 **목표 복원 → 다음 행동의 가치 점검 → 원래 요구를 보존하는 최소 변경 → 증거 수준을 구분한 검증**을 연결하는 지침과, 그 지침을 설명·시험하기 위한 문서 및 합성 사례입니다. 새 알고리즘이나 자동 인볼루션 탐지기는 아닙니다. 기존 개인 작업에서 발견한 실패 양상을 일반화했으며, 개인 대화 원문을 배포하거나 설치 사용자의 다른 프로젝트 기록을 자동 수집하지 않습니다.

따라서 ‘재사용 우선’은 현재 **기존 설계와 검증기를 활용하고 중복 엔진을 만들지 않은 것**까지입니다. 외부 하네스와의 실제 연동까지 끝냈다는 뜻은 아닙니다. 이 스킬이 프로젝트의 기존 검토와 겹치면 그 결과를 재사용합니다.

모델별 장점도 고정 순위 대신 작업별 후보로 관리합니다. 공식 설명과 실제 관측을 구분하고, 현재 모델로 해결되지 않는 구체적 이유가 있을 때 추가 비용을 검토합니다. [선택적으로 읽는 도구·모델 안내](skills/involution-guard/references/reuse-and-models.md).

## 검증과 피드백

[설계 결정·검증 범위](docs/evidence.md)를 확인하세요. 기존 개인 작업에서 발견된 패턴은 일반화한 합성 사례로만 공개합니다. 실제 원문 대화, 연구자료, 로컬 경로, 인증정보는 포함하지 않습니다.

초기 6개 합성 사례에서는 스킬 사용·미사용 모두 기준을 충족했습니다. **추가 효과나 비용 절감은 아직 입증하지 못했습니다.** 현재 공개물은 검증된 최적화 시스템이 아니라, 실사용 반례를 받아 개선하려는 작은 실험적 지침입니다.

Issues에서 “원래 목표 / 스킬이 한 일 / 실제 결과 / 불필요해진 절차”를 알려주세요. 성공담뿐 아니라 목표 축소, 과도한 검토, 잘못된 중단, 필수 검증 생략 같은 반례가 특히 유용합니다. 개인 자료는 제거하고 최소 재현 사례를 보내주세요. 피드백 요청을 게시한 것과 실제 외부 피드백을 받은 것은 구분해 기록합니다.

## 파일 안내

- `skills/involution-guard/`: 유일한 실행 지침과 선택적 참고자료
- `docs/evidence.md`: 계획·검토 결정, 검증과 남은 한계
- `.github/ISSUE_TEMPLATE/feedback.md`: 공개 피드백 양식

MIT licensed. Independent community project; not an official OpenAI product.
