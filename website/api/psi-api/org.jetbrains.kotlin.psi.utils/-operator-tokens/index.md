---
tags:
 - jvm
title: "OperatorTokens"
---

# OperatorTokens

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="index.html">OperatorTokens</a>
</span></code></pre></div>Maps between Kotlin operator tokens and the operator-convention function names they desugar to (for example, `+` maps to `plus`), and groups the operator tokens by category (unary, binary, assignment, comparison, and so on).


</div>

## Properties
### ASSIGNMENT_OPERATION_NAMES

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#assignment_operation_names">ASSIGNMENT_OPERATION_NAMES</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="p">, </span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Maps each augmented assignment operator token (such as `+=` or `*=`) to its operator-convention function name (such as `plusAssign` or `timesAssign`).


</div>

</div>
### ASSIGNMENT_OPERATION_TOKENS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#assignment_operation_tokens">ASSIGNMENT_OPERATION_TOKENS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span>Name<span class="p">, </span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The inverse of [`ASSIGNMENT_OPERATION_NAMES`](index.md#assignment_operation_names): maps each augmented assignment function name to its token.


</div>

</div>
### ASSIGNMENTS_FOR_OPERATIONS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#assignments_for_operations">ASSIGNMENTS_FOR_OPERATIONS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The inverse of [`OPERATIONS_FOR_ASSIGNMENTS`](index.md#operations_for_assignments): maps each binary operator token (such as `+`) to the corresponding augmented assignment token (such as `+=`).


</div>

</div>
### BINARY_OPERATION_NAMES

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#binary_operation_names">BINARY_OPERATION_NAMES</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="p">, </span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Maps each binary operator token (such as `*`, `+`, or `..`) to its operator-convention function name (such as `times`, `plus`, or `rangeTo`).


</div>

</div>
### BINARY_OPERATION_TOKENS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#binary_operation_tokens">BINARY_OPERATION_TOKENS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span>Name<span class="p">, </span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The inverse of [`BINARY_OPERATION_NAMES`](index.md#binary_operation_names): maps each binary operator function name to its token.


</div>

</div>
### COMPARISON_OPERATIONS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#comparison_operations">COMPARISON_OPERATIONS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The comparison operator tokens (`<`, `>`, `<=`, and `>=`), all of which desugar to `compareTo`.


</div>

</div>
### CONVENTION_NAMES

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#convention_names">CONVENTION_NAMES</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The set of fixed function names that carry a special operator meaning in Kotlin. This includes names such as `get`, `set`, `invoke`, `iterator`, `equals`, and `compareTo`, together with every unary, binary, and assignment operator name. Dynamically named `componentN` conventions are recognized by [`isConventionName`](index.md#isconventionname) but are not members of this set.


</div>

</div>
### EQUALS_OPERATIONS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#equals_operations">EQUALS_OPERATIONS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The structural equality operator tokens (`==` and `!=`), which desugar to `equals`.


</div>

</div>
### IDENTITY_EQUALS_OPERATIONS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#identity_equals_operations">IDENTITY_EQUALS_OPERATIONS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The referential equality operator tokens (`===` and `!==`).


</div>

</div>
### IN_OPERATIONS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#in_operations">IN_OPERATIONS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The containment operator tokens (`in` and `!in`), which desugar to `contains`.


</div>

</div>
### INCREMENT_OPERATIONS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#increment_operations">INCREMENT_OPERATIONS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The increment and decrement operator tokens (`++` and `--`).


</div>

</div>
### OPERATIONS_FOR_ASSIGNMENTS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#operations_for_assignments">OPERATIONS_FOR_ASSIGNMENTS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="p">, </span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Maps each augmented assignment token (such as `+=`) to the corresponding binary operator token (such as `+`).


</div>

</div>
### UNARY_OPERATION_NAMES

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#unary_operation_names">UNARY_OPERATION_NAMES</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="p">, </span>Name<span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

Maps each unary operator token (such as `++` or `-`) to its operator-convention function name (such as `inc` or `unaryMinus`).


</div>

</div>
### UNARY_OPERATION_TOKENS

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="se">JvmField</span></a>
<span class="kd">val </span><a href="index.html#unary_operation_tokens">UNARY_OPERATION_TOKENS</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="o"><</span>Name<span class="p">, </span><a href="../../org.jetbrains.kotlin.lexer/-kt-single-value-token/index.html">KtSingleValueToken</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

The inverse of [`UNARY_OPERATION_NAMES`](index.md#unary_operation_names): maps each unary operator function name to its token.


</div>

</div>
## Functions
### isConventionName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#isconventionname"><span class="nf">isConventionName</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Returns `true` if the given [`name`](index.md#isconventionname) is an operator-convention function name — either one of [`CONVENTION_NAMES`](index.md#convention_names) or a `componentN` destructuring name.


</div>

</div>
### operationName

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#operationname"><span class="nf">operationName</span></a><span class="p">(</span>token<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a><span class="p">)</span><span class="o">: </span>Name<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the operator-convention function name that the given [`token`](index.md#operationname) desugars to, considering unary, binary, and assignment operators as well as comparison, equality, and containment operators, or `null` if [`token`](index.md#operationname) is not an operator.


</div>

</div>

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#operationname"><span class="nf">operationName</span></a><span class="p">(</span>
    token<span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a><span class="p">, </span>
    unaryOperations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    binaryOperations<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span><span class="o">: </span>Name<span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the operator-convention function name that the given [`token`](index.md#operationname) desugars to, or `null` if [`token`](index.md#operationname) is not a matching operator. [`unaryOperations`](index.md#operationname) and [`binaryOperations`](index.md#operationname) control whether unary and binary operator tokens are considered; assignment, comparison, equality, and containment operators are always considered.


</div>

</div>
### operationToken

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html"><span class="se">JvmStatic</span></a>
<span class="kd">fun </span><a href="index.html#operationtoken"><span class="nf">operationToken</span></a><span class="p">(</span>name<span class="o">: </span>Name<span class="p">)</span><span class="o">: </span><a href="../../org.jetbrains.kotlin.lexer/-kt-token/index.html">KtToken</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

Returns the operator token corresponding to the given operator-convention function [`name`](index.md#operationtoken) (for binary, unary, or assignment operators), or `null` if [`name`](index.md#operationtoken) is not such an operator name.


</div>

</div>
