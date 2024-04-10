# KaDeclarationSymbol

Represents a declaration, such as a class, function or property.

## Hierarchy

Inherits from [KaSymbol](KaSymbol.md), [KaAnnotated](Annotations.md#kaannotated).

## Members

`val annotations: KaAnnotationList`
: A list of applied annotations.

`val modality: KaSymbolModality`
: Effective declaration modality (e.g., final, sealed or open).

`val visibility: KaSymbolVisibility`
: Effective declaration visibility (e.g., public, protected or private).

`val isExpect: Boolean`
: `true` if the declaration is an `expect` one.

`val isActual: Boolean`
: `true` if the declaration is an `actual `one.

`val KaDeclarationSymbol.typeParameters: List<KaTypeParameterSymbol>`
: A list of type parameters for `KaTypeParameterOwnerSymbol`, an empty list otherwise.
: **Experimental API**.

## Utilities

`fun KaDeclarationSymbol.render(renderer: KaDeclarationRenderer = KaDeclarationRendererForSource.WITH_QUALIFIED_NAMES): String`
: Render the given declaration to a `String`. The particular rendering strategy is defined by the `renderer`.
: **Experimental API**.