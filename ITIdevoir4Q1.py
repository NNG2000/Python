##Auteur: Giorgio Sawaya 
##Numero d'etudiant: 300126961

##Auteur: Geraud Ndagang 
##Numero d'etudiant: 300105965


print("Auteur: Giorgio Sawaya")
print("Numero d'etudiant: 300126961")

print("Auteur: Geraud Ndagang")
print("Numero d'etudiant: 300105965\n")


##Création de deux dictionnaires : entrpot, qui représente les quantités en stock et prix, qui représente les prix unitaires

entrepot = {"bureau":9, "chaise":25, "imprimante":46, "scanneur":17}
prix = {"bureau":75.9, "chaise":50.9, "imprimante":32.5, "scanneur":28.0}


def validerCommande(article1,quantité1, article2, quantité2, article3, quantité3):
    ''' Str, Int, Str, Int, Str, Int --> Bool
        Vérifie que les articles demandées existent et sont disponibles '''

    if ((article1 in entrepot.keys()) and (quantité1 <= entrepot[article1]) and (article2 in entrepot.keys()) and (quantité2 <= entrepot[article2]) and (article3 in entrepot.keys()) and (quantité3 <= entrepot[article3])) == True:
            return True

    else:
        return False


def calculPrix(article,quantité):

    ''' Str, Int --> float
        Prend en paramètre un article et la quantité de l'article et va retourner la multiplication entre
        le prix unitaires de l'article et la quantité commandée'''
    
    return prix[article] * quantité  



def calculTotal(article1,quantité1, article2, quantité2, article3, quantité3):
    ''' Str, Int, Str, Int, Str, Int --> float
        Cette fonction additionne tout les articles commandées '''

    coût = calculPrix(article1, quantité1)+ calculPrix(article2, quantité2)+ calculPrix(article3, quantité3)

    return coût



##Interface, Ici on demande à l'utilisateur d'entrer les données nécessaires à la commande et on s'assure que les valeurs 
##entrées ne seront pas à la source d'erreur. 

article1=str(input('Entrez le premier article:'))

while True:
    try:
        quantité1= int(input('Entrez la quantité de votre 1ère article:'))
        break
    except ValueError:
        (print('Invalide, SVP essayer encore.'))
        
article2=str(input('Entrez le deuxième article:'))

while True:
    try:
        quantité2= int(input('Entrez la quantité de votre 2ème article:'))
        break
    except ValueError:
        (print('Invalide, SVP essayer encore.'))
        

article3=str(input('Entrez le troisième article:'))

while True:
    try:
        quantité3= int(input('Entrez la quantité de votre 3ème article:'))
        break
    except ValueError:
        (print('Invalide, SVP essayer encore.'))
        


Validation = validerCommande(article1,quantité1, article2, quantité2, article3, quantité3)

if Validation == False:
    print('\nVotre commande est annulée, SVP vérifier les quantités disponibles ou le nom des articles')
    print('\nLes quantités disponibles après l\'achat sont: ',entrepot)   
    
else:
    prixFinal = calculTotal(article1,quantité1, article2, quantité2, article3, quantité3)
    print('Le prix total de votre commande est: ', prixFinal, ' $. Merci!')
    entrepot[article1]= entrepot[article1]-quantité1
    entrepot[article2]= entrepot[article2]-quantité2
    entrepot[article3]= entrepot[article3]-quantité3
    print('\n Les quantités disponibles après l\'achat sont: ',entrepot) 
    

 



 
    

    
    
    
