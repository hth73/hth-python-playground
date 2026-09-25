# pwmint – GitHub Copilot Instructions

## 1. Purpose

`pwmint` is a small Python learning project for generating secure
passwords and passphrases.

The project is primarily used to:

- learn and practice Python
- learn how to use GitHub Copilot effectively
- practice writing secure Python code
- practice unit testing
- practice CLI and GUI development
- practice code review with AI assistance

The project is intentionally small.

GitHub Copilot should help develop the project while keeping the code
simple, secure, readable and understandable.

The primary goal is not to create the shortest or most advanced Python
code.

The primary goal is to create code that a Python beginner can
understand, explain and maintain.

---

## 2. General Development Rules

Follow these general principles:

- Keep the implementation simple.
- Prefer readable code over short code.
- Prefer explicit code over clever code.
- Prefer simple solutions over complex abstractions.
- Avoid unnecessary design patterns.
- Avoid unnecessary classes.
- Avoid unnecessary dependencies.
- Use the Python standard library whenever possible.
- Do not introduce frameworks without a clear requirement.
- Do not over-engineer the application.
- Do not add functionality that is not required.
- Do not change the project architecture without a clear reason.
- Keep functions small and focused.
- Keep the code easy to debug and modify.

When multiple solutions are possible, prefer the simplest solution that
is secure and easy to understand.

---

## 3. Beginner-Friendly Python

The code must be understandable for Python beginners.

Prefer simple Python constructs such as:

- variables
- functions
- `if` statements
- `for` loops
- simple lists
- simple strings
- simple dictionaries where appropriate
- straightforward exception handling

Avoid unnecessary use of advanced Python features.

Avoid or minimize:

- complex list comprehensions
- complex generator expressions
- decorators
- metaclasses
- advanced inheritance
- complex lambda expressions
- advanced typing constructs
- overly abstract class hierarchies
- clever one-liners
- unnecessary functional programming techniques

For example, prefer a readable loop:

```python
password = ""

for _ in range(length):
    password += secrets.choice(characters)
```

over a more compact implementation when the compact version makes the
code harder for a beginner to understand.

Shorter code is not automatically better code.

---

## 4. Code Comments and Documentation

Code should contain useful comments and documentation.

Comments are important because `pwmint` is a learning project.

The code should allow a beginner to understand not only **what** the
code does, but also **why** important decisions were made.

### 4.1 Functions

Functions should normally contain a short docstring describing:

- what the function does
- the expected input
- the returned output

Example:

```python
def generate_password(length):
    """Generate a secure random password with the requested length."""
```

### 4.2 Useful Comments

Comments should explain important logic or security decisions.

Example:

```python
# secrets.choice() is used because passwords require
# cryptographically secure random values.
password += secrets.choice(characters)
```

Comments should explain **why** something is done when the reason is
not obvious.

### 4.3 Avoid Unnecessary Comments

Do not add comments that simply repeat the code.

Avoid:

```python
# Set length to 20
length = 20
```

Prefer comments that explain intent or reasoning:

```python
# Use a reasonable default length for generated passwords.
length = 20
```

### 4.4 Learning-Oriented Code

When code contains a security-sensitive or otherwise important
implementation detail, prefer a short explanatory comment.

The comments should remain concise and useful.

---

## 5. Input → Processing → Output

The preferred design principle for `pwmint` is:

```text
Input
  ↓
Processing
  ↓
Output
```

Functions should receive clearly defined input values and return
clearly defined results.

Example:

```text
Input:
    password length
    selected character sets

Processing:
    validate input
    generate password

Output:
    generated password
```

Avoid unnecessary global state.

Prefer returning values from functions instead of modifying global
variables.

The CLI and GUI should use the same core functionality.

The password and passphrase generation logic must not be duplicated in
the CLI or GUI.

---

## 6. Security

Security is a core requirement of `pwmint`.

### 6.1 Secure Randomness

Use Python's `secrets` module for password and passphrase generation.

Do not use the `random` module for generating passwords,
passphrases or other secrets.

Example:

```python
import secrets

character = secrets.choice(characters)
```

### 6.2 No Custom Cryptography

Do not implement custom cryptographic algorithms.

Use well-established Python standard library functionality where
possible.

Do not attempt to create a custom random number generator.

### 6.3 No Persistent Secrets

Generated passwords and passphrases must not be stored permanently.

Do not write generated secrets to:

- files
- databases
- configuration files
- logs

### 6.4 No Secret Logging

Never log generated passwords or passphrases.

Do not include secrets in debug messages or exception messages.

### 6.5 No Network Dependency

The password and passphrase generation functionality must work without
an Internet connection.

Do not send generated secrets to external services.

### 6.6 Input Validation

Validate user input before processing it.

Invalid input should result in a clear and understandable error
message.

### 6.7 Security Versus Simplicity

Security is important, but do not introduce unnecessary complexity.

Use simple and well-understood security mechanisms.

Do not create custom security frameworks or abstractions.

---

## 7. Project Structure

Follow the project structure defined in:

```text
.github/instructions/project-structure.md
```

The main Python core is located in:

```text
src/pwmint/
```

The core contains the actual password and passphrase generation logic.

The CLI is located in:

```text
cli/
```

The GUI is located in:

```text
gui/
```

Unit tests are located in:

```text
tests/
```

Security review documentation is located in:

```text
security-review/
```

Build-related files are located in:

```text
build/
```

Do not move files between these directories without a clear reason.

Do not create additional directories unless they are required.

---

## 8. Functions and Type Hints

Functions should have one clear responsibility.

Prefer small functions that perform one logical task.

Example:

```python
def validate_password_length(length):
    """Validate the requested password length."""
```

Functions should avoid hidden side effects.

Prefer:

```text
Input → Function → Return Value
```

over modifying global state.

### Type Hints

Use simple type hints where they improve readability.

Example:

```python
def generate_password(length: int) -> str:
    """Generate a secure random password."""
```

Do not introduce complex typing constructs unless they provide a
clear benefit.

Type hints must not make beginner-level code unnecessarily difficult
to understand.

---

## 9. Error Handling

User input must be validated.

Errors should be handled explicitly and clearly.

Error messages should be understandable to the user.

Avoid catching all exceptions without a reason.

Avoid:

```python
try:
    ...
except Exception:
    pass
```

Do not silently ignore errors.

Do not expose sensitive information in error messages.

Errors should provide enough information for the user to understand
what went wrong and, where appropriate, how to correct the input.

---

## 10. Dependencies

Prefer the Python standard library.

Before introducing an external dependency, determine whether the same
functionality can be implemented clearly using the standard library.

Do not add dependencies only because they provide a shorter
implementation.

Every additional dependency should have a clear and documented reason.

Keep the dependency count as small as practical.

---

## 11. Testing

Unit tests are an important part of the project.

Tests should primarily cover the core functionality.

Tests should verify behavior and properties rather than relying on
specific random results.

For example, a password test should verify:

- the requested length is returned
- the requested character sets are respected
- invalid input is rejected

It should not expect one specific randomly generated password.

Tests should include:

- normal cases
- invalid input
- boundary conditions
- edge cases

Tests should be simple and readable.

Test code should follow the same beginner-friendly coding principles
as production code.

The core functionality should be testable without starting the CLI or
GUI.

---

## 12. CLI and GUI

The CLI and GUI are interfaces to the core functionality.

They must not contain duplicate password or passphrase generation
logic.

Use:

```text
CLI ──┐
      ├──> pwmint Core
GUI ──┘
```

The core should perform the actual generation.

The CLI and GUI should:

- collect input
- pass input to the core
- display the result
- display understandable errors

Keep both interfaces simple.

Do not add unnecessary user-interface features.

---

## 13. Git / Changes

Changes should be small and focused.

Do not modify unrelated files when implementing a feature.

Do not rewrite working code without a clear reason.

When modifying existing code:

1. Understand the existing implementation.
2. Make the smallest reasonable change.
3. Keep the existing coding style.
4. Update tests when necessary.
5. Verify that existing functionality still works.

Do not create generated build artifacts as source files.

Do not commit secrets, generated passwords or other sensitive data.

Do not commit unnecessary temporary files.

---

## 14. Copilot Behaviour

GitHub Copilot should act as a development assistant.

Copilot should follow the requirements and project structure defined
by this project.

### 14.1 Follow Existing Requirements

Before implementing functionality, consider:

```text
requirements.md
project-structure.md
copilot-instructions.md
```

Existing project requirements take precedence over assumptions made by
Copilot.

### 14.2 Do Not Over-Engineer

Do not introduce additional architecture simply because it is possible.

Do not create abstractions for functionality that is only used once
unless there is a clear reason.

Do not create classes when a simple function is sufficient.

Do not introduce design patterns without a concrete requirement.

### 14.3 Prefer Readability

When multiple implementations are possible:

1. Choose the secure solution.
2. Prefer the simplest implementation.
3. Prefer the most readable implementation.
4. Prefer the implementation that is easiest for a beginner to
   understand.

Code length is not the primary optimization goal.

### 14.4 Explain Complex Decisions

When an implementation requires a security-sensitive or non-obvious
decision, include a short code comment explaining the reason.

For example:

```python
# Use secrets.choice() instead of random.choice()
# because this value is used to generate a password.
character = secrets.choice(characters)
```

### 14.5 Preserve the Architecture

Do not move functionality between:

```text
src/pwmint/
cli/
gui/
tests/
```

without a clear reason.

Do not duplicate functionality simply because it is easier for the
current task.

### 14.6 Ask Before Large Changes

If a requested change would require:

- a major architecture change
- a new framework
- several new dependencies
- a significant restructuring
- functionality outside the requirements

the change should be discussed before implementation.

Do not silently expand the scope of the project.

### 14.7 Keep the Learning Goal in Mind

The generated code should be understandable by the project owner.

Prefer code that can be read and explained step by step.

Do not optimize for demonstrating advanced Python knowledge.

The goal is to learn Python and effective AI-assisted development.

---

## Final Principle

For `pwmint`, follow this priority:

```text
Security
   ↓
Correctness
   ↓
Readability
   ↓
Maintainability
   ↓
Simplicity
   ↓
Performance
```

When choosing between a clever implementation and a simple,
understandable implementation, prefer the simple implementation unless
the clever implementation provides a necessary security or correctness
benefit.

**Write code that a Python beginner can understand, a developer can
maintain, and a security-conscious user can trust.**
