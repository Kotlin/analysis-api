# KaCall

Represents a call within Kotlin code. It encompasses various types of calls, including function calls, property
accesses, and other invocations. Analysis API provides a hierarchy of `KtCall` subtypes to model different call kinds.

<code-block lang="mermaid">
graph LR
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