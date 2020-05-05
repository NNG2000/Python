def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    if (num<9) and (num>=0):
        for i in (0,len(grille[row])): ##--verification sur la ligne
            if (grille[row][i] != num):
                return (True)
    ####------------fin de verification sur les lignes

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    if (num<9) and (num>=0):
        for j in (0,len(grille)): ##--verification sur les coolonnes
            if (grille[j][col] != num ):
                return (True)
    ####-----------fin de la verification sur les colonnes

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    if col in (1,4,7):
            if row in (1,4,7):####--on doit parcourir la petite matrice et verifier s'il n'a pas repetition--
                for i in [row-1,row,row+1]:
                    for j in [col-1 , col , col+1]:
                        if grille[i][j]!=num:
                            result=True
                        else:
                            return(False)
            elif row in (0,3,6):####--on doit parcourir la petite matrice-- 
                for i in [row, row+1, row+2]:
                    for j in [col-1, col, col+1]:
                        if grille[i][j]!=num:
                           result=True
                        else:
                            return(False)  
            elif row in (2,5,8):####--on doit parcourir la petite matrice--
                 for i in [row-2, row-1, row]:
                     for j in [col-1, col, col+1]:
                         if grille[i][j]!=num:
                             result=True
                         else:
                            return(False)
    elif col in (0,3,6):
             if row in (1,4,7):####--on doit parcourir la petite matrice et verifier s'il n'a pas repetition--
                 for i in [row-1, row, row+1]:
                     for j in [col , col+1, col+2]:
                         if grille[i][j]!=num:
                            result=True
                         else:
                            return(False)
             elif row in (0,3,6):####--on doit parcourir la petite matrice--
                 for i in [row, row+1, row+2]:
                     for j in [col , col+1, col+2]:
                         if grille[i][j]!=num:
                             result=True
                         else:
                            return(False)
             elif row in (2,5,8):####--on doit parcourir la petite matrice--
                 for i in [row-2,row-1,row]:
                     for j in [col , col+1 , col+2]:
                         if grille[i][j]!=num:
                             result=True
                         else:
                            return(False)
    elif col in (2,5,8):
             if row in (1,4,7):####--on doit parcourir la petite matrice et verifier s'il n'a pas repetition--
                 for i in [row-1,row,row+1]:
                     for j in [col-2 , col-1 , col]:
                         if grille[i][j]!=num:
                             result=True
                         else:
                            return(False)
             elif row in (0,3,6):####--on doit parcourir la petite matrice--
                 for i in [row,row+1,row+2]:
                     for j in [col-2 , col-1 , col]:
                         if grille[i][j]!=num:
                             result=True
                         else:
                            return(False)
             elif row in (2,5,8):####--on doit parcourir la petite matrice--
                 for i in [row-2,row-1,row]:
                     for j in [col-2 , col-1 , col]:
                         if grille[i][j]!=num:
                             result=True
                         else:
                            return(False)
    return(result)
    #---------------------------------- fin du code

def verifierGagner(grille):
    '''
            (list) ->  bool
            Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
            Verifie si la grille est completement remplie.
    '''
    
    for rangee in grille:
       for chiffre in rangee:
           if chiffre==0:          #####------parcourt la grille a la recherche d'un zero
               return False
    return True

  
def verifierValide(grille, row, col, num):
   '''
           (list, int, int, int) ->  bool
           verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
           Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   if (verifierCol(grille, col, num)==True) and (verifierLigne(grille, row, num)==True) and (verifierSousGrille(grille, row, col, num)==True):
       return True
   
   
   

