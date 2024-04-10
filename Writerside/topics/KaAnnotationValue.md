# KaAnnotationValue

`KaAnnotationValue` represents the value of an annotation argument. Annotation values must be compile-time constants
and can be of the following types:

* **Primitive Types:** Includes `Int`, `Long`, `Short`, `Byte`, `Char`, `Boolean`, `Float`, `Double`, and their unsigned
  counterparts.
* **String:** A string literal.
* **Enum Entry:** A reference to an enum entry.
* **Class Reference:** A reference to a class using the `::class` syntax.
* **Annotation:** A nested annotation call.
* **Array:** An array of any of the above types.

## Members

`val sourcePsi: KtElement?`
: The annotation value `PsiElement`. Only defined for annotations in source files, for libraries it always returns `null`.

## Subclasses

### `KaAnnotationValue.ConstantValue`

Represents a constant value, e.g., `"foo"` in `@JvmName("foo")`.

`val value: KaConstantValue`
: A constant value (a number, `Boolean`, `Char`, or a `String`, wrapped into a `KaConstantValue` abstraction).

### `KaAnnotationValue.EnumEntryValue`

Represents a enum entry value, e.g., `Color.RED`.

`val callableId: CallableId?`
: The enum entry name.

### `KaAnnotationValue.ClassLiteralValue`

Represents a class literal value, e.g., `String::class` or `Array<String>::class`.

`public val type: KaType`
: The class reference type.

### `KaAnnotationValue.NestedAnnotationValue`

Represents a nested annotation, e.g., `ReplaceWith("bar()")` in `@Deprecated("Use 'bar()' instead", ReplaceWith("bar()"))`.

`val annotation: KaAnnotation`
: The nested annotation.

### `KaAnnotationValue.ArrayValue`

Represents an array of other annotation values, passed either as `arrayOf(...)` or as a collection literal `[...]`.

`val values: Collection<KaAnnotationValue>`
: A list of annotation values inside the array.

### `KaAnnotationValue.UnsupportedValue`

Represents unsupported (invalid) expressions passed as annotation values.