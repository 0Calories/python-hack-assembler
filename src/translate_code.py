# Maps string representations of the comp portion of C-instructions to their binary equivalent
COMP_TABLE = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
}

# Maps string representations of the dest portion of C-instructions to their binary equivalent
DEST_TABLE = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

# Maps string representations of the jump portion of C-instructions to their binary equivalent
JUMP_TABLE = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

A_INSTR_PREFIX = "011"
C_INSTR_PREFIX = "111"


def translate_a_instruction(address: str) -> str:
    binary_address = bin(int(address))
    return binary_address


def translate_c_instruction(dest: str, comp: str, jump: str) -> str:
    dest_binary = DEST_TABLE.get(dest)
    comp_binary = COMP_TABLE.get(dest)
    jump_binary = JUMP_TABLE.get(dest)

    if not dest_binary:
        raise ValueError("Invalid dest portion of instruction")

    if not comp_binary:
        raise ValueError("Invalid comp portion of instruction")

    if not jump_binary:
        raise ValueError("Invalid jump portion of instruction")

    result = "{}{}{}{}".format(C_INSTR_PREFIX, comp_binary, dest_binary, jump_binary)
    return result
