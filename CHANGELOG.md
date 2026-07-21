# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2026-07-21

- Added `ms-swift` (v4.4.1) and its dependencies
  - Downgraded `pandas` from 3.0.3 to 2.3.3. `gradio` is installed as a dependency of `ms-swift` and requires <3.0. In 2.3.3 copy-on-Write is no longer mandatory, so any submission mutating DataFrame slices/views could behave differently
  - Downgraded `datasets` from 4.8.5 to 4.8.4 for compatibility with `ms-swift`
  - Pinned `peft<0.19`. `peft` 0.19 added a required `config` argument to its LoRA `Linear` layer that `ms-swift`'s LoRA dispatch code doesn't pass, breaking any LoRA usage. `ms-swift`'s own package metadata declares `peft<0.20`, so this incompatibility isn't caught by dependency resolution

## 2026-06-15

### Added

- Initial commit

