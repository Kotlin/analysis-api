---
tags:
 - jvm
title: "disposeGlobalStandaloneApplicationServices"
---

# disposeGlobalStandaloneApplicationServices

<div class="dokka-symbol-block" style="background: color-mix(in srgb, var(--md-code-bg-color) 30%, transparent); margin-top: 0.5rem; padding: 1px .7rem .2rem .7rem; border-radius: 0.5rem;" markdown>

<div markdown>

<div class="highlight"><pre><code class="md-code__content"><span markdown><span class="kd">fun </span><a href="dispose-global-standalone-application-services.html"><span class="nf">disposeGlobalStandaloneApplicationServices</span></a><span class="p">(</span><span class="p">)</span>
</span></code></pre></div>
</div>


<div markdown>

Disposes global resources which would persist after unloading Analysis API and IJ platform classes.

<strong>Important:</strong> Once this function has been called, Analysis API and IntelliJ platform classes should not be used anymore. The classes should either be unloaded or the whole program should be shut down.

You don't need to use this endpoint right before your program shuts down. The purpose of this function is rather to dispose global resources which would persist after unloading Analysis API and IJ platform classes. For example, an IJ platform class may be registered with a JDK class. If Analysis API & IJ platform classes are unloaded, this global registration may keep alive the old class loader.

Note: Everything in Standalone is experimental, but this endpoint is likely to change in the near future. Please consult with the Analysis API team if you want to use this. (We'll want to know about your use case.)


</div>

</div>
