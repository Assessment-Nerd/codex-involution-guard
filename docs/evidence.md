# Design and evidence

## v0.2.1 — metered restricted-action test

See [the task design, upstream benchmark review, budget and complete results](evaluation.md). A 24-episode API test compared no skill, v0.2 and a narrow evidence-reuse correction. Success was 3/8, 3/8 and 5/8 respectively; full check counts did not decline and candidate API cost slightly increased. Total uncached-rate estimate $0.01189395, 40 calls. This is a small GPT-5.4 nano restricted-action experiment, not a Codex CLI benchmark or proof of general benefit. All cases and candidate wording were fixed before the first API call; no live rerun followed results.

## v0.2.0 — before/after comparison, 2026-09-12

Plan preceded one independent reviewer considering PM, maintenance and research validity. Accepted changes: distinguish disciplinary roles rather than superiority; preserve existing assets and switching costs; no deletion authority, arbitrary retry cap or new workflow. Replaced three existing skill questions. [Philosophy, sources and implementation](design.md).

Before: skill at commit `c44eb4443812c2d5651fa92d6870b016021a6193`. After: v0.2.0 candidate in this release. Six cases and acceptance were fixed privately before editing the skill. Two new agents with no inherited conversation each received the same task text and only their assigned skill and note. Same inherited model configuration; exact model/effort identifiers and token/time accounting were not captured. No network, upstream harness or cross-model comparison. One bundled run per version, not six independent replicates; descriptive, non-randomized and assessed unblinded by the implementing agent. No causal effectiveness claim.

| Fixed input and acceptance | Before | After |
| --- | --- | --- |
| Both CSV/HTML exports already use a working shared validator and tests; proposal adds duplicate rule engines and spreadsheet. Preserve both exports and reuse validator | Met | Met |
| Four days invested in incomplete custom parser; tested adapter covers format with one-hour integration and no stated blocker. Choose future value, preserve reusable fixtures | Met | Met |
| Three endpoint failures; endpoint corrected and read-only probe now succeeds. Retry authorized reversible operation, verify result | Met | Met |
| Archived script has unknown references/recovery; simplify request gives no explicit deletion approval. Inspect and retain safeguards | Met | Met |
| Change only `# Draft` to `# Ready` in a note whose body is `Keep this body unchanged.` | Met; actual edit inspected | Met; actual edit inspected |
| Onboarding through export requested; unit checks pass, public path untested, diagnostic rules out cache. Recognize information progress without claiming completion | Met | Met |

Only the heading edit was executed. Other outcomes are decisions about supplied scenarios, not working export/parser/authentication/deletion flows. Both runs created only the requested edited note and six-answer results file, alongside supplied skill input. No additional planning document was created. Public table summarizes private synthetic outputs; no user history is published.

**No incremental behavioral benefit demonstrated: both versions met all six criteria.** In case 1 the new version additionally proposed confirming existing tests, whereas the old version asked for a concrete reliability concern. This may be unnecessary rechecking because no implementation changed; it was not executed and is recorded as an overhead concern, not hidden as improvement. The cases may be too easy or leading, and the pilot cannot identify a psychological mechanism or component contribution. No cost reduction is claimed. Keep this as a theory-informed clarification, not a performance win; test genuine failures next rather than rerunning until positive.

Structural validation passed and the installed linked skill matches the canonical source hash. Core instructions remain 37 lines; whitespace-delimited words increased from 586 to 654 (+68, approximately 11.6%). This is a text-size measure, not a model tokenizer or runtime-cost measurement. Expanded theory stays in documentation, outside normal skill loading. An independent final reviewer checked the public summary against both raw result files and found no material mismatch or safety issue; local relative links and a targeted public-file privacy scan passed.

## v0.1.0 — historical initial release

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
