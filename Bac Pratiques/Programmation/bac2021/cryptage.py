def genere(nb):
    mot = ""
    while nb != 0:
        R = nb % 3
        if R == 0:
            Y = "Ma"
        elif R == 1:
            Y = "Des"
        else:
            Y = "Son"
        mot = Y + mot
        nb = nb // 3
    return mot

