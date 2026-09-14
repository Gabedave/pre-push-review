# Final verification and reporting

Read this reference after findings are settled and before declaring the work complete.

## Run fresh final verification

1. Refresh the authoritative selected base when pull-request delivery is in scope. Recheck the candidate commits and complete diff, then freeze and record the final snapshot. Confirm it contains only intended changes and no secrets, sensitive data, generated noise, unrelated files, or unexplained history.
2. Refresh every criterion's changed seam against the exact final snapshot. For critical stateful/provider-facing work, also refresh the producer/data format, mutation, next consumer, collaborator, follow-up operation, and failure combinations.
3. Run focused checks invalidated by the final delta and the broadest verification proportionate to final risk using the exact final snapshot. This is the normal point for affected suites, repository-wide tests, builds, linting, types, integration tests, and repository-required checks.
4. Finalize each criterion's focused evidence, broad evidence, and result. Missing essential final-boundary proof remains blocking.
5. Ask the original reviewer to inspect repairs to Critical or Major findings when available.
6. Launch a new context-free reviewer only when a Critical/Major repair changed high-risk production behavior, scope materially expanded, the original reviewer still disputes resolution, or independent adjudication is needed.
7. Do not launch another reviewer solely because a Minor finding was documented or a non-behavioral test, comment, format, or documentation change was made.
8. Give any required new reviewer the original isolated packet updated only with final diff and fresh evidence, excluding earlier debate and expected conclusions.
9. The implementation agent confirms agreed corrections preserve intent, but that is not approval evidence. The applicable reviewer confirms the final snapshot against the frozen contract; when no review-triggering repair occurred, the completed report confirms no known Critical or Major finding remains.
10. If a command or tool mutates the candidate after final verification, compare the delta with the final snapshot and rerun invalidated checks. Never claim verification for an untested snapshot.

Consensus exists only when blockers are fixed, resolved through accepted evidence, or authoritatively adjudicated and required verification passes. Consensus is not approval unless the same verified contract version and final snapshot were evaluated and every criterion has a supported result.

## Report honestly

Keep confirmed and not-applicable entries concise. Expand blockers and failed, partial, or unverified evidence. Conclude with:

### Review scope

Summarize files, diff, requirements, and risk areas reviewed.

### Approval contract

Record contract identity, criteria and authoritative sources, authorized material changes, reviewer-confirmed non-material corrections, and the final-snapshot `criterion -> changed seam -> focused evidence -> broad evidence -> result` mapping.

### Snapshot and risk

Record authoritative default-branch lookup, selected base and override authority, complete candidate commits, unexplained-history assessment, candidate/final snapshot identities, risk and rationale, invariant-register status when applicable, reviewer-attempt count, and behavior-changing repair-cycle count.

### Findings fixed

For each fixed Critical or Major issue, state severity, problem, correction, and evidence. Write `None` if none were discovered.

### Reconciliation log

Record accepted/fixed findings, findings resolved by implementation evidence, compromises, adjudication, and non-blocking disagreements. Do not expose hidden chain-of-thought or invent history.

### Verification

List checks and outcomes, including checks that could not run and why.

### External evidence

List authoritative sources, applicable versions, and supported findings. Write `Not required` when repository evidence was sufficient.

### Changed-boundary proof

For critical stateful/provider-facing work, record the refreshed producer/data format, mutation, next consumer, collaborator, follow-up operation, and failure combinations. Connect them to the final criterion mapping and identify unverified essential proof. Otherwise write `Not required`.

### Decision records and repository gates

Record repository policy consulted, required or skipped decision record with its path/reason, and each exact-candidate gate/result. Write `Not required` only when no applicable instruction requires an additional gate.

### Remaining findings and risks

List unresolved findings, Minor observations, assumptions, and unverified areas.

### Review result

Record exactly one approval-contract result:

- `APPROVAL CONTRACT: VERIFIED` when the current contract is authoritative and complete enough to evaluate. The candidate can still fail a criterion.
- `APPROVAL CONTRACT: NOT VERIFIED` when provenance, authority, version, or completeness was not established and no human decision is requested.
- `APPROVAL CONTRACT: HUMAN DECISION REQUIRED` when authority, intent, or a material change needs an independent human/product decision.

Record exactly one independence result:

- `INDEPENDENT REVIEW: PERFORMED`
- `INDEPENDENT REVIEW: NOT PERFORMED`

Record exactly one consensus result:

- `CONSENSUS: ACHIEVED`
- `CONSENSUS: NOT ACHIEVED`
- `CONSENSUS: HUMAN DECISION REQUIRED`

End with exactly one status:

- `STATUS: READY FOR TEAM REVIEW` only when the approval contract is verified, the exact final snapshot was evaluated against that version, every criterion passes with evidence, consensus is achieved, no known Critical or Major finding remains, and required verification passes.
- `STATUS: NOT READY FOR TEAM REVIEW` when blockers remain or essential verification fails.
- `STATUS: REVIEW INCOMPLETE` when scope, independent review, essential evidence, or a required decision cannot be established.
