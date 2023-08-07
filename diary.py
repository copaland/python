# 일기 작성하는 함수 선언
def add():
    day=input("날짜 입력(ex 2023. 8. 23) : ") # 날짜 입력
    weather=input("날씨 입력 : ")            # 날씨 입력
    day=day+" "                        # 빈 문자열 추가
    weather=weather+"\n"               # 한 줄 내림 문자열 추가
    text=day+weather            # 날씨와 요일을 text 변수에 저장
    diary_text=input("일기 쓰기 : ")    # 일기장 작성
    text=text+diary_text               # 모든 글을 저장
    return text                        # text 값 반환
# 일기를 수정하는 함수 선언
def modify(text):                      # 일기장 수정 함수
    print("저장된 일기")                 # 출력
    print(text)                        # text 값 출력
    print("일기를 다시 입력하세요 \n")    # 출력
    modify_diary=add()                 # add()함수 호출
    return modify_diary                # modify_diary 값 반환
# 일기 삭제하는 함수 선언
def delete(text):
    print("작성된 일기")         # 작성된 일기 출력
    print(text)                 # text 값 출력
    print("")                   # 1번과 2번 선택에 관한 내용 출력
    print("작성된 일기 삭제는 1번, 다시 돌아가기는 2번을 선택하시오.:")
         # 삭제를 할 경우 1번, 다시 돌아가기 위해서는 2번을 입력 받음
    select=int(input(""))
    if(select==1):       # 선택이 1일 경우 빈 문자를 저장한 후 리턴
        text=""
        return text
    else:                # 2일 경우 다시 원 상태로 리턴
        return text
# 일기장 프로그램의 실행
diary=""                   # 일기를 저장할 수 있는 변수
while True: # 반복문으로 일기를 입력, 수정, 삭제, 출력할 수 있음
    print("일기장 프로그램") # 출력
    print("(일기장 프로그램 주의 사항: 입력 시 숫자 이외의 문자를 입력할 경우 오류가 발생하며, 5 이상의 숫자를 입력할 경우 종료)") # 출력
    print("1. 일기 입력 2. 일기 수정 3. 일기 삭제 4. 일기 출력 5. 종료") # 출력
    select=int(input())    # 일기장 프로그램 선택
    if(select==1):          # 값이 1인 경우
        diary=add()         # 일기 작성
    elif(select==2):        # 값이 2인 경우
        diary=modify(diary) # 일기 수정
    elif(select==3):        # 값이 3인 경우
        diary=delete(diary) # 일기 삭제
    elif(select==4):        # 값이 4인 경우
        print(diary)        #일기 출력
    else:
        break
