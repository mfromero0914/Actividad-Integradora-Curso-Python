

import random
import time 
import matplotlib.pyplot as plt
import numpy as np


#!----------------------------------------------------------------------------------------------------------------------------------
def intro():
    
    print("")
    print("     ║ ║ ╔═╗ ║  ╔═╗  ║")
    print("     ╠═╣ ║ ║ ║  ║ ║  ║")
    print("     ║ ║ ╚═╝ ╚╝ ╚═╚╝ O")

    print("")
    print("╔════════════════════════════════╦════╗")
    print("║       SELECCIONE UNA OPCION    ║ Op ║")
    print("╠════════════════════════════════╬════╣")
    print("║> PIEDRA * PAPEL * TIJERA       ║ 1  ║")
    print("╠════════════════════════════════╬════╣")
    print("║> DADOS                         ║ 2  ║")
    print("╠════════════════════════════════╬════╣")
    print("║> ADIVINANDO NUMERO             ║ 3  ║")
    print("╠════════════════════════════════╬════╣")
    print("║> GRAFICOS                      ║ 4  ║")
    print("╠════════════════════════════════╬════╣")
    print("║> SALIR                         ║ 5  ║")
    print("╚════════════════════════════════╩════╝")
    print("")

#!-----------------------------------------------------PIEDRA PAPEL TIJERA-----------------------------------------------------------------------------

def opcion_cpu():
    player_cpu = random.choice(["piedra","papel","tijera"])
    print("")
    return player_cpu

def opcion_jugador(): 
    player1 = input("Haz tu jugada:  piedra - papel - tijera: ")    

    while player1 != "piedra" and player1 != "papel" and player1 != "tijera":
        print("Por favor ingrese una opcion valida.")
        player1 = input("Haz tu jugada:  piedra - papel - tijera: ")
    return player1

ron = 0
gan = 0
emp = 0
per = 0

def jugar():
    player_cpu_1 = opcion_cpu()
    player1 = opcion_jugador()

    if player1 == "papel" and player_cpu_1 == "papel":
        time.sleep(1)
        print("")
        print("Hemos Empatado...!!! ")
        print("Mi jugada fue",player_cpu_1)
        
        return "empate"
    
    elif player1 == "papel" and player_cpu_1 == "piedra":
        time.sleep(1)
        print("")
        print("¡¡ Que suerte!! Me has Ganado...!!!")
        print("Mi jugada fue",player_cpu_1)
    
        return "ganada"

    elif player1 == "papel" and player_cpu_1 == "tijera":
        time.sleep(1)
        print("")
        print ("Perdiste...!!")
        print("Mi jugada fue",player_cpu_1)
        
        return "perdiste"

    elif player1 == "piedra" and player_cpu_1 == "papel":
        time.sleep(1)
        print("")
        print ("Perdiste...!!")
        print("Mi jugada fue",player_cpu_1)
        
        return "perdiste"

    elif player1 == "piedra" and player_cpu_1 == "piedra":
        time.sleep(1)
        print("")
        print("Hemos Empatado...!!! ")
        print("Mi jugada fue",player_cpu_1)
    
        return "empate"


    elif player1 == "piedra" and player_cpu_1 == "tijera":
        time.sleep(1)
        print("")
        print ("Perdiste...!!")
        print("Mi jugada fue",player_cpu_1)
        
        return "perdiste"

    elif player1 == "tijera" and player_cpu_1 == "papel":
        time.sleep(1)
        print("")
        print("¡¡ Que suerte!! Me has Ganado...!!!")
        print("Mi jugada fue",player_cpu_1)
        
        return "ganada"

    elif player1 == "tijera" and player_cpu_1 == "piedra":
        time.sleep(1)
        print("")
        print ("Perdiste...!!")
        print("Mi jugada fue",player_cpu_1)
    
        return "perdiste"

    elif player1 == "tijera" and player_cpu_1 == "tijera":
        time.sleep(1)
        print("")
        print("Hemos Empatado...!!! ")
        print("Mi jugada fue",player_cpu_1)
    
        return "empate"


def marcador():
    time.sleep(1)
    print("")
    print("╔════════════════════════════╦═════════╗")
    print("║> RONDAS                    ║",ron,"      ║")
    print("╠════════════════════════════╬═════════╣")
    print("║> GANADAS                   ║",gan,"      ║")
    print("╠════════════════════════════╬═════════╣")
    print("║> PERDIDAS                  ║",per,"      ║")
    print("╠════════════════════════════╬═════════╣")
    print("║> EMPATADAS                 ║",emp,"      ║")
    print("╚════════════════════════════╩═════════╝")
    print("")
#!---------------------------------------------------- DADOS ------------------------------------------------------------------------------

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
    print(".....Sigue Girando...")
    time.sleep(2)
    print("...Ya casi...")
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
    print("....Los Dados giran!!")
    time.sleep(2)
    print("Siguen Girando....")
    time.sleep(1)
    print(" .....Ya casi....")
    time.sleep(1)


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

#!--------------------------------------------------ADIVINAR NUMERO--------------------------------------------------------------------------------
def adivinando():
    intentos = 1
    num_cpu = random.randint(1,10)

    while intentos != 6:
        print("")
        print("Intento N°", intentos)
        num_jugador = int(input("Elegi un numero: "))
            
        if num_jugador == num_cpu:
            time.sleep(2)
            print("")
            print("Muy bien... Has adivinado el numero ")          
            time.sleep(2)
            print("Has Ganado despues de", intentos,"intentos..!!! El numero era:",num_cpu)

            intentos = 5
            
        else:
            time.sleep(2)
            print("No has adivinado... suerte para la proxima...!!")
            if intentos == 5:
                print("El numero era", num_cpu)
                
        intentos += 1
    print("")
    opcion = str(input("¿Quieres volver a jugar? si / no: "))
    if opcion == str("si"):

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

#!---------------------------------------------------GRAFICOS-------------------------------------------------------------------------------

def grafico_barra():
        
        time.sleep(1)
        x = np.array(["Brasil","Italia","Alemania","Uruguay","Argentina","Francia","Inglaterra","España"])
        y = np.array([5,4,4,2,2,2,1,1])
        plt.title("Paises Campeones del Mundo")
        plt.xlabel("Copas")
        plt.ylabel("Paises")
        plt.annotate("5",xy=(5,"Brasil"))
        plt.annotate("4",xy=(4,"Italia"))
        plt.annotate("4",xy=(4,"Alemania"))
        plt.annotate("2",xy=(2,"Uruguay"))
        plt.annotate("2",xy=(2,"Argentina"))
        plt.annotate("2",xy=(2,"Francia"))
        plt.annotate("1",xy=(1,"Inglaterra"))
        plt.annotate("1",xy=(1,"España"))
        plt.barh(x,y)
        plt.show()
    
def grafico_torta():
    time.sleep(1)
    valores = [29,21,15,11,9,7,5,3]
    etiquetas = ["Python","Java","javaScript","C#","PHP","C++","MatLab","Ruby"]
    separacion = [0.1,0,0,0,0,0,0,0]
       

    plt.pie(valores, labels=etiquetas, explode=separacion, shadow=True, autopct='%1.1f%%' , startangle=90)
    plt.title("Lenguajes de Programacion mas Utilizados en 2022")
    plt.show()

def grafico_interactivo():
    time.sleep(1)
    print("Hola.. haremos un Grafico...!!")
    print("")

    titulo = input("◘ Ponle un Titulo: ")
    print("")

    print("Ingresa 4 valores para X")
    x_datos = []     
    x_datos.append(int(input("1° Valor: ")))
    x_datos.append(int(input("2° Valor: ")))
    x_datos.append(int(input("3° Valor: ")))
    x_datos.append(int(input("4° Valor: ")))

    print("Ingresa 4 valores para Y")
    y_datos = []     
    y_datos.append(int(input("1° Valor: ")))
    y_datos.append(int(input("2° Valor: ")))
    y_datos.append(int(input("3° Valor: ")))
    y_datos.append(int(input("4° Valor: ")))

    x_titulo = input("◘ Ponle un Nombre para las coordenadas X: ")
    y_titulo = input("◘ Ponle un Nombre para las coordenadas Y: ")

    plt.plot([x_datos],[y_datos],"g*--")
    plt.title(titulo)
    plt.xlabel(x_titulo)
    plt.ylabel(y_titulo)
    plt.grid()
    plt.show()

#!----------------------------------------------------------------------------------------------------------------------------------






#!------------------------------------------------------OPCION 1----------------------------------------------------------------------------
menu_inicial = "si"
while menu_inicial == "si":
    intro()
    opcion = int(input("Elija una Opcion: "))

    if opcion == 1:
        print("")
        print("╔═════════════════════════════════════════╗")
        print("║      Juego PIEDRA - PAPEL - TIJERA      ║")
        print("╚═════════════════════════════════════════╝")
        print("")
        print("Hola...! Juguemos a!!!")
        print("")
        print("P_I_E_D_R_A....")
        print("")
        time.sleep(1)
        print("     P_A_P_E_L...")
        print("")
        time.sleep(1)
        print("           T_I_J_E_R_A..!!!")
        print("")
        time.sleep(1)

        volver_jugar = "si"

        while volver_jugar != "no":
            volver_jugar = jugar()

            if volver_jugar != "salir":
                ron = ron + 1

                if volver_jugar == "ganada":
                    gan = gan + 1
                elif volver_jugar == "perdiste":
                    per = per + 1
                elif volver_jugar == "empate":
                    emp = emp + 1
            marcador()
            print("")
            volver_jugar = input("Quieres volver a jugar? si - no: ")

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
        
    #!------------------------------------------------------OPCION 2---------------------------------------------------------------------------- 
    elif opcion == 2:

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
        time.sleep(1)
        print("HOLA...Tiremos los dados!!")
        time.sleep(1)
        opcion = int(input("Quiere tirar 1 o 2 dados?: "))

        time.sleep(2)

        if opcion == 1:
            dado()
        else:
            dado_2()





    #!--------------------------------------------------------OPCION 3--------------------------------------------------------------------------   
    elif opcion == 3:
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
        print("Tienes 5 intentos.... Suerte...!!!")
        time.sleep(1)
        print("") 
        adivinando()

    #!---------------------------------------------------------OPCION 4-------------------------------------------------------------------------
    elif opcion == 4:
        print("")
        print("╔═══════════════════════╦══════════════════════╦══════════════════════════╦════════════════════╗")
        print("║ 1 ► Grafico Barra     ║ 2 ► Grafico Torta    ║ 3 ► Grafico Interacivo   ║ 4 ► Salir          ║")
        print("╚═══════════════════════╩══════════════════════╩══════════════════════════╩════════════════════╝")
        print("")
        
            
        opcion = int(input("Elije una Opcion de Graficos: "))

        if opcion == 1:
            grafico_barra()
        elif opcion == 2:
            grafico_torta()
        elif opcion == 3:
            grafico_interactivo()
        else:
            opcion == 4
            print("")
            print("░░░░░░░░░░░░░░░░░░░░░░")
            print("░░┌──┐░░░░░░░░░░┌──┐░░")
            print("░╔╡▐▐╞╝░░┌──┐░░╔╡▐▐╞╝░")
            print("░░└╥╥┘░░╚╡▌▌╞╗░░└╥╥┘░░")
            print("░░░╚╚░░░░└╥╥┘░░░░╚╚░░░")
            print("░░░░░░░░░░╝╝░░░░░░░░░░")
            print("")
            print("Gracias por participar...!!")


    #!------------------------------------------------------------OPCION 5---------------------------------------------------------------------
    elif opcion == 5:
        break

    else:
        print("Opcion Incorrecta")
        opcion = int(input("Elija una Opcion: "))
    print("")
    menu_inicial = input("Quieres Volver al Menu Principal? si/no: ")
    

print("")
print( "░░░░░░░░░░░▄▄")
print( "░░░░░░░░░░█░░█")
print( "░░░░░░░░░░█░░█")
print( "░░░░░░░░░█░░░█")
print( "░░░░░░░░█░░░░█")
print( "██████▄▄█░░░░░██████▄")
print( "▓▓▓▓▓█░░░░░░░░░░░░░░█")
print( "▓▓▓▓▓█░░░░░░░░░░░░░░█")
print( "▓▓▓▓▓█░░░░░░░░░░░░░░█")
print( "▓▓▓▓▓█░░░░░░░░░░░░░░█")
print( "▓▓▓▓▓█░░░░░░░░░░░░░░█")
print( "▓▓▓▓▓█████░░░░░░░░░█")
print( "█████▀░░░░▀▀██████▀")
print("")

print("Gracias por Participar...!!")
        














































































































    # def dado():
            
    #         time.sleep(2)
    #         print("")
    #         print("╔════════════════════════════════╗")
    #         print("║         JUEGO DE DADOS         ║")
    #         print("╚════════════════════════════════╝")
    #         print("")
    #         print("╔═════════╗         ╔═════════╗")
    #         print("║ ○     ○ ║         ║ ○     ○ ║")
    #         print("║    ○    ║         ║ ○     ○ ║")
    #         print("║ ○     ○ ║         ║ ○     ○ ║")
    #         print("╚═════════╝         ╚═════════╝")
    #         print("")
    #         time.sleep(2)
    #         print("HOLA...Tiremos los dados!!")
    #         time.sleep(1)
    #         opcion = int(input("Quiere tirar 1 o 2 dados?: "))
    #         time.sleep(2)
            
    #         print("Muy bien empecemos...!!  ")
    #         print("")
    #         time.sleep(2)
    #         num_dado = random.randint(1,6)
    #         print("Tirando el Dado!!...")
    #         time.sleep(2)
    #         print("El Dado gira...")
    #         time.sleep(2)
    #         print("El Dado gira...")
    #         time.sleep(2)

    #         if num_dado == 1:
    #             time.sleep(1)
    #             print("El numero que salio es..",num_dado)
    #             print("╔═════════╗")
    #             print("║         ║")
    #             print("║    ○    ║")
    #             print("║         ║")
    #             print("╚═════════╝")
    #             print("")
                
    #         elif num_dado == 2:
    #             time.sleep(1)
    #             print("El numero que salio es..",num_dado)
    #             print("╔═════════╗")
    #             print("║ ○       ║")
    #             print("║         ║")
    #             print("║       ○ ║")
    #             print("╚═════════╝")
    #             print("")
            
    #         elif num_dado == 3:
    #             time.sleep(1)
    #             print("El numero que salio es..",num_dado)
    #             print("╔═════════╗")
    #             print("║ ○       ║")
    #             print("║    ○    ║")
    #             print("║       ○ ║")
    #             print("╚═════════╝")
    #             print("")
            
    #         elif num_dado == 4:
    #             time.sleep(1)
    #             print("El numero que salio es..",num_dado)
    #             print("╔═════════╗")
    #             print("║ ○     ○ ║")
    #             print("║         ║")
    #             print("║ ○     ○ ║")
    #             print("╚═════════╝")
    #             print("")

    #         elif num_dado == 5:
    #             time.sleep(1)
    #             print("El numero que salio es..",num_dado)
    #             print("╔═════════╗")
    #             print("║ ○     ○ ║")
    #             print("║    ○    ║")
    #             print("║ ○     ○ ║")
    #             print("╚═════════╝")
    #             print("")

    #         elif num_dado == 6:
    #             time.sleep(1)
    #             print("El numero que salio es..",num_dado)
    #             print("╔═════════╗")
    #             print("║ ○     ○ ║")
    #             print("║ ○     ○ ║")
    #             print("║ ○     ○ ║")
    #             print("╚═════════╝")
    #             print("")


    # def adivinando():

    #         intentos = 1
    #         num_cpu = random.randint(1,10)
    #         print("")
    #         print("╔════════════════════════════════╗")
    #         print("║       ADIVINADO EL NUMERO      ║")
    #         print("╚════════════════════════════════╝")
    #         print("")
    #         time.sleep(3)
    #         print("Hola... juguemos a adivinar el numero..")
    #         time.sleep(2)
    #         print("estoy pensando en un Numero del 1 al 10 ") 
    #         time.sleep(1)
    #         print("")
    #         print("Te animas adivinarlo..?")
    #         print("")
    #         time.sleep(1)
    #         print("Tienes 5 intentos.... Suerte...!!!")
    #         time.sleep(1)
    #         print("") 

    #         while intentos <= 5:
    #             print("")
    #             print("Intento N°", intentos)
    #             num_jugador = int(input("Elegi un numero: "))
                    
    #             if num_jugador == num_cpu:
    #                 time.sleep(2)
    #                 print("")
    #                 print("Muy bien... Has adivinado el numero ")
    #                 print("El Numero que pense era el ", num_cpu)
    #                 print("")
    #                 time.sleep(2)
    #                 print("Has Ganado despues de", intentos,"intentos..!!! ")
    #                 print("♥ ♥ ♥ ♥")

    #                 intentos = 5
    #                 break
                    
    #             else:
    #                 time.sleep(2)
    #                 print("No has adivinado... suerte para la proxima...!!")
    #                 print("")
                        
    #             intentos += 1

    #         print("")
    #         print("Se acabaron los intentos del juego")
    #         print("El Numero que pense era el ", num_cpu)



    # # def grafico_barra():
        
    # #     x = np.array(["Brasil","Italia","Alemania","Uruguay","Argentina","Francia","Inglaterra","España"])
    # #     y = np.array([5,4,4,2,2,2,1,1])
    # #     plt.title("Paises Campeones del Mundo")
    # #     plt.xlabel("Copas")
    # #     plt.ylabel("Paises")
    # #     plt.annotate("5",xy=(5,"Brasil"))
    # #     plt.annotate("4",xy=(4,"Italia"))
    # #     plt.annotate("4",xy=(4,"Alemania"))
    # #     plt.annotate("2",xy=(2,"Uruguay"))
    # #     plt.annotate("2",xy=(2,"Argentina"))
    # #     plt.annotate("2",xy=(2,"Francia"))
    # #     plt.annotate("1",xy=(1,"Inglaterra"))
    # #     plt.annotate("1",xy=(1,"España"))
    # #     plt.barh(x,y)
    # #     plt.show()
    
    # # def grafico_torta():
        
    # #     valores = [29,21,15,11,9,7,5,3]
    # #     etiquetas = ["Python","Java","javaScript","C#","PHP","C++","MatLab","Ruby"]
    # #     separacion = [0.1,0,0,0,0,0,0,0]
       

    # #     plt.pie(valores, labels=etiquetas, explode=separacion, shadow=True, autopct='%1.1f%%' , startangle=90)
    # #     plt.title("Lenguajes de Programacion mas Utilizados en 2022")
    # #     plt.show()
    
    # # def grafico_interactivo():
        
    # #     print("Hola.. haremos un grafico")



    # # def intro():
    # #     print("")
    # #     print("┌─────────────────────────┬──────────────────────────┬───────────────────────────┐")
    # #     print("| 1 ► Grafico Barra       | 2 ► Grafico Torta        | 3 ► Grafico Interacivo    |")
    # #     print("└─────────────────────────┴──────────────────────────┴───────────────────────────┘")
    # # intro()
        
    # # opcion = int(input("Elije un Grafico: "))

    # # if opcion == 1:
    # #     grafico_barra()
    # # elif opcion == 2:
    # #     grafico_torta()
    # # elif opcion == 3:
    # #     grafico_interactivo()