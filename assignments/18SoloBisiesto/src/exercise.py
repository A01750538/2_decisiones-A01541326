def main():
    #escribe tu código abajo de esta línea
    year = int(input("Año:"))

    if year <= 0:
        print ("Dato incorrecto")
    elif year % 4 == 0:  
        if year % 100 != 0:
            print (True)
        elif year % 400 == 0:
                print (True)
        else:
                print (False)
    else:
        print (False)

if __name__=='__main__':
    main()
