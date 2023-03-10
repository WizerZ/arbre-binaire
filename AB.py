class AB:  # définition de la classe AB

    # Constructeur de la classe, qui prend en argument la racine de l'arbre, ainsi que ses sous-arbres gauche et droit
    def __init__(self, racine=[None], gauche=None, droite=None):
        self.racine = racine  # stockage de la racine
        self.gauche = gauche  # stockage du sous-arbre gauche
        self.droite = droite  # stockage du sous-arbre droit
    
    # Accesseurs pour la racine, le sous-arbre gauche et le sous-arbre droit
    def get_racine(self):
        return self.racine
    
    def get_gauche(self):
        return self.gauche
    
    def get_droite(self):
        return self.droite
    
    # Mutateurs pour la racine, le sous-arbre gauche et le sous-arbre droit
    def set_racine(self, racine):
        self.racine = racine

    def set_gauche(self, gauche):
        self.gauche = gauche

    def set_droite(self, droite):
        self.droite = droite
    
    # Méthode qui vérifie si l'arbre est vide
    def estVide(self):
        if self.racine == [None]:  # si la racine est None, l'arbre est vide
            return True
        else:
            return False
        
    # Méthode qui calcule la taille de l'arbre (nombre de nœuds)
    def taille(self):
        taille = 0
        if self.get_gauche() != None:  # si le sous-arbre gauche existe, on calcule sa taille
            taille += self.get_gauche().taille()
        if self.get_droite() != None:  # si le sous-arbre droit existe, on calcule sa taille
            taille += self.get_droite().taille()
        return taille + 1  # on ajoute 1 pour compter le nœud courant
    
    # Méthode qui parcourt l'arbre en préfixe et renvoie une liste des valeurs des nœuds dans l'ordre parcouru
    def prefixe(self):
        if self.estVide():  # si l'arbre est vide, on renvoie une liste avec None
            return AB([None])
        prefixe = []
        prefixe += self.get_racine()  # on ajoute la valeur de la racine
        if self.get_gauche() != None:  # si le sous-arbre gauche existe, on ajoute ses valeurs
            prefixe += self.get_gauche().prefixe()
        if self.get_droite() != None:  # si le sous-arbre droit existe, on ajoute ses valeurs
            prefixe += self.get_droite().prefixe()
        return prefixe
    
        # Méthode pour obtenir l'expression postfixe de l'arbre
    def postfixe(self):
        postfixe = []
        # Si le fils gauche n'est pas vide, on ajoute son expression postfixe à la liste
        if self.get_gauche() != None:
            postfixe += self.get_gauche().postfixe()
        # Si le fils droit n'est pas vide, on ajoute son expression postfixe à la liste
        if self.get_droite() != None:
            postfixe += self.get_droite().postfixe()
        # On ajoute la racine de l'arbre à la liste
        postfixe += self.get_racine()
        return postfixe
    
    # Méthode pour obtenir l'expression infixe de l'arbre
    def infixe(self):
        infixe = []
        # Si le fils gauche n'est pas vide, on ajoute son expression infixe à la liste
        if self.get_gauche() != None:
            infixe += self.get_gauche().infixe()
        # On ajoute la racine de l'arbre à la liste
        infixe += self.get_racine()
        # Si le fils droit n'est pas vide, on ajoute son expression infixe à la liste
        if self.get_droite() != None:
            infixe += self.get_droite().infixe()
        return infixe
    
    # Méthode pour obtenir la hauteur de l'arbre
    def hauteur(self):
        # Si l'arbre est vide, sa hauteur est -1
        if self.estVide():
            return -1
        hauteur = 0
        # Si le fils gauche n'est pas vide, on met à jour la hauteur en fonction de la hauteur de ce fils
        if self.get_gauche() != None:
            hauteur = self.get_gauche().hauteur()
        # Si le fils droit n'est pas vide, on met à jour la hauteur en fonction de la hauteur de ce fils
        if self.get_droite() != None:
            if self.get_droite().hauteur() > hauteur:
                hauteur = self.get_droite().hauteur()
        # On retourne la hauteur de l'arbre + 1 (pour prendre en compte la racine)
        return hauteur + 1
    
    # Méthode qui vérifie si l'arbre est un ABR (arbre binaire de recherche)
    def estABR(self):
        # Si l'arbre est vide, c'est un ABR
        if self.estVide():
            return True
        
        # Si le sous-arbre gauche n'est pas vide
        if self.get_gauche() != None:
            # Si la racine du sous-arbre gauche est plus grande que la racine de l'arbre courant, ce n'est pas un ABR
            if self.get_gauche().get_racine() > self.get_racine():
                return False
            # Si le sous-arbre gauche n'est pas un ABR, l'arbre courant n'est pas un ABR non plus
            if not self.get_gauche().estABR():
                return False
        
        # Si le sous-arbre droit n'est pas vide
        if self.get_droite() != None:
            # Si la racine du sous-arbre droit est plus petite que la racine de l'arbre courant, ce n'est pas un ABR
            if self.get_droite().get_racine() < self.get_racine():
                return False
            # Si le sous-arbre droit n'est pas un ABR, l'arbre courant n'est pas un ABR non plus
            if not self.get_droite().estABR():
                return False
        # Si l'arbre respecte toutes les conditions, c'est un ABR
        return True
    
    # Méthode qui vérifie si l'arbre est équilibré
    def estEquilibre(self):
        hauteurGauche = 0
        hauteurDroite = 0
        # Si le sous-arbre gauche n'est pas vide
        if self.get_gauche() != None:
            # Si le sous-arbre gauche n'est pas équilibré, l'arbre courant n'est pas équilibré non plus
            if not self.get_gauche().estEquilibre():
                return False
            # On calcule la hauteur du sous-arbre gauche
            hauteurGauche = self.get_gauche().hauteur()
        # Si le sous-arbre droit n'est pas vide
        if self.get_droite() != None:
            # Si le sous-arbre droit n'est pas équilibré, l'arbre courant n'est pas équilibré non plus
            if not self.get_droite().estEquilibre():
                return False
            # On calcule la hauteur du sous-arbre droit
            hauteurDroite = self.get_droite().hauteur()
        # Si la différence de hauteur entre le sous-arbre gauche et le sous-arbre droit est plus grande que 1, l'arbre n'est pas équilibré
        if abs(hauteurGauche - hauteurDroite) > 1:
            return False
        # Sinon, l'arbre est équilibré
        else:
            return True
    
    # Méthode qui retourne la représentation en chaîne de caractères de l'arbre
    def __str__(self):
        return str(self.prefixe())
    
    def creer_arbre_avec_liste(liste): # méthode pour créer un arbre à partir d'une liste de valeurs
        arbre = AB([liste[0]]) # initialisation de l'arbre avec la première valeur de la liste
        for valeur in liste[1:]: # pour chaque valeur restante dans la liste
            noeud = arbre
            result = None
            while noeud != None: # on parcourt l'arbre jusqu'à trouver le bon emplacement pour la nouvelle valeur
                result = noeud # le dernier noeud visité est stocké dans result
                if valeur < noeud.get_racine()[0]:
                    noeud = noeud.get_gauche()
                else:
                    noeud = noeud.get_droite()
            nouveau_noeud = AB([valeur]) # création d'un nouveau noeud avec la nouvelle valeur
            if valeur < result.get_racine()[0]: # si la nouvelle valeur est plus petite que la racine du dernier noeud visité
                result.set_gauche(nouveau_noeud) # on insère le nouveau noeud à gauche
            else:
                result.set_droite(nouveau_noeud) # sinon on l'insère à droite

        return result # on retourne l'arbre construit
    
    def creer_arbre_avec_fichier(nom_fichier): # méthode pour créer un arbre à partir d'un fichier
        with open(nom_fichier, "r") as fichier: # on ouvre le fichier en mode lecture
            content = fichier.read() # on lit le contenu du fichier
        
        liste = eval(content) # on évalue le contenu du fichier (qui doit être une liste)
        return AB.creer_arbre_avec_liste(liste) # on construit l'arbre à partir de la liste et on le retourne

            
        