# KaCallableMemberCall

<warning>
<code>KaCallableMemberCall</code> is the <b>legacy</b> base for member-callable call types. New code should treat the
concrete call types (<a href="KaFunctionCall.md"/>, <a href="KaVariableAccessCall.md"/>, ...) as
<a href="KaSingleCall.md"/> instances and use the inline accessors there. The
<code>partiallyAppliedSymbol</code> member is <code>@Deprecated</code>.
</warning>

## Hierarchy

Inherits [](KaCall.md).

## Members

`val partiallyAppliedSymbol: KaPartiallyAppliedSymbol<S, C>` &mdash; **deprecated**
: A symbol wrapper, containing substituted declaration signature (parameter types for functions, return type for
functions and properties), and the actual dispatch receiver. Replaced by inline accessors on
[](KaSingleCall.md) (`signature`, `dispatchReceiver`, `extensionReceiver`, `contextArguments`).

`val typeArgumentsMapping: Map<KaTypeParameterSymbol, KaType>`
: A map containing type arguments, including the inferred ones. Available with the same name on
[](KaSingleCall.md).
