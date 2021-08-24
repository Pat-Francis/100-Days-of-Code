import tkinter

window = tkinter.Tk()
window.title("First Tkinter Window")
window.minsize(width=500, height=300)

# Create a label - label.pack() required to have item appear in the window
label = tkinter.Label(text="Hello There!", font=("Arial", 24, "bold"))
label.pack(side="left")

window.mainloop()
