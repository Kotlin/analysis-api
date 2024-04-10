# KaCompoundArrayAccessCall

Represents a compound array-like access convention involving calls both to `get()` and `set()` functions,
e.g., `a[1] += "foo"`.

## Members

`val getPartiallyAppliedSymbol: KaPartiallyAppliedFunctionSymbol<KaNamedFunctionSymbol>`
: The `get` function that's invoked when reading values corresponding to the given `indexArguments`.

`val setPartiallyAppliedSymbol: KaPartiallyAppliedFunctionSymbol<KaNamedFunctionSymbol>`
: The `set` function that's invoked when writing values corresponding to the given [indexArguments] and computed value from the
* operation.

`val compoundOperation: KaCompoundOperation`
: The compound operation kind. Also see [KaCompoundOperation](KaCompoundVariableAccessCall.md#kacompoundoperation).