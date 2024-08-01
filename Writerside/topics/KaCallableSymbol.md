# KaCallableSymbol

A base class for symbols that represent callable declarations, such as functions and properties.

## Hierarchy

A sealed class.  
Inherits from [KaDeclarationSymbol](KaDeclarationSymbol.md).

Notable inheritors: [KaFunctionSymbol](KaFunctionSymbol.md), [KaVariableSymbol](KaVariableSymbol.md).

## Members

`val callableId: CallableId?`
: The fully-qualified name of a declaration, or `null` if the declaration is a local one.

`val returnType: KaType`
: The declaration's return type. For properties, the type of the property.

`val isExtension: Boolean`
: `true` if the declaration is an extension function or an extension property.

`val receiverParameter: KaReceiverParameterSymbol?`
: The receiver parameter, or `null` if the declaration is not an extension.

## Type utilities

`val KaCallableSymbol.receiverType: KaType?`
: The receiver parameter type, or `null` if the declaration is not an extension.

## Relation utilities

`val KaCallableSymbol.directlyOverriddenSymbols: Sequence<KaCallableSymbol>`
: A sequence of declarations directly overridden by the given declaration.
: E.g., if `A.foo` overrides `B.foo`, and `B.foo` overrides `C.foo`, only `B.foo` will be returned as a directly
overridden declaration for `C.foo`.

`val KaCallableSymbol.allOverriddenSymbols: Sequence<KaCallableSymbol>`
: A sequence of declarations overridden by the given declaration, both directly and indirectly.
: E.g., if `A.foo` overrides `B.foo`, and `B.foo` overrides `C.foo`, both `A.foo` and `B.foo` will be returned as
overridden declarations for `C.foo`.

`val KaCallableSymbol.fakeOverrideOriginal: KaCallableSymbol`
: The original declared symbol for a substitution or intersection override.
: Fake overrides are unwrapped until the original declared symbol is found. For callables that are not fake overrides,
returns the given callable itself.

`val KaCallableSymbol.intersectionOverriddenSymbols: List<KaCallableSymbol>`
: ```Kotlin
interface Foo<T> { fun foo(value: T) }
interface Bar { fun foo(value: String) }
interface Both : Foo<String>, Bar
```
: The `Both` interface contains an automatically generated intersection override declaration `foo()`.