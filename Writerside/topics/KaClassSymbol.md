# KaClassSymbol

Represents a class, object, or interface declaration.

## Use Cases

* **Analyzing class hierarchies.** Use `superTypes` to navigate the inheritance hierarchy of a class and analyze its
  relationships with other classes and interfaces.
* **Exploring class members.** Use `declaredMemberScope` and `memberScope` to access members of a class,
including functions, properties, and nested classes.

## Hierarchy

Inherits from [KaClassLikeSymbol](KaClassLikeSymbol.md).

Notable inheritors: [KaNamedClassSymbol](KaNamedClassSymbol.md), [KaAnonymousObjectSymbol](KaAnonymousObjectSymbol.md).

## Members

`val classKind: KaClassKind`
: The class kind (ordinary class, interface, enum class, etc.).

`val superTypes: List<KaType>`
: A list of the direct supertypes of the class. If the class has no explicit supertypes, the supertype will be `Any`, or 
a special supertype such as `Enum` for enum classes.

## Type utilities

`fun KaClassSymbol.isSubClassOf(superClass: KaClassSymbol): Boolean`
: Check if the given class has `superClass` as its superclass in its inheritance hierarchy.

`fun KaClassSymbol.isDirectSubClassOf(superClass: KaClassSymbol): Boolean`
: Check if the given class has `superClass` listed as its direct superclass.

## Scope utilities

`val KaDeclarationContainerSymbol.memberScope: KaScope`
: A scope with non-static callables and nested classes. Also includes members inherited from the supertypes.

`val KaDeclarationContainerSymbol.declaredMemberScope: KaScope`
: A scope containing non-static callables and nested classes.
Unlike `memberScope`, the returned scope does **not** contain members inherited from supertypes.

`val KaDeclarationContainerSymbol.staticMemberScope: KaScope`
: A scope containing static members, possibly including members from supertypes.
The behavior differs based on whether the declaration is a Kotlin or Java one.
: For **Kotlin** classes, the scope contains static declarations declared only in the given declaration itself.
: For **Java** classes, the scope also contains callables from supertypes, excluding static callables from super-interfaces.
This follows Kotlin's rules about static inheritance in Java classes, where static callables are propagated from
superclasses, but nested classes are not.

`val KaDeclarationContainerSymbol.staticDeclaredMemberScope: KaScope`
: A scope containing static members of the given declaration. Unlike `staticMemberScope`, the returned scope does
**not** contain members from supertypes.

`val KaDeclarationContainerSymbol.combinedMemberScope: KaScope`
: A scope containing all declarations from both `memberScope` and `staticMemberScope`.

`val KaDeclarationContainerSymbol.combinedDeclaredMemberScope: KaScope`
: A scope containing both non-static and static members of the given declaration.
Unlike `combinedMemberScope`, the returned scope does **not** contain members from supertypes.

`val KaDeclarationContainerSymbol.delegatedMemberScope: KaScope`
: A scope containing synthetic fields created by interface delegation.

## Other utilities

`val KaClassSymbol.annotationApplicableTargets: Set<KotlinTarget>?`
: A set of applicable targets for an annotation class symbol, or `null` if the symbol is not an annotation class.
: **Experimental API**.