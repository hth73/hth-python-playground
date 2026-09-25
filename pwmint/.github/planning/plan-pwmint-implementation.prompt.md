# pwmint – Implementation Plan

## Purpose

This document defines the implementation plan for the `pwmint` project.

The project must be implemented incrementally.

Do not implement the complete project in one step.

Each implementation step should be completed, reviewed and tested before
moving to the next step.

The following project documentation is authoritative:

```text
.github/instructions/requirements.md
.github/instructions/project-structure.md
.github/instructions/copilot-instructions.md
```

These documents must be followed during implementation.

---

# CLI Design

The command-line interface should be simple and require as little
typing as possible.

The default command:

```bash
pwmint
```

must generate one secure password using the default settings.

The CLI must not require a `password` subcommand.

Passphrase generation is selected using:

```bash
pwmint --passphrase
```

or:

```bash
pwmint -p
```

---

## Default Password

The default password configuration is:

```text
length:        18
count:         1
lowercase:     enabled
uppercase:     enabled
digits:        enabled
special:       enabled
```

Example:

```bash
pwmint
```

The generated password should contain characters from the enabled
character sets.

The default length of 18 characters is intentional.

The supported password length range is:

```text
15–64 characters
```

---

## CLI Options

The following options are planned.

### Password Options

```text
--length
-l
```

Set the password length.

Example:

```bash
pwmint --length 24
```

or:

```bash
pwmint -l 24
```

---

```text
--count
-c
```

Set the number of generated passwords or passphrases.

Example:

```bash
pwmint --count 5
```

or:

```bash
pwmint -c 5
```

---

### Passphrase Options

```text
--passphrase
-p
```

Generate a passphrase instead of a password.

Example:

```bash
pwmint --passphrase
```

or:

```bash
pwmint -p
```

---

```text
--words
-w
```

Set the number of words used for a passphrase.

Example:

```bash
pwmint --passphrase --words 6
```

or:

```bash
pwmint -p -w 6
```

---

```text
--separator
-s
```

Set the separator between passphrase words.

Example:

```bash
pwmint --passphrase --separator "_"
```

The default separator is:

```text
-
```

---

## Character Set Options – V2

The first version uses all four password character sets by default.

A later version should allow individual character sets to be disabled.

The planned options are:

```text
--no-lowercase
--no-uppercase
--no-digits
--no-special
```

Examples:

```bash
pwmint --no-special
```

```bash
pwmint --no-digits --no-special
```

No short options such as:

```text
-nl
-nu
-nd
-ns
```

should be introduced.

The reason is readability and consistency with normal command-line
option conventions.

At least one character set must always remain enabled.

If all character sets are disabled, the command must return a clear
validation error.

The character-set exclusion functionality is not required for the
first password prototype.

---

# Implementation Steps

## Step 1 – Minimal Project Foundation

Establish the minimal Python project foundation.

Tasks:

- Verify the existing project structure.
- Add only files that are required for the Python package to work.
- Add the Python package marker if required.
- Add minimal project metadata only if required.
- Add `.gitignore` if it does not already exist.
- Ensure `.venv/` is ignored.
- Keep runtime dependencies at zero.
- Do not implement application functionality yet.

Do not implement:

- password generation
- passphrase generation
- CLI
- GUI
- unit tests
- PyInstaller builds
- security review

After completing this step:

1. List all created or modified files.
2. Explain briefly why each file was created or modified.
3. Verify that the Python package can be imported.
4. Do not continue with Step 2.

---

## Step 2 – Password Generator Prototype

Implement the first Password Generator prototype in:

```text
src/pwmint/password.py
```

The implementation must be simple and beginner-friendly.

### Password Length

Use:

```text
default: 18
minimum: 15
maximum: 64
```

The user must be able to select a length between 18 and 24 characters.

Values outside this range must be rejected.

### Character Sets

The first prototype must support:

- lowercase letters
- uppercase letters
- digits
- special characters

All four character sets are enabled by default.

At least one character set must be available for generation.

The V2 `--no-*` options are not required in this step.

### Secure Randomness

Use Python's:

```python
secrets.choice()
```

for password generation.

Do not use:

```python
random
```

for password generation.

Do not implement custom cryptography.

### Function Design

Create a clear function for generating one password.

The function should:

```text
Input
    ↓
Validate input
    ↓
Build character set
    ↓
Generate password
    ↓
Return password
```

The generation logic must remain independent from CLI handling.

### Code Style

Use:

- simple functions
- simple control flow
- readable variable names
- simple type hints
- useful docstrings
- useful comments

Prefer readable loops over unnecessarily compact Python constructs.

For example, this style is explicitly acceptable:

```python
password = ""

for _ in range(length):
    password += secrets.choice(characters)
```

Do not optimize this into a more complex implementation merely to
reduce the number of lines.

---

## Step 3 – Direct CLI Test Interface

Before implementing the final CLI in `cli/`, make the Password
Generator directly executable for development and testing.

The prototype should support:

```bash
python src/pwmint/password.py
```

which generates one default password.

It should also support:

```bash
python src/pwmint/password.py --length 24
```

and:

```bash
python src/pwmint/password.py -l 24
```

The temporary CLI interface should use the Python standard library.

The direct interface should:

1. Read the requested input.
2. Call the password generation function.
3. Print the generated password.
4. Report invalid input clearly.

The password generation logic must remain in a separate function.

Do not implement the complete `cli/` application yet.

The direct CLI interface exists only to make the first prototype easy
to test.

---

## Step 4 – Password Unit Tests

Implement unit tests in:

```text
tests/test_password.py
```

Tests should verify:

- default password length
- valid lengths from 15 to 64
- invalid lengths below 15
- invalid lengths above 65
- character-set selection
- at least one character set
- invalid input
- generated password properties
- basic edge cases

Tests should verify properties rather than fixed random results.

Do not test against a specific generated password.

Do not print or persist generated passwords.

---

## Step 5 – Passphrase Generator Core

Implement the passphrase generator in:

```text
src/pwmint/passphrase.py
```

Use a local word list.

The word list must:

- be stored locally
- require no network connection
- use a simple format
- contain one word per line
- be packageable with the application

### Defaults

Use:

```text
words:     4
separator: -
count:     1
```

Use:

```python
secrets.choice()
```

for word selection.

Do not use `random`.

---

## Step 6 – Passphrase Unit Tests

Implement tests in:

```text
tests/test_passphrase.py
```

Test:

- default word count
- requested word count
- separator
- local word-list membership
- invalid word counts
- invalid separators
- multiple passphrase generation
- basic edge cases

Tests must remain simple and readable.

---

## Step 7 – Final CLI

Implement the final CLI in:

```text
cli/
```

Use:

```python
argparse
```

The final CLI must support the default command:

```bash
pwmint
```

and the planned options:

```text
--length       -l
--count        -c
--passphrase   -p
--words        -w
--separator    -s
```

The CLI must call the existing core functions.

The CLI must not contain password or passphrase generation logic.

Do not duplicate validation or generation logic unnecessarily.

### V2 Character Set Options

Add:

```text
--no-lowercase
--no-uppercase
--no-digits
--no-special
```

only after the corresponding core functionality has been implemented
and tested.

---

## Step 8 – GUI

Implement the GUI in:

```text
gui/
```

Use Python's standard library:

```python
tkinter
```

The GUI should remain simple.

It should provide:

- password/passphrase selection
- relevant options
- generate action
- result display
- understandable validation errors

The GUI must use the same core functions as the CLI.

Do not duplicate generation logic.

---

## Step 9 – PyInstaller

Create separate PyInstaller build definitions for:

```text
CLI
GUI
```

Store build-related configuration in:

```text
build/
```

The local passphrase word list must be included in the packaged
application.

Do not commit generated binaries.

Do not commit temporary PyInstaller build artifacts.

---

## Step 10 – Security Review

Create the security review documentation in:

```text
security-review/
```

Review:

- use of `secrets`
- absence of `random`
- absence of custom cryptography
- input validation
- secret handling
- logging
- persistent storage
- network access
- dependencies
- local word list
- CLI behavior
- GUI behavior
- PyInstaller packaging

Document identified issues and their resolution.

---

## Step 11 – README

Complete:

```text
README.md
```

Document:

- project purpose
- password generation
- passphrase generation
- defaults
- CLI usage
- GUI usage
- development setup
- testing
- PyInstaller builds
- security considerations
- project structure

Examples must never contain real credentials.

---

## Step 12 – Final Verification

Perform a complete project verification.

Verify:

- unit tests
- default CLI execution
- password length options
- count option
- passphrase option
- passphrase word count
- separator
- invalid input
- character-set exclusion options
- GUI startup
- GUI generation
- PyInstaller CLI build
- PyInstaller GUI build
- packaged local word list
- `.gitignore`
- absence of generated secrets
- absence of credentials
- absence of unnecessary build artifacts

Compare the final implementation against:

```text
requirements.md
project-structure.md
copilot-instructions.md
```

All requirements should be fulfilled before the project is considered
complete.

---

# Implementation Rules

The following rules apply to every implementation step.

## Keep the Code Simple

Prefer:

```text
simple
readable
secure
understandable
```

over:

```text
clever
short
abstract
over-engineered
```

The project is a Python learning project.

The code should be understandable by a Python beginner.

---

## Input → Processing → Output

Use the following principle wherever possible:

```text
Input
  ↓
Processing
  ↓
Output
```

Functions should have a clear responsibility.

Avoid unnecessary global state.

---

## Comments and Documentation

Functions should contain useful docstrings.

Important or non-obvious logic should contain concise comments.

Security-related decisions should be explained with comments.

Comments should explain why something is done when the reason is not
obvious.

Do not add comments that simply repeat the code.

---

## Security

Use:

```python
secrets
```

for password and passphrase generation.

Never use:

```python
random
```

for secrets.

Do not implement custom cryptography.

Do not store generated credentials.

Do not log generated credentials.

Do not introduce network dependencies.

---

## Dependencies

Prefer the Python standard library.

The following standard-library components are preferred where
appropriate:

```text
secrets
argparse
tkinter
unittest
```

Additional dependencies require a clear justification.

---

## Incremental Development

Implement only the requested step.

Do not automatically continue with later steps.

After completing a step:

1. Report the changes.
2. Explain important decisions.
3. Run the relevant verification.
4. Wait for approval before continuing.

The project owner should be able to review each development step before
the next step begins.
