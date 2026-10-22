---
tags:
 - jvm
title: "createExtensionCandidateChecker"
---

# createExtensionCandidateChecker

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">context</span><span class="p">(</span>session<span class="o">: </span><a href="../org.jetbrains.kotlin.analysis.api/-ka-session/index.html">KaSession</a><span class="p">)</span>
<span class="kd">fun </span><a href="create-extension-candidate-checker.html"><span class="nf">createExtensionCandidateChecker</span></a><span class="p">(</span>
    originalFile<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-file/index.html">KtFile</a><span class="p">, </span>
    nameExpression<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-simple-name-expression/index.html">KtSimpleNameExpression</a><span class="p">, </span>
    explicitReceiver<span class="o">: </span><a href="../../psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.html">KtExpression</a><span class="o">?</span>
<span class="p">)</span><span class="o">: </span><a href="-ka-completion-extension-candidate-checker/index.html">KaCompletionExtensionCandidateChecker</a>
</span></code></pre></div>
</div>


<div markdown>

Returns an extension applicability checker for the given context [`nameExpression`](create-extension-candidate-checker.md). The function is meant to only be used for providing auto-completion for Kotlin in IntelliJ IDEA.

The returned checker does not cache the results for individual callable candidates.

#### Parameters


 - originalFile: The file being edited.


 - nameExpression: The expression under the caret in an in-memory copy of [`originalFile`](create-extension-candidate-checker.md)      with a placeholder identifier inserted. Also see `CompletionUtilCore.DUMMY_IDENTIFIER` in IntelliJ IDEA.


 - explicitReceiver: A receiver expression, if available (also from the in-memory copy of [`originalFile`](create-extension-candidate-checker.md)).





</div>

</div>
