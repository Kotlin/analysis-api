# References and calls

Analysis API offers two mechanisms for resolving references within Kotlin code: reference resolution and call resolution.
While they both deal with connecting names to declarations, they serve distinct purposes and provide different levels
of information.

## Reference resolution

**Reference resolution** focuses on resolving a reference, such as an identifier or a qualified expression, to the
corresponding declaration symbol. It primarily answers the question, "What declaration does this reference point to?"

To get a reference target, call `resolveToSymbols()` or `resolveToSymbol()` on a `mainReference` of a reference
expression:

```kotlin
val expression: KtReferenceExpression = ...

analyze(expression) {
    val symbols: Collection<KaSymbol> = expression
        .mainReference.resolveToSymbols()

    // Identical to resolveToSymbols().singleOrNull()
    val symbol: KaSymbol? = expression
        .mainReference.resolveToSymbol()
}
```

Normally, each correct reference resolves to a single symbol. In case of candidate ambiguity, though, there might be
several targets.

## Call resolution

**Call resolution** delves deeper into analyzing a call expression. It not only identifies the target declaration but
also provides detailed information about the call, such as substituted parameter and return types and type argument
mappings. 

To get a resolved call information, call the `resolveToCall()` function:

```kotlin
val expression: KtCallExpression = ...

analyze(expression) {
    val callInfo: KaCallInfo? = expression.resolveToCall()
}
```

The resulting `KaCallInfo` is either a `KaSuccessCallInfo` containing a single successfully resolved call,
or a `KaErrorCallInfo` containing a list of candidate calls if there are any, and resolution diagnostic information.

To simplify handling logic, Analysis API offers a few utilities.

`val KaCallInfo.calls: List<KaCall>`
: A list of call candidates. For a successful call, a single resolved call.

`fun <T : KaCall> KaCallInfo.singleCallOrNull(): T?`<br/>
`fun KaCallInfo.singleFunctionCallOrNull(): KaFunctionCall<*>?`<br/>
`fun KaCallInfo.singleVariableAccessCall(): KaVariableAccessCall?`
: Get a single call of the specified type (not necessarily successful).

`fun <T : KaCall> KaCallInfo.successfulCallOrNull(): T?`<br/>
`fun KaCallInfo.successfulFunctionCallOrNull(): KaFunctionCall<*>?`<br/>
`fun KaCallInfo.successfulVariableAccessCall(): KaVariableAccessCall?`
: Get a successful call of the specified type.

## Choosing Between Reference and Call Resolution

The choice between reference and call resolution depends on your specific needs.

* **Use reference resolution when**:
    * You simply need to identify the declaration referenced by a name or expression.
    * You are working with references that are not call expressions (e.g., type references).
* **Use call resolution when**:
    * You require detailed information about a call, such as argument mapping or type arguments.
    * You need to handle overload resolution and type inference.
    * You are working with implicit calls (e.g., `foo()` where `foo` is a variable with a functional type).

In general, call resolution provides more comprehensive information about a call expression, while reference
resolution is more lightweight and suitable for simpler scenarios.