# Resolution Candidates

Sometimes you need every callable the compiler *considered* at a call site, regardless of whether resolution
ultimately succeeded. The classic case is a code-completion or quick-fix that wants to enumerate all overloads
visible at a position; another is a diagnostic UI that wants to explain *why* a particular overload did not match.
Use `collectCallCandidates()` for this.

> Snippets on this page assume an `analyze { }` block (or `context(_: KaSession)`) is in scope and that
> `@OptIn(KaExperimentalApi::class)` is applied somewhere up the call chain.

## `collectCallCandidates`

`collectCallCandidates()` is defined on `KtResolvableCall` and returns a `List<KaCallCandidate>`:

```Kotlin
val candidates: List<KaCallCandidate> =
    callElement.collectCallCandidates()
```

Each `KaCallCandidate` wraps a [](KaSingleOrMultiCall.md) and exposes whether it was selected as a
final candidate by the compiler:

```Kotlin
sealed interface KaCallCandidate {
    val candidate: KaSingleOrMultiCall
    val isInBestCandidates: Boolean
}
```

The sealed hierarchy has two leaves:

`KaApplicableCallCandidate`
: The candidate *could* be called with the given arguments and type arguments &mdash; its arguments are complete and
assignable, and its type arguments fit all constraints. On a successful resolution every applicable candidate
participates; on an ambiguity all best matches are applicable.

`KaInapplicableCallCandidate`
: The candidate could *not* be called at this site. The reason is exposed as a `diagnostic: KaDiagnostic` &mdash; an
argument is missing or not assignable, or a type argument violates a constraint, etc.

## When to reach for candidates

Candidates are useful regardless of resolution outcome:

* **Successful code** &mdash; show every overload visible at the call site (e.g. a "show overloads" or "smart
  completion" feature). Every applicable candidate appears, including the one that the compiler ultimately chose.
* **Erroneous code** &mdash; explain *why* none of the overloads matched: collect every `KaInapplicableCallCandidate`
  and present its `diagnostic` to the user. This is more informative than the single diagnostic on the call itself,
  which only reports the overall failure.

```Kotlin
val candidates = callElement.collectCallCandidates()
val selected = candidates.filter { it.isInBestCandidates }
val rejected = candidates
    .filterIsInstance<KaInapplicableCallCandidate>()

if (rejected.isNotEmpty()) {
    rejected.forEach {
        showInapplicableHint(it.candidate, it.diagnostic)
    }
}
```

## How candidates differ from other lists of calls

The resolution API exposes lists of calls in three places. They look similar but answer different questions.

`KaCallCandidate` returned by `collectCallCandidates()`
: Every candidate the overload-resolution algorithm considered &mdash; **applicable and inapplicable**, on
both successful and erroneous code. Reach for this when you want to enumerate *all options*, not just the result.

`KaSingleCall` returned by `KaCallResolutionError.candidateCalls`
: A subset shown only when resolution **failed**: the candidates the compiler ultimately reported as candidates of an
error call. Use this to understand the error path; do not use it to enumerate overloads on successful code &mdash;
on a successful call this list is empty by definition.

`KaCallCandidateInfo` returned by `KtElement.resolveToCallCandidates()` (legacy)
: The legacy equivalent of `collectCallCandidates()`, built on the old `KaCall` hierarchy. Documented under
[](Legacy-Resolution-API.md). New code should use `KaCallCandidate`.

## Compound calls

For compound expressions (for-loops, delegated properties, `+=`, array-compound), the candidate's `candidate` field is
a [](KaMultiCall.md) rather than a `KaSingleCall`. The new compound call types provide named sub-call
accessors (`iteratorCall`, `getterCall`, `setterCall`, `operationCall`, and so on), so you can drill into the
sub-calls of a compound candidate exactly as for the resolved call itself.
