import pytest

from src.pwmint.passphrase import (
	DEFAULT_WORD_COUNT,
	MAX_WORD_COUNT,
	MIN_WORD_COUNT,
	generate_passphrase,
)


def test_default_passphrase_has_default_word_count():
	result = generate_passphrase()

	assert len(result.split("-")) == DEFAULT_WORD_COUNT


def test_minimum_word_count_is_allowed():
	result = generate_passphrase(MIN_WORD_COUNT)

	assert len(result.split("-")) == MIN_WORD_COUNT


def test_maximum_word_count_is_allowed():
	result = generate_passphrase(MAX_WORD_COUNT)

	assert len(result.split("-")) == MAX_WORD_COUNT


def test_word_count_below_minimum_is_rejected():
	with pytest.raises(ValueError):
		generate_passphrase(MIN_WORD_COUNT - 1)


def test_word_count_above_maximum_is_rejected():
	with pytest.raises(ValueError):
		generate_passphrase(MAX_WORD_COUNT + 1)


def test_invalid_word_count_type_is_rejected():
	with pytest.raises(ValueError):
		generate_passphrase("4")


def test_invalid_separator_type_is_rejected():
	with pytest.raises(ValueError):
		generate_passphrase(separator=1)


def test_words_are_unique_within_a_passphrase():
	result = generate_passphrase()
	words = result.split("-")

	assert len(words) == len(set(words))


def test_custom_separator_is_used():
	result = generate_passphrase(separator="_")

	assert "_" in result
	assert "-" not in result


def test_empty_separator_is_allowed():
	result = generate_passphrase(separator="")

	assert result
	assert "-" not in result


def test_passphrase_longer_than_maximum_length_is_rejected():
	with pytest.raises(ValueError):
		generate_passphrase(separator="x" * 120)


def test_multiple_passphrases_are_not_always_identical():
	passphrases = []

	for _ in range(5):
		passphrases.append(generate_passphrase())

	assert len(set(passphrases)) > 1
