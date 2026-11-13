from tkinter import *
from tkinter import messagebox
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
result = num1 * num2

def the_answer():
    user_answer = int(answer_entry.get())

    if user_answer == result:
            messagebox.showinfo("info", "Correct! You are a Math Whiz!")
    else:
        messagebox.showerror("error","Wrong! The answer was {}".format(result))


root = Tk()
root.title("Math Whiz")

messagebox.showinfo("info", f"Guess the product of {num1} and {num2}!")

question = Label(root, text=f"What is {num1} × {num2}?")
question.pack(pady=10)

answer_entry = Entry(root)
answer_entry.pack(pady=5)

submit_button = Button(root, text="Submit", command=the_answer)
submit_button.pack(pady=10)

root.mainloop()
