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
        s = s.strip() #����, \n ������
        rowList = s.split(',') #���ڿ��� ����Ʈ��
        printList(rowList)