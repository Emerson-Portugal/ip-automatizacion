def conversion_bin(x):
    ip = '111.21.21.21'

    # Divide la dirección IP en sus cuatro componentes
    componentes = ip.split('.')

    # Convierte cada componente en un entero
    componente1 = int(componentes[0])
    componente2 = int(componentes[1])
    componente3 = int(componentes[2])
    componente4 = int(componentes[3])

    # Combina los componentes en un solo valor numérico
    valor_numerico = (componente1 << 24) + (componente2 << 16) + (componente3 << 8) + componente4

    # Convierte el valor numérico a flotante
    nueva_ip = float(valor_numerico)

    print(nueva_ip)




def solicitar_ip():
    ip = input("Cual es tu IP: ")
    clase_red(ip)


def clase_red(ip):
    separador = "."
    separado = ip.split(separador)

    
    if int(separado[0]) >= 0 and int(separado[0]) <= 127:
        mascara = "255.0.0.0"
        print("Clase A")
        direccion_red(ip, mascara)
        

    elif int(separado[0]) >= 128 and int(separado[0]) <= 191:
        mascara = "255.255.0.0"
        print("Clase B")
        direccion_red(ip, mascara)

    elif int(separado[0]) >= 192 and int(separado[0]) <= 223:
        mascara = "255.255.255.0"
        print("Clase C")
        direccion_red(ip, mascara)

    else :
        print("Ningun Clase")



def direccion_red(ip,mascara):
    print(ip + " " + mascara )
    nueva_ip = conversion_bin(ip)
    nueva_mascara = conversion_bin(mascara)

def main():
    """Función principal"""
    solicitar_ip()



if __name__ == "__main__":
    main()
