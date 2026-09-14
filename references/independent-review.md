# Independent review

Read this reference when the platform can provide a context-isolated reviewer.

## Prepare the review packet

Create a minimal packet containing only:

- original requirements or ticket verbatim when available;
- approval-contract identity, criteria, authoritative sources, authorized version history, and documented non-material corrections;
- applicable repository instructions;
- authoritative default-branch lookup, selected review base, override authority when applicable, complete branch-only commit set, unexplained-history assessment, snapshot identity, and complete target diff;
- recorded risk and rationale, plus the high-risk invariant register when required;
- criterion-to-changed-seam evidence mapping;
- for critical stateful/provider-facing changes, producer/data format, mutation, next consumer, real-or-doubled collaborators, follow-up operation, and relevant failure combinations;
- decision-record assessment and exact-candidate repository gates;
- relevant technical, product, compatibility, and operational constraints;
- relevant tests, nearby code paths, focused results, and commands planned for final verification.

Exclude:

- the implementation conversation or plan;
- the implementer's private reasoning unless it is a stated requirement;
- self-review conclusions, suspected defects, proposed fixes, or expected answers;
- candidate-authored claims that redefine success or present changed tests, code, or documentation as requirement authority;
- prior reviewer findings during the initial independent pass.

Pass raw artifacts rather than summaries that reveal implementation conclusions.

## Run the independent review

Treat independent review as a separate execution context, not role play.

1. Launch one fresh reviewer without inherited implementation conversation when isolation is available.
2. Give it the packet and repository access, and keep the initial pass read-only.
3. Ask it to verify approval-contract provenance and completeness, selected base and override authority, complete branch-only commit set, and unexplained-history assessment. It then reconstructs intended behavior from the contract, authoritative sources, and review-base evidence; candidate code and tests only evaluate compliance. Require it to verify or produce every criterion's evidence-and-result mapping without weakening explicit requirements.
4. Require every blocking finding to include affected location, failure scenario, severity, evidence, and concise remediation direction.
5. Do not describe same-context self-review as independent.

If isolation is unavailable, perform the strongest local review possible and record `INDEPENDENT REVIEW: NOT PERFORMED`. If independent review is mandatory, use `STATUS: REVIEW INCOMPLETE`.
