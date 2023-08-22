import random

def number_guessing_game():
    random_number = random.randint(1, 50)
    attempts = 0

    print("숫자 맞추기 게임\n")
    print("─────")
    print("1에서 50 이하의 숫자만 입력하세요.")
    print("숫자를 맞출 수 있는 기회는 10번 입니다.\n")

    while attempts < 10:
        guess_number = int(input("숫자 입력 : "))
        attempts += 1

        if guess_number > random_number:
            print("입력한 숫자가 정답보다 큽니다.")
            print("숫자를 다시 입력하세요.")
            print("─────")
        elif guess_number < random_number:
            print("입력한 숫자가 정답보다 작습니다.")
            print("숫자를 다시 입력하세요.")
            print("─────")
        else:
            print("정답!")
            print("─────")
            print(f"축하!! 정답입니다. {attempts}번만에 숫자를 찾으셨군요.^^")
            break

    if attempts == 10 and guess_number != random_number:
        print("10번의 기회가 끝났습니다.")
        print("프로그램을 종료합니다.")

number_guessing_game()
