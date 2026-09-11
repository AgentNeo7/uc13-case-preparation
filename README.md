# UC13 — CRM Case Preparation Kit

Reconciles already-extracted scalar facts against explicit entity, date and source-authority requirements. Keeps provenance, rejects invalid supersession and lists conflicts or stale evidence without inventing a resolution.

Status: **bounded local prototype**, validated only against synthetic assumptions. Original R01–R05 acceptance is partial or unverified in `requirements.json`. This package is independently runnable with Python 3.13 and its standard library. It needs no sibling package, service, credentials or installation.

## Run

From this directory:

```sh
/opt/homebrew/bin/python3.13 tool.py --input examples/input.json --output result.json --expect examples/expected.json
/opt/homebrew/bin/python3.13 test_tool.py -v
```

`--expect` is optional. Its JSON is a recursive subset oracle, authored before implementation. Exit 0 means analysis completed and any supplied oracle matched. Exit 1 means configured expected-result mismatch. Exit 2 means invalid/oversized input or local I/O error. No exit code grants operational authority or establishes safety. Output cannot overwrite the named input or oracle.

## Input and output

The example is the v1 input specification. Every field is required, and unexpected fields are rejected. The envelope requires `spec_version: 1`, `evidence_class: "simulated"` and a `data` object. Limits: 1 MB input, 500 list items, bounded finite numeric values. Sources are declared references; the tool never fetches them. Passing a real record while labeling it synthetic would not make the result validated.

`examples/input.json` is a positive example. `examples/cases.json` also contains negative and unknown cases. `examples/expected.json` states selected expected output assertions. `examples/actual.json` preserves the observed local run output. Extra output fields include modeled limitations and evidence; they are not additional authoritative claims. `examples/frozen.json` pins the preimplementation oracle hashes and timestamp.

## Checks and evidence

16 unit tests passed, including three frozen scenario cases, malformed/oversized input, missing/unknown fields, deterministic immutable processing, configured mismatch and five domain-specific edge checks, including null required evidence and an empty checklist. `checks.json` retains exact commands and raw output; observed execution of synthetic cases does not turn their business assumptions into observed production behavior. One AI authored both expected cases and implementation. No independent test set, external review, uptake or recognition is claimed. No unexpected failures occurred in the first recorded check attempt. Intentional invalid/mismatch tests expect exits 2/1.

## Unsupported scope and release boundary

No PDF/OCR extraction, fuzzy entity matching, legal eligibility, approved financial/public-sector checklist, reviewer UI or comparative preparation study.

The catalog's full usable release requires applicable G01–G09 checks, domain-approved requirements, representative validation and an accepted maintenance owner. These gates have not passed. Any publication must call this a synthetic prototype and preserve these limitations. No external calls or production changes occur.

The software is a baseline utility, not evidence of differentiation. A comparative operational benchmark has not run, so value and superiority remain proposed. Narrow or stop further expansion if later comparative evidence fails.

## Sources and provenance

Primary pages were read on September 11, 2026. Product descriptions are externally reported overlap, not independently verified performance. Notes and URLs are retained in `sources.json`.

- [MuleSoft IDP overview](https://docs.mulesoft.com/idp/) — MuleSoft documents structured document extraction and human review. Local declared-fact reconciliation does not establish extraction quality or superiority to IDP.

## Authorship and license

AI generated the code, fixtures and documentation under Balaji's scope and local-execution instructions. Balaji's documented contribution here is setting the portfolio and publication direction. These files do not attribute all implementation to him. Checks by the same AI are internal checks.

Original code; no third-party implementation copied and no dependencies installed. Original code is licensed under MIT; see LICENSE. Source-linked vendor documentation retains its own terms; it is not relicensed by this package.

## Source preview status

Experimental offline source; scoped tests passed, full original acceptance is incomplete. See [release status](RELEASE_STATUS.md), [checks](release-checks.json), [requirements](requirements.json) and [attribution](ATTRIBUTION.md). No production, independent-validation or differentiation claim.
