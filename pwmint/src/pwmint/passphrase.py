"""Generate secure passphrases from dynamically generated pseudowords."""

from src.pwmint.pseudoword import generate_pseudoword

DEFAULT_WORD_COUNT = 4
DEFAULT_SEPARATOR = "-"
MIN_WORD_COUNT = 4
MAX_WORD_COUNT = 10
MAX_PASSPHRASE_LENGTH = 128


def generate_passphrase(
	word_count: int = DEFAULT_WORD_COUNT,
	separator: str = DEFAULT_SEPARATOR,
) -> str:
	"""Generate a secure passphrase with unique pseudowords."""
	if not isinstance(word_count, int) or isinstance(word_count, bool):
		raise ValueError("Word count must be a positive integer.")

	if word_count < MIN_WORD_COUNT or word_count > MAX_WORD_COUNT:
		raise ValueError(
			f"Word count must be between {MIN_WORD_COUNT} and {MAX_WORD_COUNT}."
		)

	if not isinstance(separator, str):
		raise ValueError("Separator must be a string.")

	words = []

	while len(words) < word_count:
		candidate = generate_pseudoword()
		if candidate not in words:
			words.append(candidate)

	passphrase = separator.join(words)
	if not passphrase:
		raise ValueError("The generated passphrase must not be empty.")

	if len(passphrase) > MAX_PASSPHRASE_LENGTH:
		raise ValueError(
			f"The generated passphrase must not exceed {MAX_PASSPHRASE_LENGTH} characters."
		)

	return passphrase
