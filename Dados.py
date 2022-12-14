
import random
import time

print("")
print("╔════════════════════════════════╗")
print("║         JUEGO DE DADOS         ║")
print("╚════════════════════════════════╝")
print("")
print(" ╔═════════╗         ╔═════════╗")
print(" ║ ○     ○ ║         ║ ○     ○ ║")
print(" ║    ○    ║         ║ ○     ○ ║")
print(" ║ ○     ○ ║         ║ ○     ○ ║")
print(" ╚═════════╝         ╚═════════╝")
print("")
time.sleep(2)
print("HOLA...Tiremos los dados!!")
time.sleep(1)
opcion = int(input("Quiere tirar 1 o 2 dados?: "))

time.sleep(2)

def dado():
        
    time.sleep(1)
    print("Muy bien empecemos...!!  ")
    print("")
    time.sleep(2)
    num_dado_1 = random.randint(1,6)
    print("Tirando el Dado!!...")
    time.sleep(2)
    print("El Dado gira...")
    time.sleep(2)
    print(".....El Dado gira...")
    time.sleep(2)
    print("El Dado gira...")
    time.sleep(2)

    if num_dado_1 == 1:
        time.sleep(1)
        print("El numero que salio es..",num_dado_1)
        print("╔═════════╗")
        print("║         ║")
        print("║    ○    ║")
        print("║         ║")
        print("╚═════════╝")
        print("")
            
    elif num_dado_1 == 2:
        time.sleep(1)
        print("El numero que salio es..",num_dado_1)
        print("╔═════════╗")
        print("║ ○       ║")
        print("║         ║")
        print("║       ○ ║")
        print("╚═════════╝")
        print("")
        
    elif num_dado_1 == 3:
        time.sleep(1)
        print("El numero que salio es..",num_dado_1)
        print("╔═════════╗")
        print("║ ○       ║")
        print("║    ○    ║")
        print("║       ○ ║")
        print("╚═════════╝")
        print("")
    
    elif num_dado_1 == 4:
        time.sleep(1)
        print("El numero que salio es..",num_dado_1)
        print("╔═════════╗")
        print("║ ○     ○ ║")
        print("║         ║")
        print("║ ○     ○ ║")
        print("╚═════════╝")
        print("")

    elif num_dado_1 == 5:
        time.sleep(1)
        print("El numero que salio es..",num_dado_1)
        print("╔═════════╗")
        print("║ ○     ○ ║")
        print("║    ○    ║")
        print("║ ○     ○ ║")
        print("╚═════════╝")
        print("")

    elif num_dado_1 == 6:
        time.sleep(1)
        print("El numero que salio es..",num_dado_1)
        print("╔═════════╗")
        print("║ ○     ○ ║")
        print("║ ○     ○ ║")
        print("║ ○     ○ ║")
        print("╚═════════╝")
        print("")
    
    tirar_nuevo = input("Quieres Volver a Tirar, si / no : ")
    if tirar_nuevo == "si":
        dado()
    elif tirar_nuevo == "no":
        time.sleep(1)
        print("")
        print("░░░░░░░░░░░░░░░░░░░░░░")
        print("░░┌──┐░░░░░░░░░░┌──┐░░")
        print("░╔╡▐▐╞╝░░┌──┐░░╔╡▐▐╞╝░")
        print("░░└╥╥┘░░╚╡▌▌╞╗░░└╥╥┘░░")
        print("░░░╚╚░░░░└╥╥┘░░░░╚╚░░░")
        print("░░░░░░░░░░╝╝░░░░░░░░░░")
        print("")
        print("Gracias por Participar...!!")
        


def dado_2():

    print("Empezamos...??")
    print("")
    time.sleep(1)
    num_dado_2 = random.randint(1,6)
    print("Tiramos los Dados....")
    time.sleep(1)
    print("Giran los Dados...")
    time.sleep(1)
    print(" ......Giran los Dados...")
    time.sleep(2)
    print("Giran los Dados...")
    time.sleep(1)
    print(" ......Giran los Dados...")


    if num_dado_2 == 1:
        time.sleep(1)
        print("Los Numeros son...!!")
        print("╔═════════╗")
        print("║         ║")
        print("║    ○    ║")
        print("║         ║")
        print("╚═════════╝")
        print("")
    
    elif num_dado_2 == 2:
        time.sleep(1)
        print("Los Numeros son...!!")
        print("╔═════════╗")
        print("║ ○       ║")
        print("║         ║")
        print("║       ○ ║")
        print("╚═════════╝")
        print("")

    elif num_dado_2 == 3:
        time.sleep(1)
        print("Los Numeros son...!!")
        print("╔═════════╗")
        print("║ ○       ║")
        print("║    ○    ║")
        print("║       ○ ║")
        print("╚═════════╝")
        print("")

    elif num_dado_2 == 4:
        time.sleep(1)
        print("Los Numeros son...!!")
        print("╔═════════╗")
        print("║ ○     ○ ║")
        print("║         ║")
        print("║ ○     ○ ║")
        print("╚═════════╝")
        print("")   

    elif num_dado_2 == 5:
        time.sleep(1)
        print("Los Numeros son...!!")
        print("╔═════════╗")
        print("║ ○     ○ ║")
        print("║    ○    ║")
        print("║ ○     ○ ║")
        print("╚═════════╝")
        print("")

    elif num_dado_2 == 6:
        time.sleep(1)
        print("Los Numeros son...!!")
        print("╔═════════╗")
        print("║ ○     ○ ║")
        print("║ ○     ○ ║")
        print("║ ○     ○ ║")
        print("╚═════════╝")

    num_dado_3 = random.randint(1,6)
    time.sleep(1)
    if num_dado_3 == 1:
        print("                 ╔═════════╗")
        print("                 ║         ║")
        print("                 ║    ○    ║")
        print("                 ║         ║")
        print("                 ╚═════════╝")

    elif num_dado_3 == 2:
        print("                 ╔═════════╗")
        print("                 ║ ○       ║")
        print("                 ║         ║")
        print("                 ║       ○ ║")
        print("                 ╚═════════╝")

    elif num_dado_3 == 3:
        print("                 ╔═════════╗")
        print("                 ║ ○       ║")
        print("                 ║    ○    ║")
        print("                 ║       ○ ║")
        print("                 ╚═════════╝")

    elif num_dado_3 == 4:
        print("                 ╔═════════╗")
        print("                 ║ ○     ○ ║")
        print("                 ║         ║")
        print("                 ║ ○     ○ ║")
        print("                 ╚═════════╝")

    elif num_dado_3 == 5:
        print("                 ╔═════════╗")
        print("                 ║ ○     ○ ║")
        print("                 ║    ○    ║")
        print("                 ║ ○     ○ ║")
        print("                 ╚═════════╝")

    elif num_dado_3 == 6:
        print("                 ╔═════════╗")
        print("                 ║ ○     ○ ║")
        print("                 ║ ○     ○ ║")
        print("                 ║ ○     ○ ║")
        print("                 ╚═════════╝")
    time.sleep(1)
    print("La suma de dados es:",(num_dado_2 + num_dado_3))

    tirar_nuevo_2 = input("Quieres Volver a Tirar, si / no : ")
    if tirar_nuevo_2 == "si":
        dado_2()
    elif tirar_nuevo_2 == "no":
        time.sleep(1)
        print("")
        print("░░░░░░░░░░░░░░░░░░░░░░")
        print("░░┌──┐░░░░░░░░░░┌──┐░░")
        print("░╔╡▐▐╞╝░░┌──┐░░╔╡▐▐╞╝░")
        print("░░└╥╥┘░░╚╡▌▌╞╗░░└╥╥┘░░")
        print("░░░╚╚░░░░└╥╥┘░░░░╚╚░░░")
        print("░░░░░░░░░░╝╝░░░░░░░░░░")
        print("")
        print("Gracias por Participar...!!")


if opcion == 1:
    dado()
else:
    dado_2()






