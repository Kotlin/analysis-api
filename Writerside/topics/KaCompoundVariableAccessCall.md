# KaCompoundVariableAccessCall

`KaCompoundVariableAccessCall` represents a compound access to a mutable variable. Such accesses combine reading,
modifying, and writing back the variable's value in a single expression using operators like `+=`, `-=`, `++`, or `--`.

```Kotlin
var i = 0
i += 1
i++
```

> An `<op>Assign` operator (for example, `MutableList.plusAssign` for `+=`) is represented as a plain
> [](KaFunctionCall.md), not as a `KaCompoundVariableAccessCall`. Only the three-step read-modify-write
> form (the `plus` + write path) is a compound call.

## Hierarchy

Inherits [](KaMultiCall.md). (It also inherits the [legacy](Legacy-Resolution-API.md) `KaCall` for historical
reasons.)

## Members

`val variableCall: KaVariableAccessCall`
: The variable read/write part of the compound expression &mdash; a full [](KaVariableAccessCall.md).

`val compoundOperation: KaCompoundOperation`
: The compound operation kind. See [](KaCompoundOperation.md). `compoundOperation.operationCall`
gives the resolved operator function call (e.g. `Int.plus` for `+=` or `Int.inc` for `++`); the operation call is also
available directly on the inherited `KaCompoundAccessCall.operationCall`.

`val variablePartiallyAppliedSymbol: KaPartiallyAppliedVariableSymbol<KaVariableSymbol>` &mdash; **deprecated**
: The legacy wrapper around the variable's symbol. Replaced by `variableCall`.
