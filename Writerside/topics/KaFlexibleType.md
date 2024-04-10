# KaFlexibleType

Represents a [flexible type](https://kotlinlang.org/spec/type-system.html#flexible-types)
(or a so-called [platform type](https://kotlinlang.org/docs/java-interop.html#null-safety-and-platform-types)), a range
of types from the `lowerBound` to the `upperBound` (both inclusive).

Also check [nullability utilities](KaType.md#nullability-utilities) in `KaType`.

## Hierarchy

Inherits from [KaType](KaType.md).

## Members

`val lowerBound: KaType`
: The lower bound (such as, `String` in `String!`).

`val upperBound: KaType`
: The upper bound (such as, `String?` in `String!`).