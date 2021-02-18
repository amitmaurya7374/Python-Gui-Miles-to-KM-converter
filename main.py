from tkinter import *

window = Tk()
kilometers = 0
window.title("Miles to Km Converter")
window.minsize(height=200, width=400)
window.config(padx=20, pady=20)
# ENtry
user_input = Entry()
user_input.grid(column=2, row=0)  # issue in column

# label =
miles_label = Label(text="Miles", font=("Arial", 16, "normal"))
miles_label.grid(column=3, row=0)

is_equal_to_label = Label(text="is equal to ", font=("Arial", 16, "normal"))
is_equal_to_label.grid(column=1, row=1)

converted_result = Label(text=f"{kilometers}", font=("Arial", 16, "normal"))
converted_result.grid(column=2, row=1)
km_label = Label(text="Km", font=("Arial", 16, "normal"))
km_label.grid(column=3, row=1)


# Button
def caluclate():
    """Convert miles to Km"""
    print("Convert miles to Km")


button = Button(text="calculate", command=caluclate)
button.grid(column=2, row=3)
window.mainloop()
