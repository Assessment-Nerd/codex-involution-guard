# Design and evidence — v0.1.0

## Scope and planning sequence

The intended result is more effective Codex use across development, research and learning projects, with less accumulation of work that does not advance the user's goal. It is not maximum skill count, minimum token count, or a new agent platform.

Planning preceded three independent subagent reviews (user/PM, developer/maintenance, evaluation/research). They used the same inherited model; this was not a multi-model experiment. All recommended removing the proposed aggregate comparison CLI. That decision was accepted before implementation. One skill reuses established review practices and adds an outcome/overhead checkpoint. No runtime, metric engine or mandatory dependency was added.

Historical private conversations provided examples of scope shrinkage, fragmented knowledge, redundant approval, costly repeated verification and component success reported as end-to-end completion. This was a targeted review, not a representative sample or a claim about failure prevalence. Public cases below are synthetic adaptations. Historical assistant completion reports were not treated as fresh implementation verification.

## Fixed acceptance cases

| Case | Starting request/state | Observable acceptance |
| --- | --- | --- |
| Small edit | Rename a heading in an existing short document | Edit only the requested heading; no extra planning/report artifacts |
| Scope drift | End-to-end workflow requested; only one cosmetic bug fixed | Keep the end-to-end outcome pending; choose a step that advances it |
| Research correction | User wants one integrated account instead of source-by-source summaries | Preserve the correction, shared themes and source distinctions |
| Evidence boundary | Unit checks pass; public workflow not run | Report component evidence and remaining user-path verification |
| Useful overhead | Additional source/recovery check resolves a material uncertainty | Retain the check; do not call it waste because it adds time |
| Stalled work | Same failure repeats with no changed conditions | Find a new evidential action or concrete dependency; do not loop blindly |

Success is assessed against each case's acceptance, before considering cost. Human learning effectiveness is not assessed by an agent's explanation. Unknown tokens, time and model settings remain unknown.

## Validation status

Two fresh subagents received the same six synthetic tasks, once without and once with explicit skill instructions. They were separate sessions using the same inherited model, with no external network. This is one bundled pilot per condition, not twelve independent trials. Cases were not randomized; assessment was by the implementing agent and was not blinded. Automatic skill discovery was not exercised.

| Case | Without skill | With skill | Evidence boundary |
| --- | --- | --- | --- |
| Small edit | Met | Met | Both actually edited the heading; original body remained unchanged |
| Scope drift / public path | Met | Met | Both left onboarding incomplete and proposed its public route; app was not executed |
| Research correction | Met | Met | Both wrote an integrated note with A/B/C attribution and a novel question |
| Source evidence | Met | Met | Both called for methods/results verification and qualified the snippet |
| Necessary recovery check | Met | Met | Both retained reference/recovery inspection; no deletion performed |
| Stalled authentication | Met | Met | Both proposed the alternative route; no authentication operation performed |

The implementing agent inspected the two edited notes, both study outputs and both final responses. Each run produced only the two requested files, not an extra tracker. The treatment note added a caveat that one novel-example success does not prove lasting transfer; this difference is not scored as improved human learning. Both conditions met the acceptance criteria, so **this pilot demonstrates no incremental effectiveness**. Tokens and comparable elapsed time were unavailable; no cost-saving claim is made.

A separate read-only release reviewer found no material issues in the public instructions, installation directions and privacy boundaries. Local checks cover skill frontmatter, local reference links, explicit public file selection and installation-content matching. The supplied Python validator initially lacked PyYAML; its dependency was isolated in private validation state, not added to the product. The Windows user-scope junction points to the canonical source, with identical content hashes. Host skill-picker discovery and other operating systems still need user-side confirmation.

No claim of cross-project effectiveness or cost reduction. No external feedback received at release preparation. The six easy scenarios may have a ceiling effect; the next useful evidence is a sanitized case where the baseline actually drifts or repeats ineffective work, followed by a matched comparison. Do not grow a synthetic suite just to seek a positive result.

## Upstream reuse and limits

- [Plugin Eval](https://github.com/openai/plugins/tree/main/plugins/plugin-eval): inspected CLI and metric-pack contract. Comparison already exists, so no duplicate engine. Found a maintainer-specific absolute path in improve-skill guidance: source availability alone does not prove portable installation. No upstream code copied.
- [SkillsVote](https://github.com/MemTensor/skills-vote): inspected README roadmap; local recommendation released, local attribution/evolution pending. Selective exposure informs design; the service is not a dependency.
- [SkillsBench](https://github.com/benchflow-ai/skillsbench): reusable evaluation direction; the full benchmark was not run.
- Existing local product-change-review and skill-creator guidance informed the workflow. No private guidance file is redistributed; this skill is self-contained and does not require those installations.
- [Official OpenAI model comparison](https://developers.openai.com/api/docs/models/compare) and [Luna documentation](https://developers.openai.com/api/docs/models/gpt-5.6-luna), accessed 2026-09-12: candidate role descriptions only. No cross-model superiority established here.

Further development requires a reported workflow failure, an observable acceptance case and a smaller-change explanation. Expand via upstream capabilities where possible; do not add tools just to expand the product.
