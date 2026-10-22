---
tags:
 - jvm
title: "KotlinRestrictedAnalysisService"
---

# KotlinRestrictedAnalysisService

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">interface </span><a href="index.html">KotlinRestrictedAnalysisService</a> : <a href="../../org.jetbrains.kotlin.analysis.api.platform/-kotlin-optional-platform-component/index.html">KotlinOptionalPlatformComponent</a>
</span></code></pre></div>Allows the platform to communicate to the Analysis API about restricted analysis. When analysis is restricted, the platform typically lacks full, up-to-date information about the project. For example, [`declaration providers`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md) might return incomplete results. In addition, the available information might change without associated [`modification events`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-modification-event-kind/index.md).

As a consequence, results returned by the Analysis API might be incomplete or incorrect. Handling such results is the responsibility of the Analysis API user. The user should be aware of the platform's conventions around its restricted analysis mode and develop accordingly.

During restricted analysis, the platform might require accesses of affected data (such as indices) to be wrapped in a specific handler, see [`withRestrictedDataAccess`](index.md#withrestricteddataaccess).

In IntelliJ, restricted analysis mode is synonymous with its [dumb mode](https://plugins.jetbrains.com/docs/intellij/indexing-and-psi-stubs.html#dumb-mode), which is typically enabled when files are being re-indexed.

Any exceptions which occur during restricted analysis are wrapped in [`KaRestrictedAnalysisException`](../-ka-restricted-analysis-exception/index.md) (see its KDoc for more information).

If [`KotlinRestrictedAnalysisService`](index.md) is not registered, it's assumed that the platform has no conception of restricted analysis. When there is a restricted analysis mode, but analysis should be disallowed during the mode, [`KotlinRestrictedAnalysisService`](index.md) should still be implemented, setting [`isRestrictedAnalysisAllowed`](index.md#isrestrictedanalysisallowed) to `false`.

### Implementation notes
It is the responsibility of the platform to ensure that [`declaration providers`](../../org.jetbrains.kotlin.analysis.api.platform.declarations/-kotlin-declaration-provider/index.md) and [`package providers`](../../org.jetbrains.kotlin.analysis.api.platform.packages/-kotlin-package-provider/index.md) are adapted to restricted analysis. This also extends to other platform components which might be affected by restricted analysis.

The platform must ensure that [`modification events`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-modification-event-kind/index.md) are published when entering and exiting restricted analysis mode:

 - The platform must publish modification events for all [`KaModule`](../../../analysis-api/org.jetbrains.kotlin.analysis.api.project-structure/-ka-module/index.md)s which might be affected by incomplete, inconsistent, or changing information when entering restricted analysis mode. The kind of modification event (module state modification, out-of-block modification) to publish depends on the event which triggered the restricted analysis mode.


 -  - Generally, the usual modification events published by the platform in reaction to project changes should be sufficient to cover        this requirement.



 - A [`global module state modification event`](../../org.jetbrains.kotlin.analysis.api.platform.modification/-kotlin-modification-event-kind/-g-l-o-b-a-l_-m-o-d-u-l-e_-s-t-a-t-e_-m-o-d-i-f-i-c-a-t-i-o-n/index.md) must be published when exiting restricted analysis mode, to mitigate potential issues with inconsistent cache states that accumulated during restricted analysis.



</div>

## Types
### [`Companion`](-companion/index.md)

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">object </span><a href="-companion/index.html">Companion</a>
</span></code></pre></div>
</div>

</div>
## Properties
### isAnalysisRestricted

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isanalysisrestricted">isAnalysisRestricted</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether the Analysis API platform is currently in restricted analysis mode.


</div>

</div>
### isRestrictedAnalysisAllowed

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">val </span><a href="index.html#isrestrictedanalysisallowed">isRestrictedAnalysisAllowed</a><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a>
</span></code></pre></div>
</div>


<div markdown>

Whether Analysis API access during restricted analysis mode is allowed by the platform. Such analysis activity is also called simply restricted analysis.

Depending on this setting, the Analysis API will act differently during restricted analysis mode:

 - When restricted analysis is allowed, requests to the Analysis API will be accepted, and analysis will be performed according to the rules of restricted analysis (see [`KotlinRestrictedAnalysisService`](index.md)).


 - Otherwise, the Analysis API will reject the request using [`rejectRestrictedAnalysis`](index.md#rejectrestrictedanalysis).



</div>

</div>
## Functions
### rejectRestrictedAnalysis

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><a href="index.html#rejectrestrictedanalysis"><span class="nf">rejectRestrictedAnalysis</span></a><span class="p">(</span><span class="p">)</span><span class="o">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-nothing/index.html">Nothing</a>
</span></code></pre></div>
</div>


<div markdown>

Throws an exception after Analysis API access was rejected during restricted analysis mode.


</div>

</div>
### runWithRestrictedDataAccess

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">abstract </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#runwithrestricteddataaccess">R</a><span class="o">> </span><a href="index.html#runwithrestricteddataaccess"><span class="nf">runWithRestrictedDataAccess</span></a><span class="p">(</span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="index.html#runwithrestricteddataaccess">R</a><span class="p">)</span><span class="o">: </span><a href="index.html#runwithrestricteddataaccess">R</a>
</span></code></pre></div>
</div>


<div markdown>

Runs [`action`](index.md#runwithrestricteddataaccess) in a context where the platform allows access to the data affected by restricted analysis mode.

On the client side, please use [`withRestrictedDataAccess`](index.md#withrestricteddataaccess) instead.


</div>

</div>
### withRestrictedDataAccess

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">inline </span><span class="kd">fun </span><span class="o"><</span><a href="index.html#withrestricteddataaccess">R</a><span class="o">> </span><a href="index.html">KotlinRestrictedAnalysisService</a><span class="o">?</span><span class="p">.</span><a href="index.html#withrestricteddataaccess"><span class="nf">withRestrictedDataAccess</span></a><span class="p">(</span><span class="kd">crossinline </span>action<span class="o">: </span><span class="p">(</span><span class="p">)</span><span class="o"> -> </span><a href="index.html#withrestricteddataaccess">R</a><span class="p">)</span><span class="o">: </span><a href="index.html#withrestricteddataaccess">R</a>
</span></code></pre></div>
</div>


<div markdown>

Runs [`action`](index.md#withrestricteddataaccess) with [`KotlinRestrictedAnalysisService.runWithRestrictedDataAccess`](index.md#runwithrestricteddataaccess) if deemed necessary and applicable.


</div>

</div>
