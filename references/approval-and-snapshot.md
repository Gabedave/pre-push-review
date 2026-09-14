# Approval contract and candidate snapshot

Read this reference for every review before judging the candidate.

## Establish the review scope

1. Read applicable `AGENTS.md` files, repository documentation, and local instructions.
2. Inspect repository status and the complete intended diff, including relevant staged, unstaged, and untracked files.
3. Determine the review base from the request, merge base, or repository default. When the work may create or update a pull request, independently resolve the default branch from its authoritative host and use it as the review and PR base unless the user, ticket, or governing release policy explicitly selects another target; a checkout, local branch name, linked PR, or earlier review is context rather than authority. Record the selected base and source of any override.
4. Recover intended behavior from authoritative sources that predate or are independent of the candidate: the original request, ticket, explicit acceptance criteria, applicable repository policy, public contracts, and review-base behavior. Do not derive approval criteria from tests, documentation, or implementation changed by the candidate.
5. Identify the runtime, framework, dependency, and platform versions actually used by the repository.
6. Compare the complete candidate commit set and diff with the selected base. Unexplained commits that exist only because the branch started from another target block readiness; remove unrelated history instead of retargeting it into the pull request.
7. Separate target changes from unrelated work. Do not modify or include unrelated changes.
8. If scope or intent cannot be determined safely, report the ambiguity instead of guessing.

## Freeze the approval contract

Before judging the candidate, establish an approval contract that is independent of the proposed change.

1. Record each success criterion and its authoritative source, verbatim when practical. Use this authority order:
   - explicit user decisions and the original request, ticket, or acceptance criteria;
   - applicable repository policy, public contracts, and architecture or product decisions that predate the candidate;
   - behavior and invariants established by the review base;
   - reviewer-derived safety, security, compatibility, and operational invariants that do not contradict a higher-authority source.
2. Include observable outcomes, non-negotiable invariants, required verification, material assumptions, and explicitly authorized exclusions. Record a contract identity or version covering the criteria and source revisions.
3. Treat candidate-authored or candidate-modified code, tests, snapshots, documentation, comments, and generated artifacts only as implementation or evidence. Never use them as authority for weakening or replacing a criterion.
4. The implementation agent may identify ambiguity, propose stronger checks, challenge finding evidence, request a material contract change, or propose a non-material correction. It may not approve its own material contract change or use the proposed definition to approve the same candidate.
5. A contract change is material when it changes criterion meaning, an observable outcome, an evidence obligation, required verification, an authorized exclusion, or a possible verdict. Require authorization by the user, governing policy, or a product, architecture, or other authority independent of the proposing or implementing agent. Record the authorization and rationale, issue a new contract identity, and restart affected review and verification.
6. Allow documented corrections to citations, source metadata, typos, or wording without separate authority only when the independent reviewer confirms they cannot change criterion meaning, evidence obligations, required verification, exclusions, or verdict. The proposing agent may not classify a verdict-relevant change as non-material unilaterally.
7. If product intent, authority, a criterion, or correction materiality remains ambiguous and could change the verdict, stop with `APPROVAL CONTRACT: HUMAN DECISION REQUIRED`, `CONSENSUS: HUMAN DECISION REQUIRED`, and `STATUS: REVIEW INCOMPLETE`.
8. Require the independent reviewer to verify contract provenance and completeness before evaluating the candidate and map every criterion to evidence and a result. It may add risk-derived invariants but may not weaken explicit requirements.

Freeze the approval contract before the initial independent pass. Alter it only through the authorized material-change process or reviewer-confirmed non-material correction process.

For every criterion retain:

`criterion -> changed seam -> focused evidence -> broad evidence -> result`

Use `confirmed`, `partial`, `unverified`, or `failed`.

## Freeze the candidate snapshot

1. Record a snapshot identity containing the review base, target revision when one exists, and a digest or equivalent identity for the complete intended change. Cover the tracked diff plus paths, file modes, and contents of included untracked files.
2. Do not modify the candidate while the initial independent review runs. If it changes, compare it with the recorded snapshot:
   - retain the report only when the delta is demonstrably non-behavioral and invalidates no finding or verification result;
   - treat it as stale for affected behavior when production logic, contracts, migrations, dependencies, infrastructure, or risk-relevant tests changed, and give the original reviewer the updated snapshot.
3. Record the low, medium, or high risk classification and reason.
4. If a high-risk invariant or authoritative requirement cannot be established safely, stop with `STATUS: REVIEW INCOMPLETE`. Final review cannot substitute for a missing product, architecture, or risk decision.

## Run focused candidate verification

For every risk level, run only the checks needed to establish that the candidate is coherent and reviewable before independent review:

- focused regression tests for changed behavior and important failure paths;
- the smallest relevant type, syntax, formatting, or static check;
- deterministic integration evidence when risk cannot be proven at unit level.

Defer slow broad suites, full builds, and redundant repository-wide checks until blocking review findings are settled unless repository policy requires them for meaningful review. Do not present focused checks as final verification.

For concurrency or timing behavior, require deterministic coordination using barriers, controlled clocks, transaction hooks, or equivalent synchronization. Sleep-based timing, repeated retries, and stress runs may supplement deterministic evidence but cannot be the sole proof.
