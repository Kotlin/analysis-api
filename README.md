# Kotlin Analysis API Guide

[![official project](http://jb.gg/badges/official.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repository contains documentation sources for the Kotlin Analysis API library. You might want to check the 
[Analysis API guide](https://kotl.in/analysis-api) which is generated from this repository.

The sources of the Analysis API itself live inside the [Kotlin language repository](https://github.com/JetBrains/kotlin/tree/master/analysis).

---

The Analysis API is a powerful library for analyzing code in Kotlin. Built on top of the Kotlin PSI syntax tree, it 
provides access to various semantic information, including reference targets, expression types, declaration scopes, 
diagnostics, and more.

## Editing the Website

The website is built using [Zensical](https://zensical.org/) website generator.
The config is a single [.toml](zensical.toml) file.
All `.md` documentation files are located in the `website` directory.
To adjust the website, edit the pages inside there or customize the config using the [Zensical documentation](https://zensical.org/docs/setup/basics/).

To run the website locally, call `./serve.sh` with optional arguments for `zensical serve` command.
E.g., `./serve.sh -a  localhost:8000 -o`.