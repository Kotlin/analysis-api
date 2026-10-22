---
tags:
 - jvm
title: "OutOfBlock"
---

# OutOfBlock

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">OutOfBlock</a> : <a href="../index.html">KaSourceModificationLocality</a>
</span></code></pre></div>Out-of-block modification is a source code modification that may affect the state of other declarations in the same module and the declarations of dependent modules.

#### Example 1
```
val x = 10<caret>
val z = x
```

If we change the initializer of `x` to `"str"` the return type of `x` will become `String` instead of the initial `Int`. This will change the return type of `z` as it does not have an explicit type. So, it is an <strong>out-of-block modification</strong>.

#### Example 2
```
val x: Int = 10<caret>
val z = x
```

If we change `10` to `"str"` as in the first example, it would not change the type of `z`, so it is not an <strong>out-of-block-modification</strong>.

#### Examples of out-of-block modifications
 - Modifying the body of a non-local declaration which doesn't have an explicit return type specified


 - Changing the package of a file


 - Adding a new declaration


 - Moving a declaration to another package


Generally, all modifications that happen outside the body of a callable declaration (functions, accessors, or properties) with an explicit type are considered <strong>out-of-block</strong>.


</div>

