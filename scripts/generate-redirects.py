#!/usr/bin/env python3
"""Generates redirect pages from the old Writerside URLs to the Zensical website.

Writerside published every topic as a flat, lowercase `<topic>.html` page (e.g., `fundamentals.html`), while Zensical
uses directory URLs that follow `website/` (e.g., `topics/Fundamentals/`). GitHub Pages has no server-side redirects,
so for each old URL the script writes a small HTML page into the built site that forwards to the new page and keeps
the `#anchor`. The mapping covers the pages that existed before the migration. Deleted pages that described an API
class redirect to its API reference page, and other deleted pages redirect to the home page.

Usage: scripts/generate-redirects.py. Run it after `zensical build`.
"""
import html
import os
import sys

SITE = os.path.join(os.path.dirname(__file__), "../site")

# Old page name (without `.html`) -> new page, relative to the site root.
REDIRECTS = {
    # Moved pages.
    "annotations": "topics/Annotations/",
    "diagnostics": "topics/Diagnostics/",
    "file-compilation": "topics/File-Compilation/",
    "fundamentals": "topics/Fundamentals/",
    "in-memory-file-analysis": "topics/In-memory-file-analysis/",
    "java-kotlin-bridging": "topics/Java-Kotlin-Bridging/",
    "legacy-diagnostics-api": "topics/Legacy-Diagnostics-API/",
    "legacy-resolution-api": "topics/Legacy-Resolution-API/",
    "migrating-resolution-api": "topics/Migrating-Resolution-API/",
    "receivers": "topics/Receivers/",
    "references-and-calls": "topics/References-And-Calls/",
    "resolution-candidates": "topics/Resolution-Candidates/",
    "resolution-fundamentals": "topics/Resolution-Fundamentals/",
    "resolving-calls": "topics/Resolving-Calls/",
    "resolving-symbols": "topics/Resolving-Symbols/",
    "statistics": "topics/Statistics/",
    "symbols": "topics/Symbols/",
    "typecreatormigrationguide": "topics/Migrating-Type-Creator/",
    "types": "topics/Types/",
    # API class pages replaced by the API reference.
    "kaannotation": "api/analysis-api/org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation/",
    "kaannotationcall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-annotation-call/",
    "kaannotationvalue": "api/analysis-api/org.jetbrains.kotlin.analysis.api.annotations/-ka-annotation-value/",
    "kaanonymousfunctionsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-function-symbol/",
    "kaanonymousobjectsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-anonymous-object-symbol/",
    "kabackingfieldsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-backing-field-symbol/",
    "kacall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-call/",
    "kacallablemembercall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-callable-member-call/",
    "kacallablereferencecall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-callable-reference-call/",
    "kacallablesymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-callable-symbol/",
    "kacallcandidateinfo": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-call-candidate-info/",
    "kacallinfo": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-call-info/",
    "kacallresolutionattempt": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-call-resolution-attempt/",
    "kacapturedtype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-captured-type/",
    "kaclasserrortype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-class-error-type/",
    "kaclassifiersymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-classifier-symbol/",
    "kaclasslikesymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-class-like-symbol/",
    "kaclasssymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-class-symbol/",
    "kaclasstype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-class-type/",
    "kacompoundarrayaccesscall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-array-access-call/",
    "kacompoundoperation": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-operation/",
    "kacompoundvariableaccesscall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-compound-variable-access-call/",
    "kaconstructorsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-constructor-symbol/",
    "kadeclarationsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-declaration-symbol/",
    "kadefinitelynotnulltype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-definitely-not-null-type/",
    "kadelegatedconstructorcall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-constructor-call/",
    "kadelegatedpropertycall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-delegated-property-call/",
    "kadiagnostic": "api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic/",
    "kadiagnosticcheckerkind": "api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-checker-kind/",
    "kadiagnostics": "api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostics/",
    "kadiagnosticwithpsi": "api/analysis-api/org.jetbrains.kotlin.analysis.api.diagnostics/-ka-diagnostic-with-psi/",
    "kadynamictype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-dynamic-type/",
    "kaenumentrysymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-enum-entry-symbol/",
    "kaerrortype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-error-type/",
    "kaflexibletype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-flexible-type/",
    "kaforloopcall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-for-loop-call/",
    "kafunctioncall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-function-call/",
    "kafunctionsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-function-symbol/",
    "kafunctiontype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-function-type/",
    "kaimplicitinvokecall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-implicit-invoke-call/",
    "kaintersectiontype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-intersection-type/",
    "kalocalvariablesymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-local-variable-symbol/",
    "kamulticall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-multi-call/",
    "kanamedclasssymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-named-class-symbol/",
    "kanamedfunctionsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-named-function-symbol/",
    "kapropertyaccessorsymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-property-accessor-symbol/",
    "kapropertysymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-property-symbol/",
    "kasimplecall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-call/",
    "kasimpleormulticall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-simple-or-multi-call/",
    "kasymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-symbol/",
    "kasymbolresolutionattempt": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-symbol-resolution-attempt/",
    "katype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-type/",
    "katypealiassymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-type-alias-symbol/",
    "katypeparametersymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-type-parameter-symbol/",
    "katypeparametertype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-type-parameter-type/",
    "katypeprojection": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-type-projection/",
    "kausualclasstype": "api/analysis-api/org.jetbrains.kotlin.analysis.api.types/-ka-usual-class-type/",
    "kavalueparametersymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-value-parameter-symbol/",
    "kavariableaccesscall": "api/analysis-api/org.jetbrains.kotlin.analysis.api.resolution/-ka-variable-access-call/",
    "kavariablesymbol": "api/analysis-api/org.jetbrains.kotlin.analysis.api.symbols/-ka-variable-symbol/",
    # Deleted pages.
    "case-studies": "",
    "declaring-k2-compatibility": "",
    "index_md": "",
    "kasimplefunctioncall": "",
    "migrating-from-k1": "",
    "other": "",
    "scopes": "",
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<title>Redirecting...</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace("{url}" + location.hash)</script>
</head>
<body><a href="{url}">This page has moved.</a></body>
</html>
"""

for old, new in REDIRECTS.items():
    if not os.path.exists(os.path.join(SITE, new, "index.html")):
        sys.exit(f"Redirect target for {old}.html does not exist: {new or '/'}")
    with open(os.path.join(SITE, old + ".html"), "w") as f:
        f.write(TEMPLATE.format(url=html.escape(new or "./")))
