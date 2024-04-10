# KaDiagnostic

A diagnostic message reported by the compiler checker.

## Members

`val factoryName: String`
: The name of the diagnostic factory that produced the diagnostic.

`val severity: KaSeverity`
: The severity of the diagnostic (e.g., `ERROR`, `WARNING`).

`val defaultMessage: String`
: The default text message associated with the diagnostic.