
a = 20 #전역변수
def func():
    a = 10 #지역변수
    print(a)

func()
print(a)
