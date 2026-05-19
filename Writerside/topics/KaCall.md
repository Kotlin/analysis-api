# KaCall

<warning>
<code>KaCall</code> is the <b>legacy</b> sealed base for the resolution API. New code should rely on
<a href="KaSingleOrMultiCall.md"/> &rarr; <a href="KaSingleCall.md"/> / <a href="KaMultiCall.md"/>.
See <a href="Migrating-Resolution-API.md"/>.
</warning>

`KaCall` represents a call within Kotlin code &mdash; function calls, property accesses, and other invocations &mdash;
through the legacy hierarchy that grew out of the `KtElement.resolveToCall(): KaCallInfo?` API.

<code-block lang="mermaid">
graph TB
  KaCall
  KaCall --> KaCallableMemberCall
  KaCallableMemberCall --> KaVariableAccessCall
  KaCallableMemberCall --> KaFunctionCall
  KaFunctionCall --> KaSimpleFunctionCall
  KaFunctionCall --> KaAnnotationCall
  KaFunctionCall --> KaDelegatedConstructorCall
  KaCall --> KaCompoundVariableAccessCall
  KaCall --> KaCompoundArrayAccessCall
</code-block>

The transitional types `KaFunctionCall`, `KaVariableAccessCall`, `KaAnnotationCall`, `KaDelegatedConstructorCall`,
`KaCompoundVariableAccessCall`, and `KaCompoundArrayAccessCall` still inherit `KaCall` so existing callers keep
compiling. New code reaches for the same types via [](KaSingleCall.md)/ [](KaMultiCall.md) instead.
