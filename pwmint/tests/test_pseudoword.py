import re
import pytest

from src.pwmint.pseudoword import (
    MAX_WORD_LENGTH,
    MIN_WORD_LENGTH,
    generate_pseudoword,
)


VOWEL_PATTERN = re.compile(r"[aeiou]")
CONSONANT_PATTERN = re.compile(r"[bcdfghjklmnpqrstvwxyz]")


def test_generated_word_has_valid_length():
    word = generate_pseudoword()

    assert MIN_WORD_LENGTH <= len(word) <= MAX_WORD_LENGTH


def test_generated_word_uses_lowercase_letters_only():
    word = generate_pseudoword()

    assert bool(word)
    assert word.islower()
    assert word.isalpha()
    assert set(word) <= set("abcdefghijklmnopqrstuvwxyz")


def test_generated_word_contains_a_vowel_and_a_consonant():
    word = generate_pseudoword()

    assert VOWEL_PATTERN.search(word)
    assert CONSONANT_PATTERN.search(word)


def test_generated_words_follow_cv_pattern():
    words = [generate_pseudoword() for _ in range(50)]

    for word in words:
        if len(word) == 1:
            continue

        pattern = []
        for character in word:
            if character in "aeiou":
                pattern.append("V")
            else:
                pattern.append("C")

        assert len(pattern) == len(word)
        assert all(
            pattern[index] != pattern[index - 1]
            for index in range(1, len(pattern))
        )


def test_generated_words_can_start_with_consonant_or_vowel():
    starts = {"consonant": 0, "vowel": 0}

    for _ in range(200):
        word = generate_pseudoword()
        if word[0] in "aeiou":
            starts["vowel"] += 1
        else:
            starts["consonant"] += 1

    assert starts["consonant"] > 0
    assert starts["vowel"] > 0


def test_multiple_generated_words_are_valid():
    words = [generate_pseudoword() for _ in range(20)]

    for word in words:
        assert MIN_WORD_LENGTH <= len(word) <= MAX_WORD_LENGTH
        assert word.islower()
        assert VOWEL_PATTERN.search(word)
        assert CONSONANT_PATTERN.search(word)


def test_word_lengths_vary_across_multiple_generations():
    lengths = {len(generate_pseudoword()) for _ in range(100)}

    assert lengths.issubset(set(range(MIN_WORD_LENGTH, MAX_WORD_LENGTH + 1)))
    assert len(lengths) > 1
