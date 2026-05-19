# KaCompoundOperation

`KaCompoundOperation` describes the kind of compound update applied in a `+=` / `-=` / `*=` / `/=` / `%=` assignment or
a `++` / `--` increment/decrement. It is exposed by both [](KaCompoundVariableAccessCall.md)
and [](KaCompoundArrayAccessCall.md) through their `compoundOperation` field.

## Hierarchy

<code-block lang="mermaid">
graph TB
  KaCompoundOperation
  KaCompoundOperation --> KaCompoundAssignOperation
  KaCompoundOperation --> KaCompoundUnaryOperation
</code-block>

## Members

`val operationCall: KaFunctionCall<KaNamedFunctionSymbol>`
: The call of the function that computes the value for this compound access &mdash; the `plus` for `+=`, the `inc` for
`++`, and so on. This is also exposed directly on `KaCompoundAccessCall.operationCall` for convenience.

The legacy `operationPartiallyAppliedSymbol` accessor is `@Deprecated`. Use `operationCall` instead.

## `KaCompoundAssignOperation`

Represents a [compound assignment](https://kotlinlang.org/docs/operator-overloading.html#augmented-assignments) that
reads, computes, and writes back. Note that direct calls to `<op>Assign` operator functions (like
`MutableList.plusAssign`) are *not* represented as a compound operation &mdash; they are simple `KaFunctionCall`s.

`val kind: Kind`
: One of `PLUS_ASSIGN`, `MINUS_ASSIGN`, `TIMES_ASSIGN`, `DIV_ASSIGN`, `REM_ASSIGN`.

`val operand: KtExpression`
: The right-hand-side operand. The left-hand side lives in the parent `KaVariableAccessCall` /
`KaCompoundArrayAccessCall`.

## `KaCompoundUnaryOperation`

Represents a [compound unary access](https://kotlinlang.org/docs/operator-overloading.html#increments-and-decrements)
&mdash; `++` or `--` &mdash; that reads, increments/decrements, and writes back.

`val kind: Kind`
: `INC` or `DEC`.

`val precedence: Precedence`
: Whether the operator is `PREFIX` (`++a`) or `POSTFIX` (`a++`).
