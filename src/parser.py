# type: ignore
from .translate_code import translate_a_instruction, translate_c_instruction
from .symbol_table import SymbolTable


class Parser:
    def __init__(self, file: str) -> None:
        if not file.endswith(".asm"):
            raise ValueError("Must input a valid .asm file")

        self.line_num = 0
        self.file = file
        self.symbol_table = SymbolTable()

        output_file_name = file.replace(".asm", ".hack")
        self.output_file = open(output_file_name, "x")

    def assemble(self):
        self.first_pass()
        self.second_pass()

    # The first pass scans the file for labels and inserts them into the symbol table
    def first_pass(self):
        try:
            with open(self.file, "r") as file:
                for line in file:
                    line = line.strip()

                    if line == "" or line.startswith("//"):
                        continue

                    if not line.startswith("("):
                        self.line_num += 1
                        continue

                    # Extract the value of the label
                    open_index = line.find("(")
                    close_index = line.find(")")

                    if close_index == -1:
                        raise ValueError("Label not properly closed with ')'")

                    label = line[open_index + 1 : close_index]
                    self.symbol_table.add_label(label, str(self.line_num))

        except FileNotFoundError:
            print(f"File {self.file} not found.")
            return None

    def second_pass(self):
        try:
            with open(self.file, "r") as file:
                for line in file:
                    translatedLine = self.parse_line(line)

                    if translatedLine is not None:
                        print(translatedLine)
                        self.output_file.write(translatedLine + "\n")

        except FileNotFoundError:
            print(f"File {self.file} not found.")
            return None

    def parse_line(self, line: str) -> None | str:
        line = line.strip()

        # Skip whitespace
        if line == "":
            return None

        # Skip comment lines
        if line.startswith("//"):
            return None

        # Skip labels
        if line.startswith("("):
            return None

        # Handle inline comments
        if len(line.split("//")) > 1:
            line = line.split("//")[0].strip()

        # Handle A instructions
        if line.startswith("@"):
            maybe_variable = line.split("@")
            if len(maybe_variable) > 1 and not maybe_variable[1].isdigit():
                symbol = maybe_variable[1].strip()
                result = self.symbol_table.get_symbol(symbol)

                # First instance of seeing a symbol means it must be added to the table
                if result is None:
                    result = self.symbol_table.add_symbol(symbol)

                a_instruction_line = "@" + result
                return parse_and_translate_instruction(a_instruction_line)
            elif maybe_variable[1].isdigit():
                a_instruction_line = "@" + maybe_variable[1]
                return parse_and_translate_instruction(a_instruction_line)

        # Handle C instructions
        return parse_and_translate_instruction(line)


def parse_and_translate_instruction(instruction: str) -> str:
    if instruction.startswith("@"):
        result = parse_a_instruction(instruction)
        return translate_a_instruction(result)

    dest, comp, jump = parse_c_instruction(instruction)

    return translate_c_instruction(dest, comp, jump)


def parse_c_instruction(instruction: str) -> tuple[str, str, str]:
    #  Dest and jump are optional, so they are set to an empty string by default
    dest = ""
    jump = ""

    if "=" in instruction:
        dest = instruction.split("=")[0]

    if ";" in instruction:
        jump = instruction.split(";")[1]

    if dest and not jump:
        comp = instruction.split("=")[1]

    if jump and not dest:
        comp = instruction.split(";")[0]

    if dest and jump:
        start_index = instruction.find("=")
        end_index = instruction.find(";")

        comp = instruction[start_index + 1 : end_index]

    print("dest: {}, comp: {}, jump: {}".format(dest, comp, jump))
    return (dest, comp, jump)


def parse_a_instruction(instruction: str) -> str:
    return instruction[1:]


def parse_label(label: str):
    print(label)
