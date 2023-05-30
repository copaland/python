x = int(input("줄수입력: "))
for i in range(1,x+1):
  for j in range(x+1-i):
    print("@", end='')
  print()
"""
@@@@@
@@@@
@@@
@@
@
"""