
#Hoja de trabajo 2
#Ejercicio1
#Escribir un programa que almacene una cadena de caracteres de  
# contraseña en una variable, ingresada por el usuario, pregunte 
# al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin 
# tener en cuenta mayúsculas y minúsculas.

print("████████████ PROGRAMA QUE VERIFICA LA CONTRASEÑA INGRESADA  ████████████")
pal = input("Ingresa la contraseña: ")
contra = input("Introduce la contraseña: ")
if pal == contra.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")


#Ejercicio2
#Ejercicio2
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al 
# sexo y el nombre. El grupo A esta formado por las mujeres con un nombre 
# anterior a la M y los hombres con un nombre posterior a la N y el grupo 
# B por el resto. Escribir un programa que pregunte al usuario su nombre y 
# sexo, y muestre por pantalla el grupo que le corresponde.

print("████████████ PROGRAMA QUE PREGUNTA NOMBRE Y SEXO Y MUESTRA GRUPO QUE PERTENECE  ████████████")
nombre = input("Dime... cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")
if (sexo == "M" and nombre.lower() < 'm') or (sexo == "H" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es " + grupo)