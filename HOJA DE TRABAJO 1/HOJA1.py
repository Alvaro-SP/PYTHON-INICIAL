
#Hoja de trabajo 1
#Ejercicio1
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#Ejemplo 
#El usuario ingresa el numero 5

print("████████████ PROGRAMA QUE MUESTRA UN TRIANGULO RECTÁNGULO  ████████████")
num=int(input("ingrese el numro:    "))
for i in range(num):
    print("*"*(i+1))

print("listo! ... Ahora... :") 


#Ejercicio2
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
print("████████████ PROGRAMA QUE MUESTRA SI UN NUMERO ES PRIMO O NO  ████████████")
num2=int(input("ingrese el numro para ver si es primo o no:    "))
for i in range(2, num):
    if num % i == 0:
        break
if (i + 1)  == num:
    print("El numero  "+ str(num)  +" es primo")
else: 
    print(  "El numero  "+ str(num)  +" no es primo")
print("listo! ") 
