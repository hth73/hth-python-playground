"""Command-line interface for generating passwords and passphrases."""

import argparse

from src.pwmint.passphrase import generate_passphrase
from src.pwmint.password import generate_password


def create_parser() -> argparse.ArgumentParser:
	"""Create the argument parser for the pwmint command."""
	parser = argparse.ArgumentParser(
		description="Generate secure passwords or passphrases."
	)
	parser.add_argument(
		"-l",
		"--length",
		type=int,
		metavar="[15-64]",
		help="Password length (15-64 characters).",
	)
	parser.add_argument(
		"-c",
		"--count",
		type=int,
		default=1,
		metavar="[1-100]",
		help="Number of secrets to generate.",
	)
	parser.add_argument(
		"-p",
		"--passphrase",
		action="store_true",
		help="Generate passphrases instead of passwords.",
	)
	parser.add_argument(
		"-w",
		"--words",
		type=int,
		metavar="[4-10]",
		help="Number of words (4-10, maximum 128 characters).",
	)
	parser.add_argument(
		"-s",
		"--separator",
		metavar="SEPARATOR",
		help='Separator between passphrase words (default: "-").',
	)
	return parser


def main() -> None:
    """Parse arguments, generate secrets, and print one per line."""
    parser = create_parser()
    arguments = parser.parse_args()

    if arguments.count < 1:
        parser.error("Count must be at least 1.")

    if arguments.passphrase and arguments.length is not None:
        parser.error("--length cannot be used with --passphrase.")

    if not arguments.passphrase and arguments.words is not None:
        parser.error("--words requires --passphrase.")

    if not arguments.passphrase and arguments.separator is not None:
        parser.error("--separator requires --passphrase.")

    try:
        for _ in range(arguments.count):
            if arguments.passphrase:
                options = {}

                if arguments.words is not None:
                    options["word_count"] = arguments.words

                if arguments.separator is not None:
                    options["separator"] = arguments.separator

                secret = generate_passphrase(**options)
            else:
                if arguments.length is None:
                    secret = generate_password()
                else:
                    secret = generate_password(arguments.length)

            print(secret)

    except (ValueError, TypeError) as error:
        parser.error(str(error))

if __name__ == "__main__":
	main()
