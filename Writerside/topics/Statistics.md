# Statistics

When run with the IntelliJ Kotlin plugin, the Analysis API optionally allows gathering statistics (such as metrics)
about analysis activity. All data is saved **locally** in a log file. It is *not* sent over any network connection. 
Furthermore, the feature requires an explicit opt-in.

These statistics allow us as Analysis API developers to better understand how the Analysis API handles certain
workloads. For you as a user of the Analysis API, the statistics can also provide some insights into how your plugin 
uses the Analysis API. The log files are easily shareable, allowing you to send them to us if you encounter any 
problems (especially around performance and memory consumption) or include them in your YouTrack issues.

As of now, we are tracking only a few metrics, but we're planning to add many more. It's also worth noting that only the
K2 backend of the Analysis API collects statistics.

The feature is built on the same OpenTelemetry-based framework as IntelliJ's tracing and metrics collection, so using 
the approach described in this guide can also help with IntelliJ-specific statistics such as virtual file system 
metrics. The framework is mainly developed for internal use: it is not a public API and JetBrains makes no compatibility 
guarantees. Nonetheless, you're welcome to use it as an external user.

## Configuration

To enable the local Analysis API statistics collection in IntelliJ IDEA, open the 
[Registry](https://stackoverflow.com/questions/28415695/how-do-you-set-a-value-in-the-intellij-registry) and enable the
following setting:

```
kotlin.analysis.statistics
```

If the registry setting isn't listed, it is likely that that version of IntelliJ is not recent enough.

After enabling the setting, restart the IDE. It will automatically begin to collect Analysis API metrics and write them 
to a local log file.

By default, metrics are collected every 60 seconds. This is a coarse-grained view and may not be sufficient for every 
use case. To specify more granular collection, the interval can be adjusted with a 
[system property](https://www.jetbrains.com/help/idea/tuning-the-ide.html#configure-jvm-options). For example, to 
specify an interval of one second (1000ms):

```
-Didea.diagnostic.opentelemetry.metrics-reporting-period-ms=1000
```

It is recommended to enable `kotlin.analysis.statistics` only when needed, as it will impact performance. For example,
we increment counters in hot spots like symbol providers. The metrics reporting period also contributes to the 
performance impact, not only for Analysis API statistics, but more broadly all metrics that IntelliJ locally collects 
with OpenTelemetry. So it's best to use these settings only temporarily.

## Locating & plotting metrics

The collected metrics will be written into a CSV file in IntelliJ's 
[log folder](https://intellij-support.jetbrains.com/hc/en-us/articles/207241085-Locating-IDE-log-files). The file should
be called `open-telemetry-metrics.<date>-<time>.csv`. There may be multiple files from multiple runs, and usually the 
most recent file is the relevant one. 

The CSV file contains not only Analysis API metrics, but all metrics collected by IntelliJ (such as virtual file system 
metrics). You can share this file with us, for example together with a
[new YouTrack issue](https://youtrack.jetbrains.com/newIssue?project=KT).

You can also open the CSV file in the dedicated metrics plotter. Open `open-telemetry-metrics-plotter.html`, which is
in the same log folder as the CSV, in your browser. You should see the following page:

![](statistics-metrics-plotter-open-file.png)

Drag the CSV file onto the page or open it with the file chooser.

The website will show a few default graphs, but none of them are directly related to the Analysis API. To plot Analysis 
API metrics, scroll to the last section "Plot other". In the drop-down menu, search for `kotlin.analysis` and select the 
metrics you're interested in. For example, you can select `kotlin.analysis.analysisSessions.anlyze.invocations` to check
the number of `analyze` invocations.

![](statistics-metrics-plotter-analyze-invocations.png)
