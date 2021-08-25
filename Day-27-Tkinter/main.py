from tkinter import *

window = Tk()
window.title("First Tkinter Window")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    print("Button Clicked!")
    new_text = entry.get()
    label.config(text=new_text)


# Create a label - label.pack() required to have item appear in the window
label = Label(text="Hello There!", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
label.config(padx=50, pady=50)
# New button
new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Create a button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

# Entry (input)
entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
