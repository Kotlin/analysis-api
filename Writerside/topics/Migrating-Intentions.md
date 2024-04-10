# Migrating Intentions

This guide outlines key steps for migrating intentions from the classic (K1) API to the new Kotlin Analysis API (K2).

## Applicability

1. **`isApplicableTo` to `isApplicableByPsi`**: Replace the `isApplicableTo` method with `isApplicableByPsi`. This
   method should perform lightweight checks using only PSI information, avoiding resolve operations for performance
   reasons.

```kotlin
// K1
override fun isApplicableTo(element: KtBinaryExpression, caretOffset: Int): Boolean {
    return element.isConcatenation() 
         && !element.parent.isConcatenation() 
         && !element.isInsideAnnotationEntryArgumentList()
}

// K2
override fun isApplicableByPsi(element: KtBinaryExpression): Boolean =
    element.operationToken == KtTokens.PLUS && !element.isInsideAnnotationEntryArgumentList()
```

2. **Resolve-based checks**: Move any resolve-based checks from `isApplicableTo` to `prepareContext`. This method
   leverages the K2 API within an `KtAnalysisSession` to perform more complex analysis.

```kotlin
// K2
context(KtAnalysisSession)
override fun prepareContext(element: KtBinaryExpression): Unit? {
    val parent = element.parent
    val isApplicable = element.getKtType()?.isString == true && 
         (parent !is KtBinaryExpression || parent.operationToken != KtTokens.PLUS || parent.getKtType()?.isString == false)
    return isApplicable.asUnit
}
```

3. **Applicability Range**: Implement the `getApplicableRanges` method to define the text ranges where the intention is
   available. You can utilize existing ranges from `ApplicabilityRanges` or create custom ones.

```kotlin
// K2
override fun getApplicableRanges(element: KtProperty): List<TextRange> =
    listOf(TextRange(0, element.initializer!!.startOffsetInParent))
```

### Application

1. **`applyTo` to `invoke`**: Replace the `applyTo` method with `invoke`. This method receives a `ModPsiUpdater` to
   perform PSI modifications and editor operations.

```kotlin
// K1
override fun applyTo(element: KtBinaryExpression, editor: Editor?) {
    val buildStringCall = convertConcatenationToBuildStringCall(element)
    ShortenReferences.DEFAULT.process(buildStringCall)
}

// K2
override fun invoke(
    actionContext: ActionContext,
    element: KtBinaryExpression,
    elementContext: Unit,
    updater: ModPsiUpdater,
) {
    val buildStringCall = convertConcatenationToBuildStringCall(element)
    shortenReferences(buildStringCall)
    updater.moveCaretTo(buildStringCall.endOffset)
}
```

### Context

**Context Object**: Define a data class to hold any necessary information for the intention's application. This class
should be returned by `prepareContext` and passed to `invoke`.

```kotlin
// K2
data class Context(
    val propertyType: String?,
)
```

### Example Migration

Consider this simplified intention to convert a property to a function:

```kotlin
// Classic API
class PropertyToFunctionIntention : SelfTargetingOffsetIndependentIntention<KtProperty>(KtProperty::class.java) {
    override fun isApplicableTo(element: KtProperty): Boolean = element.isLocal && element.getter == null
    
    override fun applyTo(element: KtProperty, editor: Editor?) {
        val factory = KtPsiFactory(element)
        val function = factory.createFunction("fun ${element.name}() = ${element.initializer?.text}")
        element.replace(function)
    }
}

// K2 API
class PropertyToFunctionIntention : KotlinApplicableModCommandAction<KtProperty, Unit>(KtProperty::class) {
    override fun isApplicableByPsi(element: KtProperty): Boolean = element.isLocal && element.getter == null

    context(KtAnalysisSession)
    override fun prepareContext(element: KtProperty): Unit? {
        val initializerType = element.initializer?.getKtType() ?: return null
        if (initializerType is KtErrorType) return null
        return Unit
    }

    override fun invoke(
        context: ActionContext,
        element: KtProperty,
        contextData: Unit,
        updater: ModPsiUpdater
    ) {
        val factory = KtPsiFactory(element)
        val function = factory.createFunction("fun ${element.name}() = ${element.initializer?.text}")
        element.replace(function)
    }
} 
``` 

### Additional Considerations

* **`LowPriorityAction` and `HighPriorityAction`**: These interfaces are still supported in K2.
* **`SelfTargetingIntention` and `SelfTargetingRangeIntention`**: These classes are not directly supported in K2.
  Use `KotlinApplicableModCommandAction` instead.
* **`CommentSaver`**: This utility class can still be used in K2 to preserve comments during PSI modifications.

### Conclusion

By following these steps, you can successfully migrate your intentions to the K2 API, taking advantage of its improved
performance, flexibility, and access to rich semantic information.