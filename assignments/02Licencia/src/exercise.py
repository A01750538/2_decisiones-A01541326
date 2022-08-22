'''
Comentarios
'''
def main():
    edad = int(input("Ingresa tu edad: "))
    identificacion = (input("¿Tienes identificación oficial?(s/n): "))

    if edad >0: 
        if edad >= 18:
            if identificacion == "s" or identificacion == "S":
                print ("Trámite de licencia concedido")
            elif identificacion =="n" or identificacion == "N": 
                print ("No cumples requisitos")
            else: 
                print("Respuesta incorrecta")
        else:
            print ("No cumples requisitos")
    else:
        print("Respuesta incorrecta")
if __name__ == '__main__':
    main()
