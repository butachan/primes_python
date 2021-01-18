from math import *
def isPrime(n):
    i = 2
    while(i**2 < n+1):
        p = n%i
        if p == 0:
            #print("% 3d est un diviseur de % d " %(i,n) )
            return False
        i+=1
    return True

print(isPrime(1001))

#crible à revoir
def eratosthene(n):
    liste = [i for i in range(n)]
    i = 2
    for i in range(n):
        if isPrime(i):
            for j in range(i+2,n):
                try:
                    liste.remove(j*i)
                except ValueError:
                    pass
    return liste

def primeList(n):
    liste = []
    for i in range(2,n):
        if isPrime(i): liste.append(i)
    return liste

print(eratosthene(45))
print(primeList(100))


#decomposition en facteurs premiers

def facteurs_prime2(n):
    l = []
    i=2
    if isPrime(n): return [n]
    while (not isPrime(n)):
        for i in range(2,ceil(sqrt(n))):
            p = n%i
            if p==0:
                l.append(i)
                n = n/i
    return l

print(facteurs_prime2(1001))
