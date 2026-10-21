---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.platform.java"
---

# org.jetbrains.kotlin.analysis.api.platform.java
## Types
### [`KotlinJavaModuleAccessibilityChecker`](-kotlin-java-module-accessibility-checker/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-java-module-accessibility-checker/index.html">KotlinJavaModuleAccessibilityChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Allows checking whether one Java module has access to another Java module.


</div>

</div>
### [`KotlinJavaModuleAccessibilityError`](-kotlin-java-module-accessibility-error/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">class </span><a href="-kotlin-java-module-accessibility-error/index.html">KotlinJavaModuleAccessibilityError</a>
</span></code></pre></div>
</div>


<div markdown>

An accessibility error returned by [`KotlinJavaModuleAccessibilityChecker.checkAccessibility`](-kotlin-java-module-accessibility-checker/index.md#checkaccessibility).


</div>

</div>
### [`KotlinJavaModuleAnnotationsProvider`](-kotlin-java-module-annotations-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="-kotlin-java-module-annotations-provider/index.html">KotlinJavaModuleAnnotationsProvider</a><span class="o"><</span><a href="-kotlin-java-module-annotations-provider/index.html">T</a><span class="o">></span> : <a href="../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>
</div>


<div markdown>

Provides annotations for Java modules.


</div>

</div>
### [`KotlinJavaModuleJavaAnnotationsProvider`](-kotlin-java-module-java-annotations-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-java-module-java-annotations-provider/index.html">KotlinJavaModuleJavaAnnotationsProvider</a> : <a href="-kotlin-java-module-annotations-provider/index.html">KotlinJavaModuleAnnotationsProvider</a><span class="o"><</span>JavaAnnotation<span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Directly provides JavaAnnotations, which is the representation that the Kotlin compiler expects internally. However, JavaAnnotation is a compiler-internal API, so this provider should only be preferred if the implementation directly accesses JavaAnnotations.


</div>

</div>
### [`KotlinJavaModulePsiAnnotationsProvider`](-kotlin-java-module-psi-annotations-provider/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="-kotlin-java-module-psi-annotations-provider/index.html">KotlinJavaModulePsiAnnotationsProvider</a> : <a href="-kotlin-java-module-annotations-provider/index.html">KotlinJavaModuleAnnotationsProvider</a><span class="o"><</span>PsiAnnotation<span class="o">> </span>
</span></code></pre></div>
</div>


<div markdown>

Provides PsiAnnotations for Java modules.


</div>

</div>
