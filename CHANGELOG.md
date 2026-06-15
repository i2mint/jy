# Changelog

All notable changes to this project are documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/);
each section corresponds to a git version tag (which is also the release
published to PyPI). Entries are commit subjects and PR titles, verbatim.

## [0.1.17] - 2024-12-03

### Added

- feat: enhance variable_declarations_pairs to use regex for removing 'export' keywords

## [0.1.16] - 2024-12-03

### Added

- feat: variable_declarations_pairs

## [0.1.15] - 2024-12-03

- chore: add installation note for tree-sitter version compatibility in parse_ts

## [0.1.14] - 2024-12-03

- chore: in init, from jy.ts_parse import parse_ts, parse_ts_with_oa

## [0.1.13] - 2024-11-12

- Update README.md

## [0.1.12] - 2024-10-28

### Added

- feat: remove the "don't include default in description" clause of prompt

## [0.1.11] - 2024-10-28

### Added

- feat: prompt engineering on ts parser

## [0.1.10] - 2024-10-28

### Added

- feat: parse_ts_with_oa as function instead of factory

## [0.1.9] - 2024-10-11

### Added

- feat: parse_ts_with_oa

## [0.1.8] - 2024-10-11

### Fixed

- fix: scrap doctest

## [0.1.7] - 2024-10-11

### Changed

- refactor: traverse -> parse_ts

## [0.1.6] - 2024-10-11

### Added

- feat: new CI
- feat: ts parsing (WIP)
- feat: promote func_name_and_params_pairs to root

## [0.1.0] - 2024-01-10

- Update setup.cfg
- worksite
- 0.1.5:
- Changing optional typing syntax to support older Python versions
- more ci
- add CI
- updated notebook
- 0.1.4: add doctests
- gitignore
- 0.1.3: test arrow functions
- 0.1.2:
- first push

### Added

- feat: extract_function_def_parts
- feat: extract_function_body
- feat: replace_ids_in_code
- feat: jy worksite notebook

### Changed

- refactor: Sig.kwargs_from_args_and_kwargs -> refactor: Sig.map_arguments

### Fixed

- fix: js parser
