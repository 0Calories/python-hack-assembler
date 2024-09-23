# type: ignore
from .parser import parse_and_translate_instruction


def main():
    user_input = input("Enter the full instruction: ")
    binary_instruction = parse_and_translate_instruction(user_input)

    print(binary_instruction)


if __name__ == "__main__":
    main()
