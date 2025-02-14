import customtkinter as tk
from PIL import ImageTk, Image
from Calculations import *
from tkinter import messagebox

caluc_page = tk.CTk()
caluc_page.geometry("1280x720")
caluc_page.title("Calucolator")

# ------------------ farme ------------------- :
caluc_frame = tk.CTkFrame(caluc_page, width=1280, height=720, fg_color="transparent")
caluc_frame.pack(expand=True)


# ----------------- Number Conversation ----------------- :

byte_choose = tk.StringVar(caluc_frame, 8)

# Dictionary to create multiple buttons
bytes_values = {"8 Bits": '8',
                  "16 Bits": '16',
                  "32 Bits": '32'
                  }
x = 200
for (text, value) in bytes_values.items():
    tk.CTkRadioButton(caluc_frame, text=text, variable=byte_choose, value=value).place(x=20, y=x)
    x += 30


# =================================================

sgn_choose = tk.StringVar(caluc_frame, "signed")

# Dictionary to create multiple buttons
sgn_values = {"Signed": "signed",
                "UnSigned": "unsigned",
                }
x = 200
for (text, value) in sgn_values.items():
    tk.CTkRadioButton(caluc_frame, text=text, variable=sgn_choose, value=value).place(x=120, y=x)
    x += 30




number_conversion_button_label = tk.CTkButton(caluc_frame, text="Number Conversion", font=("Times", 15, "bold"),
                                              width=500, height=30, fg_color="green")



binary_text_box = tk.CTkTextbox(caluc_frame, width=200, height=10)
binray_label = tk.CTkLabel(caluc_frame, text="Binary", font=("Times", 15, "bold"))

decimal_text_box = tk.CTkTextbox(caluc_frame, width=200, height=10)
decimal_label = tk.CTkLabel(caluc_frame, text="Decimal", font=("Times", 15, "bold"))

octal_text_box = tk.CTkTextbox(caluc_frame, width=200, height=10)
octal_label = tk.CTkLabel(caluc_frame, text="Octal", font=("Times", 15, "bold"))

hex_text_box = tk.CTkTextbox(caluc_frame, width=200, height=10)
hex_label = tk.CTkLabel(caluc_frame, text="Hex", font=("Times", 15, "bold"))

# Placing :
binray_label.place(x=35, y=450)
binary_text_box.place(x=30, y=480)

decimal_label.place(x=335, y=450)
decimal_text_box.place(x=330, y=480)

octal_label.place(x=635, y=450)
octal_text_box.place(x=630, y=480)

hex_label.place(x=935, y=450)
hex_text_box.place(x=930, y=480)


def clearTextBox():
    binary_text_box.delete("1.0", tk.END)
    decimal_text_box.delete("1.0", tk.END)
    octal_text_box.delete("1.0", tk.END)
    hex_text_box.delete("1.0", tk.END)



clear_text_box_button = tk.CTkButton(caluc_frame, command=clearTextBox, text="Clear", font=("Times", 15, "bold"),
                                     width=100, height=30, fg_color="gray")
clear_text_box_button.place(x=860, y=570)

def result():
    if len(binary_text_box.get(1.0, "end-1c")) > 0:
        option = "binary"
        value = binary_text_box.get(1.0, "end-1c")
        value= value.zfill(8)
    elif len(decimal_text_box.get(1.0, "end-1c")) > 0:
        option = "decimal"
        value = decimal_text_box.get(1.0, "end-1c")
    elif len(octal_text_box.get(1.0, "end-1c")) > 0:
        option = "octal"
        value = octal_text_box.get(1.0, "end-1c")
    elif len(hex_text_box.get(1.0, "end-1c")) > 0:
        option = "hexa"
        value = hex_text_box.get(1.0, "end-1c")
    else:
        messagebox.showerror("Error", "Fields are Empty")

    final_option = [option, byte_choose.get(), sgn_choose.get()]
    if final_option[0] == "binary":

        if int(value) == -1 :
            messagebox.showerror("Error", "You entered -1")

        elif final_option[2] == 'signed' :
            clearTextBox()
            values_list = binarySigned(value)
            decimal_text_box.insert(tk.END, f"{values_list[0]}")
            octal_text_box.insert(tk.END, f"{values_list[1]}")
            hex_text_box.insert(tk.END, f"{values_list[2]}")

        elif final_option[2] == 'unsigned':
            clearTextBox()
            values_list = binaryUnsigned(value)
            decimal_text_box.insert(tk.END, f"{values_list[0]}")
            octal_text_box.insert(tk.END, f"{values_list[1]}")
            hex_text_box.insert(tk.END, f"{values_list[2]}")


    elif final_option[0] == "decimal":
        value = int(value)
        if final_option[1] == "8":
            if final_option[2] == "signed":
                if value < -128 or value > 127:
                    messagebox.showerror("Error", "Decimal number is out of range for a signed 8-bit number")
                else :
                    clearTextBox()
                    values_list = decmial8Signed(value)
                    binary_text_box.insert(tk.END, f"{values_list[0]}")
                    hex_text_box.insert(tk.END, f"{values_list[1]}")
                    octal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                if value < 0 or value > 255:
                    messagebox.showerror("Error", "Decimal number is out of range for an unsigned 8-bit number")
                else :
                    clearTextBox()
                    values_list = decmial8UnSigned(value)
                    binary_text_box.insert(tk.END, f"{values_list[0]}")
                    hex_text_box.insert(tk.END, f"{values_list[1]}")
                    octal_text_box.insert(tk.END, f"{values_list[2]}")

        elif final_option[1] == "16":
            if final_option[2] == "signed":
                if value < -32768 or value > 32767:
                    messagebox.showerror("Error", "Decimal number is out of range for a signed 16-bit number")
                else :
                    clearTextBox()
                    values_list = decmial16Signed(value)
                    binary_text_box.insert(tk.END, f"{values_list[0]}")
                    hex_text_box.insert(tk.END, f"{values_list[1]}")
                    octal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                if value < 0 or value > 65535:
                    messagebox.showerror("Error", "Decimal number is out of range for an unsigned 16-bit number")
                else :
                    clearTextBox()
                    values_list = decmial16UnSigned(value)
                    binary_text_box.insert(tk.END, f"{values_list[0]}")
                    hex_text_box.insert(tk.END, f"{values_list[1]}")
                    octal_text_box.insert(tk.END, f"{values_list[2]}")
        elif final_option[1] == "32":
            if final_option[2] == "signed":
                if value < -2147483648 or value > 2147483647:
                    messagebox.showerror("Error", "Decimal number is out of range for a signed 32-bit number")
                else :
                    clearTextBox()
                    values_list = decmial32Signed(value)
                    binary_text_box.insert(tk.END, f"{values_list[0]}")
                    hex_text_box.insert(tk.END, f"{values_list[1]}")
                    octal_text_box.insert(tk.END, f"{values_list[2]}")
            elif final_option[2] == "unsigned":
                if value < 0 or value > 4294967295:
                    messagebox.showerror("Error", "Decimal number is out of range for an unsigned 32-bit number")
                else :
                    clearTextBox()
                    values_list = decmial32UnSigned(value)
                    binary_text_box.insert(tk.END, f"{values_list[0]}")
                    hex_text_box.insert(tk.END, f"{values_list[1]}")
                    octal_text_box.insert(tk.END, f"{values_list[2]}")

    elif final_option[0] == "octal":
        if final_option[1] == "8":

            if final_option[2] == "signed":
                clearTextBox()
                values_list = ocotal8Signed(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                hex_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                clearTextBox()
                values_list = ocotal8UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                hex_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

        elif final_option[1] == "16":
            if final_option[2] == "signed":
                clearTextBox()
                values_list = ocotal16Signed(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                hex_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                clearTextBox()
                values_list = ocotal16UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                hex_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

        elif final_option[1] == "32":
            if final_option[2] == "signed":
                clearTextBox()
                values_list = ocotal32Signed(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                hex_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                clearTextBox()
                values_list = ocotal32UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                hex_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")


    elif final_option[0] == "hexa":
        if final_option[1] == "8":

            if final_option[2] == "signed":
                clearTextBox()
                values_list = hexa8Signed(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                octal_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                clearTextBox()
                values_list = hexa8UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                octal_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")


        elif final_option[1] == "16":
            if final_option[2] == "signed":
                clearTextBox()
                values_list = hexa16UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                octal_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                clearTextBox()
                values_list = hexa16UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                octal_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

        elif final_option[1] == "32":
            if final_option[2] == "signed":
                clearTextBox()
                values_list = hexa32Signed(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                octal_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

            elif final_option[2] == "unsigned":
                clearTextBox()
                values_list = hexa32UnSigned(value)
                binary_text_box.insert(tk.END, f"{values_list[0]}")
                octal_text_box.insert(tk.END, f"{values_list[1]}")
                decimal_text_box.insert(tk.END, f"{values_list[2]}")

result_button = tk.CTkButton(caluc_frame, command=result, text="Result", font=("Times", 15, "bold"), width=400, height=30)



# Placing
number_conversion_button_label.place(x=10, y=160)
result_button.place(x=400, y=570)



# ============================================================================================================
ascii_conversion_button_label = tk.CTkButton(caluc_frame, text="Binary Arthimatics", font=("Times", 15, "bold"),
                                             width=250, height=30, fg_color="green")
first_input_box_entry = tk.CTkEntry(caluc_frame, width=120, height=5)
second_input_box_entry = tk.CTkEntry(caluc_frame, width=120, height=5)

# Placing
ascii_conversion_button_label.place(x=690, y=160)
first_input_box_entry.place(x=690, y=200)
second_input_box_entry.place(x=820, y=200)


# Addtion :
def addition():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    first_value_binray = int(first_value, 2)
    second_value_binray = int(second_value, 2)

    addtion_value = bin((first_value_binray + second_value_binray))[2:]

    clearTextBox()
    binary_text_box.insert(tk.END, f"{addtion_value}")


addtion_button = tk.CTkButton(caluc_frame, command=addition, text="Addtions", font=("Times", 15, "bold"), width=250,
                              height=10)
addtion_button.place(x=690, y=240)


# # Substruction :
def subtraction():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    first_value_binray = int(first_value, 2)
    second_value_binray = int(second_value, 2)

    addtion_value = bin((first_value_binray - second_value_binray))[2:]

    clearTextBox()
    binary_text_box.insert(tk.END, f"{addtion_value}")


substruction_button = tk.CTkButton(caluc_frame, command=subtraction, text="Subtration", font=("Times", 15, "bold"),
                                   width=250, height=10)
substruction_button.place(x=690, y=270)


# # # Multiplication :
def multiplication():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    first_value_binray = int(first_value, 2)
    second_value_binray = int(second_value, 2)

    addtion_value = bin((first_value_binray * second_value_binray))[2:]

    clearTextBox()
    binary_text_box.insert(tk.END, f"{addtion_value}")


multiplication_button = tk.CTkButton(caluc_frame, command=multiplication, text="Multiplication",
                                     font=("Times", 15, "bold"), width=250, height=10)
multiplication_button.place(x=690, y=300)


# # # # Division :
def division():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    if second_value == '0':
        clearTextBox()
        messagebox.showerror("ZeroDivisionError", "integer division or modulo by zero")
    else :
        first_value_binray = int(first_value, 2)
        second_value_binray = int(second_value, 2)

        addtion_value = bin(first_value_binray // second_value_binray)[2:]

        clearTextBox()
        binary_text_box.insert(tk.END, f"{addtion_value}")


division_button = tk.CTkButton(caluc_frame, command=division, text="Division", font=("Times", 15, "bold"), width=250,
                               height=10)
division_button.place(x=690, y=330)


# ==================================== Complements ============================================================

complements_label = tk.CTkButton(caluc_frame, text="Complements", font=("Times", 15, "bold"), width=180, height=30,
                                 fg_color="green")
binary_entry = tk.CTkEntry(caluc_frame, width=180, height=5)

# Places :
complements_label.place(x=1090, y=160)
binary_entry.place(x=1090, y=200)

def complement(binray_value):
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
    binary_text_box.insert(tk.END, f"{binray}")

first_complement_button = tk.CTkButton(caluc_frame, command=oneComplement, text="One's Complement",
                                       font=("Times", 15, "bold"), width=180, height=50)
first_complement_button.place(x=1090, y=240)

def twoComplement():
    binray = list(binary_entry.get())
    binray = complement(binray)

    twos_comp = bin(int(binray, 2) + 1)[2:]

    clearTextBox()
    binary_text_box.insert(tk.END, f"{twos_comp}")

second_complement_button = tk.CTkButton(caluc_frame, command=twoComplement, text="Two's Complement",
                                        font=("Times", 15, "bold"), width=180, height=50)
second_complement_button.place(x=1090, y=300)
# ==================================== Complements ============================================================



caluc_page.mainloop()
