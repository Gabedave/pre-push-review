# High-risk review

Read this reference only for high-risk work or critical stateful/provider-facing boundaries.

## Invariant register

Create an invariant register from requirements and repository evidence. Cover every applicable area and mark genuinely irrelevant areas not applicable with a brief reason:

- states, allowed transitions, and terminal states;
- ownership, authorization, and competing actors;
- transaction, commit, and rollback boundaries;
- known success, known failure, and unknown external outcomes;
- retries, idempotency, deduplication, and partial completion;
- authoritative clocks, deadlines, leases, and expiry behavior;
- recovery, reconciliation, observability, and manual gates.

Trace every applicable invariant through implementation and tests. Explicitly examine actor interleavings, stale reads or writes, partial commits, retries after interruption, ambiguous provider responses, and clock-boundary behavior. Do not accept a happy-path suite as evidence for these failure modes.

## Changed-boundary proof

Derive material risks from requirements, producers, and consumers before selecting checks. A repository verification map or large passing test count is an execution index, not the ceiling of review.

For critical stateful or provider-facing changes, record the real producer and data format, state changed by each step, next consumer, and which collaborators are real or doubled. Follow writes to the subsequent read, retry, rescan, reconciliation, or cleanup. A refreshed object does not prove another snapshot is current, and a return value does not prove a collaborator had no side effects.

Choose concrete failure combinations relevant to the change: partial success before an exception, a real adapter's wrapped error, a missing related record, late evidence after repair, or work performed while delivery is paused. Derive fixtures from the real writer or adapter, not only the reader under test, and preserve nearby success and no-side-effect controls.

Use the smallest check preserving the mechanism: a real state-changing collaborator, storage query, adapter, controlled interleaving, or exact command for an order-dependent failure. A stub that removes the mutation or dependency under review cannot prove the criterion. Missing essential proof of the main acceptance behavior is blocking; do not demand a live provider or broad stress run when bounded local evidence proves the same risk.
