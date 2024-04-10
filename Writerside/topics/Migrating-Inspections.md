# Migrating Inspections

This guide outlines key steps for migrating Kotlin inspections from the classic API to the new K2 API. While specific details may vary, the general approach remains consistent.

## Key Differences

*   **Resolve**: K2 uses its own resolve mechanisms, eliminating the need for `analyze()` and related methods.
*   **Symbols**: K2 operates on `KtSymbol`s, representing declarations and their properties. Access these symbols using `element.getSymbol()`.
*   **Types**: K2 introduces `KtType`, replacing the classic `KotlinType`. Use methods like `element.getKtType()` to retrieve types.
*   **Quick Fixes**: K2 employs `KotlinApplicableInspectionBase` and `KotlinModCommandQuickFix` for quick fixes, offering a more structured approach.

## Migration Steps

1.  **Extend `KotlinApplicableInspectionBase`**: Choose the appropriate subclass based on the inspection's nature (e.g., `Simple`, `SingleIntention`, `QuickFixBased`).

2.  **Implement `isApplicableByPsi`**: Perform initial PSI-based checks to determine applicability.

3.  **Implement `prepareContext`**: Utilize the `KtAnalysisSession` to gather necessary semantic information and return a context object.

4.  **Implement `getProblemDescription`**: Provide a description of the problem using the context object.

5.  **Implement `createQuickFix`**: Create a `KotlinModCommandQuickFix` to apply the desired changes.

## Simplified Example

Consider a simplified inspection that checks for redundant `toString()` calls within string templates:

**Classic API**

```kotlin
class RemoveToStringInStringTemplateInspection : AbstractKotlinInspection() {
    override fun buildVisitor(holder: ProblemsHolder, isOnTheFly: Boolean) =
        dotQualifiedExpressionVisitor(fun(expression) {
            // ... (PSI-based checks and resolve) ...
            holder.registerProblem(expression, "...", RemoveToStringFix())
        })
}
```

**K2 API**

```kotlin
class RemoveToStringInStringTemplateInspection : KotlinApplicableInspectionBase.Simple<KtDotQualifiedExpression, Unit>() {
    override fun isApplicableByPsi(element: KtDotQualifiedExpression): Boolean {
        // ... (PSI-based checks) ...
    }

    context(KtAnalysisSession)
    override fun prepareContext(element: KtDotQualifiedExpression): Unit? {
        val call = element.resolveCall()?.singleFunctionCallOrNull() ?: return null
        // ... (check if call is to 'toString()') ...
    }

    override fun getProblemDescription(element: KtDotQualifiedExpression, context: Unit) = "..."

    override fun createQuickFix(element: KtDotQualifiedExpression, context: Unit) =
        object : KotlinModCommandQuickFix<KtDotQualifiedExpression>() {
            // ... (apply fix using ModPsiUpdater) ...
        }
}
```

## Additional Notes

*   Leverage extension functions provided by K2 for common tasks like type checks and symbol navigation.
*   Utilize the `KtAnalysisSession` to access various components for analysis.
*   Explore the K2 API documentation and examples for further guidance.

By following these steps and understanding the core differences, you can effectively migrate your Kotlin inspections to the powerful K2 API.