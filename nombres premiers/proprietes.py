from basePrime import *
#godbach : tout n pair >3 = somme de 2 premiers
def godbach(n):
    l = primeList(n)
    m = "yo"
    for i in l:
        j = n-i
        if j in l :
            m = "les deux elements sont " + str(i) + " et " + str(j)
    return m

print(godbach(78))

#tout n >12 = somme de 2 composés
def listcompose(n):
    l = []
    for i in range(2,n+1):
        if (not isPrime(i)): l.append(i)
    return l
print(listcompose(54))

def godbach2(n):
    l = listcompose(n)
    m = "hi"
    for i in l:
        j = n-i
        if j in l :
            m = "les deux elements composés sont " + str(i) + " et " + str(j)
    return m
print(godbach2(78))

#nombre de fermat : 2^(2^n)+1 pas toujours premier
def Fer(n):
    x = 2**(2**n) + 1
    print(x)
    if isPrime(x): return True
    return False

print(Fer(4))

#100 entiers consécutifs non premiers
def factoriel(n):
    if n ==0 or n ==1 : return 1
    else:
        f= 1
        for i in range(2,n+1):
            f = f*i
        return f

A = factoriel(101)+1
print(A)
print(isPrime(A))
for i in range(A,A+101):
    if isPrime(i): print('{} is prime'.format(i))
print('that\' all')
#
def NonPrimeSequence(n):
    i = n
    while(i < n+101):
        if isPrime(i):
            print("%d is prime" %(i))
            return False
        i+=1
    print('{} to {} does not contain prime'.format(n, n+100))   
    return True

NonPrimeSequence(A)

def findShortestSeq(n):
    for i in range(1000,n):
        if NonPrimeSequence(i):
            print("{
            return True
        
