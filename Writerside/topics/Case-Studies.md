# Case Study: Main function should return 'Unit'

## Introduction

The `MainFunctionReturnUnitInspection` from the Kotlin IntelliJ IDEA plugin checks whether the `main()`-like function
has the `Unit` return type. If the return type is implicit, it's easy to return something different by mistake.
The inspection helps to avoid the issue.

In the following function, the author most likely intended to create a `main()` function. But in fact, it returns a
`PrintStream`.

```Kotlin
fun main(args: Array<String>) = System.err.apply {
    args.forEach(::println)
}
```

Both the K1 and K2 inspection implementations use a named function visitor.
The difference lies in the `processFunction()` implementation.

```Kotlin
internal class MainFunctionReturnUnitInspection : LocalInspectionTool() {
    override fun buildVisitor(holder: ProblemsHolder, isOnTheFly: Boolean): PsiElementVisitor {
        return namedFunctionVisitor { processFunction(it, holder) }
    }
}
```

## K1 Implementation

Here is the [old](https://github.com/JetBrains/intellij-community/blob/57c570fa9816127f425671605cc390b094e520a0/plugins/kotlin/idea/src/org/jetbrains/kotlin/idea/inspections/MainFunctionReturnUnitInspection.kt#L27),
K1-based implementation of `processFunction()`.

```Kotlin
if (function.name != "main") return
val descriptor = function.descriptor as? FunctionDescriptor ?: return
val mainFunctionDetector = MainFunctionDetector(function.languageVersionSettings) { it.resolveToDescriptorIfAny() }
if (!mainFunctionDetector.isMain(descriptor, checkReturnType = false)) return
if (descriptor.returnType?.let { KotlinBuiltIns.isUnit(it) } == true) return
holder.registerProblem(...)
```

Let's look at the implementation step by step.

```Kotlin
if (function.name != "main") return
```

Here we check whether the function is named `main` to avoid running further checking logic that depends on semantic code
analysis. It is crucial, as PSI-based checks are much faster than semantic ones.

```Kotlin
val descriptor = function.descriptor as? FunctionDescriptor ?: return
```

Then, by using `function.descriptor` we get a `DeclarationDescriptor`, a container for semantic
declaration information. In the case of a `KtNamedFunction`, it should be a `FunctionDescriptor`, holding the
function's return type.

The `function.descriptor` [helper](https://github.com/JetBrains/intellij-community/blob/76680787081992373bd0029cc54176963adcd858/plugins/kotlin/core/src/org/jetbrains/kotlin/idea/search/usagesSearch/searchHelpers.kt#L50)
calls `resolveToDescriptorIfAny()`, which itself delegates to `analyze()` to get the
`BindingContext`. The obtained `BindingContext` provides bindings between elements in the code and their semantic
representation (such as, `KtDeclaration` to `DeclarationDescriptor`).

```Kotlin
val mainFunctionDetector = MainFunctionDetector(function.languageVersionSettings) { it.resolveToDescriptorIfAny() }
if (!mainFunctionDetector.isMain(descriptor, checkReturnType = false)) return
```

Additionally, we use the `MainFunctionDetector` [compiler utility](https://github.com/JetBrains/kotlin/blob/master/compiler/frontend/src/org/jetbrains/kotlin/idea/MainFunctionDetector.kt#L36)
to check whether a descriptor indeed looks like a `main()` function. Specifically for the IDE use-cases,
`MainFunctionDetector` provides an overload that allows us to skip the return type check. The `MainFunctionDetector`
expects a descriptor, so we pass the one we've obtained from the `KtNamedFunction`.

```Kotlin
if (descriptor.returnType?.let { KotlinBuiltIns.isUnit(it) } == true) return
```

Finally, we check whether the function's return type is `Unit`. We use the `KotlinBuiltIns` class from the compiler
which has a number of static methods which check whether a type is a specific Kotlin built-in type.

If the return type is not `Unit`, the function is not a proper `main()` one, so we register a problem.

## K2 Implementation

Then, let's compare the old implementation with the [K2-based one](https://github.com/JetBrains/intellij-community/blob/9c7e738f1449985836f74ab2d58ee05ddd1a28e2/plugins/kotlin/code-insight/inspections-k2/src/org/jetbrains/kotlin/idea/k2/codeinsight/inspections/declarations/MainFunctionReturnUnitInspection.kt#L20).

```Kotlin
val detectorConfiguration = KotlinMainFunctionDetector.Configuration(checkResultType = false)

if (!PsiOnlyKotlinMainFunctionDetector.isMain(function, detectorConfiguration)) return
if (!function.hasDeclaredReturnType() && function.hasBlockBody()) return
if (!KotlinMainFunctionDetector.getInstance().isMain(function, detectorConfiguration)) return

analyze(function) {
    if (!function.symbol.returnType.isUnitType) {
        holder.registerProblem(...)
    }
}
```

Starting from the beginning, one can notice that the K2 implementation is more efficient.

```Kotlin
if (!PsiOnlyKotlinMainFunctionDetector.isMain(function, detectorConfiguration)) return
```

Here we not only check the function name, but we use the [`PsiOnlyKotlinMainFunctionDetector`](https://github.com/JetBrains/intellij-community/blob/db1bf18449fab6d4a3de8576b01ef1e35a4f0ad1/plugins/kotlin/base/code-insight/src/org/jetbrains/kotlin/idea/base/codeInsight/PsiOnlyKotlinMainFunctionDetector.kt#L13)
to check whether the function looks like a `main()` one using only PSI-based checks. In particular, the detector checks
also the presence of type/value parameters and the function location in the file.

```Kotlin
if (!function.hasDeclaredReturnType() && function.hasBlockBody()) return
```

Next, we check whether the function has a declared return type. If it doesn't, and if the function has a block body, we
assume that the return type is `Unit`, so we skip further checks.

```Kotlin
if (!KotlinMainFunctionDetector.getInstance().isMain(function, detectorConfiguration)) return
```

Then, we use another implementation of the `KotlinMainFunctionDetector` – this one performs semantic checks. For the
K2 mode, it will be [`SymbolBasedKotlinMainFunctionDetector`](https://github.com/JetBrains/intellij-community/blob/f0132d1fa64f21db0bd8dd19207a94a90c6ef301/plugins/kotlin/base/fir/code-insight/src/org/jetbrains/kotlin/idea/base/fir/codeInsight/SymbolBasedKotlinMainFunctionDetector.kt#L24).

We use the same `detectorConfiguration` as before to skip the return type check, as we want to catch `main()`-like
functions with a wrong return type.

```Kotlin
analyze(function) {
    if (!function.symbol.returnType.isUnitType) {
        holder.registerProblem(...)
    }
}
```

Finally, we perform the return type check by ourselves using the Analysis API.

The Analysis API requires all work with resolved declarations to be performed inside the `analyze {}` block.
Inside the lambda, we get access to various helpers providing semantic information about declarations visible
from the use-site module. In our case, it would be the module containing the `function` (as we passed it to `analyze()`).

We need to check whether the function has a `Unit` return type. One can get it from a `KaFunctionSymbol`,
a semantic representation of a function, similar to `FunctionDescriptor` in the old compiler.

The `symbol` property available inside the analysis block maps a `KtDeclaration` to a `KaSymbol`. Unlike K1,
the Analysis API guarantees there will be a symbol for every declaration, so we do not need an extra `?: return`.
Also, `symbol` is overloaded for different kinds of declarations, so we can avoid explicit casting to a `KaFunctionSymbol`.

Just like in the old implementation, we check whether the return type is `Unit`, and if it's not, we register a problem.