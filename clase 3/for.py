'''
Ejempo estructura de control for 
'''
#Ejemplo en c++
#for (int i = 0; i < 10; i++) {
# cout << i << endl;
#}
#contador = 10
#for i in range(contador):
 #  print ("El valor de i es: ", i) #imprimir el valor de i
 #print ("Fin del ciclo for") #mensaje al finalizar el bucle
 #Ejemplo con una lista
array = ["futbol", "pc", 18.6, 18, [6, 7, 10.4], True, False]
print(len(array))
array.append("pc")
print(array)
for i in range(len(array)):
    print("El valor del array es:", array[i]) 
print("Fin del bucle for con lista")  #mensaje al finalizar el bucle