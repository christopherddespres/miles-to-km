from tkinter import *


def calculate_button_clicked():
    miles = float(miles_entry.get())
    km = round(miles * 1.6, 2)
    calculated_label.config(text=km)


# Create window
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

# Create text entry
# miles_entry
miles_entry = Entry(width=10, font=("Arial", 20,), justify=CENTER)
miles_entry.grid(row=1, column=1)

# Create labels
# title_label
title_label = Label(text="Mile to KM Converter Tool", font=("Arial", 20, "bold"))
title_label.grid(row=0, columnspan=3)
title_label.config(pady=30)

# is_equal_to_label
is_equal_to_label = Label(text="is equal to: ", font=("Arial", 20))
is_equal_to_label.grid(row=2, column=0)
is_equal_to_label.config(padx=3, pady=3)

# miles_label
miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(row=1, column=2)
miles_label.config(padx=3, pady=3)

# km_label
km_label = Label(text="Km", font=("Arial", 20))
km_label.grid(row=2, column=2)
km_label.config(padx=3, pady=3)

# calculated_label
calculated_label = Label(text="0", font=("Arial", 20))
calculated_label.grid(row=2, column=1)
calculated_label.config(padx=3, pady=3)

# Create buttons
# calculate_button
calculate_button = Button(text="Calculate", font=("Arial", 20), command=calculate_button_clicked)
calculate_button.grid(row=3, column=1)
calculate_button.config(padx=3, pady=3)


window.mainloop()
