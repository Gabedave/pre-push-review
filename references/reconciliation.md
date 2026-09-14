# Finding reproduction and reconciliation

Read this reference only when a Critical or Major finding or material reviewer/implementation disagreement exists.

## Reproduce blocking findings

Before treating a Critical or Major finding as blocking:

1. Trace the affected execution path and requirements.
2. Reproduce the failure with a focused test or reliable static evidence when practical.
3. Check whether existing guards, invariants, types, framework behavior, or deployment constraints invalidate the concern.
4. Record the evidence and remaining uncertainty.

Avoid speculative blockers. Preserve plausible concerns as Minor or unverified when evidence is insufficient.

## Reconcile with the implementation agent

Treat reviewer and implementation agent as peers with different responsibilities. Findings are evidence to evaluate, not commands to follow automatically.

For every Critical or Major finding, the implementation agent chooses one disposition:

- **Accept**: agree and implement a correction.
- **Partially accept**: agree with the risk but propose a different correction.
- **Challenge**: disagree and provide concrete supporting reasoning.

Support partial acceptance or challenge with requirements, repository behavior, reproducible tests, version-applicable official documentation, security guidance, compatibility/performance/operational constraints, or risks introduced by the proposed alternative. Do not reject a finding using preference, authority, effort, or schedule alone.

Do not resolve a finding by materially changing the approval contract unless independent authority authorizes a new version. A proposed non-material correction is accepted only when the original reviewer confirms it cannot affect criterion meaning, evidence obligations, required verification, exclusions, or verdict. The implementation agent may challenge evidence or criterion mapping but may not redefine the criterion under dispute.

For Critical or Major findings only, give the original reviewer the response and resulting diff. It must address the implementation evidence and mark each disputed finding:

- **Resolved by implementation**
- **Resolved by accepted reasoning**
- **Still blocking**
- **Downgraded to non-blocking**
- **Requires product or human decision**

## Repair blockers

- Fix in-scope Critical and Major findings when a safe correction is clear.
- Do not automatically fix Minor findings unless an explicit review-economy exception applies.
- Add or update focused tests demonstrating corrected behavior.
- Keep comments limited to non-obvious decisions, constraints, or intent.
- Reinspect the entire resulting diff and run focused checks after each repair; defer broad verification until blockers and reconciliation are settled.
- Run relevant local security/dependency checks and confirm tests exercise the changed behavior and would fail for the original defect.
- Review repairs for regression and scope growth.

Continue while blockers remain, meaningful progress is possible, and the two-cycle budget is not exhausted. Otherwise stop instead of looping or assuming.

## Resolve disagreement

Allow one focused reconciliation exchange per behavior-changing cycle within the two-cycle total. If the same blocker remains after the second cycle, use a fresh independent adjudicator when available or request a human decision.

Give an adjudicator the original requirements, repository evidence, finding, implementation response, reviewer rebuttal, and authoritative sources. Escalate when resolution depends on product intent, risk tolerance, architecture ownership, or another decision not established by evidence.

Do not force consensus through silent concession. An unresolved blocking disagreement means the change is not ready. Minor and stylistic disagreement may remain when neither agent identifies a material correctness, security, compatibility, performance, operational, or maintainability risk.
