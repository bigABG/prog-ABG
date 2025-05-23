from math import cos

def f(x):
    return 1/(cos(x)**2)


def calcul(n, a, b):
    h = (b - a) / n
    x = a
    fi = 0
    
    for i in range(n):
        f1 = f(x)
        x += h
        f2 = f(x)
        fi += (f1 + f2) * (h/2)
    return fi

print(calcul(100, 0, 2))