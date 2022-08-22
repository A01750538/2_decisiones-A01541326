def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))

    IMC = peso / (altura*2)
    if IMC < 20:
        print(PESO BAJO)
    elif 
    
    if peso >0 and altura >0:
        indice = peso / altura**2
        if indice < 20: 
            print ("PESO BAJO")
        elif indice < 25:
            print("NORMAL")
        elif indice < 30:
            print ("SOBREPESO")
        elif indice < 40:
            print ("OBESIDAD")
        elif indice >= 40:
            print ("OBESIDAD MORBIDA")
    else:
        print ("Revisa tus datos, alguno de ellos es erróneo")
        
if __name__=='__main__':
    main()