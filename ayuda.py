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

