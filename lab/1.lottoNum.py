# 로또 번호 생성

import random

def generate_lotto_numbers():
    return random.sample(range(1, 46), 6)

lotto = generate_lotto_numbers()
print("로또번호: {}".format(lotto))
