# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2026-07-22

- Added `ms-swift` (v4.4.1) and its dependencies
  - Pinned `peft<0.19`. `peft` 0.19 added a required `config` argument to its LoRA `Linear` layer that `ms-swift`'s LoRA dispatch code doesn't pass, breaking any LoRA usage. `ms-swift`'s own package metadata declares `peft<0.20`, so this incompatibility isn't caught by dependency resolution
- `gradio` is installed as a dependency of `ms-swift` and aggressively pins packages. This results in the following major downgrades:
  - Downgraded `pandas` from 3.0.3 to 2.3.3. In 2.3.3 copy-on-Write is no longer mandatory, so any submission mutating DataFrame slices/views could behave differently
  - Downgraded `pillow` from 12.2.0 to 11.3.0
  - Downgraded `aiofiles` from 25.1.0 to 24.1.0
  - Downgraded `jmespath` from 1.1.0 to 0.10.0

## 2026-06-15

### Added

- Initial commit

