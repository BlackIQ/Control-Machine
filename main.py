import fontawesome as fa
import tkinter as tk
import pyfirmata
import time
import tkinter.messagebox as tkmsbx

white = 13
green = 12
blue = 11
red = 10

board = pyfirmata.Arduino('/dev/ttyACM0')

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
    board.digital[white].write(1)

up = tk.Button(
    master=frame,
    text=fa.icons["arrow-up"],
    fg="black",
    command=go_up
).grid(row=1, column=1)

def go_left():
    board.digital[green].write(1)

left = tk.Button(
    master=frame,
    text=fa.icons["arrow-left"],
    fg="black",
    command=go_left
).grid(row=2, column=0)

def go_right():
    board.digital[blue].write(1)

right = tk.Button(
    master=frame,
    text=fa.icons["arrow-right"],
    fg="black",
    command=go_right
).grid(row=2, column=2)

def go_down():
    board.digital[red].write(1)

down = tk.Button(
    master=frame,
    text=fa.icons["arrow-down"],
    fg="black",
    command=go_down
).grid(row=3, column=1)

window.mainloop()