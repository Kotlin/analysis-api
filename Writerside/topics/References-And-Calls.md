# References and Calls

The Analysis API answers two independent questions about resolvable Kotlin PSI:

* **What declaration does this PSI element refer to?** &mdash; the symbol the element literally points to.
  Read [](Resolving-Symbols.md).
* **How is this expression executed at this site?** &mdash; the callable selected at the call site, with receivers,
  type arguments, and value arguments. Read [](Resolving-Calls.md).

[](Resolution-Fundamentals.md) introduces both views together, the `KtResolvable` /
`KtResolvableCall` marker interfaces, and the difference between the "plain" (`resolveSymbol` / `resolveCall`) and
"try" (`tryResolveSymbols` / `tryResolveCall`) forms.

If you need every overload the compiler considered at a call site &mdash; including ones it rejected &mdash; see
[](Resolution-Candidates.md).

If you are upgrading code that uses the older `KtReference.mainReference.resolveTo...()` /
`KtElement.resolveToCall(): KaCallInfo?` API, see [](Migrating-Resolution-API.md).

<warning>
The resolution API is annotated <code>@KaExperimentalApi</code> and may change between versions until it
stabilizes. Every entry point requires <code>@OptIn(KaExperimentalApi::class)</code>.
</warning>
