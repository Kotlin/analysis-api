# Java/Kotlin Bridging

<note>Experimental API. Subject to changes.</note>

While Analysis API exposes declarations and types from the Kotlin standpoint, it works also with Java source and library
declarations. The API provides a set of utilities for converting between Kotlin and Java views of declarations.

## Types

In IntelliJ IDEA, `PsiType` is a representation for Java types. Conceptually, it is similar to [`KaType`](KaType.md).
Analysis API provides mapping between the two representations.

`fun PsiType.asKaType(useSitePosition: PsiElement): KaType?`
: Convert the given Java type to a `KaType`.
`useSitePosition` is the context element used to gather additional information related to the Java type usage.
: **Experimental API**.

`fun KaType.asPsiType(useSitePosition: PsiElement, allowErrorTypes: Boolean, mode: KaTypeMappingMode = KaTypeMappingMode.DEFAULT, isAnnotationMethod: Boolean = false, suppressWildcards: Boolean? = null, preserveAnnotations: Boolean = true): PsiType?`
: Convert the given Kotlin type to a `PsiType.`
: `useSitePosition` is used to determine if the local type needs to be approximated.
: **Experimental API**.

`fun KaType.mapToJvmType(mode: TypeMappingMode = TypeMappingMode.DEFAULT): Type`
: Convert the given Kotlin type to a JVM [ASM](https://asm.ow2.io/) type.
: **Experimental API**.

`val KaType.isPrimitiveBacked: Boolean`
: `true` if the type is backed by a primitive JVM type.
: **Experimental API**.

## Symbols

Analysis API can create symbols for Java declarations.

`val PsiClass.namedClassSymbol: KaNamedClassSymbol?`
: Map a Java class to a class symbol. Always `null` for anonymous classes and type parameters (that are also
`PsiClass`es).
: **Experimental API**.

`val PsiMember.callableSymbol: KaCallableSymbol?`
: Map a Java method or a field to a callable symbol. Always `null` for local Java declarations.
: **Experimental API**.

## Other utilities

`val KaCallableSymbol.containingJvmClassName: String?`
: The fully qualified class name containing the callable (in the `foo.bar.Class.Companion` format).
: **Experimental API**.

`val KaPropertySymbol.javaGetterName: Name`
: The JVM getter method name for the given property symbol.

`val KaPropertySymbol.javaSetterName: Name?`
: The JVM setter method name for the given property symbol.