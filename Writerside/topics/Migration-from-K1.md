# Migration from K1

## Migrating K1 Usages

### Classes

| K1 (Descriptors)                                                                   | K2 (Symbols*)                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `val classDescriptor = declaration.resolveToDescriptorIfAny() as? ClassDescriptor` | `val classSymbol = declaration.getSymbol() as? KtClassOrObjectSymbol`           |
| `descriptor.kind == ClassKind.ENUM_CLASS`                                          | `symbol is KtClassOrObjectSymbol && symbol.classKind == KtClassKind.ENUM_CLASS` |
| `descriptor.isInner`                                                               | `symbol is KtNamedClassOrObjectSymbol && symbol.isInner`                        |
| `descriptor.isData`                                                                | `symbol is KtNamedClassOrObjectSymbol && symbol.isData`                         |
| `descriptor.containingDeclaration is PackageFragmentDescriptor`                    | `symbol.getContainingSymbol() is KtPackageSymbol`                               |
| `descriptor.unsubstitutedMemberScope`                                              | `symbol.getMemberScope()`                                                       |
| `descriptor.defaultType`                                                           | `symbol.returnType`                                                             | 
| `descriptor.typeConstructor`                                                       | `symbol.getTypeConstructor()`                                                   |
| `val classDescriptor = type.constructor.declarationDescriptor as? ClassDescriptor` | `val classSymbol = type.expandedClassSymbol`                                    |
| `val classDescriptor = descriptor.containingDeclaration as? ClassDescriptor`       | `val classSymbol = symbol.getContainingSymbol() as? KtClassOrObjectSymbol`      |
| `classDescriptor.unsubstitutedMemberScope.getContributedFunctions(...)`            | `classSymbol.getMemberScope().getFunctionSymbols()...`                          |
| `val superTypes = classDescriptor.typeConstructor.supertypes`                      | `val superTypes = classOrObjectSymbol.superTypes`                               |
| `classDescriptor.isCompanionObject()`                                              | `classSymbol.classKind == KtClassKind.COMPANION_OBJECT`                         |

### Functions

| K1 (Descriptors)                                                                     | K2 (Symbols*)                                                   |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| `val functionDescriptor = element.resolveToDescriptorIfAny() as? FunctionDescriptor` | `val functionSymbol = element.getSymbol() as? KtFunctionSymbol` |
| `descriptor.isSuspend`                                                               | `symbol is KtFunctionSymbol && symbol.isSuspend`                |
| `descriptor.isOperator`                                                              | `symbol is KtFunctionSymbol && symbol.isOperator`               |
| `descriptor.isExternal`                                                              | `symbol is KtFunctionSymbol && symbol.isExternal`               |
| `descriptor.isInline`                                                                | `symbol is KtFunctionSymbol && symbol.isInline`                 |
| `descriptor.isOverride`                                                              | `symbol is KtFunctionSymbol && symbol.isOverride`               |
| `descriptor.isInfix`                                                                 | `symbol is KtFunctionSymbol && symbol.isInfix`                  |
| `descriptor.isTailrec`                                                               | `symbol is KtFunctionSymbol && symbol.isTailrec`                |
| `descriptor.returnType`                                                              | `symbol.returnType`                                             | 
| `descriptor.containingDeclaration is PackageFragmentDescriptor`                      | `symbol.getContainingSymbol() is KtPackageSymbol`               |
| `descriptor.overriddenDescriptors`                                                   | `symbol.getAllOverriddenSymbols()`                              |
| `descriptor.valueParameters`                                                         | `symbol.valueParameters`                                        |

### Parameters

| K1 (Descriptors)                                     | K2 (Symbols*)                                                |
|------------------------------------------------------|--------------------------------------------------------------|
| `context[BindingContext.VALUE_PARAMETER, parameter]` | `parameter.getParameterSymbol()`                             |
| `descriptor.isVararg`                                | `symbol is KtValueParameterSymbol && symbol.isVararg`        |
| `descriptor.declaresDefaultValue()`                  | `symbol is KtValueParameterSymbol && symbol.hasDefaultValue` |
| `descriptor.isNoinline`                              | `symbol is KtValueParameterSymbol && symbol.isNoinline`      |
| `descriptor.isCrossinline`                           | `symbol is KtValueParameterSymbol && symbol.isCrossinline`   |
| `descriptor.type`                                    | `symbol.returnType`                                          |
| `descriptor.name`                                    | `symbol.name`                                                |

### Properties

| K1 (Descriptors)                                                                                                                                                          | K2 (Symbols**)                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `val propertyDescriptor = context[BindingContext.DECLARATION_TO_DESCRIPTOR, property] as? PropertyDescriptor`                                                             | `val propertySymbol = property.getSymbol() as? KtPropertySymbol`                                                                               |
| `val propertyDescriptor = element.resolveToDescriptorIfAny() as? KtPropertyDescriptor ?: return<br> val isVisible = propertyDescriptor.visibility == Visibilities.Public` | `val propertySymbol = element.getSymbol() as? KtPropertySymbol ?: return<br> val isVisible = propertySymbol.visibility == Visibilities.Public` |
| `descriptor.isVar`                                                                                                                                                        | `symbol is KtVariableSymbol && !symbol.isVal`                                                                                                  |
| `descriptor.isLateInit`                                                                                                                                                   | `symbol is KtKotlinPropertySymbol && symbol.isLateInit`                                                                                        |
| `descriptor.isConst`                                                                                                                                                      | `symbol is KtKotlinPropertySymbol && symbol.isConst`                                                                                           |
| `descriptor.setter`                                                                                                                                                       | `symbol.setter`                                                                                                                                |
| `descriptor.getter`                                                                                                                                                       | `symbol.getter`                                                                                                                                |
| `descriptor.type`                                                                                                                                                         | `symbol.returnType`                                                                                                                            |

### Calls

| K1 (Descriptors)                                         | K2 (Symbols*)                                                                                      |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `val resolvedCall = expression.getResolvedCall(context)` | `val call = expression.resolveCall()?.singleFunctionCallOrNull()`                                  |
| `resolvedCall.resultingDescriptor`                       | `call?.partiallyAppliedSymbol?.symbol`                                                             |
| `resolvedCall.candidateDescriptor`                       | `call?.candidateSymbol`                                                                            |
| `resolvedCall.dispatchReceiver`                          | `call?.partiallyAppliedSymbol?.dispatchReceiver`                                                   |
| `resolvedCall.extensionReceiver`                         | `call?.partiallyAppliedSymbol?.extensionReceiver`                                                  |
| `resolvedCall.valueArguments`                            | `call?.argumentMapping`                                                                            |
| `resolvedCall.typeArguments`                             | `call?.typeArgumentsMapping`                                                                       |
| `descriptor.isInvokeOperator`                            | `symbol is KtFunctionSymbol && symbol.isOperator && symbol.name == OperatorNameConventions.INVOKE` |
| `descriptor.fqNameSafe.asString() == "kotlin.apply"`     | `symbol.callableIdIfNonLocal?.asSingleFqName() == StandardNames.FqNames.apply`                     |

### Types

| K1 (Descriptors)                                         | K2 (Symbols*)                                   |
|----------------------------------------------------------|-------------------------------------------------|
| `val type = context[BindingContext.TYPE, typeRef]`       | `val type = typeRef.getKtType()`                |
| `type.isMarkedNullable`                                  | `type.isMarkedNullable`                         |
| `type.isNullabilityFlexible()`                           | `type.hasFlexibleNullability`                   |
| `type.isSubtypeOf(otherType)`                            | `type isSubTypeOf otherType`                    |
| `KotlinBuiltIns.isUnit(type)`                            | `type.isUnit`                                   |
| `KotlinBuiltIns.isPrimitiveType(type)`                   | `type.isPrimitive`                              |
| `KotlinBuiltIns.isString(type)`                          | `type.isString`                                 |
| `type.constructor.declarationDescriptor.isInlineClass()` | `type.isInlineClass()`                          | 
| `type.isFunctionType`                                    | `type.isFunctionType`                           |
| `type.isKFunctionType`                                   | `type.isKFunctionType`                          | 
| `type.isSuspendFunctionType`                             | `type.isSuspendFunctionType`                    |
| `type.isKSuspendFunctionType`                            | `type.isKSuspendFunctionType`                   | 
| `type.isSubTypeOf(StandardClassIds.Collection)`          | `type.isSubTypeOf(StandardClassIds.Collection)` |

### Misc

| K1 (Descriptors)                                                                          | K2 (Symbols*)                                                                 |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `moduleDescriptor.resolveClassByFqName(fqName, NoLookupLocation.FROM_IDE)`                | `getClassOrObjectSymbolByClassId(ClassId.fromString(fqName.asString()))`      |
| `val psiElement = DescriptorToSourceUtils.descriptorToDeclaration(declarationDescriptor)` | `val psiElement = declarationSymbol.psi`                                      |
| `val descriptor = bindingContext[BindingContext.REFERENCE_TARGET, element]`               | `val symbol = element.mainReference.resolveToSymbol()`                        |
| `val visibility = declarationDescriptor.visibility`                                       | `val visibility = (declarationSymbol as? KtSymbolWithVisibility)?.visibility` |
| `descriptor.isExpect`                                                                     | `symbol is KtPossibleMultiplatformSymbol && symbol.isExpect`                  |
| `descriptor.isActual`                                                                     | `symbol is KtPossibleMultiplatformSymbol && symbol.isActual`                  |
| `descriptor.modality == Modality.FINAL`                                                   | `symbol is KtSymbolWithModality && symbol.modality == Modality.FINAL`         |

* `KtAnalysisSession` must be in the scope

## Handle Lifetime Management

* **Avoid storing Analysis API objects**: Entities obtained from the Analysis API are valid only within the read action
  and scope where they were created. Use `KtSymbolPointer` to reference symbols across different read actions.
* **Pass `KtAnalysisSession` directly**: Pass the `KtAnalysisSession` to functions as an extension receiver or a value
  parameter instead of storing it in a class.

## Example

```kotlin
// K1:
fun analyzeClass(ktClass: KtClass) {
    val bindingContext = ktClass.analyze()
    val classDescriptor = bindingContext[BindingContext.CLASS, ktClass]
    val className = classDescriptor?.name ?: return
    // ...
}

// K2:
fun analyzeClass(ktClass: KtClass) {
    analyze(ktClass) {
        val classSymbol = ktClass.getClassOrObjectSymbol()
        val className = classSymbol?.name ?: return
        // ...
    }
}
```