"""Generate secure passphrases from a small local word list."""

from pathlib import Path
import secrets

DEFAULT_WORD_COUNT = 4
DEFAULT_SEPARATOR = "-"
MIN_WORD_COUNT = 4
MAX_WORD_COUNT = 10
MAX_PASSPHRASE_LENGTH = 128
WORD_LIST_FILE = Path(__file__).with_name("wordlist.txt")


def _load_word_list() -> list[str]:
	"""Load the local word list and return one word for each list item."""
	with WORD_LIST_FILE.open(encoding="utf-8") as word_list_file:
		words = []

		for line in word_list_file:
			word = line.strip()
			if word:
				words.append(word)

	return words


def generate_passphrase(
	word_count: int = DEFAULT_WORD_COUNT,
	separator: str = DEFAULT_SEPARATOR,
) -> str:
	"""Generate a secure passphrase with unique, randomly chosen words."""
	if not isinstance(word_count, int) or isinstance(word_count, bool):
		raise ValueError("Word count must be a positive integer.")

	if word_count < MIN_WORD_COUNT or word_count > MAX_WORD_COUNT:
		raise ValueError(
			f"Word count must be between {MIN_WORD_COUNT} and {MAX_WORD_COUNT}."
		)

	if not isinstance(separator, str):
		raise ValueError("Separator must be a string.")

	words = _load_word_list()
	if not words:
		raise ValueError("The local word list must contain at least one word.")

	if word_count > len(words):
		raise ValueError(
			f"Requested {word_count} words, but the local word list contains only {len(words)} unique words."
		)

	selected_words = secrets.SystemRandom().sample(words, k=word_count)
	passphrase = separator.join(selected_words)
	if not passphrase:
		raise ValueError("The generated passphrase must not be empty.")

	if len(passphrase) > MAX_PASSPHRASE_LENGTH:
		raise ValueError(
			f"The generated passphrase must not exceed {MAX_PASSPHRASE_LENGTH} characters."
		)

	return passphrase
