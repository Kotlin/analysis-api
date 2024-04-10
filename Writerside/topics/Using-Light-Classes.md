# Using Light Classes

**Light classes** are wrappers around Kotlin declarations that present them as Java classes, methods, and fields. They
were used in K1 (the old Kotlin plugin) to leverage existing Java-based IDE features and APIs. However, they have
several drawbacks:

* **Performance:** Creating and maintaining light classes can be expensive, especially for large projects.
* **Complexity:**  They add another layer of abstraction, making the codebase more complex and harder to maintain.
* **Limitations:** Light classes may not accurately represent all Kotlin features, leading to potential inaccuracies.

K2 (the new Kotlin plugin) aims to minimize the use of light classes by introducing a new analysis API surface. This API
provides direct access to Kotlin symbols and types, eliminating the need for light classes in many scenarios.

### Why were light classes used in K1?

* **Integration with Java-based IDE features:** Many IDE features, like code completion, navigation, and refactorings,
  were built for Java. Light classes allowed Kotlin to leverage these features without rewriting them from scratch.
* **Interoperability with Java code:** Light classes facilitated interaction between Kotlin and Java code by presenting
  Kotlin declarations in a way that Java code could understand.

### Migration steps to avoid light classes in K2

1. **Use the new analysis API surface:** The new API provides direct access to Kotlin symbols and types, allowing you to
   work with Kotlin declarations directly without relying on light classes.
2. **Refactor code that relies on light classes:** Identify areas in the codebase that depend on light classes and
   refactor them to use the new API. This might involve replacing calls to `toLightClass` with calls to the appropriate
   API methods.
3. **Utilize new K2 features:** K2 offers new features that eliminate the need for light classes in specific scenarios.
   For example, the patch you mentioned introduces support for finding usages of data components without converting them
   to light classes.
4. **Gradually phase out light classes:** Don't try to eliminate all light classes at once. Instead, focus on areas
   where the new API provides a clear advantage and gradually migrate the codebase.

### Benefits of avoiding light classes

* **Improved performance:** By eliminating the overhead of creating and maintaining light classes, K2 can offer better
  performance, especially for large projects.
* **Reduced complexity:** The codebase becomes simpler and easier to maintain without the additional layer of
  abstraction introduced by light classes.
* **Enhanced accuracy:** Working with Kotlin declarations directly through the new API ensures more accurate
  representation of Kotlin features.

### Example

The `psiClass` field (a `PsiClass`) is replaced with `klass` (a `PsiElement`), allowing it to store Kotlin declarations
directly.

By following these migration steps and utilizing the new analysis API surface, we can effectively avoid light classes in
K2 and enjoy the associated benefits of improved performance, reduced complexity, and enhanced accuracy.