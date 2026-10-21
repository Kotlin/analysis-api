---
tags:
 - jvm
title: "KotlinJavaModuleAccessibilityError"
---

# KotlinJavaModuleAccessibilityError

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="index.html">KotlinJavaModuleAccessibilityError</a>
</span></code></pre></div>An accessibility error returned by [`KotlinJavaModuleAccessibilityChecker.checkAccessibility`](../-kotlin-java-module-accessibility-checker/index.md#checkaccessibility).

#### Inheritors


 - [`ModuleDoesNotReadUnnamedModule`](-module-does-not-read-unnamed-module/index.md)
 - [`ModuleDoesNotReadModule`](-module-does-not-read-module/index.md)
 - [`ModuleDoesNotExportPackage`](-module-does-not-export-package/index.md)



</div>

## Types
### [`ModuleDoesNotExportPackage`](-module-does-not-export-package/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-module-does-not-export-package/index.html">ModuleDoesNotExportPackage</a><span class="p">(</span><span class="kd">val </span>dependencyModuleName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span> : <a href="index.html">KotlinJavaModuleAccessibilityError</a>
</span></code></pre></div>
</div>


<div markdown>

The use-site module reads the referenced module, but the referenced package name is not exported by it.


</div>

</div>
### [`ModuleDoesNotReadModule`](-module-does-not-read-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">data </span><span class="kd">class </span><a href="-module-does-not-read-module/index.html">ModuleDoesNotReadModule</a><span class="p">(</span><span class="kd">val </span>dependencyModuleName<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="p">)</span> : <a href="index.html">KotlinJavaModuleAccessibilityError</a>
</span></code></pre></div>
</div>


<div markdown>

The use-site module cannot read the referenced module.


</div>

</div>
### [`ModuleDoesNotReadUnnamedModule`](-module-does-not-read-unnamed-module/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-module-does-not-read-unnamed-module/index.html">ModuleDoesNotReadUnnamedModule</a> : <a href="index.html">KotlinJavaModuleAccessibilityError</a>
</span></code></pre></div>
</div>


<div markdown>

The use-site module cannot read the referenced module because it is unnamed.


</div>

</div>
