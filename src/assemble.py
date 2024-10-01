import argparse
from parser import Parser


def main():
    cli = argparse.ArgumentParser(
        description="A script that takes .asm files containing instructions for the Hack computer, and converts them to machine code"
    )

    cli.add_argument("file", type=str, help="The path to the .asm file to be converted")

    args = cli.parse_args()

    hack_parser = Parser(args.file)
    hack_parser.assemble()


if __name__ == "__main__":
    main()
