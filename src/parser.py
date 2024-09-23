# type: ignore
from .translate_code import translate_a_instruction, translate_c_instruction


def parse_line(line: str) -> None | str:
    line = line.strip()

    # Skip whitespace
    if line == "":
        return None

    # Handle inline comments
    if line.split("//")[1]:
        line = line[0].strip()

    if line.startswith("("):
        if not line.endswith(")"):
            raise SyntaxError("Label instruction must be closed with )")

        label = line[1:-1]
        parse_label(label)
        return None

    # Handle variables
    if line.startswith("@"):
        maybe_variable = line.split("@")[1]
        if not maybe_variable.isdigit():
            # Stubbed: Add to the symbol table here
            return

    return parse_and_translate_instruction(line)


def parse_and_translate_instruction(instruction: str) -> str:
    if instruction.startswith("@"):
        result = parse_a_instruction(instruction)
        return translate_a_instruction(result)

    dest, comp, jump = parse_c_instruction(instruction)

    return translate_c_instruction(dest, comp, jump)


def parse_instruction(instruction: str):
    if not instruction.startswith("@"):
        raise ValueError("Expected A instruction to start with @")

    parse_c_instruction(instruction)


def parse_c_instruction(instruction: str) -> tuple[str, str, str]:
    # TODO: Dest and jump are optional. Update this to handle the case when there is no dest.

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


def parse_label(label: str):
    print(label)
