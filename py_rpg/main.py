import argparse
import logging

from game import Game


def main() -> None:
    program_name = "py_rpg"
    parser = argparse.ArgumentParser(prog=program_name)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level, format="%(levelname)s: %(name)s:  %(message)s")
    Game(program_name, args.debug).run()


if __name__ == "__main__":
    main()
