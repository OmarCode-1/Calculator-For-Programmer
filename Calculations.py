def binaryToDecimalSigned(binary):
    # Convert binary to decimal (signed)
    if binary[0] == '1':  # If it's negative
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary[1:])
        decimal = -int(complement, 2) - 1
    else:
        decimal = int(binary, 2)
    return decimal

def binaryToDecimalUnsigned(binary):
    # Convert binary to decimal (unsigned)
    decimal = int(binary, 2)
    return decimal

def binaryToHex(binary):
    # Convert binary to hexadecimal
    hex_value = hex(int(binary, 2))[2:].upper()
    return hex_value

def binaryToOctal(binary):
    # Convert binary to octal
    octal_value = oct(int(binary, 2))[2:]
    return octal_value

def decimalToBinarySigned(decimal):

    # Convert decimal to binary (signed)
    if decimal < 0:
        binary = bin(256 + decimal)[2:]
    else:
        binary = bin(decimal)[2:]

    # Pad the binary number with zeros to make it 8 bits long
    binary = binary.zfill(8)

    return binary


def decimalToBinaryUnsigned(decimal):

    # Convert decimal to binary (unsigned)
    binary = bin(decimal)[2:]

    # Pad the binary number with zeros to make it 8 bits long
    binary = binary.zfill(8)

    return binary

def decimalToBinary16Signed(decimal):

    # Convert decimal to binary (signed)
    if decimal < 0:
        binary = bin(65536 + decimal)[2:]
    else:
        binary = bin(decimal)[2:]

    # Pad the binary number with zeros to make it 16 bits long
    binary = binary.zfill(16)

    return binary

def decimalToBinary16Unsigned(decimal):

    # Convert decimal to binary (unsigned)
    binary = bin(decimal)[2:]

    # Pad the binary number with zeros to make it 16 bits long
    binary = binary.zfill(16)

    return binary
def decimalToBinary32Signed(decimal):


    # Convert decimal to binary (signed)
    if decimal < 0:
        binary = bin(4294967296 + decimal)[2:]
    else:
        binary = bin(decimal)[2:]

    # Pad the binary number with zeros to make it 32 bits long
    binary = binary.zfill(32)

    return binary


def decimalToBinary32UnSigned(decimal):


    # Convert decimal to binary (unsigned)
    binary = bin(decimal)[2:]

    # Pad the binary number with zeros to make it 32 bits long
    binary = binary.zfill(32)

    return binary

def octalToBinarySigned(octal):
    # Convert octal to binary
    binary = bin(int(octal, 8))[2:].zfill(8)

    # If the most significant bit is 1, it's a negative number
    if binary[0] == '1':
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(complement, 2) + 1)[2:].zfill(8)

    return binary

def octalToBinaryUnsigned(octal):
    # Convert octal to binary and remove the '0b' prefix
    binary = bin(int(octal, 8))[2:]

    # Pad the binary number with leading zeros to make it 8 bits long
    binary = binary.zfill(8)

    return binary
def octalToBinary16Signed(octal):
    # Convert octal to binary
    binary = bin(int(octal, 8))[2:].zfill(16)

    # If the most significant bit is 1, it's a negative number
    if binary[0] == '1':
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(complement, 2) + 1)[2:].zfill(16)

    return binary
def octalToBinary16Unsigned(octal):
    # Convert octal to binary and remove the '0b' prefix
    binary = bin(int(octal, 8))[2:]

    # Pad the binary number with leading zeros to make it 16 bits long
    binary = binary.zfill(16)

    return binary

def octalToBinary32Signed(octal):
    # Convert octal to binary
    binary = bin(int(octal, 8))[2:].zfill(32)

    # If the most significant bit is 1, it's a negative number
    if binary[0] == '1':
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(complement, 2) + 1)[2:].zfill(32)

    return binary
def octalToBinary32Unsigned(octal):
    # Convert octal to binary and remove the '0b' prefix
    binary = bin(int(octal, 8))[2:]

    # Pad the binary number with leading zeros to make it 32 bits long
    binary = binary.zfill(32)

    return binary
def hexToBinarySigned(hexadecimal):
    # Convert hexadecimal to binary
    binary = bin(int(hexadecimal, 16))[2:].zfill(8)

    # If the most significant bit is 1, it's a negative number
    if binary[0] == '1':
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(complement, 2) + 1)[2:].zfill(8)

    return binary

def hexToBinaryUnsigned(hexadecimal):
    # Convert hexadecimal to binary and remove the '0b' prefix
    binary = bin(int(hexadecimal, 16))[2:]

    # Pad the binary number with leading zeros to make it 8 bits long
    binary = binary.zfill(8)

    return binary
def hexToBinary16Signed(hexadecimal):
    # Convert hexadecimal to binary
    binary = bin(int(hexadecimal, 16))[2:].zfill(16)

    # If the most significant bit is 1, it's a negative number
    if binary[0] == '1':
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(complement, 2) + 1)[2:].zfill(16)

    return binary


def hexToBinary16Unsigned(hexadecimal):
    # Convert hexadecimal to binary and remove the '0b' prefix
    binary = bin(int(hexadecimal, 16))[2:]

    # Pad the binary number with leading zeros to make it 16 bits long
    binary = binary.zfill(16)

    return binary
def hexToBinary32Signed(hexadecimal):
    # Convert hexadecimal to binary
    binary = bin(int(hexadecimal, 16))[2:].zfill(32)

    # If the most significant bit is 1, it's a negative number
    if binary[0] == '1':
        # Convert to positive by taking two's complement
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        binary = bin(int(complement, 2) + 1)[2:].zfill(32)

    return binary

def hexToBinary32Unsigned(hexadecimal):
    # Convert hexadecimal to binary and remove the '0b' prefix
    binary = bin(int(hexadecimal, 16))[2:]

    # Pad the binary number with leading zeros to make it 32 bits long
    binary = binary.zfill(32)

    return binary
# =============================================================================================


def binarySigned(value):
    decimal_value = binaryToDecimalSigned(value)
    hex_value = binaryToHex(value)
    octal_value = binaryToOctal(value)

    return decimal_value, hex_value, octal_value



def binaryUnsigned(value):
    decimal_value = binaryToDecimalUnsigned(value)
    hex_value = binaryToHex(value)
    octal_value = binaryToOctal(value)

    return decimal_value, hex_value, octal_value



def decmial8Signed(value):
    binary_value = decimalToBinarySigned(value)
    hex_value = binaryToHex(binary_value)
    octal_value = binaryToOctal(binary_value)

    return binary_value, hex_value, octal_value

def decmial8UnSigned(value):
    binary_value = decimalToBinaryUnsigned(value)
    hex_value = binaryToHex(binary_value)
    octal_value = binaryToOctal(binary_value)

    return binary_value, hex_value, octal_value




def decmial16Signed(value):
    binary_value = decimalToBinary16Signed(value)
    hex_value = binaryToHex(binary_value)
    octal_value = binaryToOctal(binary_value)

    return binary_value, hex_value, octal_value





def decmial16UnSigned(value):

    binary_value = decimalToBinary16Unsigned(value)
    hex_value = binaryToHex(binary_value)
    octal_value = binaryToOctal(binary_value)

    return binary_value, hex_value, octal_value



def decmial32Signed(value):
    binary_value = decimalToBinary32Signed(value)
    hex_value = binaryToHex(binary_value)
    octal_value = binaryToOctal(binary_value)

    return binary_value, hex_value, octal_value


def decmial32UnSigned(value):
    binary_value = decimalToBinary32UnSigned(value)
    hex_value = binaryToHex(binary_value)
    octal_value = binaryToOctal(binary_value)

    return binary_value, hex_value, octal_value



def ocotal8Signed(value):
    binary_value = octalToBinarySigned(value)
    decimal_value = binaryToDecimalSigned(binary_value)
    hex_value = binaryToHex(binary_value)

    return binary_value, hex_value, decimal_value




def ocotal8UnSigned(value):
    binary_value = octalToBinaryUnsigned(value)
    decimal_value = binaryToDecimalUnsigned(binary_value)
    hex_value = binaryToHex(binary_value)

    return binary_value, hex_value, decimal_value




def ocotal16Signed(value):
    binary_value = octalToBinary16Signed(value)
    decimal_value = binaryToDecimalSigned(binary_value)
    hex_value = binaryToHex(binary_value)

    return binary_value, hex_value, decimal_value



def ocotal16UnSigned(value):
    binary_value = octalToBinary16Unsigned(value)
    decimal_value = binaryToDecimalUnsigned(binary_value)
    hex_value = binaryToHex(binary_value)

    return binary_value, hex_value, decimal_value



def ocotal32Signed(value):
    binary_value = octalToBinary32Signed(value)
    decimal_value = binaryToDecimalSigned(binary_value)
    hex_value = binaryToHex(binary_value)

    return binary_value, hex_value, decimal_value





def ocotal32UnSigned(value):
    binary_value = octalToBinary32Unsigned(value)
    decimal_value = binaryToDecimalUnsigned(binary_value)
    hex_value = binaryToHex(binary_value)

    return binary_value, hex_value, decimal_value


def binary_to_octal(binary_num):
    # Pad the binary number with leading zeros to make its length a multiple of 3
    while len(binary_num) % 3 != 0:
        binary_num = '0' + binary_num

    # Group the binary digits into sets of three starting from the right
    groups = [binary_num[i:i + 3] for i in range(0, len(binary_num), 3)]

    # Convert each group into its octal equivalent
    octal_num = ''
    for group in groups:
        octal_digit = str(int(group, 2))  # Convert binary to decimal
        octal_num += octal_digit

    return int(octal_num)

def hexa8Signed(value):
    binary_value = hexToBinarySigned(value)
    decimal_value = binaryToDecimalSigned(binary_value)
    octal_value = binary_to_octal(binary_value)

    return binary_value, octal_value, decimal_value


def hexa8UnSigned(value):
    binary_value = hexToBinaryUnsigned(value)
    decimal_value = binaryToDecimalUnsigned(binary_value)
    octal_value = binary_to_octal(binary_value)

    return binary_value, octal_value, decimal_value





def hexa16Signed(value):
    binary_value = hexToBinary16Signed(value)
    decimal_value = binaryToDecimalSigned(binary_value)
    octal_value = binary_to_octal(binary_value)

    return binary_value, octal_value, decimal_value


def hexa16UnSigned(value):
    binary_value = hexToBinary16Unsigned(value)
    decimal_value = binaryToDecimalUnsigned(binary_value)
    octal_value = binary_to_octal(binary_value)

    return binary_value, octal_value, decimal_value




def hexa32Signed(value):
    binary_value = hexToBinary32Signed(value)
    decimal_value = binaryToDecimalSigned(binary_value)
    octal_value = binary_to_octal(binary_value)

    return binary_value, octal_value, decimal_value


def hexa32UnSigned(value):
    binary_value = hexToBinary32Unsigned(value)
    decimal_value = binaryToDecimalUnsigned(binary_value)
    octal_value = binary_to_octal(binary_value)

    return binary_value, octal_value, decimal_value

