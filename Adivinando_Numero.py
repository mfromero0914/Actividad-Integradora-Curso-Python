    

import random
import time


print("")
print("╔═══╦═══╦═══╦════════════════════════════╦═══╦═══╦═══╗")
print("║ ? ║ 8 ║ ? ║    ADIVINANDO EL NUMERO    ║ 2 ║ ? ║ 5 ║")
print("╚═══╩═══╩═══╩════════════════════════════╩═══╩═══╩═══╝")
print("")
time.sleep(2)
print("Hola... juguemos a adivinar el numero..")
time.sleep(2)
print("Estoy pensando en un Numero del 1 al 10 ") 
time.sleep(1)
print("")
print("Te animas adivinarlo..?")
print("")
time.sleep(1)
print("Tienes 4 intentos.... Suerte...!!!")
time.sleep(1)
print("") 


def adivinando():


    num_cpu = random.randint(1,10)
    intentos = 1
    while intentos != 5:
        print("Intento N°", intentos)
        num_jugador = int(input("Que Numero pensaste?: "))
        
        if num_jugador < 1 or num_jugador > 10:
            print("Ingresa solo numeros del 1 al 10")
            # num_jugador = int(input("Que Numero pensaste?: "))
        print("")
        # num_jugador = int(input("Que Numero pensaste?: "))
        if num_jugador == num_cpu:
            time.sleep(2) 
            print("")
            print("Muy bien... Has adivinado el numero ")          
            time.sleep(2)
            print("Has Ganado despues de", intentos,"intentos..!!! El numero era:",num_cpu)

            intentos = 4
            
        else:
            time.sleep(2)
            print("No has adivinado... suerte para la proxima...!!")
            if intentos == 4:

                print("El numero era", num_cpu)
                
        intentos += 1
    print("")

    opcion = input("¿Quieres volver a Jugar?: si - no ")
   
    if opcion == "si":

        adivinando()
    else:
        time.sleep(1)
        print("")
        print("░░░░░░░░░░░░░░░░░░░░░░")
        print("░░┌──┐░░░░░░░░░░┌──┐░░")
        print("░╔╡▐▐╞╝░░┌──┐░░╔╡▐▐╞╝░")
        print("░░└╥╥┘░░╚╡▌▌╞╗░░└╥╥┘░░")
        print("░░░╚╚░░░░└╥╥┘░░░░╚╚░░░")
        print("░░░░░░░░░░╝╝░░░░░░░░░░")
        print("")
        print("Gracias por Participar..!!")


adivinando()
    



    

        

    


    

        
