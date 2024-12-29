#A simple interactive resistor calculator using Python

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_resistance():
    color_code = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6, "violet": 7,
        "gray": 8, "white": 9
    }

    multiplier_values = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000,
        "yellow": 10000, "green": 100000, "blue": 1000000,
        "violet": 10000000, "gray": 100000000, "white": 1000000000
    }

    tolerance_values = {
        "brown": "±1%", "red": "±2%", "green": "±0.5%",
        "blue": "±0.25%", "violet": "±0.1%", "gray": "±0.05%",
        "gold": "±5%", "silver": "±10%"
    }

    band1 = band1_var.get().lower()
    band2 = band2_var.get().lower()
    multiplier = multiplier_var.get().lower()
    tolerance = tolerance_var.get().lower()

    if band1 not in color_code or band2 not in color_code or multiplier not in multiplier_values or tolerance not in tolerance_values:
        messagebox.showerror("Invalid Input", "Please select valid resistor colors.")
        return

    digit1 = color_code[band1]
    digit2 = color_code[band2]
    resistance_value = (digit1 * 10 + digit2) * multiplier_values[multiplier]

    if resistance_value >= 1e6:
        result = f"{resistance_value / 1e6} MΩ"
    elif resistance_value >= 1e3:
        result = f"{resistance_value / 1e3} kΩ"
    else:
        result = f"{resistance_value} Ω"

    tolerance_result = tolerance_values[tolerance]
    # Display the result
    result_label.config(text=f"Resistance: {result} {tolerance_result}")


root = tk.Tk()
root.title("Resistor Calculator")
root.geometry("400x400")

style = ttk.Style(root)
style.theme_use("clam")

color_options = [
    "Black", "Brown", "Red", "Orange", "Yellow",
    "Green", "Blue", "Violet", "Gray", "White"
]
tolerance_options = [
    "Brown", "Red", "Green", "Blue", "Violet", "Gray", "Gold", "Silver"
]

ttk.Label(root, text="Band 1 (First Digit):").pack(pady=5)
band1_var = tk.StringVar(value="Black")
ttk.Combobox(root, textvariable=band1_var, values=color_options, state="readonly").pack()

ttk.Label(root, text="Band 2 (Second Digit):").pack(pady=5)
band2_var = tk.StringVar(value="Black")
ttk.Combobox(root, textvariable=band2_var, values=color_options, state="readonly").pack()

ttk.Label(root, text="Multiplier:").pack(pady=5)
multiplier_var = tk.StringVar(value="Black")
ttk.Combobox(root, textvariable=multiplier_var, values=color_options, state="readonly").pack()

ttk.Label(root, text="Tolerance:").pack(pady=5)
tolerance_var = tk.StringVar(value="Gold")
ttk.Combobox(root, textvariable=tolerance_var, values=tolerance_options, state="readonly").pack()

ttk.Button(root, text="Calculate", command=calculate_resistance).pack(pady=10)

result_label = ttk.Label(root, text="Resistance: ", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
