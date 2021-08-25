from tkinter import *

# Create Tk window
window = Tk()
window.title("Miles to KM converter")
# window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# Function to run when the calculate button is clicked
def calculate_kilometres():
    miles = float(miles_entry.get())
    km = miles * 1.609
    calculated_kilometers.config(text=f"{km}")


# Entry to accept input from the user
miles_entry = Entry(text=0)
miles_entry.grid(column=1, row=0)
miles_entry.config(width=10)

# 'Miles' label
is_equal_to = Label(text="Miles")
is_equal_to.grid(column=2, row=0)

# 'is equal to' label
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Kilometer value
calculated_kilometers = Label(text=round(float(0)))
calculated_kilometers.grid(column=1, row=1)

# 'Kilometers' label
is_equal_to = Label(text="Km")
is_equal_to.grid(column=2, row=1)

# Calculate button
calculate = Button(text="Calculate", command=calculate_kilometres)
calculate.grid(column=1, row=2)

window.mainloop()