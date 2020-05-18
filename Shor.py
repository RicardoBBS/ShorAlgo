import sys
from math import log, ceil
from Quantum import quantum_period


"""
This code is a simplified implementation of the Shor's Algorithm for N=15
The code is  written to run on a 5Qbit IBMQ quantum processor
"""


def main():

    N = 3*5

    print ("\n")
    print ("===========================================")
    print ("             SHOR'S  ALGPRITHM")
    print ("===========================================")
    print ("\n")
    
    #N is the prime factor to be factorized, 
    #    (Currently, the IBMQ processor has 5qbits, 
    #     So the number to be factorized should be less 2^5 = 32)
    
    Check(N)
    
    # for large N's randint() should be used to generate guesses instead of range()
    for a in range(2, N-1): 
        divisor = gcd(a, N)
        if divisor!=1: #we found a non trivial factor of N
            print("Factors found without shor: N=", divisor, " * " , N/divisor)
            break
        else:
            p1, p2 = Shor(N, a)
            if(p1 != 1 and p2 != 1):
                print("Factors found with shor: N =", int(p1), "*", int(p2))
                break
	
    
        
# https://en.wikipedia.org/wiki/Shor%27s_algorithm#Procedure
def Check(N):
    # checks if N is even
    if N % 2 == 0:
        print("Factors found: N =", N/2, "*", 2)
        raise ValueError('N is even, 2 is a trivial factor')
  
    # checks if N has any integer roots N^(1/k), for 2 < k < log2(N)
    for k in range(2,int(log(N,2))):
        root = N**(1/k) 
        if root.is_integer():
            raise ValueError('N has a natural nth root. N = {}^{}'.format(int(root), k))




# https://en.wikipedia.org/wiki/Greatest_common_divisor
def gcd(a, b):   # Compute the GCD with Euclide algorithm
    while b:
        a, b = b, a%b
    return a	
	
	
	
def Shor(N, a):
 
    n_bit = ceil(log(N,2))           # amount of bits necessary for given N
    print('Using {} qubits'.format(n_bit))
 
    # https://en.wikipedia.org/wiki/Shor%27s_algorithm#Finding_the_period
    r = quantum_period(a, N, n_bit)  # Quantum part of the algorithm


    # https://en.wikipedia.org/wiki/Shor%27s_algorithm#Obtaining_factors_from_period
    if r % 2 == 0 :
        if a**(r/2) % N != -1:  
            
            p1 = gcd(a**(r/2)-1,N)
            p2 = gcd(a**(r/2)+1,N)

            print ("\n Attempt N =", int(p1), "*", int(p2))
            if (p1!=1 and p1!=N): 
                return  p1, N/p1
            if (p2!=1 and p2!=N):
                return  p2, N/p2
            return p1, p2        


if __name__ == '__main__':
    main()
        