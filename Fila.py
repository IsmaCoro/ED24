import os

os.system('cls' if os.name == 'nt' else 'clear')



fila = []
#Añadir elementos a la fila

fila.append('Cliente1')
fila.append('Cliente2')
fila.append('Cliente3')
fila.append('Cliente4')

print("Los elementos de la Fila son" , fila)

#Atender al elemento por orden en la fila
Cliente_Atendido = fila.pop(0)
print("Cliente fue atendido" , Cliente_Atendido)
print("LAs filas despues de atendera un cleinte son:" , fila)
