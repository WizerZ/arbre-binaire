from AB import AB  # Importe la classe AB depuis le module AB

# Crée un arbre vide, vérifie s'il est vide avec la méthode estVide() et affiche le résultat
A1 = AB()
print("Test estVide sur un arbre vide: ",A1.estVide())

# Crée un arbre avec une racine contenant la valeur 5, vérifie s'il est vide avec la méthode estVide() et affiche le résultat
A2 = AB([5])
print("Test estVide sur un arbre avec une racine: ",A2.estVide())

# Crée un nouvel arbre avec une racine contenant la valeur 3
A3 = AB([3])

# Ajoute le noeud A3 comme fils gauche de la racine de l'arbre A2
A2.set_gauche(A3)

# Crée trois arbres AtestGauche, AtestDroite et Atest qui sont des sous-arbres de l'arbre Atest
AtestGauche = AB([5], AB([3], AB([2])), AB([8]))
AtestDroite = AB([12])
Atest = AB([10], AtestGauche, AtestDroite) 

# Affiche diverses informations sur l'arbre Atest
print("Test est vide sur l'arbre Test: ",Atest.estVide())
print("Test taille: ",Atest.taille())
print("Test prefixe: ",Atest.prefixe())
print("Test postfixe: ",Atest.postfixe())
print("Test infixe: ",Atest.infixe())
print("Test hauteur: ",Atest.hauteur())
print("Test estABR: ",Atest.estABR())
print("Test estEquilibre: ",Atest.estEquilibre()) 

# Crée un arbre en lisant les données à partir d'un fichier nommé "data.txt"
arbre = AB.creer_arbre_avec_fichier("data.txt")

# Affiche le parcours postfixe de l'arbre créé à partir du fichier
print("postfixe arbre fichier: ",arbre.prefixe())
print("postfixe arbre fichier: ",arbre.postfixe())
