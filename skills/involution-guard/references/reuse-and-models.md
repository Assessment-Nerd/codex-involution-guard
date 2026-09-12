# Optional reuse and model decisions

Read only when choosing an evaluation tool or model. Reviewed 2026-09-12. These are source-based options, not installed dependencies or verified compatibility claims.

## Reuse the narrowest existing capability

| Decision | Existing candidate | Boundary |
| --- | --- | --- |
| Skill structure, token budget, version comparison | [Plugin Eval](https://github.com/openai/plugins/tree/main/plugins/plugin-eval) | Local CLI and skills; custom metric packs already exist. Inspect the current checkout and command help before use. |
| Effect with/without a skill in the real CLI | [agent-skill-eval](https://github.com/tardigrde/agent-skill-eval) | Early project. Baseline, repeated runs and budget controls; local compatibility must be checked. |
| Existing AI application's regression suite | [Promptfoo](https://learn.chatgpt.com/use-cases/ai-app-evals) | Use the actual application path, not just a raw model prompt. |
| Configuration validity | [agnix](https://github.com/agent-sh/agnix) | Static warnings do not establish user benefit. |
| Which existing skills to expose | [SkillsVote](https://github.com/MemTensor/skills-vote) | Local recommendation exists; local attribution/evolution was still on the roadmap at review. |
| Research-grade reusable task fixtures | [SkillsBench](https://github.com/benchflow-ai/skillsbench) | Benchmark performance is not a guarantee for this project's tasks. |

Existing project review workflows take precedence. Reuse their findings instead of adding a second review gate. No dependency is needed for the core skill. Add an adapter or metric only after a real case exposes a gap in an upstream tool.

For a strict dollar cap, inspect when budget limits are enforced. The reviewed agent-skill-eval guards run after each case, so they alone cannot prevent a single expensive call. Reserve bounded input/output cost before any paid call; include retries, judges and hosted tools. Do not equate subscription CLI usage with a verified API-dollar ceiling.

## Model strengths are conditional

The [official OpenAI model comparison](https://developers.openai.com/api/docs/models/compare) describes Astra for difficult end-to-end work, Sol for complex professional work, and Terra as balancing capability and cost. [Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna) targets cost-sensitive workloads. This suggests candidate roles, not verified superiority:

- Hard architecture or unresolved reasoning: consider a stronger model if the current model has a demonstrated limitation.
- Bounded implementation and review: keep the current capable model; compare alternatives only if quality or cost warrants it.
- Repeated narrow extraction/formatting: a less expensive candidate may suffice after representative checks.

Do not silently switch models or equate API prices with Codex subscription usage. Other providers remain eligible; verify their current primary documentation when considering them. Do not import a leaderboard rank as a project decision.

For a useful comparison, hold task, starting artifacts, tool access and acceptance criteria fixed. Record model/provider, reasoning setting, skill revision, success evidence and available cost/time measurements in the existing project record. Preserve the first failure and final recovery. Unavailable data stays unknown. A small pilot supports a local choice; do not advertise general effectiveness or human learning gains from it.
