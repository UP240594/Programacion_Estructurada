#Matriz de 4x3
#Matriz 
Matriz = [[1,2,3] , 
	[4,5,6],
	[7,8,9],
 	[10,11,12]]

F = len(Matriz) 	# Sacamos los renglones totales
C= len(Matriz[0])  #Se pone esto por ley pq asi sabemos que sacamos el total de renglones en columnas

#Normal
for i in range(F): #filas
	for j in range(C): #Columnas
		print(Matriz[i][j], end="\t")
	print() #Nueva linea después de cada fila

print("----------------")
#Transpuesta
for i in range(C): #filas
	for j in range(F): #Columnas
		print(Matriz[j][i], end="\t")
	print() #Nueva linea después de cada fila

#Se quedan fijo las columnas y se van incrimentando las filas . Primero filas y luego columnas

print("----------------")

#Sacar las diagonales

for i in range(F): #filas
	for j in range(C): #Columnas
		print(Matriz[i][j], end="\t")
	print() #Nueva linea después de cada fila
