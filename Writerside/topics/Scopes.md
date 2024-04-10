# Scopes

A scope acts as a container for declarations, including functions, properties, classes, and type aliases. When resolving
a reference to a name, the compiler searches through a series of scopes to find the corresponding declaration. The order
and types of scopes considered depend on the context of the reference.

In Analysis API, scopes are visible through the `KaScope` interface. To get a scope, use the
[scope utilities](KaClassSymbol.md#scope-utilities) defined on classes and scripts.

## Members

`val declarations: Sequence<KaDeclarationSymbol>`
: All declarations available in the scope.

`val classifiers: Sequence<KaClassifierSymbol>`
: All classifier declarations available in the scope.

`fun classifiers(nameFilter: (Name) -> Boolean): Sequence<KaClassifierSymbol>`
: Classifier declarations available in the scope, filtered with the supplied `nameFilter`.

`val callables: Sequence<KaCallableSymbol>`
: All callable declarations available in the scope.

`fun callables(nameFilter: (Name) -> Boolean): Sequence<KaCallableSymbol>`
: Callable declarations available in the scope, filtered with the supplied `nameFilter`.

`val constructors: Sequence<KaConstructorSymbol>`
: Constructor declarations available in the scope.