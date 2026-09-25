"""Generate a single secure pseudoword for passphrase creation."""

import secrets

MIN_WORD_LENGTH = 6
MAX_WORD_LENGTH = 12
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def generate_pseudoword() -> str:
    """Generate a random lowercase pseudoword using secrets."""
    length = secrets.randbelow(MAX_WORD_LENGTH - MIN_WORD_LENGTH + 1) + MIN_WORD_LENGTH
    start_with_vowel = secrets.choice((True, False))

    word = []

    for index in range(length):
        is_vowel_position = (index % 2 == 0) == start_with_vowel

        if is_vowel_position:
            word.append(secrets.choice(VOWELS))
        else:
            word.append(secrets.choice(CONSONANTS))

    return "".join(word)
