x = int(input("줄수입력: "))
for i in range(1,x+1):
  for j in range(i):
    print("@", end='')
  print()

"""
def starW(i):
  if i==6:
    return
  print("@"*i)
  i = i+1
  starW(i)

starW(1)

@
@@
@@@
@@@@
@@@@@
"""
"""
*****
****
***
**
*
"""