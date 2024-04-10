# KaSimpleFunctionCall

Represents a simple, direct call to a function, without any delegation or special syntax involved.

## Hierarchy

Inherits [KaFunctionCall](KaFunctionCall.md).

## Members

`val isImplicitInvoke: Boolean`
: `true` if the call is an [implicit invoke call](https://kotlinlang.org/docs/operator-overloading.html#invoke-operator)
on a value that has an `invoke` member function.