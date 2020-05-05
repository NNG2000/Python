##Auteur: Giorgio Sawaya 
##Numero d'etudiant: 300126961

##Auteur: Geraud Ndagang 
##Numero d'etudiant: 300105965


print("Auteur: Giorgio Sawaya")
print("Numero d'etudiant: 300126961")

print("Auteur: Geraud Ndagang")
print("Numero d'etudiant: 300105965\n")
from jeuSudoku import *

def afficherGrille(grille):
    '''
    (list) -> None
    Affiche le grille de jeu Sudoku
    Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    print("   ", end="")
    col = 0
    while col < len(grille):
      print(col, end="  ")
      col += 1
    print()
    row = 0
    while row < len(grille):
       print(row, end="")
       col = 0
       while col < len(grille[row]):
         print(" ", grille[row][col], end="")
         col += 1
       print()
       row += 1

def jouer(grille, row, col, num): 
    ''' 
    (list, int, int, int) -> Bool
    Jouer une étape de jeu Sudoku
    Preconditions: grille est une réference sur une liste de 9x9 contient seulement des nombres
    grille est modifié (un element est ajouté dans la grille) si la case est valide est correcte.
    '''
    c=verifierCol(grille, col, num)
    l=verifierLigne(grille, row, num)
    sg=verifierSousGrille(grille, row, col, num)
    if (c==True)and(l==True)and(sg==True):
        return(True)
    #---------------------------------- fin du code
    
# Créer le tableau de jeu (9 x 9)
grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
          [7, 4, 6, 0, 3, 2, 8, 1, 9],
          [1, 9, 2, 0, 8, 4, 3, 5, 6],
          [8, 7, 1, 2, 6, 3, 4, 9, 5],
          [3, 2, 9, 4, 5, 7, 1, 6, 8],
          [4, 6, 5, 9, 1, 8, 7, 2, 3],
          [0, 0, 4, 3, 7, 9, 5, 8, 2],
          [9, 8, 3, 1, 0, 5, 6, 7, 4],
          [2, 5, 0, 8, 4, 6, 9, 3, 1]]  # la seule matrice utilisé dans le programme.
print("Menu: 1- Commencer un nouveau jeu.")
print("     ", "2- Continuer le jeu.")
print("     ", "3- Quitter le jeu.")
while True:
    try :
        choix = int(input("SVP entrez votre choix: 1, 2 ou 3: "))
        break
    except ValueError:
        print("votre choix doit etre 1, 2 ou 3: ")
    
while choix < 3 and choix > 0:
      if choix == 1:
          # Créer le tableau de jeu (9 x 9)
          grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
                    [7, 4, 6, 5, 3, 2, 8, 1, 9],
                    [1, 9, 2, 7, 8, 4, 3, 5, 6],
                    [8, 7, 1, 2, 6, 3, 4, 9, 5],
                    [3, 2, 9, 4, 5, 7, 1, 6, 8],
                    [4, 6, 5, 9, 1, 8, 7, 2, 3],
                    [6, 1, 4, 3, 7, 9, 5, 8, 2],
                    [9, 8, 3, 1, 2, 5, 6, 7, 4],
                    [2, 5, 0, 8, 4, 6, 9, 3, 1]]  # la seule matrice utilisé dans le programme.
      afficherGrille(grille)
      while True:
            try :
                row = int(input("entrez votre choix de case ligne "))
                break
            except ValueError:
                print("votre choix doit etre un entier entre 0 et 8 ")
      while True:
            try :
                col = int(input("entrez votre choix de case col "))
                break
            except ValueError:
                print("votre choix doit etre un entier entre 0 et 8 ")
      
      while True:
            try :
                num = int(input("entrez votre choix de case num "))
                break
            except ValueError:
                print("votre choix doit etre un entier entre 1 et 9 ")
      
      if grille[row][col] == 0:
          ajout = jouer(grille, row, col, num)
          if (ajout == True):
              print("Bravo!!")
              grille[row][col] = num
          else:
              print("Echec :(")
      else:
          print("Case deja rempli")
      afficherGrille(grille)
      if verifierGagner(grille) == True:
          print("Bravo!! Vous avez gagne")
          choix = -1
      else:
         print("Menu: 1- Commencer un nouveau jeu.")
         print("     ", "2- Continuer le jeu.")
         print("     ", "3- Quitter le jeu.")
         choix = int(input("SVP entrez votre choix: 1, 2 ou 3: "))
if choix==3:
    print("Au revoir")
