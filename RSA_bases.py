from random import randint, randrange
from math import log, isqrt


class Theorem: 

    def Korselt (boundary: int) -> list: 
        ''' KORSELT method which takes CARMICHAEL numbers lower than the boundary '''

        composite_numbers = Prime.Eratosthenes_C_sieve(boundary)
        Carmichael_numbers = []
        
        ## TAKE THE COMPOSITE NUMBERS which SATISFIES THE KORSELT THEOREM
        for composite in composite_numbers: 
            
            factors = Prime.factors (composite)

            c = True
            for factor in factors: 
                
                ## CONDITION 1: (factor * factor) NOT DIVIDE (c)
                condition_two = (composite % (factor * factor) == 0)

                ## CONDITION 2: THE GENERATOR CLASSES DIVIDES ORDER OF
                condition_one = ((composite - 1) % (factor - 1) != 0)

                ## IF BOTH TRUE WE HAVE CARMICHAEL NUMBER
                if (condition_one or condition_two): 
                    c = False
                    break

            if (c == True): 
                Carmichael_numbers.append(composite)

        return (Carmichael_numbers)

    def Carmichael (boundary: int) -> list: 
        ''' Naive method which takes CARMICHAEL numbers lower than the boundary '''

        ## TAKE THE COMPOSITE PSEUDO-PRIMES
        Carmichael_numbers = [pp for pp in Fermat.pseudo_primes (boundary) if len (Prime.factors (pseudo_prime)) > 1]

        return (Carmichael_numbers)

    def Euclides (a: int, b: int) -> (int, int, int): 
        ''' Return the result of the Extended Euclidian Algorithm '''

        if a == 0: 
            return b, 0, 1

        if b == 0: 
            return a, 1, 0

        # INIT THE ALGORITHM VALUES
        dividend, divisor = a, b
        x, x_one = 1, 0
        y, y_one = 0, 1

        while True: 
            
            # UPDATE THE CORE ALGORITHM VALUES
            curr_quotient, curr_remainder = divmod (dividend, divisor)
            x_two = (x - (x_one * curr_quotient))
            y_two = (y - (y_one * curr_quotient))

            # REACH TO GCD (a, b)
            if curr_remainder == 0: 
                return divisor, x_one, y_one
            
            # UPDATE THE ALGORITHM VALUES
            dividend, divisor = divisor, curr_remainder
            x, x_one = x_one, x_two
            y, y_one = y_one, y_two

class Fermat: 

    def composite_test_one (number: int, random=None) -> bool: 
        ''' FERMAT test which assess if NUMBER is COMPOSITE '''
        
        if (random == None): 
            random = randint (2, number)

        if (pow (random, number, number) == (random % number)): 
            return (False)
        else: 
            return (True)
            
    def composite_test_two (number: int, random=None) -> bool: 
        ''' FERMAT test which assess if NUMBER is COMPOSITE '''
        
        if (random == None): 

            random = randint (2, number - 1)

            if ((random % number) == 0): 
                random = randint (2, number - 1)

        if ((random % number) == 0): 
            raise ValueError ("The basis and number has to be co-primes")
        
        if (pow (random, number - 1, number) == 1): 
            return (False)
        else: 
            return (True)

    def pseudo_primes (boundary: int) -> list: 
        ''' Return the PSEUDO-PRIMES lower than the boundary '''
        
        pseudo_primes = [2]
        
        for odd_number in range (3, boundary, 2): 

            for basis in range (2, odd_number + 1): 
                
                if (Fermat.composite_test_one (odd_number, basis)):
                    break
                
                if (basis == odd_number): 
                    pseudo_primes.append (odd_number)
                    break
        
        return (pseudo_primes)

    def factors (number: int) -> (int, int): 
        ''' FERMAT method to return two factors of NUMBER '''

        ## THE METHOD JUST TAKES ODD NUMBERS
        if (number % 2 == 0): 
            return (number // 2, number // 2)

        ## INIT THE X VALUE TO COMPUTE
        x = math.isqrt(number)
        if (x == number): 
            return (x, x)

        while (True): 
            
            x += 1
            y = math.isqrt((x * x) - number)

            ## THE Y IS INTEGER AND WE FOUND TWO FACTORS
            if ((y * y) == ((x * x) - number)): 

                return (x + y, x - y)
            
            ## THE NUMBER IS PRIME
            if (x == (number + 1) // 2): 

                factors = {number: 1}
                return (number, 1)
           
class Prime: 

    def Eratosthenes_C_sieve (boundary: int) -> list: 
        ''' Return COMPOSITE numbers less than the boundary '''

        sieve_vector = [False] * (boundary + 1) 

        ## RECORD THE EVEN COMPOSITE NUMBERS
        for number in range (4, boundary + 1, 2): 

            sieve_vector [number] = True

        ## RECORD THE OOD COMPOSITE NUMBERS
        for number in range (3, (int (boundary ** 0.5)) + 1, 2): 

            if (sieve_vector [number] == False): 
                
                for c in range (number * number, boundary + 1, (2 * number)):
                    sieve_vector [c] = True

        composite_vector = [num for num, number in enumerate (sieve_vector) if number]

        return (composite_vector)

    def Eratosthenes_P_sieve (boundary: int) -> list: 
        ''' Return PRIME numbers less than the boundary '''

        sieve_vector = [True] * (boundary + 1) 

        for number in range (4, boundary + 1, 2): 

            sieve_vector [number] = False

        for number in range (3, (int (boundary ** 0.5)) + 1, 2): 

            for c in range (number * number, boundary + 1, (2 * number)): 

                sieve_vector [c] = False

        sieve_vector [0] = sieve_vector [1] = False

        prime_vector = [number for number, prime in enumerate (sieve_vector) if prime]

        return (prime_vector)


    def Hadamard_number (x: int, e: int) -> int: 
        ''' Return the amount of PRIME numbers between (x) and (x + e) '''

        minimum_value = 10 ** 50
        if (x < minimum_value): 
            raise (ValueError (f"The number is too small, should be at least {minimum_value}"))

        H = int (e // (math.log (x)))
        return (H)

    def Mersenne_number (n: int) -> int: 
        ''' Return the MERSENNE number (M(N) = (2^N) - 1) '''

        M = (2**n) - 1
        return (M)
    
    def Fermat_number (n: int) -> int: 
        ''' Return the FERMAT number (F(N) = (2^N) + 1) '''

        F = (2**n) + 1
        return (F)
    

    def test_MRA (number: int, tests: list = None) -> str: 
        ''' MILLER-RABIN test which assess if NUMBER is PRIME '''

        k = (number - 1)
        even_factors = 0

        if (tests == None): 

            tests = []
            for i in range (10): 

                number = randint (2, number)
                tests.append (number)

        ## COUNT HOW MANY EVEN FACTORS THE (number - 1) HAS
        while ((k % 2) == 0): 

            k //= 2
            even_factors += 1

        ## THE TESTS CAN UNLUCKY TOOK 10 STRONG PSEUDOPRIMES TO EACH BASIS
        for basis in tests: 

            remainder = pow (basis, k, number)

            ## CONTRAPOSITION OF FERMAT THEOREM
            if ((remainder != 1) and (remainder != number - 1)):  

                for factor in range (even_factors + 1): 

                    remainder = ((remainder ** 2) % number)
                    
                    if ((remainder == number - 1) or (remainder == 1)): 
                        break

                    ## WE REACHED TO THE LAST EVEN FACTOR
                    if (factor == even_factors): 
                        return ('False')

        return ('inconclusive')

    def test_BLS (number: int) -> bool: 
        ''' BRILHART, LEHMER and SELFRIDGE test which assess if NUMBER is PRIME '''

        if (number == 2): 
            return True

        n = number - 1
        n_factors = Prime.factors (n)

        for n_factor in n_factors: 

            for b in range (3, n + 1): 
                
                if (pow (b, n, number) != 1): 
                    return (False)

                if (pow (b, (n // n_factor), number) != 1): 
                    break
                
                if (b == n): 
                    return (False)

        return (True)


    def factors (number: int) -> dict: 
        ''' Return the PRIME factors as dict  '''
        
        factors = {}
        iterator = Prime.iterator ()
        iterator_number = next (iterator)

        if (number < 2):
            raise ValueError ("Prime numbers are >= 2")
        if (number == 2): 
            return ({2: 1})
        if (number == 3): 
            return ({3: 1})
        
        try: 
            
            while (number > 1): 
                
                ## ASSES IF THE NUMBER IS COMPOSITE
                if (number % iterator_number == 0): 
                    number //= iterator_number
                    
                    if (iterator_number not in factors): 
                        factors [iterator_number] = 1
                    else: 
                        factors [iterator_number] += 1
                else: 
                    iterator_number = next (iterator)
                
                ## WE REACH TO THE LAST POSSIBLE PRIME DIVISOR
                if (iterator_number ** 2 > number): 
                    
                    if (iterator_number % number == 0): 
                        factors [iterator_number] += 1   
                    else: 
                        factors [number] = 1
                        
                    return (factors)
                
        except KeyboardInterrupt: 
            raise ValueError ("Value not factorized")

    def iterator () -> int: 
        ''' Function which return PRIMES each time called '''

        iterator_list = []
        current = 2 
        
        while True: 

            ## IF (N) IS COMPOSITE SO THE LOWER FACTOR (F) IS (F <= N**0.5)
            break_point = current ** 0.5
            is_prime = True

            ## TAKE THE MANUEL DIVISION TO ASSES IF IS COMPOSITE
            for prime in iterator_list: 
                
                if (prime > break_point): 
                    break
                
                if (current % prime == 0): 
                    is_prime = False
                    break
            
            ## FOUND THE PRIME AND YIELD
            if (is_prime): 
                iterator_list.append (current)
                yield current
                
            current += 1


if (__name__ == '__main__'): 

    n = int (input ("Erastothenes sieve to: "))
    print (f"Primes: {Prime.Eratosthenes_C_sieve (n)}")
