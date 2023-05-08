import ipaddress


def solicitar_ip():
    #ip = "192.168.55.44"
    ip = input("Cual es tu IP: ")
    subRed = int(input("Cantidad de Sub Redes: "))
    host = int(input("Cantidad aproximada de Host: "))
    subRed_nueva = clase_subRed(subRed)
    clase_red(ip, subRed_nueva,subRed, host)

def clase_subRed(subRed):
    i = 0
    while True:
        valor = 2**i
        if  valor>= subRed:
            return i
            #print(i)
            #break
        i = i + 1
    #return valor

def salto_red(m):
    return 256-m

def clase_host(m):
    #return (2**m)-2
    print(m)
    return m


def clase_red(ip,subRed_nueva, subRed, host):
    separador = "."
    separado = ip.split(separador)

    if int(separado[0]) >= 0 and int(separado[0]) <= 127:
        mascara = "255.0.0.0"
        valor_clase = "A"
        print(f"\n Clase {valor_clase} \n")
        direccion_red(ip, mascara,subRed_nueva,valor_clase,subRed, host)

    elif int(separado[0]) >= 128 and int(separado[0]) <= 191:
        mascara = "255.255.0.0"
        valor_clase = "B"
        print(f"\n Clase {valor_clase} \n")
        direccion_red(ip, mascara,subRed_nueva,valor_clase,subRed, host)

    elif int(separado[0]) >= 192 and int(separado[0]) <= 223:
        mascara = "255.255.255.0"
        valor_clase = "C"
        print(f"\n Clase {valor_clase} \n")
        direccion_red(ip, mascara,subRed_nueva,valor_clase, subRed, host)

    else:
        print("Ningun Clase")


def direccion_red(ip, mascara,subRed_nueva,valor_clase, subRed, host):
    separador = "."
    separado_ip = ip.split(separador)
    separado_mascara = mascara.split(separador)

    direcionRed = []

    for i in range(len(separado_ip)):
        direcionRed.append(str(int(separado_ip[i]) & int(separado_mascara[i])))

    optener_nueva_mascara(direcionRed, separado_mascara,subRed_nueva, valor_clase, subRed, host)
    #print(direcionRed)


def optener_nueva_mascara(direcionRed, mascara,subRed_nueva, valor_clase, subRed, host):
    ## limitacion para una sola mascara
    valor_global = ['128','192','224','240','248','252','254','255']
    if valor_clase == "A":
        valor_clase_nueva = 1
        mascara[1] = valor_global[subRed_nueva-1]
        nueva_mascara = []

        for i in mascara:
            nueva_mascara.append(bin(int(i))[2:])

        for j in range(len(nueva_mascara)):
            if j >= 2:
                nueva_mascara[j] = '00000000'
        
        contador = 0    
        for i in range(len(nueva_mascara)):
            for j in range(len(nueva_mascara[i])):
                if nueva_mascara[i][j] == "0":
                    contador = contador + 1
        #host_nuevo = clase_host(contador)
        host_nuevo = host
        salto_red_nueva = salto_red(int(valor_global[subRed_nueva-1]))

        tabla_red(direcionRed, salto_red_nueva, host_nuevo, subRed, valor_clase_nueva)
    elif valor_clase == "B":
        valor_clase_nueva = 2
        mascara[2] = valor_global[subRed_nueva-1]
        nueva_mascara = []

        for i in mascara:
            nueva_mascara.append(bin(int(i))[2:])

        for j in range(len(nueva_mascara)):
            if j >= 3:
                nueva_mascara[j] = '00000000'
        
        contador = 0    
        for i in range(len(nueva_mascara)):
            for j in range(len(nueva_mascara[i])):
                if nueva_mascara[i][j] == "0":
                    contador = contador + 1
        #host_nuevo = clase_host(contador)
        host_nuevo = host
        salto_red_nueva = salto_red(int(valor_global[subRed_nueva-1]))

        tabla_red(direcionRed, salto_red_nueva, host_nuevo, subRed, valor_clase_nueva)
    elif valor_clase == "C":
        valor_clase_nueva = 3
        mascara[3] = valor_global[subRed_nueva-1]
        nueva_mascara = []

        for i in mascara:
            nueva_mascara.append(bin(int(i))[2:])
        
        contador = 0    
        for i in range(len(nueva_mascara)):
            for j in range(len(nueva_mascara[i])):
                if nueva_mascara[i][j] == "0":
                    contador = contador + 1
        #host_nuevo = clase_host(contador)
        host_nuevo = host
        salto_red_nueva = salto_red(int(valor_global[subRed_nueva-1]))

        tabla_red(direcionRed, salto_red_nueva, host_nuevo, subRed, valor_clase_nueva)
    else:
        print("Error")



def tabla_red(direcionRed, salto_red_nueva, host_nuevo, subRed, valor_clase_nueva):

    
    print("SUB_RED            PRIMERA_IP        ULTIMA_IP            DIRECCION_BROADCAST     CANTIDAD DE HOST")
    print("---------------------------------------------------------------------------------------------")

    salto_red_nueva_valor = 0
    for i in range(subRed):
        direcionRed[valor_clase_nueva] = str(salto_red_nueva_valor)
        subRed_nueva = '.'.join(direcionRed)
        direccion_ip = ipaddress.IPv4Address(subRed_nueva)

        direccion_ip_suma_p = direccion_ip + 1
        direccion_ip_suma_u = direccion_ip + host_nuevo + 2
        direccion_ip_suma_b = direccion_ip_suma_u + 1

        print("{:<19s} {:<15s} {:<23s} {:<23s} {:<15s}".format(subRed_nueva, str(direccion_ip_suma_p), str(direccion_ip_suma_u), str(direccion_ip_suma_b), str(host_nuevo)))

        salto_red_nueva_valor = salto_red_nueva_valor + salto_red_nueva

    

def main():
    """Función principal"""
    solicitar_ip()


if __name__ == "__main__":
    main()

    