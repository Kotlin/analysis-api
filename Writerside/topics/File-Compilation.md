# File Compilation

<note>Experimental API. Subject to changes.</note>

Analysis API enables in-memory compilation of Kotlin files. This allows your tools and plugins to generate and compile
Kotlin code without writing files to disk or invoking the command-line compiler.

## Usage

To compile Kotlin code, you need to provide:

* `KtFile`: The Kotlin file to compile (might be a `KtCodeFragment`);
* `CompilerConfiguration`: A configuration instance containing compiler settings, such as a module name, and a target
  language version;
* `KaCompilerTarget`: The target platform for compilation (currently, only JVM is supported
  with `KaCompilerTarget.Jvm`);
* `allowedErrorFilter`: A function that filters allowed diagnostics. Compilation fails if there are errors
  that this function rejects.

Here's an example of compiling a `KtFile`:

```kotlin
@RequiresReadLock
@OptIn(KaExperimentalApi::class)
fun performCompilation(file: KtFile): List<ByteArray> {
    val configuration = CompilerConfiguration() // configure compiler settings
    val target = KaCompilerTarget.Jvm(ClassBuilderFactories.BINARIES)

    analyze(file) {
        val result = useSiteSession.compile(file, configuration, target) {
            // Filter allowed diagnostics (optional)
            it.severity != KaSeverity.ERROR
        }

        when (result) {
            is KaCompilationResult.Success -> {
                // Process compiled output
                return result.output.map { it.content }
            }
            is KaCompilationResult.Failure -> {
                // Handle compilation errors
                throw RuntimeException("Compilation failed: ${result.errors}")
            }
        }
    }
}
```

The `compile` function throws a `KaCodeCompilationException` if any unexpected errors occur during compilation.
Handle this exception appropriately in your code.

## KaCompilationResult

The `compile` function returns a `KaCompilationResult`, which can be either:

* `KaCompilationResult.Success`: Compilation was successful. You can access the generated output files through
  the `output` property.
* `KaCompilationResult.Failure`: Compilation failed due to errors. The `errors` property contains a list of the
  encountered diagnostics.

## Output Files

The `output` property of `KaCompilationResult.Success` provides a list of `KaCompiledFile` instances, each containing:

`val path: String`
: The relative path of the compiled file.

`val sourceFiles: List<File>`
: The source files that contributed to the compiled file.

`val content: ByteArray`
: The content of the compiled file as a byte array.