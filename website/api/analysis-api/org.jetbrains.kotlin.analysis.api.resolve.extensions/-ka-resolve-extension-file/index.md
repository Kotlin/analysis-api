---
tags:
 - jvm
title: "KaResolveExtensionFile"
---

# KaResolveExtensionFile

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">class </span><a href="index.html">KaResolveExtensionFile</a>
</span></code></pre></div>Represents a Kotlin file that contains generated declarations. It is provided by its [`resolve extension`](../-ka-resolve-extension/index.md).

The file content is built lazily with [`buildFileText`](index.md#buildfiletext), which ensures that resolve extension files are only initialized when needed. The additional information provided by functions like [`getFilePackageName`](index.md#getfilepackagename) and [`getTopLevelClassifierNames`](index.md#gettoplevelclassifiernames) is used to avoid building the resolve extension file's text unless absolutely necessary.

All member implementations should:

 - Consider caching the results for subsequent invocations.


 - Be lightweight and avoid building the whole file structure eagerly.


 - Avoid using Kotlin resolution, as these functions are called during session initialization, so Analysis API access is forbidden.


#### See also


 - [`KaResolveExtension`](../-ka-resolve-extension/index.md)



</div>

## Constructors
### KaResolveExtensionFile

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Functions
### buildFileText

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#buildfiletext"><span class="nf">buildFileText</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

Builds the text of the generated Kotlin source file. It should be valid Kotlin code.

The content must be consistent with other information provided by [`KaResolveExtensionFile`](index.md):

 - The file's package name must be equal to [`getFilePackageName`](index.md#getfilepackagename).


 - The names of all top-level classifiers declared in the file must be contained in [`getTopLevelClassifierNames`](index.md#gettoplevelclassifiernames).


 - The names of all top-level callables declared in the file must be contained in [`getTopLevelCallableNames`](index.md#gettoplevelcallablenames).


In addition, the file text has the following restrictions:

 - The file should not contain the [`JvmMultifileClass`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-multifile-class/index.html) and [`JvmName`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-name/index.html) annotations on the file level.


 - All declaration types should be specified explicitly.



</div>

</div>
### createNavigationTargetsProvider

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#createnavigationtargetsprovider"><span class="nf">createNavigationTargetsProvider</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="../-ka-resolve-extension-navigation-targets-provider/index.html">KaResolveExtensionNavigationTargetsProvider</a>
</span></code></pre></div>
</div>


<div markdown>

Creates a [`KaResolveExtensionNavigationTargetsProvider`](../-ka-resolve-extension-navigation-targets-provider/index.md) for this [`KaResolveExtensionFile`](index.md).


</div>

</div>
### getFileName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getfilename"><span class="nf">getFileName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>
</span></code></pre></div>
</div>


<div markdown>

The name of the Kotlin file which will be generated. It should have the `.kt` extension.

If the file contains top-level properties or functions, the name will be used as a Java facade name. For example, given the file name `myFile.kt`, a `MyFileKt` facade would be generated.


</div>

</div>
### getFilePackageName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getfilepackagename"><span class="nf">getFilePackageName</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span>FqName
</span></code></pre></div>
</div>


<div markdown>

The FqName of the package that the resolve extension file belongs to.

The function might be called regularly, so it should be fast and avoid building the whole file text.


</div>

</div>
### getTopLevelCallableNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettoplevelcallablenames"><span class="nf">getTopLevelCallableNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the set of top-level callable names (functions and properties) in the file. It must contain all such names in the package, but may contain additional false positives.

The function might be called regularly, so it should be fast and avoid building the whole file text.


</div>

</div>
### getTopLevelClassifierNames

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#gettoplevelclassifiernames"><span class="nf">getTopLevelClassifierNames</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Returns the set of top-level classifier names (classes, interfaces, objects, and type-aliases) in the file. It must contain all such names in the package, but may contain additional false positives.

The function might be called regularly, so it should be fast and avoid building the whole file text.


</div>

</div>
