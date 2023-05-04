ip = '111.21.21.21'

# Divide la dirección IP en sus cuatro componentes
componentes = ip.split('.')

# Convierte cada componente en un entero
componente1 = int(componentes[0])
componente2 = int(componentes[1])
componente3 = int(componentes[2])
componente4 = int(componentes[3])

# Combina los componentes en un solo valor numérico

componente1 = (bin(componente1)[2:])
componente2 = (bin(componente2)[2:])
componente3 = (bin(componente3)[2:])
componente4 = (bin(componente4)[2:])


""" 
# Defina dos números enteros
a = 10   # Representación binaria: 0b1010
b = 6    # Representación binaria: 0b0110

# Realice la operación AND a nivel de bit entre los dos números
c = a & b

# Imprima los números y su resultado en su representación binaria y entera
print("a en binario:", bin(a))
print("b en binario:", bin(b))
print("c en binario:", bin(c))
print("a en entero:", a)
print("b en entero:", b)
print("c en entero:", c)
"""

