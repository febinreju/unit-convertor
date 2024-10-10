import tkinter as tk
from tkinter import ttk
def convert_units():
    unit_type = unit_type_combo.get()
    value = float(entry_value.get())

    if unit_type == "METERS TO KILOMETERS":
        result = value / 1000
    elif unit_type == "KILOMETERS TO MILES":
        result = value * 0.621371
    elif unit_type == "MILES TO FEET":
        result = value * 5280
    elif unit_type == "FEET TO METERS":
        result = value * 0.3048
    elif unit_type == "GRAMS TO KILOGRAMS":
        result = value / 1000
    elif unit_type == "KILOGRAMS TO POUNDS":
        result = value * 2.20462
    elif unit_type == "POUNDS TO GRAMS":
        result = value * 453.592
    elif unit_type == "CELSIUS TO FAHRENHEIT":
        result = (value * 9 / 5) + 32
    elif unit_type == "FAHRENHEIT TO CELSIUS":
        result = (value - 32) * 5 / 9
    elif unit_type == "CELSIUS TO KELVIN":
        result = value + 273.15
    else:
        result = "INVALID SELECTION"

    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Unit Converter App")

# Create the UI components
label_instructions = tk.Label(root, text="Select conversion and enter value:")
label_instructions.pack(pady=10)

unit_types = [
    "METERS TO KILOMETERS", "KILOMETERS TO MILES", "MILES TO FEET", "FEET TO METERS",
    "GRAMS TO KILOGRAMS", "KILOGRAMS TO POUNDS", "POUNDS TO GRAMS",
    "CELSIUS TO FAHRENHEIT", "FAHRENHEIT TO CELSIUS", "CELSIUS TO KELVIN"
]

unit_type_combo = ttk.Combobox(root, values=unit_types)
unit_type_combo.set("Select conversion")
unit_type_combo.pack(pady=10)

entry_value = tk.Entry(root)
entry_value.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=20)

# Run the application
root.mainloop()
