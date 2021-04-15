
#PIDO DATOS AL USUARIO
peso=input("ingrese su peso en (kg)")

estatura=input("ingrese su estatura en (m)")

#Calculo el indice de masa corporal

pesoredondeado= round(float(peso))

indice = round(pesoredondeado/float(estatura)**2,2)

print("Tu índice de masa corporal es",indice)
