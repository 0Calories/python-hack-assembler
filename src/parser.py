def parse_instruction(instruction: str):
    if instruction.startswith("@"):
        parse_a_instruction(instruction)

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
    print("Stubbed")
    return ""
