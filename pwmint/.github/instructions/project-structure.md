# pwmint – Project Structure

## 1. Overview

The `pwmint` project uses a simple and clearly separated directory
structure.

The project is intentionally kept small.

The structure separates:

- project documentation
- Python core functionality
- unit tests
- CLI
- GUI
- security review
- build files

The goal is to keep the project easy to understand and maintain.

---

## 2. Directory Structure

The current project structure is:

```text
pwmint/
│
├── .github/
│   └── instructions/
│       ├── requirements.md
│       ├── project-structure.md
│       └── copilot-instructions.md
│
├── src/
│   └── pwmint/
│       ├── password.py
│       └── passphrase.py
│
├── tests/
│   ├── test_password.py
│   └── test_passphrase.py
│
├── cli/
│
├── gui/
│
├── security-review/
│
├── build/
│
└── README.md
```

---

## 3. `.github/instructions/`

This directory contains project instructions and documentation used
during development.

### Files

#### `requirements.md`

Defines what `pwmint` should do.

It contains:

- functional requirements
- security requirements
- CLI requirements
- GUI requirements
- testing requirements
- build requirements
- out-of-scope functionality

This file defines the functional scope of the project.

---

#### `project-structure.md`

Describes the project structure and defines where different types of
files belong.

This file should be updated if the project structure changes.

---

#### `copilot-instructions.md`

Contains the development instructions for GitHub Copilot.

It defines how Copilot should generate and modify code.

Examples include:

- coding style
- simplicity
- readability
- security requirements
- testing expectations
- project structure
- dependency usage

---

## 4. `src/pwmint/`

This directory contains the Python core of the application.

`pwmint` is the Python package containing the actual password and
passphrase generation logic.

The core must not depend on the CLI or GUI.

### `password.py`

Contains the password generation functionality.

Responsibilities include:

- password generation
- character set handling
- password length handling
- input validation related to password generation

The module must not contain CLI- or GUI-specific code.

---

### `passphrase.py`

Contains the passphrase generation functionality.

Responsibilities include:

- passphrase generation
- word selection
- word count handling
- separator handling
- input validation related to passphrase generation

The module must not contain CLI- or GUI-specific code.

---

## 5. `tests/`

This directory contains unit tests for the Python core.

Tests should test the functionality in:

```text
src/pwmint/
```

The tests should not require the CLI or GUI to be started.

### `test_password.py`

Contains tests for:

```text
src/pwmint/password.py
```

Examples:

- password length
- character sets
- invalid input
- edge cases
- generated password properties

---

### `test_passphrase.py`

Contains tests for:

```text
src/pwmint/passphrase.py
```

Examples:

- word count
- separator
- invalid input
- edge cases
- generated passphrase properties

---

## 6. `cli/`

This directory contains the command-line interface for `pwmint`.

The CLI is responsible for:

- reading command-line arguments
- validating CLI-specific input
- calling the Python core
- displaying results
- displaying help and error messages

The CLI must not implement its own password or passphrase generation
logic.

Instead, it must use the functionality provided by:

```text
src/pwmint/
```

The CLI is an interface to the core functionality.

---

## 7. `gui/`

This directory contains the graphical user interface for `pwmint`.

The GUI is responsible for:

- displaying the user interface
- reading user input
- displaying generated results
- handling GUI-specific errors

The GUI must not implement its own password or passphrase generation
logic.

Instead, it must use the functionality provided by:

```text
src/pwmint/
```

The GUI is an interface to the core functionality.

The GUI should remain simple and easy to understand.

---

## 8. `security-review/`

This directory contains documentation related to the security review
of the project.

The security review should examine topics such as:

- secure random number generation
- input validation
- handling of generated secrets
- logging
- dependencies
- accidental persistence
- CLI security
- GUI security

The security review is part of the learning process.

It should not introduce a complex security framework into the
application itself.

---

## 9. `build/`

This directory is used for build-related files and artifacts.

PyInstaller can be used to create standalone applications.

The build process should create separate applications for:

- CLI
- GUI

Temporary build files and generated binaries should not be treated as
source code.

Generated build artifacts should normally not be committed to Git.

---

## 10. `README.md`

The root `README.md` contains the user-facing project documentation.

It should explain:

- what `pwmint` is
- what it can do
- how to install or build it
- how to use the CLI
- how to use the GUI
- basic security information
- development and testing
- project structure

The README should be understandable without reading the source code.

---

## 11. Separation of Responsibilities

The project follows a simple separation of responsibilities.

```text
                 ┌─────────────┐
                 │     CLI     │
                 └──────┬──────┘
                        │
                        ▼
                ┌───────────────┐
                │  pwmint Core  │
                │               │
                │   password    │
                │   passphrase  │
                └───────────────┘
                        ▲
                        │
                 ┌──────┴──────┐
                 │     GUI     │
                 └─────────────┘
```

The core contains the actual application logic.

The CLI and GUI provide different ways to interact with the core.

The password and passphrase generation logic must exist only once.

---

## 12. Core Design Principle

The core functionality should follow a simple:

```text
Input
  ↓
Processing
  ↓
Output
```

model.

Functions should receive clearly defined input values and return
clearly defined results.

Global state should be avoided.

The CLI and GUI should consume the results returned by the core.

---

## 13. Adding New Files

New files should be placed in the directory that matches their
responsibility.

Examples:

```text
Password generation logic
    → src/pwmint/

Unit tests
    → tests/

CLI functionality
    → cli/

GUI functionality
    → gui/

Security review documentation
    → security-review/

Build-related files
    → build/
```

Files should not be placed in the root directory unless there is a
clear reason.

---

## 14. Keeping the Project Simple

The directory structure should not be expanded without a clear need.

Do not create additional directories simply to follow a particular
software architecture pattern.

The project should remain small enough that the complete structure can
be understood at a glance.

**Simple structure and clear responsibilities are preferred over
complex architecture.**
