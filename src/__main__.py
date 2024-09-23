# type: ignore
from parser import parse_instruction
from translate_code import translate_a_instruction, translate_c_instruction


def main():
    user_input = input("Enter the full instruction: ")
    parse_instruction(user_input)


if __name__ == "__main__":
    main()
