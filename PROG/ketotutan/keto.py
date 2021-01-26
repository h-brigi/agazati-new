# coding: utf8
# Nagy János, 2020-11-26, esti szoft1

print('Nagy János, 2020-11-26, esti szoft1')
print('Feladat 1607 megoldása')
print('Dolgozók adatainak feldolgozása')
print()
print('{:20}{:10}'.format("Név", "Fizetés"))
print('------------------------------------')

fp = open('dolgozok.txt', 'r', encoding='utf-8')

# a mező nevek kiolvasása
fp.readline()  

# az első dolgozó beolvasása
line = fp.readline()
while line != '':
        lineList = line.split(';')        
        belepesIdeje = lineList[7];
        belepesIdejeList = belepesIdeje.split('-')
        belepesEve = belepesIdejeList[0]
        belepesEve = belepesEve.replace('"', '')
        if int(belepesEve) > 2005:
            print('{:20}{:10}'.format(lineList[1], lineList[5]))
        line = fp.readline()
fp.close()
