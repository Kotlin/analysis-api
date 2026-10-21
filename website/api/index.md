---
tags:
title: "Reference"
---

# Reference
## All modules
### [analysis-api](analysis-api/index.md)
- User-facing layer of the Analysis API. Maps the Kotlin PSI to its semantic representation
- Accessed through the [`analyze`](analysis-api/org.jetbrains.kotlin.analysis.api.session/analyze.md) entry point, which opens a
  [`KaSession`](analysis-api/org.jetbrains.kotlin.analysis.api/-ka-session/index.md) as a context parameter; capabilities are exposed as
  top-level `context(session: KaSession)` endpoints
- Key entities: [`KaSession`](analysis-api/org.jetbrains.kotlin.analysis.api/-ka-session/index.md),
  [`KaSymbol`](analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/index.md),
  [`KaType`](analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-type/index.md)

### [analysis-api-platform-interface](analysis-api-platform-interface/index.md)
- Abstraction layer between the API and its execution environments
- Defines how the API interacts with project structure and file systems
- Key entities: [`KotlinPlatformComponent`](analysis-api-platform-interface/org.jetbrains.kotlin.analysis.api.platform/-kotlin-platform-component/index.md),
  [`KaEngineService`](analysis-api-platform-interface/org.jetbrains.kotlin.analysis.api.platform/-ka-engine-service/index.md)

### [analysis-api-standalone](analysis-api-standalone/index.md)
- Command-line implementation for using the API outside of IDEs
- Provides project structure management that IDEs typically handle automatically

### [psi-api](psi-api/index.md)
- Foundation layer providing syntax tree representation through [`KtElement`](psi-api/org.jetbrains.kotlin.psi/-kt-element/index.md)
  hierarchy
- Uses `Kt` prefix (compared to `Ka` for Analysis API)
- Has own stability annotations mirroring the Analysis API ones:
  [`@KtExperimentalApi`](psi-api/org.jetbrains.kotlin.psi/-kt-experimental-api/index.md),
  [`@KtImplementationDetail`](psi-api/org.jetbrains.kotlin.psi/-kt-implementation-detail/index.md),
  [`@KtNonPublicApi`](psi-api/org.jetbrains.kotlin.psi/-kt-non-public-api/index.md),
  [`@KtIdeApi`](psi-api/org.jetbrains.kotlin.psi/-kt-ide-api/index.md),
  [`@KtPlatformInterface`](psi-api/org.jetbrains.kotlin.psi/-kt-platform-interface/index.md), `@KtSpi`, and
  [`@KtSpiExtensionPoint`](psi-api/org.jetbrains.kotlin.psi/-kt-spi-extension-point/index.md)
- Key entities: [`KtFile`](psi-api/org.jetbrains.kotlin.psi/-kt-file/index.md),
  [`KtDeclaration`](psi-api/org.jetbrains.kotlin.psi/-kt-declaration/index.md),
  and [`KtExpression`](psi-api/org.jetbrains.kotlin.psi/-kt-expression/index.md)

<hr/>
