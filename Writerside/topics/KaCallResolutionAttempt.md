# KaCallResolutionAttempt

`KaCallResolutionAttempt` is the rich result type of `tryResolveCall()`. Unlike the plain `resolveCall()` &mdash; which
collapses failures to `null` &mdash; an attempt always carries everything the compiler considered: either the resolved
call, or a diagnostic together with candidate calls. For compound calls (for-loops, delegated properties, `+=`, array
compound), the attempt additionally addresses each sub-call independently, so partial success is observable.

This page documents the sealed hierarchy and helper extensions. For the high-level view, see
[](Resolving-Calls.md).

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaCallResolutionAttempt
  KaCallResolutionAttempt --> KaSingleCallResolutionAttempt
  KaSingleCallResolutionAttempt --> KaCallResolutionSuccess
  KaSingleCallResolutionAttempt --> KaCallResolutionError
  KaCallResolutionAttempt --> KaMultiCallResolutionAttempt
  KaMultiCallResolutionAttempt --> KaForLoopCallResolutionAttempt
  KaMultiCallResolutionAttempt --> KaDelegatedPropertyCallResolutionAttempt
  KaMultiCallResolutionAttempt --> KaCompoundVariableAccessCallResolutionAttempt
  KaMultiCallResolutionAttempt --> KaCompoundArrayAccessCallResolutionAttempt
</code-block>

## Single-call attempts

### `KaSingleCallResolutionAttempt`

Sealed: either `KaCallResolutionSuccess` or `KaCallResolutionError`. Both `KaCallResolutionSuccess.call` and
`KaCallResolutionError.candidateCalls` always contain [](KaSingleCall.md) instances.

### `KaCallResolutionSuccess`

`val call: KaSingleCall<*, *>`
: The resolved single call.

### `KaCallResolutionError`

`val diagnostic: KaDiagnostic`
: The diagnostic associated with the error (e.g. `INVISIBLE_REFERENCE`, `UNRESOLVED_REFERENCE`).

`val candidateCalls: List<KaSingleCall<*, *>>`
: The candidate calls the compiler considered. The list may be empty &mdash; an error does not have to expose
candidates.

## Multi-call attempts

`KaMultiCallResolutionAttempt` represents a compound or desugared call. When every sub-call resolves, the attempt
assembles a [](KaMultiCall.md); when any sub-call fails, the assembled `call` is `null` but the individual
sub-attempts remain addressable.

```Kotlin
sealed interface KaMultiCallResolutionAttempt :
    KaCallResolutionAttempt {
    // null if any sub-call failed
    val call: KaMultiCall?
    // every sub-call attempt
    val attempts: List<KaSingleCallResolutionAttempt>
}
```

The concrete subtypes match the four kinds of compound calls:

### `KaForLoopCallResolutionAttempt`

For a `for (item in expr)` loop. `call` is `KaForLoopCall?` &mdash; non-null only when all three sub-calls resolve.

| Member                   | Description                                    |
|--------------------------|------------------------------------------------|
| `iteratorCallAttempt`    | Resolution attempt for the `iterator()` call.  |
| `hasNextCallAttempt`     | Resolution attempt for the `hasNext()` call.   |
| `nextCallAttempt`        | Resolution attempt for the `next()` call.      |

### `KaDelegatedPropertyCallResolutionAttempt`

For a `by`-delegated property. `call` is `KaDelegatedPropertyCall?`.

| Member                          | Description                                                            |
|---------------------------------|------------------------------------------------------------------------|
| `valueGetterCallAttempt`        | Resolution attempt for the `getValue()` call.                          |
| `valueSetterCallAttempt`        | Resolution attempt for the `setValue()` call (null for `val`).         |
| `provideDelegateCallAttempt`    | Resolution attempt for the `provideDelegate()` call (null if absent).  |

### `KaCompoundVariableAccessCallResolutionAttempt`

For `i += 1` / `i++` / `i--` on a variable. `call` is `KaCompoundVariableAccessCall?`.

| Member                   | Description                                                                  |
|--------------------------|------------------------------------------------------------------------------|
| `variableCallAttempt`    | Resolution attempt for the variable read/write.                              |
| `operationCallAttempt`   | Resolution attempt for the operator function (`plus`, `inc`, ...).           |

### `KaCompoundArrayAccessCallResolutionAttempt`

For `a[i] += v` and similar. `call` is `KaCompoundArrayAccessCall?`.

| Member                   | Description                                                                  |
|--------------------------|------------------------------------------------------------------------------|
| `getterCallAttempt`      | Resolution attempt for the `get()` call.                                     |
| `operationCallAttempt`   | Resolution attempt for the operator function.                                |
| `setterCallAttempt`      | Resolution attempt for the `set()` call.                                     |

## Helper extensions

Two extension properties cover the common cases without forcing a pattern match.

`val KaCallResolutionAttempt.calls: List<KaSingleOrMultiCall>`
: A flattened list of resolved/candidate calls. On `KaCallResolutionSuccess` returns the resolved call as a one-element
list. On `KaCallResolutionError` returns `candidateCalls`. On `KaMultiCallResolutionAttempt` returns the assembled
multi-call when all sub-attempts succeeded; otherwise returns the combined calls from each sub-attempt.

`val KaCallResolutionAttempt.successfulCall: KaSingleOrMultiCall?`
: The resolved call if everything succeeded, otherwise `null`. For a compound attempt this is the assembled
`KaMultiCall` only when **every** sub-attempt resolved.

For full control:

```Kotlin
fun <T> KaCallResolutionAttempt.fold(
    onSuccess: (KaSingleOrMultiCall) -> T,
    onFailure: (List<KaSingleCallResolutionAttempt>) -> T,
): T
```

`onSuccess` is called with the resolved call when the attempt is a successful single call or a fully successful
multi-call. `onFailure` is called with the list of failed sub-attempts otherwise (a one-element list for a
`KaCallResolutionError`, the multi-call's `attempts` for a partially-failed compound).

## Example

```Kotlin
@OptIn(KaExperimentalApi::class)
fun describe(call: KtCallElement): String = analyze(call) {
    val attempt = call.tryResolveCall() 
        ?: return@analyze "no attempt"

    attempt.fold(
        onSuccess = { call ->
            val name = (call as? KaSingleCall<*, *>)?.symbol?.name
            "Resolved: $name"
        },
        onFailure = { errors ->
            val diagnostics = errors
                .filterIsInstance<KaCallResolutionError>()
                .map { it.diagnostic.factoryName }
            
            "Failed: $diagnostics"
        },
    )
}
```
