from tkinter import *
window = Tk()

window.title("강아지 사진")
photo = PhotoImage(file = "D:\\py\\dog.png" )
photo2 = PhotoImage(file = "D:\\py\\cat.png" )
label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)
label1.pack(side=LEFT)
label2.pack(side=RIGHT)
window.mainloop()