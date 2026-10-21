---
tags:
 - jvm
title: "KotlinIntersectionScopeMergeTarget"
---

# KotlinIntersectionScopeMergeTarget

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinIntersectionScopeMergeTarget</a>
</span></code></pre></div>A marker interface for GlobalSearchScopes that can be factored out of an intersection scope using the distributive property. This helps the intersection scope merge strategy to pick the correct targets.

The marker should be applied to scopes which have the following characteristics:

1. They are frequently applied in intersection scopes (e.g., via [`KotlinContentScopeRefiner.getRestrictionScopes`](../-kotlin-content-scope-refiner/index.md#getrestrictionscopes)).


1. The same scope is applied in multiple intersection scopes, allowing the scope merger to merge intersections by factoring it out.


### Illustration
Take the following combination of sets `A`, `B`, and `C` (with `&` denoting intersection and `|` denoting union):

```
(B & A) | (C & A)
```

With the distributive law, we can factor out `A`:

```
(B | C) & A
```

Exactly the scope `A` would be marked with [`KotlinIntersectionScopeMergeTarget`](index.md).


</div>

