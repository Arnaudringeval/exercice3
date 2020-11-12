#a = 5
#print(a)
#b = 8.2
#print(a +b)

#a = b+ 1
#print(a)

#c = 1
#c = c + 3
#print(c)

#a, b = 4, 5.2


#print(type(a))
#print(type(b))

#{chaine = 'Et voilà prout bisous aujourd\'hui'
#print(chaine)

#var = 10
#print(type(var))
#var = str(var)
#print(type)

#reponse = input() # Une ligne vide apparait et attend que l'utilisateur entre une information

#age = input("Age : ") # "Age : " est affiché en début de ligne puis attend une information

# `age` et `reponse` contiennent ce que l'utilisateur a entré

#age = int(input("quel age avez vous?"))

#if age > 18:
#    print("vous êtes mageur")
#elif age < 9:
#   print("débile")
#else:
#   print("connard")#

#print(7 > 5 < 1)


#couleur = input("couleur?")
#poids = int(input("poids?"))
#if couleur == "rouge":
#   if poids == "10 kg":
#       print (couleur, poids)
#   else:
#       print(poids)
#else:
#   print("pas rouge gros")

#if couleur == "rouge" and poids > 10:
#    print(couleur, poids)

#if couleur == "verte" or poids == 15:
#    print(couleur, poids)

#i = 0
#while i < 10:
#    i += 1
#    if i%2 == 0:
#        continue
#    print(i)

def affiche_menu():
    print("menu:")
    print("Action 1")
    print("Action 2")

affiche_menu()

def prout(texte):
     print('# '  + texte)

prout('bonjour')
prout('au revoir')

def addition(a, b):
    return a + b

print(addition(5, 10))