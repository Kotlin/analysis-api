# KaCallInfo

<warning>
<code>KaCallInfo</code> is the result type of the <b>legacy</b> <code>KtElement.resolveToCall()</code> entry point.
New code should use <code>KtResolvableCall.tryResolveCall()</code> and the
<a href="KaCallResolutionAttempt.md"/> hierarchy. See <a href="Migrating-Resolution-API.md"/>.
</warning>

`KaCallInfo` is the sealed result of `KtElement.resolveToCall(): KaCallInfo?` &mdash; the legacy entry point on any
`KtElement`. The call may have either resolved successfully (`KaSuccessCallInfo`) or failed (`KaErrorCallInfo`,
carrying candidate calls and a diagnostic).

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaCallInfo
  KaCallInfo --> KaSuccessCallInfo
  KaCallInfo --> KaErrorCallInfo
</code-block>

## Members

### `KaSuccessCallInfo`

`val call: KaCall`
: The successfully resolved call.

### `KaErrorCallInfo`

`val candidateCalls: List<KaCall>`
: The candidates considered during resolution that were not selected. May be empty &mdash; an error call is not
guaranteed to have candidates.

`val diagnostic: KaDiagnostic`
: The diagnostic describing the error.

## Helper extensions

`val KaCallInfo.calls: List<KaCall>`
: The list of calls. A one-element list for `KaSuccessCallInfo`; the `candidateCalls` for `KaErrorCallInfo`.

`inline fun <reified T : KaCall> KaCallInfo.singleCallOrNull(): T?`
: The single `KaCall` of type `T` from the list, or `null` if no such single call exists. For an error call, returns a
single candidate of type `T`.

`fun KaCallInfo.singleFunctionCallOrNull(): KaFunctionCall<*>?`<br/>
`fun KaCallInfo.singleVariableAccessCall(): KaVariableAccessCall?`<br/>
`fun KaCallInfo.singleConstructorCallOrNull(): KaFunctionCall<KaConstructorSymbol>?`
: Specialized variants of `singleCallOrNull` for the common cases.

`inline fun <reified T : KaCall> KaCallInfo.successfulCallOrNull(): T?`
: The successful call of type `T`, or `null` if the call is not successful or is of a different type.

`fun KaCallInfo.successfulFunctionCallOrNull(): KaFunctionCall<*>?`<br/>
`fun KaCallInfo.successfulVariableAccessCall(): KaVariableAccessCall?`<br/>
`fun KaCallInfo.successfulConstructorCallOrNull(): KaFunctionCall<KaConstructorSymbol>?`
: Specialized variants of `successfulCallOrNull` for the common cases.

## Replacement mapping

| `KaCallInfo` member                    | New equivalent                                                                                                |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `KaSuccessCallInfo.call`               | `KaCallResolutionSuccess.call` (a `KaSingleCall<*, *>`), or `KaMultiCallResolutionAttempt.call` for compound. |
| `KaErrorCallInfo.candidateCalls`       | `KaCallResolutionError.candidateCalls`.                                                                       |
| `KaErrorCallInfo.diagnostic`           | `KaCallResolutionError.diagnostic`.                                                                           |
| `KaCallInfo.calls`                     | `KaCallResolutionAttempt.calls` extension.                                                                    |
| `KaCallInfo.successfulCallOrNull<T>()` | `KaCallResolutionAttempt.successfulCall as? T`.                                                               |
| `KaCallInfo.singleCallOrNull<T>()`     | `attempt.calls.singleOrNull { it is T }`.                                                                     |
