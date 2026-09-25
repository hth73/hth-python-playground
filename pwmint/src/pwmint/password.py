"""Generate secure passwords for the first pwmint prototype."""

import argparse
import secrets
import string

DEFAULT_PASSWORD_LENGTH = 18
MIN_PASSWORD_LENGTH = 15
MAX_PASSWORD_LENGTH = 64

def generate_password(
	length: int = DEFAULT_PASSWORD_LENGTH,
	use_lowercase: bool = True,
	use_uppercase: bool = True,
	use_digits: bool = True,
	use_special: bool = True,
) -> str:
	"""Generate a secure password with the requested length and character sets."""
	if not isinstance(length, int) or isinstance(length, bool):
		raise ValueError("Password length must be an integer.")

	if length < MIN_PASSWORD_LENGTH or length > MAX_PASSWORD_LENGTH:
		raise ValueError(
			f"Password length must be between {MIN_PASSWORD_LENGTH} "
			f"and {MAX_PASSWORD_LENGTH} characters."
		)

	characters = ""

	if use_lowercase:
		characters += string.ascii_lowercase
	if use_uppercase:
		characters += string.ascii_uppercase
	if use_digits:
		characters += string.digits
	if use_special:
		characters += string.punctuation

	if not characters:
		raise ValueError("At least one character set must be enabled.")

	password = ""

	for _ in range(length):
		# secrets.choice() provides cryptographically secure random selection.
		password += secrets.choice(characters)

	return password


def main() -> None:
	"""Read the prototype command-line input and print one password."""
	parser = argparse.ArgumentParser(description="Generate a secure password.")
	parser.add_argument(
		"-l",
		"--length",
		type=int,
		default=DEFAULT_PASSWORD_LENGTH,
		help=(
			"Password length, from "
			f"{MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH} characters."
		),
	)
	arguments = parser.parse_args()

	try:
		password = generate_password(arguments.length)
	except ValueError as error:
		parser.error(str(error))

	print(password)


if __name__ == "__main__":
	main()
