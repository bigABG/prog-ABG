def fonction(x):
    return 1 / x

def suite(a, n):
    if n == 0:
        return a
    else:
        return fonction(suite(a, n - 1))
    
def Point_Fixe(a, epsilon):
    
    f = a
    Si = suite(a, f)
    Sf = suite(a, f + 1)
    while not abs(Sf - Si) <= epsilon:
        Si = Sf
        f += 1
        Sf = suite(a, f)
    return Sf

print(Point_Fixe(2, 0.0001))