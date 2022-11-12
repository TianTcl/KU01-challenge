import math
limF, limC = [int(_) for _ in input().split()]
# Find prime within range
primes = [2]
def isPrime(number):
    # if number < 2 or number%2==0: return False
    # elif number==2: return True
    for denominator in primes: # range(3, number, 2)
        if number<denominator: break
        elif number%denominator==0: return False
    return True
for primeCheck in range(3, limC*3+1, 2): # limF*3+(0 if limF%2 else 1)
    if isPrime(primeCheck): primes.append(primeCheck)
del primeCheck
# Enumerate triple
triples = 0
# for num1 in range(limF, limC+1):
#     for num2 in range(num1, limC+1):
#         for num3 in range(num2, limC+1):
#             if num1+num2+num3 in primes: triples += 1
for prime in primes:
    if prime>=3*limF and prime<=3*limC:
        for num1 in range(limF, limC+1):
            if prime-num1<=2*limC:
                for num2 in range(num1, limC+1):
                    num3 = prime-num1-num2
                    if num2<=num3 and num3<=limC: triples += 1
                # Calculate pair
                # _ = prime-num1*2
                # if _ > limC: _ = limC
                # if _ >= num1 and num1+2*_>=prime: triples += math.ceil((_-num1+1)/2)
print(triples)