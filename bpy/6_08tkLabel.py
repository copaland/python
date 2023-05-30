from tkinter import *

window = Tk()
window.title("레이블")
label1 = Label(window, text="안녕하세요! 김랑기 입니다.")
label2 = Label(window, text="Python<br>Korea", font=("궁서체",30),fg="red")
label3 = Label(window, text="Love is", bg="yellow", width=20,height=5, anchor=NE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()