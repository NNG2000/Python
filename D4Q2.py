##Auteur: Giorgio Sawaya 
##Numero d'etudiant: 300126961

##Auteur: Geraud Ndagang 
##Numero d'etudiant: 300105965


print("Auteur: Giorgio Sawaya")
print("Numero d'etudiant: 300126961")

print("Auteur: Geraud Ndagang")
print("Numero d'etudiant: 300105965\n")
import math
def modifier_Mat(m):
    for i in range (len(m)):
        for j in range (len(m[0])):
            if (m[i][j]%2 ==0):
                m[i][j]=math.sqrt(m[i][j])
    return (m)

matrice = [[5, 3, 8],[7, 4, 6],[1, 9, 2],[8, 7, 1],[3, 2, 9],[4, 6, 5]]
print(matrice)
print(modifier_Mat(matrice))              
                
