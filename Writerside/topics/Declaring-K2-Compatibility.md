# Declaring compatibility with K2

The Kotlin IntelliJ plugin assumes that a dependent third-party plugin *does not* support K2 Kotlin out of the box. Such
incompatible plugins will not be loaded if the K2 mode is currently enabled.

Once a plugin has been migrated to the Analysis API, a setting should be added to its `plugin.xml` to declare its
compatibility with the K2 mode. Even if the plugin does not use any of the old K1 analysis functions and no migration to
the Analysis API is needed, compatibility with the K2 Kotlin plugin should be declared explicitly nonetheless.

Starting from IntelliJ 2024.2.1 (Preview), the following setting in the `plugin.xml` can be used to declare
compatibility with the K2 mode:

```xml
<extensions defaultExtensionNs="org.jetbrains.kotlin">
    <supportsKotlinPluginMode supportsK2="true" />
</extensions>
```

It is also possible to declare compatibility with *only* the K2 mode:

```xml
<extensions defaultExtensionNs="org.jetbrains.kotlin">
    <supportsKotlinPluginMode supportsK1="false" supportsK2="true" />
</extensions>
```

Currently, the default setting for `supportsK1` is `true` and for `supportsK2` is `false`.

To test it locally when using the [IntelliJ Platform Gradle Plugin](https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin.html), add a [dependency](https://plugins.jetbrains.com/docs/intellij/tools-intellij-platform-gradle-plugin-dependencies-extension.html) on the IntelliJ IDEA Community 2024.2.1 (`intellijIdeaCommunity("2024.2.1")`) or higher.

A number of third-party plugins may already be enabled in the K2 mode without a `supportsK2` declaration. The IntelliJ
Kotlin plugin keeps an [internal list](https://github.com/JetBrains/intellij-community/blob/master/platform/core-impl/resources/pluginsCompatibleWithK2Mode.txt)
of plugins which are known to be compatible with the K2 mode as they do not use Kotlin analysis. The authors of these
plugins should not be surprised if their plugin already works in the K2 mode. However, it's still advised to check and
declare K2 support explicitly as this list is not future-proof and could potentially contain unsafe plugins due to some
circumstances.