###예제4) ft -> cm로 바꾸는 단위 변환기 만들기
# Entry: input과 비슷한 역할 (사용자가 입력한 내용 전달)
# get: Entry를 사용한 입력 내용 가져올 수 있다.
# delete: 사용자 입력 삭제
# Frame: 컨테이너, 창 안에 프레임 생성
# grid: 격자 배치
from tkinter import *
tk = Tk()
tk.title('길이 변환기')
def Ft2Cm():
    ft2cm = entry1.get()
    entry2.delete(0,"end")
    entry2.insert(0,round(float(ft2cm)*30.48,4))
def Cm2Ft():
    cm2ft = entry2.get()
    entry1.delete(0,"end")
    entry1.insert(0,round(float(cm2ft)/30.48,4))

label1 = Label(tk,text='피트(ft)').grid(row=0, column=0)
label2 = Label(tk,text='센티미터(cm)').grid(row=1,column=0)

# 각 단위 입력받는 부분 만들기
entry1 = Entry(tk)
entry2 = Entry(tk)


entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

btn1 = Button(tk,text='ft->cm',bg='black',fg='white',command=Ft2Cm).grid(row=2,column=0)
btn2 = Button(tk,text='cm->ft',bg='black',fg='white',command=Cm2Ft).grid(row=2,column=1)

tk.mainloop()