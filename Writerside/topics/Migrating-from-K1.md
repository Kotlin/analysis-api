# Migrating from K1

For many years, the only practical way to analyze Kotlin code in IntelliJ IDEA and other tools was to use the Kotlin
compiler's internals, an unsafe API not designed for external usage.

The Analysis API, on the other hand, offers a much cleaner and robust set of utilities. It exposes almost the same set
of concepts. Thus, if you already have code that depends on the Kotlin compiler, migrating it to the new API should not
be time-consuming. This migration guide outlines the differences between the APIs and explains how to port the
descriptor-based resolution logic to the Analysis API.

Once an IntelliJ plugin has been migrated to the Analysis API, it will need to [declare its compatibility with the K2 
Kotlin mode](#declaring-compatibility-with-the-k2-kotlin-mode). Otherwise, the plugin will not be loaded when the K2
mode is active.

## The Conceptual Difference

The cornerstone of the old compiler API is a `BindingContext`, a universal dictionary:

- `BindingContext` maps syntactic declarations (`KtDeclaration`) to their semantic parts, `DeclarationDescriptor`s. For
  instance, for a `KtFunction` that represents a function in code, there is a `FunctionDescriptor` with semantic
  information, which includes resolved parameter and return types.
- In a similar fashion, a type reference (`KtTypeReference`) is mapped to a `KotlinType` with resolved type attributes.
- For calls, including `KtCallExpression`, there is a `ResolvedCall` object containing data collected by call resolution
  and inference machinery.

A `BindingContext` merely acts as a storage that is filled up during declaration analysis. In the compiler, an instance
of `BindingContext` goes through the whole compilation pipeline, collecting more and more semantic information, and
used later for code generation. The IDE does not, however, analyze the entire project at once, as it would take a lot
of time. Instead, a declaration is analyzed only when some IDE feature needs to understand it better.

Therefore, in the IDE, a `BindingContext` only contains mappings for declarations that have already been analyzed. The
correct filling and use of the dictionary is the caller's responsibility.

Moreover, classes such as `DeclarationDescriptor` and `KotlinType` do not have any specific lifecycle, so there's
nothing stopping them from being passed around or cached. This is unfortunate because these classes usually retain the
entire compiler resolution session, a very heavy tree of objects. As sporadic errors on outdated descriptor usage are
rare, it becomes easy to inadvertently create a substantial memory leak.

The Analysis API significantly simplifies this by offering a single [`analyze {}`](Fundamentals.md#kasession) entry
point. Inside the analysis block, all declarations are analyzed on-demand, eliminating occasional "descriptor was not
found for declaration" errors. Further, entities representing declarations and
types [can only be accessed](Fundamentals.md#kalifetimeowner) from within the owning analysis block. This way,
The Analysis API not only guards against memory leaks but also ensures that all analysis results are consistent.

## Analysis Entry Point

The Kotlin 1.0 compiler itself does not offer any stable code analysis entry points. However, the Kotlin IntelliJ IDEA
plugin, which is built on top of the compiler, does provide several:

```Kotlin
// Simply returns a 'BindingContext' containing "certain" information about the element
fun KtElement.analyze(bodyResolveMode: BodyResolveMode): BindingContext

// Returns the semantic declaration abstraction, calls 'analyze()' under the hood
fun KtDeclaration.resolveToDescriptorIfAny(bodyResolveMode: BodyResolveMode): DeclarationDescriptor?

// Returns the resolved call information, also delegates to 'analyze()'
fun KtElement.resolveToCall(bodyResolveMode: BodyResolveMode): ResolvedCall<out CallableDescriptor>?
```

These are not the only ones available – there are numerous more sophisticated ones,
including `analyzeWithAllCompilerChecks()`, `analyzeWithContent()`, `analyzeInContext()`, and others.

In contrast, the Analysis API offers a single `analyze {}` entry point. Most of the API surface is accessible inside the
lambda, including the `symbol` extension property that maps a `KtDeclaration` to its symbol:

```Kotlin
analyze(declaration) {
    // 'KaSymbol' is similar to 'DeclarationDescriptor'
    val symbol: KaSymbol = declaration.symbol
}
```

This is not just a syntax difference. The Analysis API requires all analysis-related code to be housed in a single
location. You can, of course, extract parts of the logic to separate functions, and even create your set of utilities.
Nevertheless, you cannot freely mix symbols from unrelated analysis sessions.

While this change might seem like a significant new restriction, it actually has always been in place. Careless handling
of `BindingContext` and its contents was often a source of exceptions, incorrect behavior, and leaks. Therefore, the new
API naturally guides you on how to analyze the code correctly.

You can read more about the API entity lifetime in the [KaLifetimeOwner](Fundamentals.md#kalifetimeowner) documentation
section.

## Declarations

Both the old compiler API and the Analysis API are built on top of `PsiElement`, the API in IntelliJ IDEA responsible
for creating syntax trees. However, unlike some other language implementations, Kotlin distinctly separates PSI and
semantic declaration representation. Refer to the [Symbols vs. PSI](Symbols.md#symbols-vs-psi) section for additional
information.

In the old compiler, this semantic representation is called `DeclarationDescriptor`. There are specific interfaces for
each declaration type, including `ClassDescriptor`, `FunctionDescriptor`, and `PropertyDescriptor`. Descriptors are
obtained from a `BindingContext`:

```Kotlin
val descriptor: DeclarationDescriptor =
    bindingContext[BindingContext.DECLARATION_TO_DESCRIPTOR, declaration]
```

In the Analysis API, a concept similar to descriptors is named `KaSymbol`. Just like descriptors, there
are `KaClassSymbol`, `KaFunctionSymbol`, and `KaPropertySymbol`.

To get a symbol for a `KtDeclaration`, simply use the `symbol` extension property.
`symbol` is overloaded for subtypes of `KaSymbol`, meaning that if you call it on some specific declaration type,
you will get a more precise symbol type. For instance:

```Kotlin
val property: KtProperty = ...

analyze(property) {
    val symbol = property.symbol
    // symbol is a 'KaPropertySymbol'
}
```

For a `KtClassOrObject`, however, `symbol` will return just a `KaDeclarationSymbol`.
The reason for this is Kotlin PSI's legacy: A `KtEnumEntry` is a subtype of `KtClassOrObject`, whereas in K2, an enum
entry is a variable. So, you may wish to use `ktClassOrObject.classSymbol` instead, as it will return
a `KaClassSymbol?`.

Approach the [symbol](Symbols.md) documentation for more detailed information about symbols.

### Declaration Names

In the old compiler, `FqName` was often used to store fully-qualified declaration names. Although it is a
straightforward abstraction, `FqName` cannot differentiate between package and classifier components. For instance,
in `foo.Bar.Baz`, `Bar` could either be a package or an outer class name. While Kotlin's coding
conventions [discourage](https://kotlinlang.org/docs/coding-conventions.html#naming-rules) capitalized package names,
technically it remains possible. Consequently, the Analysis API employs a different abstraction for storing qualified
names, namely `ClassId` for classes and `CallableId` for functions and properties.

To construct a `ClassId`, merely pass its text representation to `ClassId.fromString()`. The slashes `/` separate
package components, whereas dots `.` distinguish nested class names.

```Kotlin
val intClassId = ClassId.fromString("kotlin/Int")
val nestedClassId = ClassId.fromString("foo/bar/Outer.Nested")
```

The [`StandardClassIds`](https://github.com/JetBrains/kotlin/blob/master/core/compiler.common/src/org/jetbrains/kotlin/name/StandardClassIds.kt)
class provides `ClassId`s for many common class names from the Kotlin standard library.

You can construct a `CallableId` by supplying either an outer `ClassId` or a package `FqName` and a callable name.

```Kotlin
val suspendCallableId = CallableId(FqName("kotlin"), Name.identifier("suspend"))
val equalsCallableId = CallableId(ClassId("kotlin/Any"), Name.identifier("equals"))
```

### Classes

Class-related hierarchies are quite similar in both K1 and K2 APIs.

<code-block lang="mermaid">
graph LR
  ClassifierDescriptor
  ClassifierDescriptor --> ClassDescriptor
  ClassifierDescriptor --> TypeParameterDescriptor
  ClassifierDescriptor --> TypeAliasDescriptor
</code-block>

The difference is that in the Analysis API, named and anonymous classes have distinct subclasses.

<code-block lang="mermaid">
graph LR
  KaClassifierSymbol
  KaClassifierSymbol --> KaClassSymbol
  KaClassSymbol --> KaNamedClassSymbol
  KaClassSymbol --> KaAnonymousObjectSymbol
  KaClassifierSymbol --> KaTypeParameterSymbol
  KaClassifierSymbol --> KaTypeAliasSymbol
</code-block>

Getting simple and qualified class names
: Old API: `classDescriptor.name`, `classDescriptor.classId`, `classDescriptor.fqNameSafe`
: Analysis API: `classSymbol.name`, `classSymbol.classId` (`FqName` represents nested classes ambiguously, always
use `ClassId`)

Checking class kind
: Old API: `classDescriptor.kind == ClassKind.INTERFACE`
: Analysis API: `classSymbol.classKind == KaClassKind.INTERFACE`

Checking ordinary class traits
: Old API: `classDescriptor.isData`
: Analysis API: `(classSymbol as? KaNamedClassSymbol)?.isData` (anonymous classes cannot be `data`)

Getting class supertypes
: Old API: `classDescriptor.typeConstructor.supertypes`
: Analysis API: `classSymbol.superTypes`
: There is no `TypeConstructor` abstraction in the Analysis API. Use symbols directly.

Getting class declarations
: Old API: `classDescriptor.unsubstitutedMemberScope.getContributedDescriptors()`
: Analysis API: `classSymbol.memberScope.declarations` (or `classifiers`, `callables` for specific kinds)

### Functions

Both APIs have almost the same set of classes representing functions, constructors and property accessors.

<code-block lang="mermaid">
graph LR
  FunctionDescriptor
  FunctionDescriptor --> SimpleFunctionDescriptor
  SimpleFunctionDescriptor --> AnonymousFunctionDescriptor
  SimpleFunctionDescriptor --> SamConstructorDescriptor
  FunctionDescriptor --> ConstructorDescriptor
  FunctionDescriptor --> VariableAccessorDescriptor
  VariableAccessorDescriptor --> PropertyAccessorDescriptor
  PropertyAccessorDescriptor --> PropertyGetterDescriptor
  PropertyAccessorDescriptor --> PropertySetterDescriptor
</code-block>

In the Analysis API, the hierarchy is rather flat. The most significant change is that anonymous function is not an
ordinary "named" function anymore.

<code-block lang="mermaid">
graph LR
  KaFunctionSymbol
  KaFunctionSymbol --> KaNamedFunctionSymbol
  KaFunctionSymbol --> KaAnonymousFunctionSymbol
  KaFunctionSymbol --> KaConstructorSymbol
  KaFunctionSymbol --> KaSamConstructorSymbol
  KaFunctionSymbol --> KaPropertyAccessorSymbol
  KaPropertyAccessorSymbol --> KaPropertyGetterSymbol
  KaPropertyAccessorSymbol --> KaPropertySetterSymbol
</code-block>

Getting simple and qualified callable names
: Old API: `functionDescriptor.fqNameSafe`
: Analysis API: `functionDescriptor.callableId`

Getting parameter and return types
: Old API: `functionDescriptor.valueParameters.map { it.type }`, `functionDescriptor.returnType`
: Analysis API: `functionSymbol.valueParameters.map { it.returnType }`, `functionSymbol.returnType`

Checking function visibility
: Old API: `functionDescriptor.visibility == DescriptorVisibilities.PUBLIC`
: Analysis API: `functionSymbol.visibility == KaSymbolVisibility.PUBLIC`

Checking function traits
: Old API: `functionDescriptor.isInline`
: Analysis API: `functionSymbol.isInline`

### Variables

In the old API, the variable hierarchy was quite basic.

<code-block lang="mermaid">
graph LR
  FieldDescriptor
  VariableDescriptor
  VariableDescriptor --> LocalVariableDescriptor
  VariableDescriptor --> PropertyDescriptor
  PropertyDescriptor --> JavaPropertyDescriptor
  PropertyDescriptor --> SyntheticJavaPropertyDescriptor
  VariableDescriptor --> ValueParameterDescriptor
</code-block>

In the Analysis API, backing fields, receiver parameters enum entries became a part of the variable hierarchy.
The changes reflect evolution of these concepts in the language and the K2 compiler.

<code-block lang="mermaid">
graph LR
  KaVariableSymbol
  KaVariableSymbol --> KaLocalVariableSymbol
  KaVariableSymbol --> KaPropertySymbol
  KaPropertySymbol --> KaKotlinPropertySymbol
  KaPropertySymbol --> KaSyntheticJavaPropertySymbol
  KaVariableSymbol --> KaParameterSymbol
  KaParameterSymbol --> KaValueParameterSymbol
  KaParameterSymbol --> KaReceiverParameterSymbol
  KaVariableSymbol --> KaBackingFieldSymbol
  KaVariableSymbol --> KaJavaFieldSymbol
  KaVariableSymbol --> KaEnumEntrySymbol
</code-block>

Getting getter and setter
: Old API: `propertyDescriptor.getter`, `propertyDescriptor.setter`
: Analysis API: `propertySymbol.getter`, `propertySymbol.setter`

Getting a return type
: Old API: `propertyDescriptor.type`
: Analysis API: `propertySymbol.returnType`

### Calls and references

Check out the difference between reference and call resolution in the
[References and calls](References-And-Calls.md) article.

The old API offered a single `ResolveCall` class that represented all kinds of calls (successful and error calls,
simple and compound calls). For compound calls, `ResolveCall` itself represents only one of calls,
while additional data was available in quite obscure places, like `CallTransformer.CallForImplicitInvoke`.

The Analysis API makes the distinction between calls explicit, making it harder to forget about more sophisticated
call kinds.

<code-block lang="mermaid">
graph TB
  KaCall
  KaCall --> KaCallableMemberCall
  KaCallableMemberCall --> KaVariableAccessCall
  KaCallableMemberCall --> KaFunctionCall
  KaFunctionCall --> KaSimpleFunctionCall
  KaFunctionCall --> KaAnnotationCall
  KaFunctionCall --> KaDelegatedConstructorCall
  KaCall --> KaCompoundVariableAccessCall
  KaCall --> KaCompoundArrayAccessCall
</code-block>

In addition, the Analysis API separates successful and error calls. In the IDE, the user edits and refactors code all
the time, and source files often contain unresolved or ambiguous references. Handling them properly (or skipping them)
during static checks is important.

Resolving a reference
: Old API: `bindingContext[BindingContext.REFERENCE_TARGET, referenceExpression]`
: Analysis API: `referenceExpression.mainReference.resolveToSymbol()`

Resolving a successful call
: Old API: `expression.getResolvedCall(bindingContext)?.takeIf { it.isReallySuccess() }`
: Analysis API: `expression.resolveToCall().successfulCallOrNull()`

Getting parameter-argument mapping
: Old API:
```Kotlin
val call = unaryExpression.getResolvedCall(bindingContext) ?: return
call.valueArguments
```
: Analysis API:
```Kotlin
val call = expression.resolveToCall()?.successfulFunctionCallOrNull() ?: return
call.argumentMapping
```

Getting dispatch and extension receivers
: Old API:
```Kotlin
val call: ResolvedCall<*> = ...
operatorCall.dispatchReceiver
operatorCall.extensionReceiver
```
: Analysis API:
```Kotlin
val call: KaCallableMemberCall<*, *> = ...
call.partiallyAppliedSymbol.dispatchReceiver
call.partiallyAppliedSymbol.extensionReceiver
```

### Types

The old compiler had a sophisticated hierarchy of `KotlinType`s, including wrapped, deferred and delegating types.
The Analysis API provides much simpler API that actually represents all language types.

<code-block lang="mermaid">
graph LR
  KaType
  KaType --> KaClassType
  KaClassType --> KaUsualClassType
  KaClassType --> KaFunctionType
  KaType --> KaTypeParameterType
  KaType --> KaFlexibleType
  KaType --> KaIntersectionType
  KaType --> KaCapturedType
  KaType --> KaDynamicType
  KaType --> KaErrorType
  KaErrorType --> KaClassErrorType
</code-block>

The `KaType` is a base interface for all Kotlin types. The most common type kind is a `KaClassType`, which represents
not-null and nullable class types, such as `kotlin.Int` or `List<String>?`.

Check the [type](Types.md) documentation for more details.

Resolving a type reference
: Old API: `context[BindingContext.TYPE, typeReference]`
: Analysis API: `typeReference.type`

Getting an expression type
: Old API: `expression.getType(bindingContext)`
: Analysis API: `expression.expressionType`

Checking for a built-in type
: Old API: `KotlinBuiltIns.isUnit(type)`
: Analysis API: `type.isUnitType`

Checking for a primitive type
: Old API: `KotlinBuiltIns.isPrimitiveType(type)`
: Analysis API: `type.isPrimitive`

### Misc

Getting a containing declaration
: Old API: `descriptor.containingDeclaration`
: Analysis API: `symbol.containingDeclaration` or `symbol.containingSymbol`

Checking for annotation presence
: Old API: `descriptor.annotations.hasAnnotation(FqName("kotlin.jvm.JvmName"))`
: Analysis API: `ClassId.fromString("kotlin/jvm/JvmName") in symbol.annotations`
: Check the [Annotations](Annotations.md) documentation for more details.

## Example

Below, the same annotation check is implemented with the old compiler API, and with the Analysis API.

### Using the old compiler API

```Kotlin
val SPECIAL_ANNOTATION_NAME = FqName("my.app.Special")

fun hasAnnotation(declaration: KtDeclaration): Boolean {
    val bindingContext = declaration.analyze()
    val descriptor = bindingContext[BindingContext.DECLARATION_TO_DESCRIPTOR, declaration]
        ?: return false
    
    return descriptor.annotations.hasAnnotation(SPECIAL_ANNOTATION_NAME)
}
```

### Using Analysis API

```Kotlin
val SPECIAL_ANNOTATION_CLASS_ID = ClassId.fromString("my/app/Special")

fun hasAnnotation(declaration: KtDeclaration): Boolean {
    analyze(declaration) {
        return SPECIAL_ANNOTATION_CLASS_ID in declaration.symbol.annotations
    }
}
```

## Declaring compatibility with the K2 Kotlin mode

The Kotlin IntelliJ plugin assumes that a dependent third-party plugin *does not* support K2 Kotlin out of the box. Such
incompatible plugins will not be loaded if the K2 mode is currently enabled.

Once a plugin has been migrated to the Analysis API, a setting should be added to its `plugin.xml` to declare its
compatibility with the K2 mode. Even if the plugin does not use any of the old K1 analysis functions and no migration to 
the Analysis API is needed, compatibility with the K2 Kotlin plugin should be declared explicitly nonetheless.

Starting from IntelliJ 2024.2.1 (Preview), the following setting in the `plugin.xml` can be used to declare 
compatibility with the K2 mode:

```xml
<extensions defaultExtensionNs="org.jetbrains.kotlin">
    <supportsKotlinPluginMode supportsK2="true" />
</extensions>
```

It is also possible to declare compatibility with *only* the K2 mode:

```xml
<extensions defaultExtensionNs="org.jetbrains.kotlin">
    <supportsKotlinPluginMode supportsK1="false" supportsK2="true" />
</extensions>
```

Currently, the default setting for `supportsK1` is `true` and for `supportsK2` is `false`.

To test it locally when using the [IntelliJ Platform Gradle Template](https://github.com/JetBrains/intellij-platform-plugin-template), the `platformVersion` in `gradle.properties` should be set to at least `242.21829.15`, which corresponds to `IntelliJ 2024.2.1 (Preview)`.

A number of third-party plugins may already be enabled in the K2 mode without a `supportsK2` declaration. The IntelliJ 
Kotlin plugin keeps an [internal list](https://github.com/JetBrains/intellij-community/blob/master/platform/core-impl/resources/pluginsCompatibleWithK2Mode.txt) 
of plugins which are known to be compatible with the K2 mode as they do not use Kotlin analysis. The authors of these
plugins should not be surprised if their plugin already works in the K2 mode. However, it's still advised to declare K2
support explicitly.
