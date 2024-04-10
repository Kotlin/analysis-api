# KaDelegatedConstructorCall

Represents a call to another constructor within the same class, or to a superclass constructor.
This corresponds to the use of `this(...)` or `super(...)` within a constructor's body to delegate initialization to
another constructor.

## Hierarchy

Inherits [KaFunctionCall](KaFunctionCall.md).

## Members

`val kind: Kind`
: The call kind (`SUPER_CALL` or `THIS_CALL`).