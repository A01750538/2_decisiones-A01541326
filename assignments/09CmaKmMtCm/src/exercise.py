def main():
    # Escribe tu código abajo de esta línea
    numero = int(input("Introduce los cm:"))
    
    if numero < 100:
        print (numero , " cm")
    elif numero<100000: 
        print (numero//100, " m")
    else: 
        numero1 = numero//100000
        print (numero1, " km")
        numero2= numero%100000
        if numero2> 0:
            numero3 = numero2//100
            print (numero3," m")
            numero4 = numero2%100
            if numero > 0:
                print (numero4*100, " cm")

if __name__ == '__main__':
    main()
