# Codex Involution Guard

Codex 작업이 복잡해지기만 하고 원래 목표는 멀어질 때, 다음 행동을 다시 정렬하는 작은 스킬입니다. 개발·연구·학습 프로젝트에서 기존 지시와 작업 기록을 이어받습니다.

Experimental v0.1.0. One instruction skill; no server, API key, background process or required evaluation framework. It helps preserve intended outcomes and question unnecessary work. It does not mechanically enforce behavior or guarantee lower cost.

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

기존 product-change-review 작업 방식에서 계획·구현 책임·사용자 검증을 이어받고, 목표 이탈·반복·관리비용 점검을 보완했습니다. 이 스킬이 기존 검토와 중복될 때는 그 검토 결과를 재사용합니다.

[Plugin Eval](https://github.com/openai/plugins/tree/main/plugins/plugin-eval)의 비교·지표 확장, [SkillsVote](https://github.com/MemTensor/skills-vote)의 필요한 스킬만 노출하는 원리, [SkillsBench](https://github.com/benchflow-ai/skillsbench)의 행동 검증을 참고했습니다. 첫 버전은 이 도구들의 엔진을 복사하거나 재구현하지 않습니다. 실제 측정이 필요할 때 기존 도구를 사용합니다.

모델별 장점도 고정 순위 대신 작업별 후보로 관리합니다. 공식 설명과 실제 관측을 구분하고, 현재 모델로 해결되지 않는 구체적 이유가 있을 때 추가 비용을 검토합니다. [선택적으로 읽는 도구·모델 안내](skills/involution-guard/references/reuse-and-models.md).

## 검증과 피드백

[설계 결정·검증 범위](docs/evidence.md)를 확인하세요. 기존 개인 작업에서 발견된 패턴은 일반화한 합성 사례로만 공개합니다. 실제 원문 대화, 연구자료, 로컬 경로, 인증정보는 포함하지 않습니다.

Issues에서 “원래 목표 / 스킬이 한 일 / 실제 결과 / 불필요해진 절차”를 알려주세요. 성공담뿐 아니라 목표 축소, 과도한 검토, 잘못된 중단, 필수 검증 생략 같은 반례가 특히 유용합니다. 개인 자료는 제거하고 최소 재현 사례를 보내주세요. 피드백 요청을 게시한 것과 실제 외부 피드백을 받은 것은 구분해 기록합니다.

## 파일 안내

- `skills/involution-guard/`: 유일한 실행 지침과 선택적 참고자료
- `docs/evidence.md`: 계획·검토 결정, 검증과 남은 한계
- `.github/ISSUE_TEMPLATE/feedback.md`: 공개 피드백 양식

MIT licensed. Independent community project; not an official OpenAI product.
