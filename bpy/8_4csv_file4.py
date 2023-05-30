with open("D:\\LangKim\\py\\4612source\\CSV\\singer1.csv",'r') as f:
    with open("D:\\LangKim\\py\\4612source\\CSV\\singer2.csv",'w') as fs:
        h = f.readline()
        h = h.strip()
        hList = h.split(',')

        idx1 = hList.index('아이디')
        idx2 = hList.index('이름')
        idx3 = hList.index('평균 키')

        hList = [hList[idx1],hList[idx2],hList[idx3]]
        hStr = ','.join(map(str,hList))
        fs.write(hStr + '\n')
        for s in f :
            s = s.strip()
            rList = s.split(',')
            if int(rList[idx3]) >= 165:
                rList = [rList[idx1], rList[idx2], rList[idx3]]
                rStr = ','.join(map(str,rList))
                fs.write(rStr + '\n')

print('Save OK!')