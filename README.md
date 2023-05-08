# Subnet Calculator

Este script de calculadora de subredes en Python te permite calcular y visualizar las subredes en base a una dirección IP y los parámetros de red deseados.

## Funcionamiento

1. Ingresa la dirección IP base.
2. Ingresa la cantidad de bits para la máscara de subred.
3. El script calculará automáticamente la configuración de subred y mostrará los detalles de cada subred, como la dirección de red, la primera dirección IP disponible, la última dirección IP disponible y la dirección de broadcast.

## Ejemplo de uso

```python
# Ingresa la dirección IP base
ip = "192.168.0.0"

# Ingresa la cantidad de bits para la máscara de subred
bits = 26

# Calcula las subredes
subredes = calcular_subredes(ip, bits)

# Muestra los resultados
for subred in subredes:
    print(f"Dirección de red: {subred['direccion_red']}")
    print(f"Primera dirección IP: {subred['primera_ip']}")
    print(f"Última dirección IP: {subred['ultima_ip']}")
    print(f"Dirección de broadcast: {subred['broadcast']}")
    print("-------------------------")
```

## Requisitos del entorno

- Python 3.0 o superior.


