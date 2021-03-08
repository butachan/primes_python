from random import *
"""prérequis: l'inverse modulo : euclide étendu"""

def Bezoutcoef(a,b):
    r0 = a
    r1 = b
    u0 = 1
    v0 = 0
    u1 = 0
    v1 = 1
    while r1 > 0:
        r2 = r0 % r1 #reste
        q = r0 // r1
        r0 = r1 #diviseur devient dividande
        r1 = r2 #reste devient diviseur
        u2 = u0 - q*u1
        v2 = v0 - q*v1
        u0,v0 = u1,v1
        u1,v1 = u2,v2
    return r0, u0, v0
        
        
def Inversemod(x,p):
    r , u , v = Bezoutcoef(p,x)
    if r > 1 :
        print('{} n\'est pas inversible modulo {}'.format(x,p))
        return None
    return v

"""reste chinois à 2 équations : """
#resoudre n = a[p] et n = b[q]
def Resteschinois(a,p ,b, q):
    invP = Inversemod(p,q)
    invQ = Inversemod(q,p)
    n = a * q * invQ + b * p * invP
    N = n%(p*q)
    return N
"""peut être utiliser pour traiter les équations par paire"""


#fonctions pour faire produit des éléments d'une liste
def produit(x, y): return x * y
# [a, b, c] -> callback(callback(a, b), c)
def reduce(callback, liste, valeur_initiale):
    if liste == []: return valeur_initiale
    else: return callback(liste[0], reduce(callback, liste[1:], valeur_initiale))


def ResteChinois(*equations):
    taille = len(equations)
    restes = [] 
    modules = [] #nombres premiers entre eux
    coeffmod = []
    coeffinv = []
    for i in range(taille):
        restes.append(equations[i][0])
        modules.append(equations[i][1]) 
    M= reduce(produit, modules,1) #modulo du resultat final
    for i in range(len(modules)):
        coeffmod.append(M/modules[i])
        coeffinv.append(Inversemod(coeffmod[i], modules[i]))

    resultat = [restes[i]*coeffmod[i]*coeffinv[i] for i in range(taille)]
    resultat = sum(resultat)
    resultat = resultat%M
    return restes, resultat

def ResteAvecErreur(*equations):
    taille = len(equations)
    j = randint(0,taille-1) #la j-ieme équation sera fausse
    xj_rj = randint(0,20) # 
    restes = [] 
    modules = [] 
    coeffmod = []
    coeffinv = []
    for i in range(taille):
        restes.append(equations[i][0])
        modules.append(equations[i][1])
    restes[j] = restes[j] + xj_rj #on fausse le reste d'une équation
    M= reduce(produit, modules,1) 
    for i in range(len(modules)):
        coeffmod.append(M/modules[i])
        coeffinv.append(Inversemod(coeffmod[i], modules[i]))

    resultat = [restes[i]*coeffmod[i]*coeffinv[i] for i in range(taille)]
    resultat = sum(resultat)
    resultat = resultat%M
    return restes, resultat


print( ResteChinois((1,3),(3,5),(2,7),(8,13)) )
print(ResteAvecErreur((1,3),(3,5),(2,7),(8,13)))
x = ((1,3),(3,5),(2,7),(8,13))

#-------pi supplémentaires------------
"""on construit les(n-k) pi supplémentaires"""
"""on fait une liste de nombres premiers"""
def IsPrime(p):
    i = 2
    while(i**2 < p+1):
        k = p%i
        if k == 0:
            return False
        i+=1
    return True

#liste des nombres premiers entre pk et n
def PrimeListe(pk, n):
    liste = []
    for i in range(pk,n):
        if IsPrime(i): liste.append(i)
    return liste


def NbPremiersSuivants(x, n_k, primeMax):
    listeSupplements = []
    pk = max(x)
    for pi in PrimeListe(pk+1,primeMax):
        while(len(listeSupplements)<n_k):
            listeSupplements.append(pi)
    listeTotale = x + listeSupplements
    return listeSupplements , listeTotale

def Pisupplementaires(x ,n_k, primeMax):
    liste = [i for i in range(2,primeMax)]
    for i in liste:
        for j in x:
            if (Bezoutcoef(i,j)[0] > 1):
                liste.remove(i)
                break
    return liste    

