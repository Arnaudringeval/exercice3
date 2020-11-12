a = 5
print(a)
b = 8.2
print(a +b)

a = b+ 1
print(a)

c = 1
c = c + 3
print(c)

a, b = 4, 5.2


print(type(a))
print(type(b))

chaine = 'Et voilà prout bisous aujourd\'hui'
print(chaine)

var = 10
print(type(var))
var = str(var)
print(type)

reponse = input() # Une ligne vide apparait et attend que l'utilisateur entre une information

age = input("Age : ") # "Age : " est affiché en début de ligne puis attend une information

# `age` et `reponse` contiennent ce que l'utilisateur a entré

age = int(input("quel age avez vous?"))

if age > 18:
    print("vous êtes mageur")
elif age < 9:
    print("débile")
else:
    print("connard")