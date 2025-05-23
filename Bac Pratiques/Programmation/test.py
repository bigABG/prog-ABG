def f(x):
    return 1/(1 + (x ** 2))

def integral_rectangle(n ,a ,b):
    h = (b - a) / n
    x = a
    fi = 0
    for i in range(n):
        f1 = f(x)
        x += h
        f2 = f(x)
        fi += (f1 + f2) * (h / 2)
    return fi


print(integral_rectangle(100, 0, 2))


def integral_trapeze(n, a, b):
    h  = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        total += f(x)
    return total * h

print(integral_trapeze(100, 0, 2))