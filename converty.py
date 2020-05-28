#coding:utf-8

i = input("Traducteur : ")
# Met ton texte ici

m = ' '.join(format(ord(x), 'b') for x in i)
# Traduction en cours...

print(m)
# Affichage de la traduction
