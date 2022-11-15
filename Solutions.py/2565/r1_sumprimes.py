import math
[limF, limC], primes, triples = [int(_) for _ in input().split()], [2], 0
# Find prime within range
def isPrime(number):
    # if number < 2 or number%2==0: return False
    # elif number==2: return True
    for denominator in primes: # range(3, number, 2)
        if number/2+1<denominator: break
        elif number%denominator==0: return False
    return True
for prime in range(3, limC*3+1, 2): # limF*3+(0 if limF%2 else 1)
    if isPrime(prime):
        primes.append(prime)
        # Enumerate triple
        # for num1 in range(limF, limC+1):
        #     for num2 in range(num1, limC+1):
        #         for num3 in range(num2, limC+1):
        #             if num1+num2+num3 in primes: triples += 1
        # for prime in primes:
        if prime>=3*limF and prime<=3*limC:
            for num1 in range(limF, limC+1):
                if prime-num1<=2*limC:
                    # for num2 in range(num1, limC+1):
                    #     num3 = prime-num1-num2
                    #     if num2<=num3 and num3<=limC: triples += 1
                    # Calculate pair
                    num2 = num1
                    num3 = prime-num1-num2
                    if num3>limC:
                        num3 = limC
                        num2 = prime-num1-num3
                    if num2<=num3: triples += math.ceil((num3-num2+1)/2)
                    else: break
print(triples)
# Passed