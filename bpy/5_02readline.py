f = open("D:\\LangKim\\py\\bpy\\txt\\c.txt",'w')
f.write("동해물과 백두산이 마르고 닳도록\n안녕하세요.\nHello World!!")
f.close()

f=open("D:\\LangKim\\py\\bpy\\txt\\c.txt",'rt')
lines = f.readlines()
for line in lines:
  print(line, end='')
f.close()