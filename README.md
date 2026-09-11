# UC13 — Case Preparation for Salesforce

Bulk user-mode Case evidence packets with mandatory contact/description checks and source modification stamps.

This is Salesforce API 64.0 source, not a Python wrapper. Native compilation and Apex tests have **not** run. Original acceptance is tracked in module.json and remains partial. No novelty, operational benefit, independent recognition or legal merits result is claimed.

## Local checks

Node 22 or later; no runtime packages or service credentials: `npm test`.
These checks inspect package contracts and local fixtures, not Apex execution.

## Sandbox validation

Inspect the package and use the pending disposable Developer org alias `eb1a-dev`. Run the command in module.json only after confirming that alias resolves to that Developer org. Dry-run validation can execute tests and org automation; it is not performed here. Resolve org-specific Case statuses, validation rules and required fields. Test visible and denied-user cases and a 200-item Flow batch before any release. Permission set grants class access only: administrators must grant narrowly scoped Case/Task object and field rights separately. USER_MODE operations fail closed on missing access. Bind invocable actions in a reviewed Flow/Agentforce custom action; no agent action registration or activation is claimed.

## Operational limits

Bulk user-mode Case evidence packets with mandatory contact/description checks and source modification stamps. Original detailed requirements and gaps are in module.json. No managed package, native compile pass, org integration, corpus-complete retrieval or production rollout is asserted. No callouts, external messages or real customer records were used. Standard platform functions are the baseline; a comparative benchmark and domain review are required before differentiation claims.

## Provenance

Original code and synthetic checks were AI-authored. Balaji supplied Salesforce focus, architecture direction and publication preferences. Do not attribute all implementation work to him. `SOURCES.md` records public references. No private resume or petition evidence is bundled.

## Validation record

`offline-checks.log` preserves the local Node test output. The supplied package passed native Developer-org dry-run validation. Actual failures and fixes are preserved in the local run3 evidence. This result covers supplied metadata and scoped unit tests, not every original requirement.

## Distribution

Salesforce is the primary implementation. Historical Python source is under `legacy/python-prototype`. See `RELEASE_STATUS.md` and `SALESFORCE_VALIDATION.json`. Full acceptance remains partial.
