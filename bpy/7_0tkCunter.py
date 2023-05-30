from tkinter import *
from tkinter.font import *

#카운터 클래스 생성
class Counting:
    cnt = 0
    #카운터 창 생성
    def __init__(self, counter):
        #Window setting
        counter.title("카운터 프로그램")
        counter.geometry("300x150+100+100")
        counter.resizable(False, False)
        self.contents(counter)
        count.insert(0, 0)
        count.bind("<Return>", self.getEnter)
        
    #버튼을 누르면 카운트 업 되는 메소드
    def countUp(self):
        self.cnt += 1
        count.delete(0, 12)
        count.insert(0, self.cnt)
        return self.cnt
    
    #버튼을 누르면 카운트 다운 되는 메소드
    def countDown(self):
        self.cnt -= 1
        if(self.cnt <= 0):
            self.cnt = 0
        count.delete(0, 12)
        count.insert(0, self.cnt)
        return self.cnt
        
    #버튼을 누르면 초기화 되는 메소드
    def reset(self):
        self.cnt = 0
        count.delete(0, 12)
        count.insert(0, self.cnt)
        return self.cnt
    #엔터 입력하면 값으로 설정
    def getEnter(self, enter):
        self.enter = count.get()
        self.cnt = int(count.get())
    #윈도우 창 설정
    def contents(self, counter):
        #Tkinter window
        text = Label(counter, text = "숫자 카운터 프로그램", font = Font(size = 20))
        global count
        count = Entry(counter, width = 12, justify = "right", font = Font(size = 30))
        upCounter = Button(counter, text = "증가", font = Font(size = 20), command = self.countUp)
        downCounter = Button(counter, text = "감소", font = Font(size = 20), command = self.countDown)
        counterReset = Button(counter, text = "초기화", font = Font(size = 20), command = self.reset)
        #Window initialize
        text.place(x = 20, y = 0)
        count.place(x = 0, y = 30)
        upCounter.place(x = 0, y = 80, width = 100, height = 70)
        downCounter.place(x = 100, y = 80, width = 100, height = 70)
        counterReset.place(x = 200, y = 80, width = 100, height = 70)

    
def main():
    counter = Tk()
    Count = Counting(counter)
    counter.mainloop()

if __name__ == '__main__':
    main()
