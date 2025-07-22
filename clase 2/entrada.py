'''
entrada de datos por teclado
'''

#ejemplo final 
cadena = input('ingrese nombre de su proyecto:')
print('el nombre de su proyecto es:', cadena)


numero = int(input('¿Que version es?:'))
print(f'la version del proyecto es: {numero+1}')





#ejemplo 1
nombre = input('ingrese su nombre:')
apellido = input('ingrese su apellido:')
cadena = nombre + ' ' + apellido
print('hola', cadena)


#Otras maneras de realizarlo

nombre = input('ingrese su nombre:')
apellido = input('ingrese su apellido:')
print("nombre", nombre, "apellido", apellido)
print(f"nombre: {nombre} apellido: {apellido}")