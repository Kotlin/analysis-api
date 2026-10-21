---
tags:
 - jvm
title: "Whitespace"
---

# Whitespace

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">Whitespace</a> : <a href="../index.html">KaSourceModificationLocality</a>
</span></code></pre></div>Whitespace modification covers changes in whitespace and comments.

It usually has no effect, but it can affect compiler diagnostics. For example, when we have `if (x) "a"else "b"`, the compiler produces the error "literals must be surrounded by whitespace" (see KT-82629). Changing it to `if (x) "a" else "b"` fixes the problem, but for the cached error to disappear, caches that can be affected by PSI-only changes need to be invalidated.

Whitespace modification is distinct from [`in-block modification`](../-in-block/index.md). While in-block modification can affect both the syntax and the semantics of the code, whitespace modification is guaranteed to only have a syntactic effect and preserve semantics. (Whitespace deletions which might affect code semantics would be reported as [`InBlock`](../-in-block/index.md) or [`OutOfBlock`](../-out-of-block/index.md).) Since just the PSI is affected, only the PSI-based subset of the compiler's checkers can be affected by such a change.

Whitespace modification can occur in any location. Even if it occurs outside a declaration, whitespace modification only affects its containing declaration or the file itself, not the whole module.


</div>

