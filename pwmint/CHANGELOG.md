# Changelog

## [1.0.1] - 2026-09-26

### Added

- `--version` / `-v` option to display the current pwmint version.
- Configurable password character sets.
- Options to exclude lowercase letters with `--no-lowercase`.
- Options to exclude uppercase letters with `--no-uppercase`.
- Options to exclude digits with `--no-digits`.
- Options to exclude special characters with `--no-special`.
- Structured command-line help with common, password and passphrase options.
- Additional unit tests for password character set selection.

## [1.0.0] - 2026-09-25

### Added

- Secure password generation using Python `secrets`.
- Configurable password length from 15 to 64 characters.
- Secure passphrase generation with 4 to 10 pseudowords.
- Dynamic pseudoword generation without a persistent wordlist.
- Pseudowords with alternating consonant/vowel patterns.
- Configurable passphrase separator.
- Generation of multiple passwords or passphrases.
- Command-line interface.
- Unit tests for password, passphrase and pseudoword generation.
- PyInstaller builds for Linux x86_64 and ARM64.
