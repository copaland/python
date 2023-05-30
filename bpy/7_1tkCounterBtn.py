# 예제 3) 버튼 클릭시 실행될 이벤트(함수) 설정
from tkinter import *
from tkinter.font import *

tk = Tk()

# 다른 함수 정의(버튼 누를때마다 카운트를 세는 함수)
counter = 0
def countUp():
    global counter #전역변수 counter
    counter += 1
    label1['text'] = '카운트 : ' + str(counter)

def countDn():
    global counter #전역변수 counter
    counter -= 1
    label1['text'] = '카운트 : ' + str(counter)

# 리셋 함수(카운트 초기화)
def reset():
    global counter
    counter = 0
    label1['text'] = '버튼을 누르세요.'
## GUI 구성(텍스트,버튼) ##

# 창 이름 설정
tk.title('GUI카운트') 

# 텍스트 font = Font(size = 30)
label1=Label(tk, text='카운트 : ',fg='blue',font=("나눔고딕",30)) # fg는 글자 색 지정, font로 글자 설정
label1.pack(padx=10, pady=10)
# 버튼1
button3 = Button(tk,text='증가',bg='yellow',font = Font(size = 20),width=10,height=5,command= countUp) #command로 버튼 클릭 시 동작할 함수 지정, bg로 색상지정, width,height로 각각 넓이 높이 지정
button3.pack(side=LEFT, padx=5, pady=5)
# 버튼2
button4 = Button(tk,text='리셋',bg='red',width=10,height=5,font = Font(size = 20),command=reset)
button4.pack(side=LEFT,padx=5, pady=5)
# 버튼3
button3 = Button(tk,text='감소',bg='cyan',font = Font(size = 20),width=10,height=5,command= countDn) #command로 버튼 클릭 시 동작할 함수 지정, bg로 색상지정, width,height로 각각 넓이 높이 지정
button3.pack(side=LEFT, padx=5, pady=5)
tk.mainloop()