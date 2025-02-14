import customtkinter as tk
from PIL import ImageTk, Image  

caluc_page = tk.CTk()
caluc_page.geometry("1280x720")
caluc_page.title("Calucolator")

# ------------------ farme ------------------- :
caluc_frame = tk.CTkFrame(caluc_page, width=1280, height=720, fg_color="transparent")
caluc_frame.pack( expand=True)


# ----------------- Text Box ----------------- :
text_box_button_label = tk.CTkButton(caluc_frame, text = "Caluclations",font=("Times",15,"bold"),width=400, height=30, fg_color="gray")
text_box = tk.CTkTextbox(caluc_frame, width= 1260, height=380)

# Placing :
text_box_button_label.place(x = 450, y = 270)
text_box.place(x = 10, y = 320)


def clearTextBox():
    text_box.delete("1.0", tk.END)

clear_text_box_button = tk.CTkButton(caluc_frame, command=clearTextBox, text = "Clear", font=("Times",15,"bold"), width=100, height=30, fg_color="gray")
clear_text_box_button.place(x = 860, y = 270)

# ----------------- Buttons ----------------- :
def numberConversion():
    
    number_conversion_button_label = tk.CTkButton(caluc_frame, text = "Number Conversion",font=("Times",15,"bold"),width=400, height=30, fg_color="green")
    input_box_label = tk.CTkLabel(caluc_frame, text = "input value",width=10,font=("Times",15,"bold"))
    input_box_entry = tk.CTkEntry(caluc_frame, width=200, height=5)

    # Placcing
    number_conversion_button_label.place(x = 10, y = 20)
    input_box_label.place(x=50, y = 60)
    input_box_entry.place(x = 200, y= 60)

    # Binary to decimal :
    def binaryToDecimal():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 2)
        clearTextBox()
        text_box.insert(tk.END, f"The Decimal of given Binary Number is : {decimal_number}")

    binary_to_decimal_button = tk.CTkButton(caluc_frame, command = binaryToDecimal, text = "Binary to Decimal", font=("Times",15,"bold"), width=130, height=10)
    binary_to_decimal_button.place(x = 10, y = 100)

    # Octal to decimal :
    def octalToDecimal():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 8)
        clearTextBox()
        text_box.insert(tk.END, f"The Decimal of given Ocatl Number is : {decimal_number}")

    octal_to_decimal_button = tk.CTkButton(caluc_frame, command = octalToDecimal, text = "Octal to Decimal", font=("Times",15,"bold"), width=130, height=10)
    octal_to_decimal_button.place(x = 145, y = 100)

    # Hexadecimal to decimal:
    def HexaToDecimal():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 16)
        clearTextBox()
        text_box.insert(tk.END, f"The Decimal of given Hexadecimal Number is : {decimal_number}")

    hexa_to_decimal_button = tk.CTkButton(caluc_frame, command = HexaToDecimal, text = "Hexa to Decimal", font=("Times",15,"bold"), width=130, height=10)
    hexa_to_decimal_button.place(x = 280, y = 100)




    # # Decimal to Binary :
    def decimalToBinary():
        input_value = int(input_box_entry.get())
        binary_number = bin(input_value)[2:]
        clearTextBox()
        text_box.insert(tk.END, f"The Binary of given Decimal Number is : {binary_number}")

    decimal_to_binary_buuton = tk.CTkButton(caluc_frame, command = decimalToBinary, text = "Decimal to Binary", font=("Times",15,"bold"), width=130, height=10)
    decimal_to_binary_buuton.place(x = 10, y = 130)

    # # Decimal to octal :
    def decimaToOctal():
        input_value = int(input_box_entry.get())
        octal_number = oct(input_value)[2:]
        clearTextBox()
        text_box.insert(tk.END, f"The Octal of given Decimal Number is : {octal_number}")

    decimal_to_octal_button = tk.CTkButton(caluc_frame, command = decimaToOctal, text = "Decimal to Octal", font=("Times",15,"bold"), width=130, height=10)
    decimal_to_octal_button.place(x = 145, y = 130)

    # # Decimal to Hexa :
    def decimalToHexa():
        input_value = int(input_box_entry.get())
        hexadecimal_number = hex(input_value)[2:]
        clearTextBox()
        text_box.insert(tk.END, f"The Hexadecimal of given Decimal Number is : {hexadecimal_number}")

    decimal_to_hexa_button = tk.CTkButton(caluc_frame, command = decimalToHexa, text = "Decimal to Hexa", font=("Times",15,"bold"), width=130, height=10)
    decimal_to_hexa_button.place(x = 280, y = 130)




    # # # Octal to binary :
    def octoToBinary():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 8)
        binary_number = bin(decimal_number)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Binary of given Octal Number is : {binary_number}")

    octal_to_binary_button = tk.CTkButton(caluc_frame, command = octoToBinary, text = "Octal to Binary", font=("Times",15,"bold"), width=130, height=10)
    octal_to_binary_button.place(x = 10, y = 160)

    # # # Octal to Hexa :
    def octalToHexa():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 8)
        hexadecimal_number = hex(decimal_number)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Hexadecimal of given Octal Number is : {hexadecimal_number}")

    octal_to_hexa_button = tk.CTkButton(caluc_frame, command = octalToHexa, text = "Octal to Hexa", font=("Times",15,"bold"), width=130, height=10)
    octal_to_hexa_button.place(x = 145, y = 160)

    # # # Binary to Octal :
    def binaryToOctal():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 2)
        octal_number = oct(decimal_number)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Octal of given Binary Number is : {octal_number}")

    octal_to_hexa_button = tk.CTkButton(caluc_frame, command = binaryToOctal, text = "Binary To Octal", font=("Times",15,"bold"), width=130, height=10)
    octal_to_hexa_button.place(x = 280, y = 160)




    # # # # Binary to Hexa :
    def binaryToHexa():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 2)
        hexadecimal_number = hex(decimal_number)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Hexadecimal of given Binary Number is : {hexadecimal_number}")

    binary_to_hexa_button = tk.CTkButton(caluc_frame, command = binaryToHexa, text = "Binary to Hexa", font=("Times",15,"bold"), width=130, height=10)
    binary_to_hexa_button.place(x = 10, y = 190)


    # # # # Hexa to Decimal :
    def hexaToBinary():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 16)
        binary_number = bin(decimal_number)[2:]
        
        clearTextBox()
        text_box.insert(tk.END, f"The Binary of given Hexa Number is : {binary_number}")

    hexa_to_binary_button = tk.CTkButton(caluc_frame, command = hexaToBinary, text = "Hexa to Binary", font=("Times",15,"bold"), width=130, height=10)
    hexa_to_binary_button.place(x = 145, y = 190)

    # # # # Hexa to Octal :
    def hexaToOctal():
        input_value = input_box_entry.get()
        decimal_number = int(input_value, 16)
        octal_number = oct(decimal_number)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Octal of given Hexa Number is : {octal_number}")

    hexa_to_octal_button = tk.CTkButton(caluc_frame, command = hexaToOctal, text = "Hexa to Octal", font=("Times",15,"bold"), width=130, height=10)
    hexa_to_octal_button.place(x = 280, y = 190)


def asciiConversion():
    ascii_conversion_button_label = tk.CTkButton(caluc_frame, text = "Ascii Conversion",font=("Times",15,"bold"),width=400, height=30, fg_color="green")
    input_box_label = tk.CTkLabel(caluc_frame, text = "input value",width=10,font=("Times",15,"bold"))
    input_box_entry = tk.CTkEntry(caluc_frame, width=200, height=5)

    # Placcing
    ascii_conversion_button_label.place(x = 450, y = 20)
    input_box_label.place(x = 490, y = 60)
    input_box_entry.place(x = 640, y= 60)


    # Binary to Ascii :
    def binaryToAscii():
        input_value = input_box_entry.get()
        ascii_number = chr(int(input_value, 2))

        clearTextBox()
        text_box.insert(tk.END, f"The Ascii of given Binary Number is : {ascii_number}")

    binary_to_asccii_button = tk.CTkButton(caluc_frame, command = binaryToAscii, text = "Binary to Ascii", font=("Times",15,"bold"), width=198, height=10)
    binary_to_asccii_button.place(x = 450, y = 100)

    # Ascii to binary :
    def asciiToBinary():
        input_value = input_box_entry.get()
        binary_number = format(ord(input_value), '08b')

        clearTextBox()
        text_box.insert(tk.END, f"The Binary of given Ascii Number is : {binary_number}")


    ascii_to_binary_button = tk.CTkButton(caluc_frame, command = asciiToBinary, text = "Ascii to Binary", font=("Times",15,"bold"), width=198, height=10)
    ascii_to_binary_button.place(x = 650, y = 100)

    # # Decimal to Ascii :
    def decimalToAscii():
        input_value = int(input_box_entry.get())
        ascii_number = chr(input_value)

        clearTextBox()
        text_box.insert(tk.END, f"The Ascii of given Decimal Number is : {ascii_number}")

    decimal_to_ascii_button = tk.CTkButton(caluc_frame, command = decimalToAscii, text = "Decimal To Ascii", font=("Times",15,"bold"), width=198, height=10)
    decimal_to_ascii_button.place(x = 450, y = 130)

    # # Ascii to Decimal :
    def asciiToDecimal():
        input_value = input_box_entry.get()
        decimal_value = ord(input_value)

        clearTextBox()
        text_box.insert(tk.END, f"The Decimal of given Ascii Number is : {decimal_value}")

    ascii_to_decimal_button = tk.CTkButton(caluc_frame, command = asciiToDecimal, text = "Ascii to Decimal", font=("Times",15,"bold"), width=198, height=10)
    ascii_to_decimal_button.place(x = 650, y = 130)

    # # # Octal to Ascii :
    def octalToAscii():
        input_value = input_box_entry.get()
        decimal_value = int(input_value, 8)
        ascii_character = chr(decimal_value)
        
        clearTextBox()
        text_box.insert(tk.END, f"The Ascii of given Octal Number is : {ascii_character}")

    octal_to_ascii_button = tk.CTkButton(caluc_frame, command = octalToAscii, text = "Octal To Ascii", font=("Times",15,"bold"), width=198, height=10)
    octal_to_ascii_button.place(x = 450, y = 160)

    # # # Ascii to Octal :
    def asciiToOctal():
        input_value = input_box_entry.get()
        decimal_value = ord(input_value)
        octal_representation = oct(decimal_value)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Octal of given Ascii Number is : {octal_representation}")

    ascii_to_octal_button = tk.CTkButton(caluc_frame, command = asciiToOctal, text = "Ascii to Octal", font=("Times",15,"bold"), width=198, height=10)
    ascii_to_octal_button.place(x = 650, y = 160)

    # # # # Hexa to Ascii :
    def hexaToAscii():
        input_value = input_box_entry.get()
        ascii_representation = bytes.fromhex(input_value).decode('utf-8')

        clearTextBox()
        text_box.insert(tk.END, f"The Ascii of given Hexa Number is : {ascii_representation}")

    hexa_to_ascii_button = tk.CTkButton(caluc_frame, command = hexaToAscii, text = "Hexa To Ascii", font=("Times",15,"bold"), width=198, height=10)
    hexa_to_ascii_button.place(x = 450, y = 190)

    # # # # Ascii to Hexa :
    def asciiToHexa():
        input_value = input_box_entry.get()
        hexadecimal_representation = bytes(input_value, 'utf-8').hex()

        clearTextBox()
        text_box.insert(tk.END, f"The Hexa of given Ascii Number is : {hexadecimal_representation}")

    ascii_to_Hexa_button = tk.CTkButton(caluc_frame, command = asciiToHexa, text = "Ascii to Hexa", font=("Times",15,"bold"), width=198, height=10)
    ascii_to_Hexa_button.place(x = 650, y = 190)


def binaryArthimatics():
    ascii_conversion_button_label = tk.CTkButton(caluc_frame, text = "Binary Arthimatics",font=("Times",15,"bold"),width=190, height=30, fg_color="green")
    first_input_box_entry = tk.CTkEntry(caluc_frame, width=92, height=5)
    second_input_box_entry = tk.CTkEntry(caluc_frame, width=92, height=5)

    # Placcing
    ascii_conversion_button_label.place(x = 890, y = 20)
    first_input_box_entry.place(x = 890, y= 60)
    second_input_box_entry.place(x = 990, y= 60)

    # Addtion :
    def addition():
        first_value = first_input_box_entry.get()
        second_value = second_input_box_entry.get()

        first_value_binray = int(first_value, 2)
        second_value_binray = int(second_value, 2)

        addtion_value = bin((first_value_binray + second_value_binray))[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Addition of binray two number is: {addtion_value}")

    addtion_button = tk.CTkButton(caluc_frame, command = addition, text = "Addtions", font=("Times",15,"bold"), width=190, height=10)
    addtion_button.place(x = 890, y = 100)

    # # Substruction :
    def subtraction():
        first_value = first_input_box_entry.get()
        second_value = second_input_box_entry.get()

        first_value_binray = int(first_value, 2)
        second_value_binray = int(second_value, 2)

        addtion_value = bin((first_value_binray - second_value_binray))[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The subtraction of binray two number is: {addtion_value}")
        
    substruction_button = tk.CTkButton(caluc_frame, command = subtraction, text = "Subtration", font=("Times",15,"bold"), width=190, height=10)
    substruction_button.place(x = 890, y = 130)

    # # # Multiplication :
    def multiplication():
        first_value = first_input_box_entry.get()
        second_value = second_input_box_entry.get()

        first_value_binray = int(first_value, 2)
        second_value_binray = int(second_value, 2)

        addtion_value = bin((first_value_binray * second_value_binray))[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The multiplication of binray two number is: {addtion_value}")

    multiplication_button = tk.CTkButton(caluc_frame, command = multiplication, text = "Multiplication", font=("Times",15,"bold"), width=190, height=10)
    multiplication_button.place(x = 890, y = 160)

    # # # # Division :
    def division():
        first_value = first_input_box_entry.get()
        second_value = second_input_box_entry.get()

        if second_value == 0 :
            clearTextBox()
            text_box.insert(tk.END, "Error: Division by zero")
            
        first_value_binray = int(first_value, 2)
        second_value_binray = int(second_value, 2)
        

        addtion_value = bin(first_value_binray // second_value_binray)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Addition of division two number is: {addtion_value}")

    division_button = tk.CTkButton(caluc_frame, command = division, text = "Division", font=("Times",15,"bold"), width=190, height=10)
    division_button.place(x = 890, y = 190)



def complements():
    complements_label = tk.CTkButton(caluc_frame, text = "Complements",font=("Times",15,"bold"),width=180, height=30, fg_color="green")
    binary_entry = tk.CTkEntry(caluc_frame, width = 180, height=5)

    # Places :
    complements_label.place(x = 1090, y = 20)
    binary_entry.place(x = 1090, y = 60)

    def complement(binray_value) :
        # Flip each bit
        for i in range(len(binray_value)):
            if binray_value[i] == '0':
                binray_value[i] = '1'
            else:
                binray_value[i] = '0'

        return ''.join(binray_value)
    
    def oneComplement():
        binray = list(binary_entry.get())

        binray = complement(binray)
        
        clearTextBox()
        text_box.insert(tk.END, f"The One's Complement is : {binray}")

    first_complement_button = tk.CTkButton(caluc_frame, command = oneComplement, text = "One's Complement", font=("Times",15,"bold"), width=180, height=50)
    first_complement_button.place(x = 1090, y = 100)

    def twoComplement():
        binray = list(binary_entry.get())
        binray = complement(binray)

        twos_comp = bin(int(binray, 2) + 1)[2:]

        clearTextBox()
        text_box.insert(tk.END, f"The Two's Complement is : {twos_comp}")

    second_complement_button = tk.CTkButton(caluc_frame, command = twoComplement, text = "Two's Complement", font=("Times",15,"bold"), width=180, height=50)
    second_complement_button.place(x = 1090, y = 160)
    


numberConversion()
asciiConversion()
binaryArthimatics()
complements()
caluc_page.mainloop()