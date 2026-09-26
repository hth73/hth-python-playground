import string

import pytest

from src.pwmint.password import (
  DEFAULT_PASSWORD_LENGTH,
  MAX_PASSWORD_LENGTH,
  MIN_PASSWORD_LENGTH,
  generate_password,
)


def test_default_password_has_default_length():
  password = generate_password()

  assert len(password) == DEFAULT_PASSWORD_LENGTH


def test_minimum_password_length_is_allowed():
  password = generate_password(MIN_PASSWORD_LENGTH)

  assert len(password) == MIN_PASSWORD_LENGTH


def test_maximum_password_length_is_allowed():
  password = generate_password(MAX_PASSWORD_LENGTH)

  assert len(password) == MAX_PASSWORD_LENGTH


def test_password_length_below_minimum_is_rejected():
  with pytest.raises(ValueError):
    generate_password(MIN_PASSWORD_LENGTH - 1)


def test_password_length_above_maximum_is_rejected():
  with pytest.raises(ValueError):
    generate_password(MAX_PASSWORD_LENGTH + 1)


def test_string_password_length_is_rejected():
  with pytest.raises(ValueError):
    generate_password("18")


def test_password_without_character_sets_is_rejected():
  with pytest.raises(ValueError):
    generate_password(
      use_lowercase=False,
      use_uppercase=False,
      use_digits=False,
      use_special=False,
    )


@pytest.mark.parametrize(
  "use_lowercase, use_uppercase, use_digits, use_special, allowed_characters",
  [
    (
      False,
      True,
      True,
      True,
      string.ascii_uppercase + string.digits + string.punctuation,
    ),
    (
      True,
      False,
      True,
      True,
      string.ascii_lowercase + string.digits + string.punctuation,
    ),
    (
      True,
      True,
      False,
      True,
      string.ascii_lowercase + string.ascii_uppercase + string.punctuation,
    ),
    (
      True,
      True,
      True,
      False,
      string.ascii_lowercase + string.ascii_uppercase + string.digits,
    ),
  ],
)
def test_password_uses_only_enabled_character_sets(
  use_lowercase,
  use_uppercase,
  use_digits,
  use_special,
  allowed_characters,
):
  password = generate_password(
    use_lowercase=use_lowercase,
    use_uppercase=use_uppercase,
    use_digits=use_digits,
    use_special=use_special,
  )

  assert all(character in allowed_characters for character in password)


def test_multiple_passwords_are_not_identical():
  passwords = []

  for _ in range(5):
    passwords.append(generate_password())

  assert len(set(passwords)) == len(passwords)
  