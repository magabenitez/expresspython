'''
Condicionales if en Python
'''

dato=int(input('ingrese un numero: '))
if dato > 0:
    print('el numero es positivo')
elif dato < 0:
    print('el numero es negativo')
else:
    print('el numero es cero')
    
#Un if
if dato % 2 == 0:
    print('el numero es par')   

    #if else
if dato % 2 == 0:
    print('el numero es par')
else:
    print('el numero es impar')
    
    #if elif else
if dato> 0:
    print('el numero es positivo')  
elif dato < 0:
    print('el numero es negativo')
elif dato == 0:
    print('el numero es cero')
else:
    print('el numero es cero')