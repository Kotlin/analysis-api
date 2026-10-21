---
tags:
 - jvm
title: "KaDataFlowExitPointSnapshot"
---

# KaDataFlowExitPointSnapshot

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="index.html">KaDataFlowExitPointSnapshot</a><span class="p">(</span>
    <span class="kd">val </span>defaultExpressionInfo<span class="o">: </span><a href="-default-expression-info/index.html">KaDataFlowExitPointSnapshot.DefaultExpressionInfo</a><span class="o">?</span><span class="p">, </span>
    <span class="kd">val </span>valuedReturnExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>returnValueType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span><span class="p">, </span>
    <span class="kd">val </span>jumpExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    <span class="kd">val </span>hasJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasEscapingJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasMultipleJumpKinds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>hasMultipleJumpTargets<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    <span class="kd">val </span>variableReassignments<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-variable-reassignment/index.html">KaDataFlowExitPointSnapshot.VariableReassignment</a><span class="o">></span>
<span class="p">)</span>
</span></code></pre></div><strong>The type has been moved to a new package. Use </strong>[`<strong>org.jetbrains.kotlin.analysis.api.dataflow.KaDataFlowExitPointSnapshot</strong>`](../../org.jetbrains.kotlin.analysis.api.dataflow/-ka-data-flow-exit-point-snapshot/index.md)<strong> instead.</strong>


</div>

## Constructors
### KaDataFlowExitPointSnapshot

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">constructor</span><span class="p">(</span>
    defaultExpressionInfo<span class="o">: </span><a href="-default-expression-info/index.html">KaDataFlowExitPointSnapshot.DefaultExpressionInfo</a><span class="o">?</span><span class="p">, </span>
    valuedReturnExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    returnValueType<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span><span class="p">, </span>
    jumpExpressions<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span><span class="p">, </span>
    hasJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    hasEscapingJumps<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    hasMultipleJumpKinds<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    hasMultipleJumpTargets<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">, </span>
    variableReassignments<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-variable-reassignment/index.html">KaDataFlowExitPointSnapshot.VariableReassignment</a><span class="o">></span>
<span class="p">)</span>
</span></code></pre></div>
</div>

</div>
## Types
### [`DefaultExpressionInfo`](-default-expression-info/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-default-expression-info/index.html">DefaultExpressionInfo</a><span class="p">(</span><span class="kd">val </span>expression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span><span class="kd">val </span>type<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Represents a default expression (generally, a last given statement if it has a meaningful result type). Expressions that always return [`Nothing`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html), such as `return`, `break`, `continue` or `throw`, cannot be default expressions.


</div>

</div>
### [`VariableReassignment`](-variable-reassignment/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-variable-reassignment/index.html">VariableReassignment</a><span class="p">(</span>
    <span class="kd">val </span>expression<span class="o">: </span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="p">, </span>
    <span class="kd">val </span>variable<span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/index.html">KaVariableSymbol</a><span class="p">, </span>
    <span class="kd">val </span>isAugmented<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
<span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Represents a local variable reassignment.


</div>

</div>
## Properties
### defaultExpressionInfo

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#defaultexpressioninfo">defaultExpressionInfo</a><span class="o">: </span><a href="-default-expression-info/index.html">KaDataFlowExitPointSnapshot.DefaultExpressionInfo</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A default expression, if any.

**See also**



 - [`DefaultExpressionInfo`](-default-expression-info/index.md): for more information.





</div>

</div>
### hasEscapingJumps

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#hasescapingjumps">hasEscapingJumps</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if next-executed instructions for the potential default expression and jump expressions are different.


</div>

</div>
### hasJumps

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#hasjumps">hasJumps</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if there are any control-flow statements that jump outside given statements. Jumps include both loop jumps (`break` and `continue`) and `return`s. Conditional blocks (`if`) and `throw`s are not considered as jumps.


</div>

</div>
### hasMultipleJumpKinds

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#hasmultiplejumpkinds">hasMultipleJumpKinds</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if there are jumps of different kinds (e.g., there is both a `break` and a `return`).


</div>

</div>
### hasMultipleJumpTargets

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#hasmultiplejumptargets">hasMultipleJumpTargets</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

`true` if two or more jumps have different next-executed instructions. Such as, there are both inner and outer loop `break`, or a `break` and `continue` for the same loop.


</div>

</div>
### jumpExpressions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#jumpexpressions">jumpExpressions</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

All jump expressions.

**See also**



 - [`hasJumps`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-exit-point-snapshot/--root--.md): for the definition of jumps.





</div>

</div>
### returnValueType

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#returnvaluetype">returnValueType</a><span class="o">: </span><a href="../../org.jetbrains.kotlin.analysis.api.types/-ka-type/index.html">KaType</a><span class="o">?</span>
</span></code></pre></div>
</div>


<div markdown>

A common supertype of values in [`valuedReturnExpressions`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.components/-ka-data-flow-exit-point-snapshot/--root--.md).


</div>

</div>
### valuedReturnExpressions

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#valuedreturnexpressions">valuedReturnExpressions</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="../../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

A list of expressions that return a value.

The expressions are not necessarily [`KtReturnExpression`](../../../psi-api/org.jetbrains.kotlin.psi/-kt-return-expression/index.md)s. For instance, implicit return from a lambda can be an arbitrary expression.


</div>

</div>
### variableReassignments

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">val </span><a href="index.html#variablereassignments">variableReassignments</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="o"><</span><a href="-variable-reassignment/index.html">KaDataFlowExitPointSnapshot.VariableReassignment</a><span class="o">></span>
</span></code></pre></div>
</div>


<div markdown>

local variable reassignments found in given statements.


</div>

</div>
