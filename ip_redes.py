

def solicitar_ip():
    ip = input("Cual es tu IP: ")
    clase_red(ip)


def clase_red(ip):
    separador = "."
    separado = ip.split(separador)
    
    if int(separado[0]) >= 0 and int(separado[0]) <= 127:
        print("Clase A")
    elif int(separado[0]) >= 128 and int(separado[0]) <= 191:
        print("Clase B")
    elif int(separado[0]) >= 192 and int(separado[0]) <= 223:
        print("Clase C")
    else :
        print("Ningun Clase")



def main():
    """Función principal"""
    solicitar_ip()



if __name__ == "__main__":
    main()
