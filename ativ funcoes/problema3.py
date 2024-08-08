def verifica_triangulo (x, y, z):
    return (x + y > z) and (x + z > y) and (y + z > x)

def tipo_triangulo (x, y, z):
    if (x==y) and (y==z) and (z==x):
        return 'Equilátero'
    elif (x==y) or (y==z) or (z==x):
        return 'Isósceles'
    else:
        return 'Escaleno'
    
    
