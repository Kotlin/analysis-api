# KaFunctionType

Represents Kotlin function types, such as `(String) -> Int` or `suspend () -> List<Any>`.

## Hierarchy

Inherits from [KaClassType](KaClassType.md).

## Members

`val isSuspend: Boolean`
: `true` if the type is a suspend function type.

`val isReflectType: Boolean`
: `true` if the type is a reflect function type (`kotlin.reflection.KFunctionN`).

`val arity: Int`
: The number of type parameters.

`val parameterTypes: List<KaType>`
: A list of parameter types. Not to confuse with `typeArguments` which also include the function return type.

`val returnType: KaType`
: The function return type.

`val hasReceiver: Boolean`
: `true` if the given type is an extension function type.

`val receiverType: KaType?`
: The extension receiver type, or `null` if the given type is not an extension function type.

`val hasContextReceivers: Boolean`
: `true` if the function type has context receiver parameters.
: **Experimental API**.

`val contextReceivers: List<KaContextReceiver>`
: A list of context receiver parameters.
: **Experimental API**.