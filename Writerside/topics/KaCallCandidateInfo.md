# KaCallCandidateInfo

<warning>
<code>KaCallCandidateInfo</code> is the result type of the <b>legacy</b>
<code>KtElement.resolveToCallCandidates()</code> entry point. New code should use
<code>KtResolvableCall.collectCallCandidates()</code> and the <code>KaCallCandidate</code> hierarchy. See
<a href="Resolution-Candidates.md"/> for the new shape and
<a href="Migrating-Resolution-API.md"/>.
</warning>

`KaCallCandidateInfo` represents one of the candidates considered during
[overload resolution](https://kotlinlang.org/spec/overload-resolution.html) of a call. Unlike `KaErrorCallInfo.candidateCalls`,
retrieving a candidate via `KaCallCandidateInfo` does not imply that the call is erroneous &mdash; you can list
candidates on successful code too.

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaCallCandidateInfo
  KaCallCandidateInfo --> KaApplicableCallCandidateInfo
  KaCallCandidateInfo --> KaInapplicableCallCandidateInfo
</code-block>

## Members

`val candidate: KaCall`
: The candidate represented as a `KaCall` (the legacy base type).

`val isInBestCandidates: Boolean`
: Whether the candidate is in the final set the compiler considered. Multiple best candidates indicate ambiguity.

### `KaApplicableCallCandidateInfo`

A candidate that *could* be called at the site &mdash; its arguments are complete and assignable, and its type
arguments fit all the constraints.

### `KaInapplicableCallCandidateInfo`

A candidate that *could not* be called at the site.

`val diagnostic: KaDiagnostic`
: The reason for the candidate's missing applicability (e.g. argument type mismatch, missing value for a parameter,
type-argument constraint violation).

## Replacement mapping

| Legacy member                                                                               | Replacement                                                                      |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `KaCallCandidateInfo` / `KaApplicableCallCandidateInfo` / `KaInapplicableCallCandidateInfo` | `KaCallCandidate` / `KaApplicableCallCandidate` / `KaInapplicableCallCandidate`. |
| `KaCallCandidateInfo.candidate: KaCall`                                                     | `KaCallCandidate.candidate: KaSingleOrMultiCall`.                                |
| `KtElement.resolveToCallCandidates(): List<KaCallCandidateInfo>`                            | `KtResolvableCall.collectCallCandidates(): List<KaCallCandidate>`.               |
