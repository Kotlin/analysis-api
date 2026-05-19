# KaSimpleFunctionCall

<warning>
<code>KaSimpleFunctionCall</code> is <b>deprecated</b>. Use <a href="KaFunctionCall.md"/> directly, and check for
an implicit invoke with <code>call is KaImplicitInvokeCall</code> (see <a href="KaImplicitInvokeCall.md"/>).
See <a href="Migrating-Resolution-API.md"/>.
</warning>

Represents a simple, direct call to a function, without any delegation or special syntax involved.

## Hierarchy

Inherits [](KaFunctionCall.md).

## Members

`val isImplicitInvoke: Boolean` &mdash; **deprecated**
: `true` if the call is an [implicit invoke call](https://kotlinlang.org/docs/operator-overloading.html#invoke-operator)
on a value that has an `invoke` member function. Replaced by the type check `call is KaImplicitInvokeCall`.
