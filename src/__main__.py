# type: ignore
from .parser import Parser


def main():
    # user_input = input("Enter the full instruction: ")
    # binary_instruction = parse_and_translate_instruction(user_input)

    # print(binary_instruction)
    parser = Parser("/home/ash/code/python-hack-assembler/test.asm")
    parser.assemble()


if __name__ == "__main__":
    main()
