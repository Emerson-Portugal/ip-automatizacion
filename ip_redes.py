def solicitar_ip():
    ip = "192.168.55.44"
    # ip = input("Cual es tu IP: ")
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

    else:
        print("Ningun Clase")


def direccion_red(ip, mascara):
    separador = "."
    separado_ip = ip.split(separador)
    separado_mascara = mascara.split(separador)

    valor_nuevo = []

    for i in range(len(separado_ip)):
        valor_nuevo.append(str(int(separado_ip[i]) & int(separado_mascara[i])))

    print(valor_nuevo)
    # direccion_red = ".".join(valor_nuevo)
    # return direccion_red


def main():
    """Función principal"""
    solicitar_ip()


if __name__ == "__main__":
    main()