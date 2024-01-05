# Library to define functions obtained from GeeksForGeeks 
# to generate large prime numbers

# Link to page: https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/

import random



# Function to generate a number of bit-length k
def nBitRandom(k):
    k_bit_random_number = random.getrandbits(k) | 1
    return k_bit_random_number

#I changed this one as it seemed like this was more efficient than the provided function below

#def nBitRandom(n): 
#   
#    # Returns a random number 
#    # between 2**(n-1)+1 and 2**n-1''' 
#    return(random.randrange(2**(n-1)+1, 2**n-1))






# Function to generate prime candidate using list of smallPrimes
def get_low_level_prime(n):
    '''Generate a prime candidate divisible 
      by first primes'''
    

    #list of smallPrimes
    smallPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

    # Repeat until a number satisfying 
    # the test isn't found 
    while True:  
   
        # Obtain a random number 
        prime_candidate = nBitRandom(512)   #512 specifies how many bits we want this prime number to have
   
        for divisor in smallPrimes:  
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate: 
                break

            # If no divisor found, return value 
            else: 
                return prime_candidate



# Function to test for primality, current level of understanding is beginner, it works though
def isMillerRabinPassed(miller_rabin_candidate): 
    '''Run 20 iterations of Rabin Miller Primality test'''
   
    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1
   
    while evenComponent % 2 == 0: 
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1) 
   
    def trialComposite(round_tester): 
        if pow(round_tester, evenComponent,  
               miller_rabin_candidate) == 1: 
            return False
        for i in range(maxDivisionsByTwo): 
            if pow(round_tester, 2**i * evenComponent, 
                   miller_rabin_candidate) == miller_rabin_candidate-1: 
                return False
        return True
   
    # Set number of trials here 
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials): 
        round_tester = random.randrange(2, 
                       miller_rabin_candidate) 
        if trialComposite(round_tester): 
            return False
    return True


#Initially wrote below function in main, decided it wasn't necessary there and swapped it here to maintain consistency (this file primes, the other file no primes)

#Function to utilize above functions in order to generate actual prime number (used for choosing p and q)
def generate_prime_number():
    i = 0
    while True:
        num = get_low_level_prime(512)
        if isMillerRabinPassed(num) == True:
            #print(num)
            #print(f"\n\nNumber of iterations: ",i)
            break
        i = i + 1
    return num