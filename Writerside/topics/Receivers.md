# Receivers

Receivers play a vital role in Kotlin, enabling extension functions and member functions. The Analysis API
provides abstractions for different kinds of receivers, allowing you to analyze them in your code.

## Types of Receivers

There are two primary types of receivers in Kotlin:

* **Dispatch receiver:** Represents the instance of a class on which a member function is called. It's implicitly passed
  to the member function and accessible using the `this` keyword.
* **Extension receiver:** Represents the object that an extension function extends. It's explicitly declared in the
  function signature and accessible using the `this` keyword within the function body.

In addition, there are context receivers, which are deprecated and will be eventually replaced with
[context parameters](https://github.com/Kotlin/KEEP/blob/context-parameters/proposals/context-parameters.md).

### Dispatch Receiver

A dispatch receiver is associated with member functions, which are functions defined within a class. When a member
function is called on an object, the object itself becomes the dispatch receiver.

**Example:**

```kotlin
class MyClass {
    fun memberFunction() {
        // `this` refers to the dispatch receiver (instance of MyClass)
        println(this)
    }
}

val myObject = MyClass()
myObject.memberFunction() // `myObject` is the dispatch receiver
```

### Extension Receiver

An extension receiver is associated with extension functions, which are functions that extend the functionality of a
class without modifying the class itself. The extension receiver is the object being extended.

**Example:**

```kotlin
fun String.extensionFunction() {
    // `this` refers to the extension receiver (instance of String)
    println(this.length)
}

val myString = "Hello"
myString.extensionFunction() // `myString` is the extension receiver
```

## Key Differences

While both dispatch and extension receivers are accessible using the `this` keyword within the function body, there
are a few differences.

* **Declaration.** Dispatch receivers are implicit and don't appear in the function signature. Extension receivers are
  explicitly declared in the function signature.
* **Purpose.** Dispatch receivers are used for member functions that operate on the state of an object. Extension
  receivers are used to add new functions to existing classes.

## Analysis API Representation

The Analysis API represents receivers using the `KaReceiverValue` sealed class. The specific subclasses are:

* **KaExplicitReceiverValue:** Represents an explicit receiver expression, e.g., `foo` in `foo.toString()`;
* **KaImplicitReceiverValue:** Represents an implicit receiver, such as in `toString()` (without an explicit receiver).

## Declarations with both receivers

Member extension functions can have both dispatch and extension receivers. For example:

```kotlin
class MyClass {
    fun String.extensionFunction() {
        // `this` refers to the String receiver (extension receiver)
        // `this@MyClass` refers to the MyClass instance (dispatch receiver)
        println(this.length + this@MyClass.hashCode())
    }
}
```

In the Analysis API, you can access both receivers using the corresponding properties of `KtCallableMemberCall`:

```kotlin
val callInfo = ...
when (callInfo) {
    is KtSuccessCallInfo -> {
        val call = callInfo.call
        if (call is KtSimpleFunctionCall) {
            val dispatchReceiver = call.partiallyAppliedSymbol.dispatchReceiver
            val extensionReceiver = call.partiallyAppliedSymbol.extensionReceiver
            // Use dispatchReceiver and extensionReceiver
        }
    }
}
```