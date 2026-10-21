---
tags:
 - jvm
title: "KotlinJavaModuleAnnotationsProvider"
---

# KotlinJavaModuleAnnotationsProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">sealed </span><span class="kd">interface </span><a href="index.html">KotlinJavaModuleAnnotationsProvider</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.html">KotlinPlatformComponent</a>
</span></code></pre></div>Provides annotations for Java modules.

The platform must define one of the following annotation providers:

 - [`KotlinJavaModulePsiAnnotationsProvider`](../-kotlin-java-module-psi-annotations-provider/index.md) (recommended)


 - [`KotlinJavaModuleJavaAnnotationsProvider`](../-kotlin-java-module-java-annotations-provider/index.md)


#### Inheritors


 - [`KotlinJavaModulePsiAnnotationsProvider`](../-kotlin-java-module-psi-annotations-provider/index.md)
 - [`KotlinJavaModuleJavaAnnotationsProvider`](../-kotlin-java-module-java-annotations-provider/index.md)



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Functions
### getAnnotationsForModuleOwnerOfClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="../-kotlin-java-module-java-annotations-provider/index.html#getannotationsformoduleownerofclass"><span class="nf">getAnnotationsForModuleOwnerOfClass</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="index.html">T</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns all annotations of the Java module where the class with the given [`classId`](../-kotlin-java-module-java-annotations-provider/index.md#getannotationsformoduleownerofclass) is defined.

**Example**

```
// module-info.java
@MyAnnotation
module myModule {
}

// MyClass.java
package myModule

public class MyClass {
}
```

Here, when given `myModule.MyClass`, [`getAnnotationsForModuleOwnerOfClass`](../-kotlin-java-module-java-annotations-provider/index.md#getannotationsformoduleownerofclass) should return `@MyAnnotation`.


</div>

</div>
