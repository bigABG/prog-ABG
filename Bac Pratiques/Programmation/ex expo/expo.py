def puissance(n, p):
    s = 1
    for i in range(p):
        s *= n
    return s


def factoriel(n):
    if  n == 0:
        return 1
    else:
        return n * factoriel(n - 1)
    
def calcul(eps, x):
    i = 2
    exp_in = 1 
    exp_fin = 1 + x
    while not abs(exp_fin - exp_in) <= eps:
        exp_in = exp_fin
        exp_fin = exp_in + (puissance(x, i) / factoriel(i))
        i += 1
        print(i)
    return exp_in

print(calcul(0.00001, 2))   