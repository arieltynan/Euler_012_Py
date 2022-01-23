# Highly divisible triangular number

import math

#Factor generator function
    #Output factors to list
def primeFactors(n):
    pf = [] #array of prime factors
    while n % 2 == 0:
        pf.append(2)
        n=n/2
    for j in range(3,int(math.sqrt(n))+1,2):
        while n % j == 0:
            pf.append(j)

            n = n/j
    if n > 1:
        pf.append(n)
    #print(pf)

    #Convert pfs to total number of divisors 
    powers = []
    solo_primes = list(dict.fromkeys(pf))
    for prime in solo_primes: #counts # of each prime in factors list
        powers.append(pf.count(prime)) #array of powers of each factor
    #print(powers) #prints power of each prime factor

    #Multiply all elements in list
    tf = 1
    for x in powers:
        tf = tf*(x + 1) #tf is total factors
    return tf


#Triangular number generator
    #Ouput array of triangle nums

tri = [] #array of triangle numbers
i = 1
#while divisors < 500
for count in range(1,100000):
    tri.append(i)
    i = 1 + i + count
#print(tri) #prints all triangle numbers

cond = 0
for n in tri:
    if primeFactors(n) > 500: #if more than 500 factors, break
        break
print(n) #answer