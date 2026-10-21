---
tags:
 - jvm
title: "org.jetbrains.kotlin.analysis.api.standalone"
---

# org.jetbrains.kotlin.analysis.api.standalone
## Types
### [`StandaloneAnalysisAPISession`](-standalone-analysis-a-p-i-session/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-standalone-analysis-a-p-i-session/index.html">StandaloneAnalysisAPISession</a>
</span></code></pre></div>
</div>

</div>
### [`StandaloneAnalysisAPISessionBuilder`](-standalone-analysis-a-p-i-session-builder/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">class </span><a href="-standalone-analysis-a-p-i-session-builder/index.html">StandaloneAnalysisAPISessionBuilder</a><span class="p">(</span>projectDisposable<span class="o">: </span>Disposable<span class="p">, </span>unitTestMode<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="p">)</span>
</span></code></pre></div>
</div>

</div>
### [`StandaloneWorkaroundApi`](-standalone-workaround-api/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html"><span class="se">Target</span></a><span class="p">(</span>allowedTargets<span class="o"> = </span><span class="p">[</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-l-a-s-s/index.html">AnnotationTarget.CLASS</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-p-r-o-p-e-r-t-y/index.html">AnnotationTarget.PROPERTY</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-c-o-n-s-t-r-u-c-t-o-r/index.html">AnnotationTarget.CONSTRUCTOR</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html">AnnotationTarget.FUNCTION</a><span class="p">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-t-y-p-e-a-l-i-a-s/index.html">AnnotationTarget.TYPEALIAS</a><span class="p">]</span><span class="p">)</span>
<span class="se">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-requires-opt-in/index.html"><span class="se">RequiresOptIn</span></a><span class="p">(</span>message<span class="o"> = </span><span class="s">"This API is provided as a workaround. Please read the API's documentation before opting in."</span><span class="p">)</span>
<span class="kd">annotation class </span><a href="-standalone-workaround-api/index.html">StandaloneWorkaroundApi</a>
</span></code></pre></div>
</div>


<div markdown>

Marks an API as a workaround. Before such an API is used, the user should read its documentation to understand its purpose and tradeoffs.


</div>

</div>
## Functions
### [`buildStandaloneAnalysisAPISession`](build-standalone-analysis-a-p-i-session.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><a href="build-standalone-analysis-a-p-i-session.html"><span class="nf">buildStandaloneAnalysisAPISession</span></a><span class="p">(</span>
    projectDisposable<span class="o">: </span>Disposable<span class="o"> = </span>Disposer.newDisposable("StandaloneAnalysisAPISession.project")<span class="p">, </span>
    unitTestMode<span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a><span class="o"> = </span><span class="kc">false</span><span class="p">, </span>
    init<span class="o">: </span><a href="-standalone-analysis-a-p-i-session-builder/index.html">StandaloneAnalysisAPISessionBuilder</a><span class="p">.</span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html">Unit</a>
<span class="p">)</span><span class="o">: </span><a href="-standalone-analysis-a-p-i-session/index.html">StandaloneAnalysisAPISession</a>
</span></code></pre></div>
</div>

</div>
### [`disposeGlobalStandaloneApplicationServices`](dispose-global-standalone-application-services.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="dispose-global-standalone-application-services.html"><span class="nf">disposeGlobalStandaloneApplicationServices</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Disposes global resources which would persist after unloading Analysis API and IJ platform classes.


</div>

</div>
