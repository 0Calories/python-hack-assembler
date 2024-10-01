class SymbolTable:
    def __init__(self):
        # Initialize the table with the predefined symbols
        self.table = {
            # Reserved registers
            "R0": "0",
            "R1": "1",
            "R2": "2",
            "R3": "3",
            "R4": "4",
            "R5": "5",
            "R6": "6",
            "R7": "7",
            "R8": "8",
            "R9": "9",
            "R10": "10",
            "R11": "11",
            "R12": "12",
            "R13": "13",
            "R14": "14",
            "R15": "15",
            # Peripherals
            "SCREEN": "16384",
            "KBD": "24576",
            # OS symbols
            "SP": "0",
            "LCL": "1",
            "ARG": "2",
            "THIS": "3",
            "THAT": "4",
        }

        # Addresses for variables start at register 16
        self.reg_number = 16

    def add_symbol(self, symbol: str) -> str:
        self.table[symbol] = str(self.reg_number)
        self.reg_number += 1

        return self.table[symbol]

    # When labels are added, their value is determined by the
    # line number of the subsequent instruction.
    # This value is provided by the parser
    def add_label(self, label: str, value: str):
        self.table[label] = value

    def get_symbol(self, symbol: str) -> str | None:
        if symbol not in self.table:
            return None

        return self.table[symbol]
