---
tags:
 - jvm
title: "KotlinEmptyDeclarationProvider"
---

# KotlinEmptyDeclarationProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">KotlinEmptyDeclarationProvider</a> : <a href="../-kotlin-declaration-provider/index.html">KotlinDeclarationProvider</a>
</span></code></pre></div>
</div>

## Properties
### hasSpecificCallablePackageNamesComputation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#hasspecificcallablepackagenamescomputation">hasSpecificCallablePackageNamesComputation</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration provider has a specific implementation of [`computePackageNamesWithTopLevelCallables`](../-kotlin-file-based-declaration-provider/index.md#computepackagenameswithtoplevelcallables). This allows the Analysis API backend to determine whether callable package sets are computed and cached separately or with [`computePackageNames`](../-kotlin-declaration-provider/index.md#computepackagenames).


</div>

</div>
### hasSpecificClassifierPackageNamesComputation

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">val </span><a href="index.html#hasspecificclassifierpackagenamescomputation">hasSpecificClassifierPackageNamesComputation</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the declaration provider has a specific implementation of [`computePackageNamesWithTopLevelClassifiers`](../-kotlin-file-based-declaration-provider/index.md#computepackagenameswithtoplevelclassifiers). This allows the Analysis API backend to determine whether classifier package sets are computed and cached separately or with [`computePackageNames`](../-kotlin-declaration-provider/index.md#computepackagenames).


</div>

</div>
## Functions
### computePackageNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#computepackagenames"><span class="nf">computePackageNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Calculates the set of package names which can be provided by this declaration provider.

The set may contain false positives. `null` may be returned if the package set is too expensive or impossible to compute.

[`computePackageNames`](../-kotlin-declaration-provider/index.md#computepackagenames) is used as the default implementation for [`computePackageNamesWithTopLevelClassifiers`](../-kotlin-file-based-declaration-provider/index.md#computepackagenameswithtoplevelclassifiers) and [`computePackageNamesWithTopLevelCallables`](../-kotlin-file-based-declaration-provider/index.md#computepackagenameswithtoplevelcallables) if either returns `null`. It depends on the declaration provider whether it's worth computing separate package sets for classifiers and callables, or just one set containing all package names.


</div>

</div>
### computePackageNamesWithTopLevelCallables

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kotlin-file-based-declaration-provider/index.html#computepackagenameswithtoplevelcallables"><span class="nf">computePackageNamesWithTopLevelCallables</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Calculates the set of package names which contain callables and can be provided by this declaration provider.

The set may contain false positives. `null` may be returned if the package set is too expensive or impossible to compute.


</div>

</div>
### computePackageNamesWithTopLevelClassifiers

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">fun </span><a href="../-kotlin-file-based-declaration-provider/index.html#computepackagenameswithtoplevelclassifiers"><span class="nf">computePackageNamesWithTopLevelClassifiers</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Calculates the set of package names which contain classifiers and can be provided by this declaration provider.

The set may contain false positives. `null` may be returned if the package set is too expensive or impossible to compute.


</div>

</div>
### findFilesForFacade

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#findfilesforfacade"><span class="nf">findFilesForFacade</span></a><span class="p">(</span>facadeFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### findFilesForFacadeByPackage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#findfilesforfacadebypackage"><span class="nf">findFilesForFacadeByPackage</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### findFilesForScript

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#findfilesforscript"><span class="nf">findFilesForScript</span></a><span class="p">(</span>scriptFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-script/index.html">KtScript</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### findInternalFilesForFacade

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#findinternalfilesforfacade"><span class="nf">findInternalFilesForFacade</span></a><span class="p">(</span>facadeFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Currently we want only classes from libraries.


</div>

</div>
### getAllClassesByClassId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getallclassesbyclassid"><span class="nf">getAllClassesByClassId</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-or-object/index.html">KtClassOrObject</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getAllTypeAliasesByClassId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getalltypealiasesbyclassid"><span class="nf">getAllTypeAliasesByClassId</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-type-alias/index.html">KtTypeAlias</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getClassLikeDeclarationByClassId

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#getclasslikedeclarationbyclassid"><span class="nf">getClassLikeDeclarationByClassId</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-like-declaration/index.html">KtClassLikeDeclaration</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns a [`KtClassLikeDeclaration`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-class-like-declaration/index.md) that has the given [`classId`](../-kotlin-declaration-provider/index.md#getclasslikedeclarationbyclassid), or `null` if no such declaration exists.

[`getClassLikeDeclarationByClassId`](../-kotlin-declaration-provider/index.md#getclasslikedeclarationbyclassid) does not guarantee a stable result for ambiguous class IDs. If multiple declarations share the same class ID, the declaration provider may return any one of them. To get a list of all possibilities, [`getAllClassesByClassId`](../-kotlin-declaration-provider/index.md#getallclassesbyclassid) and [`getAllTypeAliasesByClassId`](../-kotlin-declaration-provider/index.md#getalltypealiasesbyclassid) should be used instead.


</div>

</div>
### getTopLevelCallableFiles

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#gettoplevelcallablefiles"><span class="nf">getTopLevelCallableFiles</span></a><span class="p">(</span>callableId<span class="o">: </span>CallableId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getTopLevelCallableNamesInPackage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#gettoplevelcallablenamesinpackage"><span class="nf">getTopLevelCallableNamesInPackage</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getTopLevelFunctions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#gettoplevelfunctions"><span class="nf">getTopLevelFunctions</span></a><span class="p">(</span>callableId<span class="o">: </span>CallableId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-named-function/index.html">KtNamedFunction</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getTopLevelKotlinClassLikeDeclarationNamesInPackage

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#gettoplevelkotlinclasslikedeclarationnamesinpackage"><span class="nf">getTopLevelKotlinClassLikeDeclarationNamesInPackage</span></a><span class="p">(</span>packageFqName<span class="o">: </span>FqName<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>

</div>
### getTopLevelProperties

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">open </span><span class="kd">override </span><span class="kd">fun </span><a href="index.html#gettoplevelproperties"><span class="nf">getTopLevelProperties</span></a><span class="p">(</span>callableId<span class="o">: </span>CallableId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-property/index.html">KtProperty</a><span class="o">></span>
</span></code></pre></div>
</div>

</div>
