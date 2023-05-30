#버튼
from tkinter import *

tk = Tk()
tk.geometry("300x200")
button1 = Button(tk, text="파이썬 종료", fg="blue", bg="yellow", command=quit)
button1.pack()

tk.mainloop()