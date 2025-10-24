# Testing in K1 Locally

From IntelliJ IDEA version 2025.3, K2 mode is the default. If you need to test the plugin in K1 mode locally, pass the -Didea.kotlin.plugin.use.k1=true VM option to the IntelliJ IDEA run configuration or to the test task.

> If you are using IntelliJ IDEA version 2025.2 or older, use -Didea.kotlin.plugin.use.k2=false to enable K1 mode.

When using the [IntelliJ Platform Gradle Plugin](https://github.com/JetBrains/intellij-platform-gradle-plugin), you can specify the option directly in the `build.gradle.kts`
file.

To run in a debug IntelliJ IDEA instance, submit the option to the `RunIdeTask`:
```kotlin
tasks.named<RunIdeTask>(“runIde”) {
    jvmArgumentProviders += CommandLineArgumentProvider {
        listOf(“-Didea.kotlin.plugin.use.k1=true”)
    }
}
```

To run tests against the Kotlin IntelliJ IDEA plugin in the K1 mode, add the option to the `test` task:
```kotlin
tasks.test {
    jvmArgumentProviders += CommandLineArgumentProvider {
        listOf(“-Didea.kotlin.plugin.use.k1=true”)
    }
}
```
