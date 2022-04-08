# ord('A')  -- retourne le numero ASCII
# chr(65)  -- transforme numero ASCII en Text
# zip() -- sert à fusionner 2 tableaux ensembles (comme une fermeture éclaire) https://www.programiz.com/python-programming/methods/built-in/zip


def XorEncrypt (text, key):

    # Ajuster la taille de la clé ici (si celle ci est plus petite que le texte)

    a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(text, key)]
    s3 = "".join(a_list)
    return s3



text = input("Entrez votre message : ")
key = input("Entrez une clé de chiffrement : ")

# Chiffrement (on stocke le message chiffré dans la variable message_chiffre)
message_chiffre = XorEncrypt(text, key)

# Afficher le message chiffré
print("\nVotre message chiffré =", message_chiffre,"\n")



# Partie déchiffrement
asked_key = input("Entrez la clé : ")
message_dechiffre = XorEncrypt(message_chiffre, asked_key)

print(message_dechiffre)