
import random
import time

# class Juego_PPT():

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


   
        

 




   

















# import random
# import time

# class Juego_PPT():

#     # print("")
#     # print("╔═════════════════════════════════════════╗")
#     # print("║      Juego PIEDRA - PAPEL - TIJERA      ║")
#     # print("╚═════════════════════════════════════════╝")
#     # # print("")
#     # # print("Hola...! Juguemos a!!!")
#     # print("")
#     # print("P_I_E_D_R_A....")
#     # print("")
#     # time.sleep(1)
#     # print("     P_A_P_E_L...")
#     # print("")
#     # time.sleep(1)
#     # print("           T_I_J_E_R_A..!!!")
#     # print("")
#     # time.sleep(1)

    

#     def opcion_jugador():
#         player1 = input("Haz tu jugada:  piedra - papel - tijera -- / salir: ")    
    
#         while player1 != "piedra" and player1 != "papel" and player1 != "tijera":

#             if player1 == "salir":
#                 time.sleep(1)
#                 print("")
#                 print("░░░░░░░░░░░░░░░░░░░░░░")
#                 print("░░┌──┐░░░░░░░░░░┌──┐░░")
#                 print("░╔╡▐▐╞╝░░┌──┐░░╔╡▐▐╞╝░")
#                 print("░░└╥╥┘░░╚╡▌▌╞╗░░└╥╥┘░░")
#                 print("░░░╚╚░░░░└╥╥┘░░░░╚╚░░░")
#                 print("░░░░░░░░░░╝╝░░░░░░░░░░")
#                 print("")
#                 print("Gracias por Participar..!!")
#                 break

#             print("Por favor ingrese una opcion valida.")
#             player1 = input("Haz tu jugada:  piedra - papel - tijera -- / Salir: ")

#         return player1

#     def opcion_cpu():
#         player_cpu = random.choice(["piedra","papel","tijera"])
#         print("")
#         # print("Mi jugada fue",player_cpu)
#         return player_cpu
    

#     ron = 0
#     gan = 0
#     emp = 0
#     per = 0


   
   

#     player1 = opcion_jugador()
#     player_cpu_1 = opcion_cpu()

#     if player1 == "papel" and player_cpu_1 == "papel":
#         time.sleep(1)
#         print("Me has Empatado...!!! ")
#         print("Mi jugada fue",player_cpu_1)
#         emp = emp + 1
    
#     elif player1 == "papel" and player_cpu_1 == "piedra":
#         time.sleep(1)
#         print("Me has Ganado...!!!")
#         print("Mi jugada fue",player_cpu_1)
#         gan = gan + 1

#     elif player1 == "papel" and player_cpu_1 == "tijera":
#         time.sleep(1)
#         print ("Perdiste...!!")
#         print("Mi jugada fue",player_cpu_1)
#         per = per + 1

#     elif player1 == "piedra" and player_cpu_1 == "papel":
#         time.sleep(1)
#         print ("Perdiste...!!")
#         print("Mi jugada fue",player_cpu_1)
#         per = per + 1

#     elif player1 == "piedra" and player_cpu_1 == "piedra":
#         time.sleep(1)
#         print("Me has Empatado...!! ")
#         print("Mi jugada fue",player_cpu_1)
#         emp = emp + 1

#     elif player1 == "piedra" and player_cpu_1 == "tijera":
#         time.sleep(1)
#         print ("Perdiste...!!")
#         print("Mi jugada fue",player_cpu_1)
#         per = per + 1

#     elif player1 == "tijera" and player_cpu_1 == "papel":
#         time.sleep(1)
#         print("Me has Ganado...!!!")
#         print("Mi jugada fue",player_cpu_1)
#         gan = gan + 1

#     elif player1 == "tijera" and player_cpu_1 == "piedra":
#         time.sleep(1)
#         print ("Perdiste...!!")
#         print("Mi jugada fue",player_cpu_1)
#         per = per + 1

#     elif player1 == "tijera" and player_cpu_1 == "tijera":
#         time.sleep(1)
#         print("Me has Empatado...!!! ")
#         print("Mi jugada fue",player_cpu_1)
#         emp = emp + 1
    
#     print("")
#     opcion = str(input("¿Quieres volver a jugar? si / no: "))
#     if opcion == str("si"):
#         opcion_jugador()
    

    
#     time.sleep(1)
#     print("╔════════════════════════════╦═════════╗")
#     print("║> RONDAS                    ║",ron,"      ║")
#     print("╠════════════════════════════╬═════════╣")
#     print("║> GANADAS                   ║",gan,"      ║")
#     print("╠════════════════════════════╬═════════╣")
#     print("║> PERDIDAS                  ║",per,"      ║")
#     print("╠════════════════════════════╬═════════╣")
#     print("║> EMPATADAS                 ║",emp,"      ║")
#     print("╚════════════════════════════╩═════════╝")

        