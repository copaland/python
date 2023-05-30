from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지 너무 귀엽죠^^")

tk = Tk()
photo = PhotoImage(file="D:\\py\\dog.png")
#button1 = Button(tk, text="파이썬 종료", fg="blue", bg="yellow", command=quit)
button1 = Button(tk, image=photo, command=myFunc)

button1.pack()
tk.mainloop()