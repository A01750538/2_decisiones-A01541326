def main():
    # Escribe tu código abajo de esta línea
    numero = int(input("Introduce los cm:"))
    
    if numero < 100:
        print (f"{numero} cm")
    elif numero<100000: 
        print (f"{numero//100} m")
        numero4 = numero%100
        if numero4 > 0:
                print (f"{numero4} cm")
    else: 
        numero1 = numero//100000
        print (f"{numero1} km")
        numero2= numero%100000
        if numero2> 0:
            numero3 = numero2//100
            if numero3 > 0:
                print (f"{numero3} m")
            numero4 = numero2%100
            if numero4 > 0:
                print (f"{numero4} cm") 

if __name__ == '__main__':
    main()
