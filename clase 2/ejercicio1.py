'''
crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par
o si ambos lo son
#si ambos son pares, mostrar el mensaje "ambos son pares"
#si uno es par y el otro impar, mostrar el mensaje "uno es par y el otro impar"

'''



n1= int(input('Ingrese un numero: '))
n2= int(input('Ingrese otro numero: '))

if ((n1%2 ==0) and (n2%2 == 0)):
    print('Ambos son pares')
elif ((n1%2 ==0) and (n2%2 !=0)):
    print(f"{n1} es par")
    print(f"{n2} es impar")
elif ((n1%2 !=0) and (n2%2 == 0)):
    print(f"{n1} es impar")
    print(f"{n2} es par")
else:
    print("los dos numeros son impares")