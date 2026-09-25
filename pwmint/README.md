# pwmint - Secure Password and Passphrase Generator

<p align="center">
    <img src="images/pwmint.png" width="50%" height="50%" alt="pwmint - Secure Password and Passphrase Generator" />
</p>

## Description

`pwmint` is a small Python-based command-line tool for generating secure passwords and passphrases.

Passwords are generated using Python's `secrets` module and configurable character sets.

Passphrases are generated from dynamically created pseudowords. The pseudowords are generated in memory when needed and are not stored in a wordlist or cache.

`pwmint` is designed as a simple, local command-line utility without accounts, databases, network communication, or persistent secret storage.

### Project Goals

- Generate secure passwords from the command line
- Generate readable pseudoword-based passphrases
- Use Python's cryptographically secure `secrets` module
- Keep generated secrets in memory only
- Provide a small and easy-to-use CLI
- Support Linux AMD64 and ARM64
- Provide standalone binaries through PyInstaller
- Use automated testing and GitHub Actions

### Features

- Secure password generation
- Password length from 15 to 64 characters
- Lowercase, uppercase, digits and special characters
- Secure passphrase generation
- 4 to 10 pseudowords per passphrase
- Dynamically generated pseudowords
- Pseudowords with alternating consonant/vowel patterns
- Random pseudoword length from 6 to 12 characters
- Configurable passphrase separator
- Generate multiple passwords or passphrases
- No persistent wordlist
- No network communication
- No database
- No generated-secret logging
- Linux AMD64 support
- Linux ARM64 support
- PyInstaller standalone binaries
- Automated unit tests
- GitHub Actions build pipeline

## Security

`pwmint` uses Python's `secrets` module as the source of randomness for password and pseudoword generation.

The application does not use Python's `random` module for secret generation.

Generated passwords and passphrases are not stored in files, databases, caches, or other persistent storage.

The passphrase generator does not use a static wordlist. Pseudowords are generated dynamically in memory when a passphrase is created.

The pseudoword structure is designed to make generated passphrases easier to read while still using random character selection.

`pwmint` does not implement its own cryptographic algorithms.

### Important

`pwmint` is a password and passphrase generator. It is not a password manager.

Generated secrets are only printed to the terminal and should be handled appropriately by the user.

## Installation

### Linux AMD64

Download the latest AMD64 binary from the GitHub release page and make it executable:

```bash
wget -O ~/bin/pwmint https://github.com/hth73/hth-python-playground/releases/latest/download/pwmint-linux-amd64
chmod +x ~/bin/pwmint
```

Make sure `~/bin` is part of your `PATH`.

Check the installation:

```bash
pwmint --help
```

### Linux ARM64

Download the ARM64 binary:

```bash
wget -O ~/bin/pwmint https://github.com/hth73/hth-python-playground/releases/latest/download/pwmint-linux-arm64
chmod +x ~/bin/pwmint
```

Then:

```bash
pwmint --help
```

## Usage

### Generate a Password

Generate a password using the default length:

```bash
pwmint
```

Example:

```text
N"HFqz-gnE]aBzq15?
```

The default password length is 18 characters.

### Specify Password Length

Generate a 24-character password:

```bash
pwmint --length 24
```

or:

```bash
pwmint -l 24
```

Valid password lengths are:

```text
15-64 characters
```

### Generate Multiple Passwords

Generate five passwords:

```bash
pwmint --count 5
```

or:

```bash
pwmint -c 5
```

### Generate a Passphrase

Generate a passphrase with the default four pseudowords:

```bash
pwmint --passphrase
```

Example:

```text
olilonah-dubiyahota-upuhubepis-uxafudatazu
```

### Specify the Number of Words

Generate a passphrase with six pseudowords:

```bash
pwmint --passphrase --words 6
```

or:

```bash
pwmint -p -w 6
```

Valid values are:

```text
4-10 words
```

### Change the Separator

Use an underscore as the separator:

```bash
pwmint --passphrase --separator _
```

Example:

```text
fudebikuj_razikef_oqusijujurax_urokahixuqe
```

The separator can be an arbitrary string.

### Generate Multiple Passphrases

Generate five passphrases:

```bash
pwmint --passphrase --count 5
```

or:

```bash
pwmint -p -c 5
```

### Combine Options

Generate five six-word passphrases using `_` as separator:

```bash
pwmint --passphrase --words 6 --separator _ --count 5
```

## Command-Line Options

```text
usage: pwmint.py [-h] [-l LENGTH] [-c COUNT] [-p] [-w WORDS] [-s SEPARATOR]

Generate secure passwords or passphrases.

options:
  -h, --help            show this help message and exit
  -l, --length          Password length (15-64 characters).
  -c, --count           Number of secrets to generate.
  -p, --passphrase      Generate passphrases instead of passwords.
  -w, --words           Number of words (4-10, maximum 128 characters).
  -s, --separator       Separator between passphrase words (default: "-").
```

## Pseudoword Generator

Passphrases are generated from pseudowords rather than a static dictionary.

Each pseudoword:

- Is randomly generated in memory
- Contains 6 to 12 characters
- Uses lowercase letters `a-z`
- Uses the vowels `aeiou`
- Uses the consonants `bcdfghjklmnpqrstvwxyz`
- Starts randomly with either a vowel or consonant
- Alternates between vowels and consonants

Examples:

```text
gegicenof
exiqeqo
sojoxunuzoj
ofogogubid
```

The words are intended to be readable pseudowords and are not required to be real dictionary words.

Pseudowords are generated independently for each passphrase and are not persisted between executions.

## Development

Clone the repository:

```bash
git clone https://github.com/hth73/hth-python-playground.git
cd hth-python-playground/pwmint
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
pip install .
```

For development and testing, install the required development tools:

```bash
pip install pytest pyinstaller
```

### Run the CLI

```bash
python -m cli.pwmint
```

Example:

```bash
python -m cli.pwmint --passphrase --words 6
```

## Testing

`pwmint` includes unit tests for password, passphrase and pseudoword generation.

Run the complete test suite:

```bash
pytest
```

Current test status:

```text
28 passed
```

The test suite covers:

- Password length validation
- Password character sets
- Password generation
- Passphrase word count validation
- Passphrase separator handling
- Passphrase length validation
- Pseudoword length
- Pseudoword character set
- Vowel/consonant structure
- Random starting character type
- Pseudoword generation

## Building

`pwmint` uses PyInstaller to create standalone Linux binaries.

The project contains a PyInstaller specification file:

```text
pwmint.spec
```

Build locally:

```bash
pyinstaller pwmint.spec
```

The resulting binary is created in:

```text
dist/pwmint
```

Test the binary:

```bash
./dist/pwmint
```

Generate a passphrase:

```bash
./dist/pwmint --passphrase
```

### Supported Architectures

The GitHub Actions build pipeline creates standalone binaries for:

```text
Linux AMD64
Linux ARM64
```

The generated artifacts are named:

```text
pwmint-linux-amd64
pwmint-linux-arm64
```

## GitHub Actions

The project uses GitHub Actions to automatically build the standalone binaries.

The build pipeline:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs PyInstaller
4. Installs the `pwmint` project
5. Builds the binary using `pwmint.spec`
6. Runs a basic binary smoke test
7. Uploads the architecture-specific binary as an artifact

## Project Structure

```text
pwmint/
├── .github/
│   ├── instructions/
│   │   ├── copilot-instructions.md
│   │   ├── project-structure.md
│   │   └── requirements.md
│   └── planning/
│       └── plan-pwmint-pseudoword-generator.prompt.md
│
├── cli/
│   └── pwmint.py
│
├── src/
│   └── pwmint/
│       ├── passphrase.py
│       ├── password.py
│       └── pseudoword.py
│
├── tests/
│   ├── test_passphrase.py
│   ├── test_password.py
│   └── test_pseudoword.py
│
├── build/
├── dist/
├── pwmint.spec
├── pyproject.toml
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Project Status

`pwmint` is a personal learning project focused on Python development, secure random generation, CLI development, testing, packaging and CI/CD.

The project intentionally keeps the implementation small and focused.

It does not aim to become a password manager or credential storage solution.

## License

`pwmint` is licensed under the MIT License.

Copyright (c) 2026 Helmut Thurnhofer

See the [LICENSE](LICENSE) file for the complete license text.

---

© 2026 Helmut Thurnhofer - License: MIT
