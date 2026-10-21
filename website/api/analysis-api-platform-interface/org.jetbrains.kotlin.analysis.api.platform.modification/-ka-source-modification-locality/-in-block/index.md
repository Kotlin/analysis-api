---
tags:
 - jvm
title: "InBlock"
---

# InBlock

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">InBlock</a> : <a href="../index.html">KaSourceModificationLocality</a>
</span></code></pre></div>In-block modification is a source code modification that doesn't affect the state of other non-local declarations.

#### Example 1
```
val x: Int = 10<caret>
val z = x
```

If we change `10` to `"str"`, it would not change the type of `z`, so it is an <strong>in-block-modification</strong>.

#### Example 2
```
val x = 10<caret>
val z = x
```

If we change the initializer of `x` to `"str"`, as in the first example, the return type of `x` will become `String` instead of the initial `Int`. This will change the return type of `z` as it does not have an explicit type. So, it is an <strong>out-of-block modification</strong>.


</div>

