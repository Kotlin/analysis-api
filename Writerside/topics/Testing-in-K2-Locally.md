# Testing in K2 Locally

To test the plugin in K2 mode locally, pass the `-Didea.kotlin.plugin.use.k2=true` VM option to the IntelliJ IDEA
run test, or to the test task.

When using the [IntelliJ Platform Gradle Plugin](https://github.com/JetBrains/intellij-platform-gradle-plugin), you can specify the option directly in the `build.gradle.kts`
file.

To run in a debug IntelliJ IDEA instance, submit the option to the `RunIdeTask`:

```kotlin
tasks.named<RunIdeTask>("runIde") {
    jvmArgumentProviders += CommandLineArgumentProvider {
        listOf("-Didea.kotlin.plugin.use.k2=true")
    }
}
```

To run tests against the Kotlin IntelliJ IDEA plugin in the K2 mode, add the option to the `test` task:

```kotlin
tasks.test {
    jvmArgumentProviders += CommandLineArgumentProvider {
        listOf("-Didea.kotlin.plugin.use.k2=true")
    }
}
```
