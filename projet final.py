#la fontion menu qui permet d'afficher les choix de l'utilisateur
def menu():
    n = int(input("0-quitter \n 1-écrire dans le répertoire \n 2-rechercher dans le répertoire \n Votre choix : "))
    if n == 0:
        run = False
    if n == 1:
        adt()
    if n == 2:
        read()
#la fontion adt permet à l'utilisateur d'ajouter un contact
def adt():
    with open('Répertoire_téléphonique','a') as repertoire:
        nom = input('Nom du contact : ')
        if nom == 0:
            menu()
        numero = input('Numéro du contact : ')
        repertoire.write(nom)
        repertoire.write(" : ")
        repertoire.write(numero)
        repertoire.write("\n")
        repertoire.close
    menu()
#la fonction read permet de rechercher un contact grâce a son nom
def read():
    with open('Répertoire_téléphonique','r') as repertoire:
              nom_d = input("Donne un nom : ")
              for line in repertoire:
                  if line.startswith(nom_d):
                      print(line)
    menu()
run = True
while run == True:
    menu()