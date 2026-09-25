# pwmint – Requirements

## 1. Project Goal

`pwmint` is a small Python project for generating secure passwords and
passphrases.

The project is primarily a **Python learning project** and is used to
practice development with GitHub Copilot.

The application should provide:

- a Password Generator
- a Passphrase Generator
- a CLI
- a simple GUI
- unit tests
- a standalone build using PyInstaller

The application is intended primarily for personal use.

The project should remain small, understandable and easy to maintain.

---

## 2. General Requirements

The following principles apply to the complete project:

- Keep the application simple.
- Prefer readable code over clever code.
- Prefer simple solutions over complex abstractions.
- Avoid unnecessary design patterns.
- Avoid unnecessary dependencies.
- Do not introduce frameworks unless they provide a clear benefit.
- Use standard Python functionality whenever possible.
- Code should be understandable for Python beginners.
- Functions should have a clear and limited responsibility.
- Prefer simple `Input -> Processing -> Output` logic.
- Avoid overly complex one-liners.
- Avoid "fancy" Python code when a simple solution is available.
- Code should be easy to read, debug and modify.
- Security must not be sacrificed for simplicity.
- The project should not be over-engineered.

---

## 3. Password Generator

The Password Generator must be able to generate random passwords.

### 3.1 Password Length

The user must be able to specify the password length.

A reasonable default password length should be provided.

The application must validate the requested length.

Invalid values must result in a clear and understandable error message.

### 3.2 Character Sets

The Password Generator should support the following character sets:

- lowercase letters
- uppercase letters
- digits
- special characters

The user should be able to select which character sets are used.

At least one character set must be selected.

### 3.3 Password Generation

Passwords must be generated using a cryptographically secure random
number generator.

Python's `secrets` module must be used.

The standard `random` module must not be used for password generation.

The generated password must be returned to the caller.

The generator must not store generated passwords.

### 3.4 Multiple Passwords

The application should support generating more than one password in a
single operation.

This feature should remain simple and should not introduce unnecessary
complexity.

---

## 4. Passphrase Generator

The Passphrase Generator must generate random passphrases consisting
of multiple words.

Example:

    correct-horse-battery-staple

Another example:

    correct-horse-battery-staple-forest

### 4.1 Number of Words

The user must be able to specify the number of words.

A reasonable default should be provided.

The requested number of words must be validated.

### 4.2 Word List

The application should use a local word list.

The word list must not require a network connection.

The format and location of the local word list will be defined during implementation.

The source and format of the word list should be simple and easy to
understand.

### 4.3 Separator

The passphrase should use a configurable separator.

The default separator should be:

    -

### 4.4 Random Selection

Words must be selected using a cryptographically secure random
number generator.

Python's `secrets` module must be used.

The standard `random` module must not be used for passphrase generation.

---

## 5. CLI

The application must provide a simple command-line interface.

The CLI should provide commands for:

- generating passwords
- generating passphrases

Example:

    pwmint password

    pwmint password --length 20

    pwmint passphrase

    pwmint passphrase --words 5

The CLI should provide understandable help output.

Invalid arguments must result in a clear error message.

The CLI should not expose generated passwords through logging or
debug output.

---

## 6. GUI

The application should provide a simple graphical user interface.

The GUI should provide access to the same password and passphrase
generation functionality as the CLI.

The GUI should remain intentionally simple.

The GUI should not contain unnecessary features.

The GUI should:

- allow the user to select password or passphrase generation
- allow the relevant options to be configured
- display the generated result
- provide a simple way to generate a new result

The GUI should use the existing Python core functionality.

Password and passphrase generation logic must not be duplicated in
the GUI.

---

## 7. Security Requirements

Security is an important requirement of `pwmint`.

### 7.1 Secure Randomness

All password and passphrase generation must use Python's `secrets`
module.

The `random` module must not be used for generating secrets.

### 7.2 No Persistent Storage

Generated passwords and passphrases must not be stored permanently.

The application must not write generated credentials to files,
databases or configuration files.

### 7.3 No Logging of Secrets

Generated passwords and passphrases must never be written to:

- log files
- debug output
- error messages
- test output unless explicitly required for a test

### 7.4 No Network Dependency

The core password and passphrase generation functionality must work
without an Internet connection.

`pwmint` must not send generated passwords or passphrases to external
services.

### 7.5 No Custom Cryptography

The project must not implement its own cryptographic algorithms.

Python's standard security functionality should be used whenever
possible.

### 7.6 Input Validation

User input must be validated before it is used.

Invalid values must be rejected with understandable error messages.

### 7.7 Secrets in Memory

The application should avoid unnecessary copies of generated
passwords and passphrases.

No custom secure-memory implementation is required.

Python's normal string handling is acceptable for this learning
project.

### 7.8 Clipboard

Clipboard integration is not required for the first version.

If clipboard functionality is added later, it must be reviewed
separately from a security perspective.

---

## 8. Code Quality Requirements

The code should be written for readability and learning.

### 8.1 Beginner-Friendly Python

The implementation should use simple Python constructs.

Prefer:

- simple functions
- clear variable names
- straightforward control flow
- small modules
- standard library functionality

Avoid unnecessary use of:

- decorators
- metaclasses
- advanced generators
- complex comprehensions
- overly abstract class hierarchies
- unnecessary design patterns
- clever one-liners

A simple implementation is preferred over a shorter but harder to
understand implementation.

### 8.2 Functions

Functions should have one clear responsibility.

The preferred structure is:

    Input
      ↓
    Processing
      ↓
    Output

Functions should return their result instead of relying on global
state.

Where useful, functions should contain a short comment or docstring
describing:

- what the function does
- the expected input
- the returned output

Comments should explain **why** something is done when the reason is
not obvious from the code.

Comments should not simply repeat every line of code.

### 8.3 Type Hints

Type hints should be used where they improve readability.

Type hints should remain simple and understandable.

Do not introduce complex typing constructs without a clear reason.

---

## 9. Testing Requirements

The project must contain unit tests for the core functionality.

Tests should cover at least:

- password generation
- passphrase generation
- password length validation
- passphrase word count validation
- character set selection
- invalid input
- empty character sets
- basic edge cases

Tests should verify properties of generated values rather than relying
on specific random results.

Tests must not depend on real passwords or fixed random output.

The tests should be deterministic where possible.

The core generation logic should be testable without starting the CLI
or GUI.

---

## 10. Build Requirements

The application should be buildable as a standalone application
using PyInstaller.

The project should provide separate builds for:

- CLI
- GUI

Build artifacts should not be treated as source code.

Temporary build files and generated binaries should not be committed
to the source repository unless explicitly required.

---

## 11. Out of Scope

The following functionality is explicitly outside the scope of the
first version:

- password manager functionality
- password storage
- database
- cloud integration
- network API
- user accounts
- authentication
- password synchronization
- password breach checking
- online word lists
- browser integration
- complex configuration management
- enterprise functionality
- multi-user functionality
- custom cryptographic algorithms
- complex secure-memory management
- unnecessary external dependencies

Additional functionality can be considered later if it provides a
clear learning benefit.

---

## 12. Project Philosophy

`pwmint` is a learning project.

The primary goals are:

1. Learn and practice Python.
2. Learn how to use GitHub Copilot effectively.
3. Practice writing requirements before implementation.
4. Practice unit testing.
5. Practice CLI and GUI development.
6. Practice basic security-aware development.
7. Practice code review with AI assistance.
8. Build a small application that is actually usable.

The project should remain small enough to understand in its entirety.

**Simple, readable and secure code is preferred over clever or
over-engineered code.**
