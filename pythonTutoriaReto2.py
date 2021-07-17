"""
Reto 2
"""

# Ex. 1
variable1 = "OK"
print(variable1)

variable1 = "\"OK\"" # NOK
print(variable1)  # NOK

# Ex. 2
  # v1
entrada = input()
print(entrada, "--", type(entrada))
temporal = entrada + 45  # Error

entrada = int(entrada)  # Cast
                        # Solo para un dato
                        # float(entrada) 
print(entrada, "--", type(entrada))
temporal = entrada + 45

  # v2
entrada = int(input())
print(entrada, "--", type(entrada))

# Ex. 3
variable1 = "Buenos dias compañeros de Python"
variable2 = variable1.split(" ")
print(len(variable2))
print(variable2, "--", type(variable2))
variable2[0]
variable2[1]
variable2[2]

# Ex. 4
  # v1
variable1, variable2, variable3, variable4 = input().split()
variable1
variable2
variable3
variable4
  # v2
newData = input().split()
print(newData, "--", type(newData))

# Ex. 5
  # m to Km
vMetros = 2000
vKm     = vMetros/1000

  # s to hours
     # v1
vSeconds = 7200
vMinutes = vSeconds/60
vHours   = vMinutes/60
     # v2
vSeconds = 7200
vHours   = vSeconds/3600

# Ex. 6 - Percentage
valor = 200
percentage = 4
resultado = valor*percentage/100
print(resultado)

recargo   = valor + resultado
print(recargo)
descuento = valor - resultado
print(descuento)

# Ex. 7
# Sí - Afirmativo  - Yes
# Si - Condicional - IF
num = 0
if num>1:
    print(":) , entró en la sección verdadera")
else: #sino
    print(":( , entró en la sección falsa")
print("1.) Continua el código")
print("2.) Continua el código")
print("3.) Continua el código")

# Ex. 8
choice = 1

if choice==1:
    print("Usted escogió la opción {}".format(choice))
else:
    if choice==2:
        print("Usted escogió la opción {}".format(choice))
    else:
        if choice==3:
            print("Usted escogió la opción {}".format(choice))
        else:
            if choice==4:
                print("Usted escogió la opción {}".format(choice))
            else:
                print("Valor inválido")
print("1.) Continua el código")
print("2.) Continua el código")
print("3.) Continua el código")

# Ex. 9
choice = 4

if choice==1:
    print("Usted escogió la opción {}".format(choice))
elif choice==2:
    print("Usted escogió la opción {}".format(choice))
elif choice==3:
    print("Usted escogió la opción {}".format(choice))
elif choice==4:
    print("Usted escogió la opción {}".format(choice))
else:
    print("Valor inválido")
print("1.) Continua el código")
print("2.) Continua el código")
print("3.) Continua el código")

# Ex. 10
a = 12
b = 20
c = 30
# and
# False and False ==> False
# False and True  ==> False
# True  and False ==> False
# True  and True  ==> True
if a>=12 and b<50 and c!=65:
    print(":) , entró en la sección verdadera")
else:
    print(":( , entró en la sección falsa")
print("1.) Continua el código")
print("2.) Continua el código")
print("3.) Continua el código")

# or
# False and False ==> False
# False and True  ==> True
# True  and False ==> True
# True  and True  ==> True

# Ex. 11
myList = ["10", "11", "12", "13"]
print(myList)
myList =  list(map(int,myList))
print(myList)