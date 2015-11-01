


def arr(datapac, col=3):
    c=len(datapac)//col
    i=0
    pac=[]
    for p in range(col):
        pac.append([])
        for collum in range(c):
            pac[p].append(datapac[i])
            i += 1

    return pac




