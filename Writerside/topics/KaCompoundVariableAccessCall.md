# KaCompoundVariableAccessCall

Represents a compound access to a mutable variable within Kotlin code. These accesses
combine reading, modifying, and writing back the variable's value in a single expression, using operators
like `+=`, `-=`, `++`, or `--`.

## Hierarchy

Inherits [KaCall](KaCall.md).

## Members

`val compoundOperation: KaCompoundOperation`
: The compound operation kind.

## `KaCompoundOperation`

The `compoundOperation` property returns an instance of `KaCompoundOperation` which might be:

* `KaCompoundAssignOperation`: A compound assignment operation (`+=`, `*=`, etc.).
* `KaCompoundUnaryOperation`: An infix and postfix increment (`++`) and decrement (`--`) operations.