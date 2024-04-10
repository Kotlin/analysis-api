# KaNamedFunctionSymbol

Represents a named [function](https://kotlinlang.org/docs/functions.html) declaration, such as a top-level function, a
class method, or a named local function.

## Hierarchy

Inherits from [KaFunctionSymbol](KaFunctionSymbol.md).

## Members

`val name: Name`
: The function name.

`val typeParameters: List<KaTypeParameterSymbol>`
: A list of declared type parameters.

`val isExternal: Boolean`
: `true` if the function is an external function.

`val isInfix: Boolean`
: `true` if the function is an infix function.

`val isInline: Boolean`
: `true` if the function is an inline function.

`val isOverride: Boolean`
: `true` if the function is an override.

`val isSuspend: Boolean`
: `true` if the function is a suspend function.

`val isStatic: Boolean`
: `true` if the function is a static function.

`val isOperator: Boolean`
: `true` if the function is an operator function.

`val isTailRec: Boolean`
: `true` if the function is marked with `tailrec`.

`val isBuiltinFunctionInvoke: Boolean`
: `true` if the function is the `invoke()` method defined on the Kotlin built-in functional type.

`val contractEffects: List<KaContractEffectDeclaration>`
: A list of defined [contracts](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.contracts/).