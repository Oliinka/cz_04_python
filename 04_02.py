def

def znamky(seznam):
    novy_seznam = []

    for znamka in seznam:
        if znamka == 1:
            novy_seznam.append("vyborny")
        elif znamka == 2:
            novy_seznam.append("vyborny")
        elif znamka == 3:
            novy_seznam.append("vyborny")
        elif znamka == 4:
            novy_seznam.append("vyborny")
        elif znamka == 5:
            novy_seznam.append("vyborny")
        else:
            novy_seznam.append("error")

    
    return novy_seznam
hodnoceni = [1, 2, 3, 4, 5]
print(znamky(hodnoceni))
print(znamky([1, 2, 3, 4, 5, 6, -1]))

nezaokrouhlenecislo = 3.5
print(round(nezaokrouhlenecislo))
