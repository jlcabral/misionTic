"""
Reto 3
"""

# Ex. 1
   # v1
entrada = input()
print(entrada, "--", type(entrada))
temporal = entrada + 12   # Error

entrada = int(entrada)  # Válida para un solo dato
                        # Números con decimal. ==> float(entrada)
print(entrada, "--", type(entrada))
temporal = entrada + 12   # Ok
print(temporal)

  # v2
entrada = int(input()) # Válido, solo para un dato
print(entrada, "--", type(entrada))

# Ex. 2
  # v1
userPreferences = [3,      4,      35,        4]
     #            #banos - #Hab. - time2job - #parques
  # v2
userPreferences = {"banos":3 , "hab":4 , "time2job":35 , "parques":4}
userPreferences["banos"]

# Ex. 3
    # 1.) ==> Acquisition section
       # 1.1.) ==> Houses number   (1 línea)

       # 1.2.) ==> Houses features (N líneas)

    # 2.) ==> Preferences evaluation

# Ex. 4
       # 1.2.) ==> Houses features (N líneas)
registerNumber = 5
for i in range(0, registerNumber):
    print( "Value of i is: {}".format(i) )
print("1.) Continua el código")
print("2.) Continua el código")

# Ex. 5
  # v1
newData = list("3 3 36 2 5500".split(" "))
print(newData, "--", type(newData))
print(newData[3], "--", type(newData[3]))
newData =  list(map(int,newData))  # <== !!!!
print(newData, "--", type(newData))
print(newData[3], "--", type(newData[3]))

  # v2
newData =  list( map(int, list("3 3 36 2 5500".split(" "))) )
print(newData)

# Ex. 6 - Multilist
db = []
db

newData =  list( map(int, list("3 3 36 2 5500".split(" "))) )
print(newData, "--", type(newData))
db.append(newData)
print(db)

newData =  list( map(int, list("45 87 32 11 100000".split(" "))) )
print(newData, "--", type(newData))
db.append(newData)
print(db)
print(db[0])
print(db[0][3])
print(db[1][2])

# Ex. 7
newData = [10, 33, 84, 765]
if newData[0]==50 and newData[1]>=12 and newData[1]<70 and newData[2]!=68:
    print(":) , entró en la sección verdadera")
else:
    print(":( , entró en la sección falsa")
print("1.) Continua el código")
print("2.) Continua el código")
#and 
# False and False ==> False
# False and True  ==> False
# True  and False ==> False
# True  and True  ==> True

