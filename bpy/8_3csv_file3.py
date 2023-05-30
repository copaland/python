def printList(pList) :
    for data in pList :
        print(data, end='\t')
    print()

with open("D:\\LangKim\\py\\4612source\\CSV\\singer1.csv",'r') as f :
#    header = f.readline()
#    header = header.strip()
#    headerList = header.split(',')
#    printList(headerList)
    for s in f:
        s = s.strip() #공백, \n 없애줌
        rowList = s.split(',') #문자열을 리스트로
        printList(rowList)