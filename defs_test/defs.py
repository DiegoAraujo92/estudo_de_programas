def bascara(a, b, c):
    
    delta= b**2 - 4*a*c
    
    
    if delta < 0:
        return None  
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    return print(raiz1, raiz2)

bascara(1, -5, 4)
print()

def soma(x, y ,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} =', x + y + z)
        print()
    else:
        print(f'{x=} {y=} =', x + y)
        print()

soma(1, 2)
soma(1, 2, 3)
soma(123, 456, 0)

