# Annotations

Annotations play a crucial role in Kotlin, providing metadata and influencing code behavior.
The Analysis API allows you to access and analyze annotations applied to both declarations and types.

## KaAnnotated

`KaAnnotated` is an interface exposing a list of annotations. All [types](Types.md) and almost all
[symbols](Symbols.md) implement it.

<code-block lang="mermaid">
graph TD
  KaAnnotated
  KaAnnotated --> KaType
  KaAnnotated --> KaAnnotatedSymbol
  KaAnnotatedSymbol --> KaFileSymbol
  KaAnnotatedSymbol --> KaScriptSymbol
  KaAnnotatedSymbol --> KaDeclarationSymbol
</code-block>

The only property `KaAnnotated` declares is `annotations` of the `KaAnnotationList` type. `KaAnnotationList` itself
is implements a `List<KaAnnotation>`, so you can directly iterate over annotations:

```Kotlin
fun KaSession.processAnnotations(symbol: KaDeclarationSymbol) {
    for (anno in symbol.annotations) {
        // Process the 'annotation'
    }
}
```

`KaAnnotationsList` is not just a list. It can also efficiently check whether an annotation with some `ClassId`
is there:

```Kotlin
fun KaSession.hasDeprecatedAnnotation(symbol: KaDeclarationSymbol) {
    val classId = ClassId.fromString("kotlin/Deprecated")
    return classId in symbol.annotations
}
```

You can also get a list of annotations with a specific `ClassId`. Kotlin allows repeatable annotations, so a list
of them is returned:

```Kotlin
fun KaSession.findDeprecatedAnnotation(symbol: KaDeclarationSymbol): KaAnnotation? {
    val classId = ClassId.fromString("kotlin/Deprecated")
    return symbol.annotations[classId].firstOrNull()
}
```

Finally, `KaAnnotationList` exposes a collection of all annotation `ClassId`s:

```Kotlin
fun KaSession.collectAnnotations(types: List<KaType>): Set<ClassId> {
    return types.flatMapTo(HashSet()) { it.annotations.classIds }
}
```

## Use-Site Targets

Annotations on declarations can have use-site targets, specifying where the annotation applies (e.g., property, field,
or parameter). You can use the `useSiteTarget` property of `KtAnnotation` to access this information.