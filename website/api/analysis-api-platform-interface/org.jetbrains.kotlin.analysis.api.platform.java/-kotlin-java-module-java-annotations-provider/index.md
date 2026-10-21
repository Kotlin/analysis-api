---
tags:
 - jvm
title: "KotlinJavaModuleJavaAnnotationsProvider"
---

# KotlinJavaModuleJavaAnnotationsProvider

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinJavaModuleJavaAnnotationsProvider</a> : <a href="../-kotlin-java-module-annotations-provider/index.html">KotlinJavaModuleAnnotationsProvider</a><span class="o"><</span>JavaAnnotation<span class="o">> </span>
</span></code></pre></div>Directly provides JavaAnnotations, which is the representation that the Kotlin compiler expects internally. However, JavaAnnotation is a compiler-internal API, so this provider should only be preferred if the implementation directly accesses JavaAnnotations.


</div>

## Functions
### getAnnotationsForModuleOwnerOfClass

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#getannotationsformoduleownerofclass"><span class="nf">getAnnotationsForModuleOwnerOfClass</span></a><span class="p">(</span>classId<span class="o">: </span>ClassId<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../-kotlin-java-module-annotations-provider/index.html">T</a><span class="o">></span><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns all annotations of the Java module where the class with the given [`classId`](index.md#getannotationsformoduleownerofclass) is defined.

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

Here, when given `myModule.MyClass`, [`getAnnotationsForModuleOwnerOfClass`](index.md#getannotationsformoduleownerofclass) should return `@MyAnnotation`.


</div>

</div>
