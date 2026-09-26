# pwmint - Secure Password and Passphrase Generator

<p align="center">
    <img src="images/pwmint.png" width="50%" height="50%" alt="pwmint - Secure Password and Passphrase Generator" />
</p>

## Description

**pwmint** is a small command-line tool for generating secure passwords and passphrases.

The project was created as a practical Python learning project with a focus on:

- simple and readable Python code
- secure random generation
- command-line interfaces
- unit testing with pytest
- application packaging with PyInstaller
- GitHub Actions and CI/CD
- AI-assisted development with GitHub Copilot

The project deliberately avoids unnecessary complexity.

> Learn. Build. Experiment. Secure.

---

## Features

### Password Generation

- Secure password generation using Python `secrets`
- Default password length: **18 characters**
- Supported password length: **15-64 characters**
- Configurable character sets
- Uppercase letters
- Lowercase letters
- Digits
- Special characters
- Generate multiple passwords with a single command

### Passphrase Generation

- Secure passphrase generation using Python `secrets`
- 4-10 pseudowords per passphrase
- Maximum passphrase length: **128 characters**
- Configurable word separator
- No repeated pseudowords within the same passphrase
- Dynamic pseudoword generation without a persistent wordlist

### Pseudoword Generator

Pseudowords are generated dynamically in memory.

Each pseudoword:

- contains 6-12 lowercase letters
- uses vowels and consonants
- follows an alternating vowel/consonant pattern
- can start with either a vowel or consonant
- is generated using `secrets`

No external wordlist or persistent word database is required.

---

## Security

pwmint uses Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module for random generation.

The project does not use `random` for password or passphrase generation.

Generated passwords and passphrases are not:

- stored
- transmitted
- uploaded
- written to a database
- sent to an external service

pwmint is a generator, not a password manager.

---

## Installation

### Python

Python **3.12 or newer** is required.

Clone the repository and install pwmint in editable mode:

```bash
git clone https://github.com/hth73/hth-python-playground.git
cd hth-python-playground/pwmint

python -m venv .venv
source .venv/bin/activate

python -m pip install -e .
```

### Run from Source

```bash
python -m cli.pwmint
```

---

## Usage

### Generate a Password

```bash
pwmint
```

Example:

```text
dV*MZu%MlJ"=K2[2Y4
```

### Generate a Password with a Specific Length

```bash
pwmint --length 24
```

or:

```bash
pwmint -l 24
```

### Generate Multiple Passwords

```bash
pwmint --count 5
```

or:

```bash
pwmint -c 5
```

The `--count` option can be used for both passwords and passphrases.

---

## Password Character Sets

All character sets are enabled by default.

Individual character sets can be excluded when required.

### Exclude Lowercase Letters

```bash
pwmint --no-lowercase
```

### Exclude Uppercase Letters

```bash
pwmint --no-uppercase
```

### Exclude Digits

```bash
pwmint --no-digits
```

### Exclude Special Characters

```bash
pwmint --no-special
```

### Combine Options

Options can be combined:

```bash
pwmint --no-digits --no-special
```

This generates passwords containing only uppercase and lowercase letters.

Another example:

```bash
pwmint --no-digits --no-special --no-lowercase
```

This generates passwords containing only uppercase letters.

At least one character set must remain enabled.

---

## Generate Passphrases

Use `--passphrase` or `-p`:

```bash
pwmint --passphrase
```

Example:

```text
fudebikuj-razikef-oqusijujurax-urokahixuqe
```

### Generate Multiple Passphrases

```bash
pwmint --passphrase --count 5
```

or:

```bash
pwmint -p -c 5
```

### Number of Words

The default is 4 words.

```bash
pwmint --passphrase --words 6
```

or:

```bash
pwmint -p -w 6
```

The supported range is 4-10 words.

### Custom Separator

```bash
pwmint --passphrase --separator "_"
```

Example:

```text
fudebikuj_razikef_oqusijujurax_urokahixuqe
```

An empty separator is also supported.

---

## Command-Line Options

```text
usage: pwmint.py [-h] [-v] [-c [1-100]] [-l [15-64]]
                 [--no-lowercase] [--no-uppercase] [--no-digits]
                 [--no-special] [-p] [-w [4-10]] [-s SEPARATOR]

Generate secure passwords or passphrases.

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

common options:
  -c [1-100], --count [1-100]
                        Number of secrets to generate.

password options:
  -l [15-64], --length [15-64]
                        Password length (15-64 characters).
  --no-lowercase        Exclude lowercase letters.
  --no-uppercase        Exclude uppercase letters.
  --no-digits           Exclude digits.
  --no-special          Exclude special characters.

passphrase options:
  -p, --passphrase      Generate passphrases instead of passwords.
  -w [4-10], --words [4-10]
                        Number of words (4-10, maximum 128 characters).
  -s SEPARATOR, --separator SEPARATOR
                        Separator between passphrase words (default: "-").
```

---

## Version

Display the installed pwmint version with:

```bash
pwmint --version
```

or:

```bash
pwmint -v
```

Example:

```text
pwmint 1.0.1
```

The version is defined centrally in `pyproject.toml`.

---

## Testing

pwmint uses [pytest](https://pytest.org/) for unit testing.

Run the complete test suite:

```bash
pytest -v
```

The current test suite covers:

- password generation
- password length validation
- password character sets
- password uniqueness
- passphrase generation
- passphrase validation
- separator handling
- pseudoword generation
- pseudoword length and character validation

Current test status:

```text
31 passed
```

---

## Building

pwmint can be packaged as a standalone executable using [PyInstaller](https://pyinstaller.org/).

Build locally:

```bash
rm -rf build dist
pyinstaller pwmint.spec
```

The resulting executable is:

```text
dist/pwmint
```

Test the binary:

```bash
./dist/pwmint
./dist/pwmint --passphrase
./dist/pwmint --version
```

---

## GitHub Actions

GitHub Actions automatically builds pwmint for:

- Linux AMD64
- Linux ARM64

The workflow uses:

- Python 3.12
- PyInstaller
- GitHub Actions
- separate runners for AMD64 and ARM64

The generated binaries are uploaded as GitHub Actions artifacts.

Workflow:

```text
Checkout
    ↓
Setup Python
    ↓
Install Dependencies
    ↓
Build with PyInstaller
    ↓
Test Binary
    ↓
Upload Artifact
```

---

## Project Structure

```text
pwmint/
├── .github/
│   ├── instructions/
│   └── planning/
│
├── build/
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
├── pwmint.spec
├── pyproject.toml
├── README.md
├── CHANGELOG.md
└── LICENSE
```

Generated directories such as `build/`, `dist/`, `.pytest_cache/` and `__pycache__/` are not part of the source distribution.

---

## Development

The project is intentionally kept small and easy to understand.

The architecture separates:

```text
CLI
 │
 ├── Password Generator
 │
 └── Passphrase Generator
        │
        └── Pseudoword Generator
```

The core generation logic is kept independent from the command-line interface so that it can be reused by other interfaces in the future.

A graphical user interface is currently not part of the project scope.

---

## Project Status

Current version: **1.0.1**

The project is a personal learning and experimentation project focused on Python development, secure random generation, testing, packaging and CI/CD.

---

## License

This project is licensed under the MIT License.

See [LICENSE](../LICENSE) for details.
