# KaClassLikeSymbol

Represents a class, object, interface or a type alias declaration.

## Hierarchy

A sealed class.  
Inherits from [KaClassifierSymbol](KaClassifierSymbol.md).

Notable inheritors: [KaClassSymbol](KaClassSymbol.md), [KaTypeAliasSymbol](KaTypeAliasSymbol.md).

## Members

`val classId: ClassId?`
: The fully-qualified name of a declaration, or `null` if the declaration is local.

## Utilities

`val KaClassLikeSymbol.samConstructor: KaSamConstructorSymbol?`
: Associated `KaSamConstructorSymbol` if the given `KaClassLikeSymbol` is a functional interface type (SAM).