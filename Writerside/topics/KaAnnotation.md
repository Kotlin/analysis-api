# KaAnnotation

Represents an [annotation](https://kotlinlang.org/docs/annotations.html) call, such as `@JvmName("foo")`.

## Members

`val classId: ClassId?`
: The qualified annotation class name, or `null` if the annotation call is unresolved.

`val constructorSymbol: KaConstructorSymbol?`
: The called annotation constructor, or `null` if the annotation call is unresolved.

`val hasArguments: Boolean`
: `true` if the annotation call has one or more arguments.

`val arguments: List<KaNamedAnnotationValue>`
: A list of arguments passed to the annotation constructor.

`val psi: KtCallElement?`
: The annotation call `PsiElement`. Only defined for annotations in source files, for libraries it always returns `null`.

`val useSiteTarget: AnnotationUseSiteTarget?`
: The [use-site target](https://kotlinlang.org/docs/annotations.html#annotation-use-site-targets), if specified.