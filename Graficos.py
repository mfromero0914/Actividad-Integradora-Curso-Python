
import matplotlib.pyplot as plt
import numpy as np
import time

class Graficos():

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


    

    def intro():
        print("")
        print("╔═══════════════════════╦══════════════════════╦══════════════════════════╦════════════════════╗")
        print("║ 1 ► Grafico Barra     ║ 2 ► Grafico Torta    ║ 3 ► Grafico Interacivo   ║ 4 ► Salir          ║")
        print("╚═══════════════════════╩══════════════════════╩══════════════════════════╩════════════════════╝")
        print("")
    intro()
        
    opcion = int(input("Elije un Grafico: "))

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





