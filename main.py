import fontawesome as fa
import tkinter as tk

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

# br = tk.Label(
#     text="",
#     foreground="black",
#     background="white",
#     font=50
# ).pack()

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

up = tk.Button(
    master=frame,
    text=fa.icons["arrow-up"],
    fg="black"
).grid(row=1, column=1)

left = tk.Button(
    master=frame,
    text=fa.icons["arrow-left"],
    fg="black"
).grid(row=2, column=0)

right = tk.Button(
    master=frame,
    text=fa.icons["arrow-right"],
    fg="black"
).grid(row=2, column=2)

left = tk.Button(
    master=frame,
    text=fa.icons["arrow-down"],
    fg="black"
).grid(row=3, column=1)

window.mainloop()