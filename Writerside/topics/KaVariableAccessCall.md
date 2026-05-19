# KaVariableAccessCall

`KaVariableAccessCall` represents a simple access to a variable or property within Kotlin code &mdash; reading or
writing the value.

## Hierarchy

Inherits [](KaSingleCall.md). (For historical reasons it also inherits the
[legacy](Legacy-Resolution-API.md) `KaCallableMemberCall`; new code should treat `KaVariableAccessCall` as a
`KaSingleCall` and use the inline accessors documented there.)

## Members

In addition to the [](KaSingleCall.md) members, `KaVariableAccessCall` adds the access kind and a
context-sensitive-resolution flag.

`val kind: Kind`
: The kind of access &mdash; `Kind.Read` or `Kind.Write` (with `Write.value: KtExpression?` exposing the right-hand
side of the assignment).

`val isContextSensitive: Boolean`
: Whether the call was resolved using the
[context-sensitive resolution](https://github.com/Kotlin/KEEP/issues/379) feature.

### `Kind`

Sealed:

`Kind.Read`
: The variable is being read.

`Kind.Write`
: The variable is being written. `value: KtExpression?` is the new value; `null` only if the assignment is incomplete
and lacks the new value in source code.
