# type: ignore
from .translate_code import translate_a_instruction, translate_c_instruction


def parse_and_translate_instruction(instruction: str) -> str:
    if instruction.startswith("@"):
        result = parse_a_instruction(instruction)
        return translate_a_instruction(result)

    dest, comp, jump = parse_c_instruction(instruction)
    print(dest)
    print(comp)
    print(jump)

    return translate_c_instruction(dest, comp, jump)


def parse_instruction(instruction: str):
    if not instruction.startswith("@"):
        raise ValueError("Expected A instruction to start with @")

    parse_c_instruction(instruction)


def parse_c_instruction(instruction: str) -> tuple[str, str, str]:
    split_instruction = instruction.split("=")
    dest = split_instruction[0]

    if ";" in split_instruction[1]:
        comp, jump = split_instruction[1].split(";")
    else:
        comp = split_instruction[1]
        jump = ""

    print("dest: {}, comp: {}, jump: {}".format(dest, comp, jump))
    return (dest, comp, jump)


def parse_a_instruction(instruction: str) -> str:
    return instruction[1:]
