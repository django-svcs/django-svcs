---
title: Changelog
---

# 0.3.0

## Breaking Changes

- `svcs_from()` now accepts either an HTTP request or it infers the context from the `asgiref.Local()`, enabling use in async Django [#4]

## New Functionality

- Implement the DJP plugin interface [#6]

# 0.2.0

Basically the first semi-public release. A librarified version of the functionality I built to support [NomNom](https://nomnom.fans)
