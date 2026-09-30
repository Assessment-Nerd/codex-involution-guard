# Contract-recovery replay

[English](#english) · [한국어](#한국어)

## English

A small, optional Python-stdlib development fixture derived from a recorded research-assistant integration problem. It is not installed with the skill. No API, server, credentials or third-party framework is required. Python 3.12 on Windows was tested.

The initial program already produces the correct answer, but information lost between interpretation and review causes avoidable recovery calls. The task is to improve that path without deleting useful review, guessing missing requirements or weakening the result. A frozen deterministic service replaces language-model sampling: its call counts are **not live latency, tokens or money**.

### Reproduce the evaluator's own checks

From the repository root:

```text
python evals/contract_replay/grader.py --selfcheck
```

This executes ten authored controls in temporary copies: unchanged seed, general repair, symptom-only repair, full-representation-first repair, two valid local-correction routes, missing review, ignored review, changed request and changed tests. Complete alternatives pass; incomplete generalization, unreviewed completion and protected-input changes do not. Each applicable run includes a wrong-source injection and ambiguous/unsupported requests. These are evaluator checks, not model A/B trials.

### Run an actual worker

Copy **only `seed/`** into a new, isolated working directory. Give a fresh worker that directory, the assigned skill version and the request in `task.txt`. Do not give it the grader, `probe.py`, reference implementation, another worker's artifacts, or later feedback. Preserve the frozen service, original request and original tests. The worker should implement and execute the task, not merely describe a patch.

Then, outside the worker's context:

```text
python evals/contract_replay/grader.py PATH_TO_WORKER_DIRECTORY
```

The evaluator copies the workspace before running it. Successful output includes `quality_pass`, `calls_on_supported_reads`, `avoidable_recoveries`, necessary-review and clarification cases. `protected_files_unchanged` compares provider/request/original tests against the seed; `files_unchanged` separately compares non-cache files before/after grader execution. Inspect case detail before interpreting the combined `pass`. Isolation is by instruction and separate directories, **not a security sandbox for untrusted code**.

For an authored reference in a new directory:

```text
python evals/contract_replay/grader.py --materialize-reference PATH_TO_NEW_DIRECTORY
```

### Interpretation

**Instruction clarification after the Luna comparison:** the seed README now explicitly requires byte-identical provider/request/tests and a separate file for added tests. The six Luna trials used the earlier ambiguous wording, “preserve the original tests”; five retained original assertions but added tests in the same file. Their frozen raw failures remain recorded separately from successful product behavior. This wording correction is prospective, not a retroactive authority violation or a new model trial. The grader implementation is unchanged.

The unchanged seed uses ten substitute-service calls across two supported requests; an authored general repair uses four, with all seven quality/control cases satisfied. One current-skill worker also achieved four. This demonstrates a code repair by the existing skill, **not improvement from a new skill version**. Each worker is one development episode, not seven independent samples. The neighboring capability is a prospective transfer check, not another recorded historical failure.

[The observed worker patch](observed-worker.patch) records that worker's actual application change. Applying it to a fresh seed copy and grading the result reproduced four calls and zero avoidable recoveries. Its reconstructed source matches the worker's source after normalizing line endings. Keep this solution outside any new worker's inputs.

The public evaluator is a **post-run revision**, `post_run_clean_review_audit_v2`. The original frozen evaluator required a service-repair call and two reviews on the injected fault; this incorrectly excluded valid local correction. The revision observes actual reviews and independently checks their plan against the full unchanged request and evidence. It accepts local correction while rejecting completion without a clean meaningful review. Audit-only validation calls are evaluator overhead, not worker-service calls. The original model scores/hashes remain in [the cycle record](../trajectory_results.json); rescoring the existing worker and patch copy preserved 4 calls / 0 recoveries. No new model comparison was run.

`avoidable_recoveries` counts extra service interpretations plus service repairs on the two supported non-fault requests. It does not measure local corrective computation, total work or all possible forms of recovery. The public executable seed and task match the local trial; the evaluator revision is deliberately distinguished from its frozen predecessor.

This public fixture contains project-authored synthetic code and records, not the private original application or raw conversations. Identifying narrative details were removed from the seed README. The shorter, clearer repository can make the task easier than real work. See [the complete cycle and limits](../../docs/trajectory-evaluation.md).

## 한국어

**Luna 비교 후 지시문 명확화:** 이제 초기 README에 서비스·요청·테스트 파일의 바이트 동일성과 추가 검사의 별도 파일 작성을 명시했습니다. 기존 6개 시험에는 ‘원래 테스트 보존’이라는 모호한 표현이 있었고, 5개 작업자가 원 assertion을 유지하면서 같은 파일에 검사를 추가했습니다. 원 채점 실패와 제품 동작 성공을 구분하여 보존합니다. 이번 명확화를 이전 작업자의 명백한 권한 위반으로 소급 적용하지 않으며, 채점 코드 변경이나 새 모델 시험도 아닙니다.

실제 연구 보조 도구에서 관찰한 통합 문제를 작게 재구성한 **선택형 개발 시험**입니다. 스킬 설치 시 따라오는 실행 의존성이 아니며 API·서버·키·외부 프레임워크가 필요하지 않습니다. Windows의 Python 3.12에서 확인했습니다.

초기 코드도 최종 답은 맞히지만, 앞 단계에서 빠진 정보를 뒷 단계가 복구하느라 호출을 반복합니다. 목표는 결과·금지 조건·필요한 검토를 유지하면서 그 복구를 줄이는 것입니다. 실제 LLM 대신 결정론적 대체 서비스를 쓰므로 호출 수를 실제 지연·토큰·요금으로 해석하면 안 됩니다.

위 `--selfcheck` 명령은 원본·일반 수정·증상 수정·전체 표현 우선·로컬 정정 두 방식·무검토·오류 검토 무시·요청 변경·테스트 변경의 작성자 통제 10개를 실행합니다. 모델 비교 결과가 아닙니다. 실제 비교에는 `seed/`만 새 폴더로 복사하고, 별도 문맥의 작업자에게 사용할 스킬과 `task.txt` 요청을 제공합니다. 채점기·정답·다른 작업자 결과는 제공하지 않습니다. 작업 후 `grader.py PATH_TO_WORKER_DIRECTORY`로 실제 결과를 검사합니다.

품질과 금지 조건을 먼저 판정하고, 일반 요청에서 불필요한 재해석·수정이 남았는지 봅니다. 의도적으로 잘못된 분석대상을 반환하면 수정과 재검토가 필요하며, 모호하거나 미지원인 요청에는 명확화를 요구해야 합니다. 검토를 없애서 호출을 줄이는 답은 인정하지 않습니다. 작업 폴더는 임시 복사본에서 실행하지만 악성 코드를 격리하는 보안 샌드박스는 아닙니다.

두 일반 요청의 대체 서비스 호출은 원본 10회, 작성자 일반 수정 4회였고, 기존 스킬 작업자도 4회를 달성했습니다. 이는 **기존 스킬을 사용한 코드 개선이지, 새 스킬의 성능 향상이 아닙니다.** 일곱 검사 항목도 독립 표본 일곱 개가 아닙니다. 실제 비공개 코드·대화는 포함하지 않았고, 짧고 정돈된 재구성이 현실보다 쉬울 수 있다는 한계가 있습니다.

[실제 작업자의 수정 패치](observed-worker.patch)도 남겼습니다. 새 원본 복사본에 적용하여 호출 4회·불필요한 서비스 복구 0회를 다시 확인했습니다. 새 비교 작업자에게 정답으로 노출하지 마세요. 공개 채점기는 서비스·원 요청·원 테스트를 초기본과 비교하고, 채점 실행 중 다른 파일이 변했는지도 구분해 검사합니다.

공개 판정기는 **모델 시험 후 보완한 v2**입니다. 원 판정기는 오류 주입 시 서비스의 특정 복구 호출과 검토 2회를 강요해 유효한 로컬 정정을 배제했습니다. 이제 실제 검토 호출의 계획이 원 요청·근거 전체에 맞는지 독립적으로 확인하여, 로컬 수정은 허용하되 정상 검토 없이 완료하는 구현은 거부합니다. 평가자 내부 감사 호출은 작업자 서비스 호출 수에서 제외합니다. 원 점수와 해시는 [결과 원장](../trajectory_results.json)에 보존했고, 기존 작업자와 패치 사본을 새 판정기로 확인해도 4회·0회였습니다. 새 모델 A/B를 수행한 것은 아닙니다.

복구 수는 두 일반 요청의 추가 서비스 해석·수정 호출만 셉니다. 로컬 정정 연산이나 전체 작업량·모든 종류의 복구를 측정하지 않습니다. 실행용 원본과 과제는 실제 시험과 같고, 공개 판정기는 사후 수정본임을 구분합니다.
