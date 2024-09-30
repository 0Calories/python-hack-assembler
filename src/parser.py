# type: ignore
from .translate_code import translate_a_instruction, translate_c_instruction

# TODO:
# - Finish the case handling for c instructions
# - Add a line counter that will keep track of the line number of the current instruction
# - Map line numbers to instructions during the 'first pass'
# - The first pass will also assign labels in the symbol table
# - Finish implementing the symbol table class, add all handling inside the class
#     - New variables get assigned a unique address starting at 16
#     - Labels get assigned the line number of the subsequent instruction


class Parser:
    def __init__(self, file: str) -> None:
        if not file.endswith(".asm"):
            raise ValueError("Must input a valid .asm file")

        self.lineNum = 0
        self.file = file
        self.outputFile = file.replace(".asm", ".hack")

    def assemble(self):
        try:
            with open(self.file, "r") as file:
                for line in file:
                    self.read_line(line)

        except FileNotFoundError:
            print(f"File {self.file} not found.")
            return None

    def read_line(self, line):
        print(line)


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
