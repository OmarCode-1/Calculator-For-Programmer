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


# ----------------- Text Box ----------------- :

sys_choose = tk.StringVar(caluc_frame, 'binary')

sys_values = {"Binary": 'binary',
              "Decimal": 'decimal',
              "Octal": 'octal',
              "Hexa": 'hex'
             }
x = 200
for (text, value) in sys_values.items():
    tk.CTkRadioButton(caluc_frame, text=text, variable=sys_choose, value=value).place(x=20, y=x)
    x += 30

# ----------------- Number Conversation ----------------- :
byte_choose = tk.StringVar(caluc_frame, 8)


# Dictionary to create multiple buttons
bytes_values = {"8 Bits": '8',
                  "16 Bits": '16',
                  "32 Bits": '32'
                  }
x = 200
for (text, value) in bytes_values.items():
    tk.CTkRadioButton(caluc_frame, text=text, variable=byte_choose, value=value).place(x=120, y=x)
    x += 30


# =================================================

sgn_choose = tk.StringVar(caluc_frame, "signed")

# Dictionary to create multiple buttons
sgn_values = {"Signed": "signed",
                "UnSigned": "unsigned",
                }
x = 200
for (text, value) in sgn_values.items():
    tk.CTkRadioButton(caluc_frame, text=text, variable=sgn_choose, value=value).place(x=220, y=x)
    x += 30




number_conversion_button_label = tk.CTkButton(caluc_frame, text="Number Conversion", font=("Times", 15, "bold"),
                                              width=500, height=30, fg_color="green")



binary_var = tk.StringVar()
decimal_var = tk.StringVar()
octal_var = tk.StringVar()
hex_var = tk.StringVar()


binary_entry = tk.CTkEntry(caluc_frame, textvariable=binary_var, width=200, height=10)
binray_label = tk.CTkLabel(caluc_frame, text="Binary", font=("Times", 15, "bold"))

decimal_entry = tk.CTkEntry(caluc_frame, textvariable=decimal_var, width=200, height=10)
decimal_label = tk.CTkLabel(caluc_frame, text="Decimal", font=("Times", 15, "bold"))

octal_entry = tk.CTkEntry(caluc_frame, textvariable=octal_var, width=200, height=10)
octal_label = tk.CTkLabel(caluc_frame, text="HEX", font=("Times", 15, "bold"))

hex_entry = tk.CTkEntry(caluc_frame, textvariable=hex_var, width=200, height=10)
hex_label = tk.CTkLabel(caluc_frame, text="Octal", font=("Times", 15, "bold"))

# Placing :
binray_label.place(x=35, y=450)
binary_entry.place(x=30, y=480)

decimal_label.place(x=335, y=450)
decimal_entry.place(x=330, y=480)

octal_label.place(x=635, y=450)
octal_entry.place(x=630, y=480)

hex_label.place(x=935, y=450)
hex_entry.place(x=930, y=480)




def binary(*args):
    try :
        if len(binary_entry.get()) > 0:
            final_option = [byte_choose.get(), sgn_choose.get()]
            value = binary_entry.get()
            if byte_choose.get() == "8":
                value = value.zfill(8)
            elif byte_choose.get() == "16":
                value = value.zfill(16)
            elif byte_choose.get() == "32":
                value = value.zfill(32)
            print(value)
            if int(value) == -1:
                messagebox.showerror("Error", "You entered -1")
            if final_option[1] == 'signed' :
                values_list = binarySigned(value)
                decimal_var.set(f"{values_list[0]}")
                octal_var.set(f"{values_list[1]}")
                hex_var.set(f"{values_list[2]}")
            else :
                values_list = binaryUnsigned(value)
                decimal_var.set(f"{values_list[0]}")
                octal_var.set(f"{values_list[1]}")
                hex_var.set(f"{values_list[2]}")
        else :
            decimal_entry.delete(0, tk.END)
            octal_entry.delete(0, tk.END)
            hex_entry.delete(0, tk.END)
    except ValueError:
        pass

def decimal(*args):
    try:
        if len(decimal_entry.get()) > 0:
            final_option = [byte_choose.get(), sgn_choose.get()]
            value = decimal_entry.get()
            value = int(value)
            if final_option[0] == "8":
                if final_option[1] == "signed":
                    if value < -128 or value > 127:
                        messagebox.showerror("Error", "Decimal number is out of range for a signed 8-bit number")
                    else:
                        values_list = decmial8Signed(value)
                        binary_var.set(f"{values_list[0]}")
                        hex_var.set( f"{values_list[1]}")
                        octal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    if value < 0 or value > 255:
                        messagebox.showerror("Error", "Decimal number is out of range for an unsigned 8-bit number")
                    else:
                        values_list = decmial8UnSigned(value)
                        binary_var.set(f"{values_list[0]}")
                        hex_var.set(f"{values_list[1]}")
                        octal_var.set(f"{values_list[2]}")

            elif final_option[0] == "16":
                if final_option[1] == "signed":
                    if value < -32768 or value > 32767:
                        messagebox.showerror("Error", "Decimal number is out of range for a signed 16-bit number")
                    else:
                        values_list = decmial16Signed(value)
                        binary_var.set(f"{values_list[0]}")
                        hex_var.set(f"{values_list[1]}")
                        octal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    if value < 0 or value > 65535:
                        messagebox.showerror("Error", "Decimal number is out of range for an unsigned 16-bit number")
                    else:

                        values_list = decmial16UnSigned(value)
                        binary_var.set(f"{values_list[0]}")
                        hex_var.set(f"{values_list[1]}")
                        octal_var.set(f"{values_list[2]}")
            elif final_option[0] == "32":
                if final_option[1] == "signed":
                    if value < -2147483648 or value > 2147483647:
                        messagebox.showerror("Error", "Decimal number is out of range for a signed 32-bit number")
                    else:
                        values_list = decmial32Signed(value)
                        binary_var.set(f"{values_list[0]}")
                        hex_var.set(f"{values_list[1]}")
                        octal_var.set(f"{values_list[2]}")
                elif final_option[1] == "unsigned":
                    if value < 0 or value > 4294967295:
                        messagebox.showerror("Error", "Decimal number is out of range for an unsigned 32-bit number")
                    else:
                        values_list = decmial32UnSigned(value)
                        binary_var.set(f"{values_list[0]}")
                        hex_var.set(f"{values_list[1]}")
                        octal_var.set(f"{values_list[2]}")
        else:
            binary_entry.delete(0, tk.END)
            octal_entry.delete(0, tk.END)
            hex_entry.delete(0, tk.END)
    except ValueError:
        pass



def octal(*args):
    try:
        if len(octal_entry.get()) > 0:
            final_option = [byte_choose.get(), sgn_choose.get()]
            value = octal_entry.get()
            if final_option[0] == "8":

                if final_option[1] == "signed":
                    values_list = ocotal8Signed(value)
                    binary_var.set(f"{values_list[0]}")
                    hex_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    values_list = ocotal8UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    hex_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

            elif final_option[0] == "16":
                if final_option[1] == "signed":
                    values_list = ocotal16Signed(value)
                    binary_var.set(f"{values_list[0]}")
                    hex_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    values_list = ocotal16UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    hex_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

            elif final_option[0] == "32":
                if final_option[1] == "signed":
                    values_list = ocotal32Signed(value)
                    binary_var.set(f"{values_list[0]}")
                    hex_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    values_list = ocotal32UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    hex_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")
        else:
            binary_entry.delete(0, tk.END)
            decimal_entry.delete(0, tk.END)
            hex_entry.delete(0, tk.END)
    except :
        pass


def hexa(*args):
    try:
        if len(hex_entry.get()) > 0:
            final_option = [byte_choose.get(), sgn_choose.get()]
            value = hex_entry.get()
            if final_option[0] == "8":

                if final_option[1] == "signed":
                    values_list = hexa8Signed(value)
                    binary_var.set(f"{values_list[0]}")
                    octal_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    values_list = hexa8UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    octal_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")


            elif final_option[0] == "16":
                if final_option[1] == "signed":
                    values_list = hexa16UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    octal_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    values_list = hexa16UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    octal_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

            elif final_option[0] == "32":
                if final_option[1] == "signed":
                    values_list = hexa32Signed(value)
                    binary_var.set(f"{values_list[0]}")
                    octal_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")

                elif final_option[1] == "unsigned":
                    values_list = hexa32UnSigned(value)
                    binary_var.set(f"{values_list[0]}")
                    octal_var.set(f"{values_list[1]}")
                    decimal_var.set(f"{values_list[2]}")
        else:
            binary_entry.delete(0, tk.END)
            decimal_entry.delete(0, tk.END)
            octal_entry.delete(0, tk.END)
    except:
        pass



def update(*args):

    choose = sys_choose.get()
    if choose == 'binary':
        binary()
    elif choose == 'decimal':
        decimal()
    elif choose == 'octal':
        octal()
    elif choose == 'hex':
        hexa()

def clear():
    binary_entry.delete(0, tk.END)
    decimal_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)
    octal_entry.delete(0, tk.END)






# Placing
number_conversion_button_label.place(x=10, y=160)




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

    clear()
    binary_var.set(f"{addtion_value}")


addtion_button = tk.CTkButton(caluc_frame, command=addition, text="Addtions", font=("Times", 15, "bold"), width=250,
                              height=10)
addtion_button.place(x=690, y=240)


# # Substruction :
def subtraction():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    first_value_binray = int(first_value, 2)
    second_value_binray = int(second_value, 2)

    subtraction_value = bin((first_value_binray - second_value_binray))[2:]

    clear()
    binary_var.set(f"{subtraction_value}")


substruction_button = tk.CTkButton(caluc_frame, command=subtraction, text="Subtration", font=("Times", 15, "bold"),
                                   width=250, height=10)
substruction_button.place(x=690, y=270)


# # # Multiplication :
def multiplication():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    first_value_binray = int(first_value, 2)
    second_value_binray = int(second_value, 2)

    multiplication_value = bin((first_value_binray * second_value_binray))[2:]

    clear()
    binary_var.set(f"{multiplication_value}")


multiplication_button = tk.CTkButton(caluc_frame, command=multiplication, text="Multiplication",
                                     font=("Times", 15, "bold"), width=250, height=10)
multiplication_button.place(x=690, y=300)


# # # # Division :
def division():
    first_value = first_input_box_entry.get()
    second_value = second_input_box_entry.get()

    if second_value == '0':
        clear()
        messagebox.showerror("ZeroDivisionError", "integer division or modulo by zero")
    else :
        first_value_binray = int(first_value, 2)
        second_value_binray = int(second_value, 2)

        division_value = bin(first_value_binray // second_value_binray)[2:]

        clear()
        binary_var.set(f"{division_value}")


division_button = tk.CTkButton(caluc_frame, command=division, text="Division", font=("Times", 15, "bold"), width=250,
                               height=10)
division_button.place(x=690, y=330)


# ==================================== Complements ============================================================

complements_label = tk.CTkButton(caluc_frame, text="Complements", font=("Times", 15, "bold"), width=180, height=30,
                                 fg_color="green")

binary2_entry = tk.CTkEntry(caluc_frame, width=180, height=5)

# Places :
complements_label.place(x=1090, y=160)
binary2_entry.place(x=1090, y=200)

def complement(binray_value):
    # Flip each bit
    for i in range(len(binray_value)):
        if binray_value[i] == '0':
            binray_value[i] = '1'
        else:
            binray_value[i] = '0'

    return ''.join(binray_value)

def oneComplement():
    try :
        binray = list(binary2_entry.get())

        binray = complement(binray)

        clear()
        binary_var.set(f"{binray}")
    except:
        pass
first_complement_button = tk.CTkButton(caluc_frame, command=oneComplement, text="One's Complement",
                                       font=("Times", 15, "bold"), width=180, height=50)
first_complement_button.place(x=1090, y=240)

def twoComplement():
    try :
        binray = list(binary2_entry.get())
        binray = complement(binray)

        twos_comp = bin(int(binray, 2) + 1)[2:]

        clear()
        binary_var.set(f"{twos_comp}")
    except:
        pass
second_complement_button = tk.CTkButton(caluc_frame, command=twoComplement, text="Two's Complement",
                                        font=("Times", 15, "bold"), width=180, height=50)
second_complement_button.place(x=1090, y=300)

# ==================================== Complements ============================================================
binary_var.trace_add('write', update)

decimal_var.trace_add('write', update)

octal_var.trace_add('write', update)

hex_var.trace_add('write', update)
caluc_page.mainloop()
