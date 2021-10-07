import fontawesome as fa
import tkinter as tk
import tkinter.messagebox as tkmsbx

window = tk.Tk()

window.title("Car controller")
window.configure(background="white")
window.geometry("250x250")
window.resizable(False, False)

br = tk.Label(
    text="",
    foreground="black",
    background="white",
    font=50
).pack()

heading = tk.Label(
    text="Car controller",
    foreground="black",
    background="white",
    font=50
).pack()

text = tk.Label(
    text="Control the car with this pad",
    foreground="black",
    background="white",
).pack()

br = tk.Label(
    text="",
    foreground="black",
    background="white",
    font=50
).pack()

frame = tk.Frame(master=window, width=2, height=2, bg="white")
frame.pack()

def go_up():
   tkmsbx.showinfo("Up", "Go up")

up = tk.Button(
    master=frame,
    text=fa.icons["arrow-up"],
    fg="black",
    command=go_up
).grid(row=1, column=1)

def go_left():
   tkmsbx.showinfo("Left", "Go left")

left = tk.Button(
    master=frame,
    text=fa.icons["arrow-left"],
    fg="black",
    command=go_left
).grid(row=2, column=0)

def go_right():
   tkmsbx.showinfo("Right", "Go right")

right = tk.Button(
    master=frame,
    text=fa.icons["arrow-right"],
    fg="black",
    command=go_right
).grid(row=2, column=2)

def go_down():
   tkmsbx.showinfo("Down", "Go down")

down = tk.Button(
    master=frame,
    text=fa.icons["arrow-down"],
    fg="black",
    command=go_down
).grid(row=3, column=1)

window.mainloop()