import tkinter

window = tkinter.Tk()
window.title("Laura's Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


#Label
my_label = tkinter.Label(text="I Love the Baby", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="I love the Baby the Most")
# my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
def button_clicked():
    print("And she loves me")
    new_text = input.get()
    my_label.config(text="And she loves me")

button = tkinter.Button(text="Still Love the baby", command=button_clicked)
button.pack()
# button.grid(column=1, row=1)

new_button = tkinter.Button(text="Laura")
# new_button.grid(column=2, row=0)
button.pack()

#Entry
input =tkinter.Entry(width=10)
print(input.get())
# input.grid(column=3, row=2)

input.pack()



window.mainloop()
