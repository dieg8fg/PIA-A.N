import numpy as np 

print("******* MATRIZ INVERSA POR ADJUNTOS *******\n\n")

#Se le pide al usuario tamaño de matriz NxN
filas = int(input("Cantidad de filas: "))
columnas = int(input("cantidad de columnas: "))
while (filas != columnas):
    print("\n La matriz debe ser cuadrada")
    filas = int(input("\nCantidad de filas: "))
    columnas = int(input("cantidad de columnas: "))
    
matriz= [] #Arreglo donde se guardará la Matriz A
det=float  #variable para determinante de A
while (det != 0):
    for i in range(filas):
        valor=[]
        for j in range(columnas):
            j= int(input("Ingrese un numero en ("+str(i+1)+","+str(j+1)+") : "))
            valor.append(j)
        print()
        matriz.append(valor)

    for i in range(filas): #ciclo que imprime matriz A
        for j in range(columnas):
            print(matriz[i][j],end=" ")
        print()

    det= np.linalg.det(matriz) #Fn que calcula el determinante de A
    print("det(A): "+str(det))


