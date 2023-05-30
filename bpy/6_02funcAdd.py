c = 0
def add(a,b):
    "두개의 변수를 받아 더하는 함수"
    global c
    c = a+b
    # print(c) #pass

def addr(a,b):
    return a+b

add(10,20)
print(c)
print("------------")
y = addr(10,20)
print(y)