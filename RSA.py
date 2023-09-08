from Bases import *
from DCS import *


# ------------------------------------------------------------------
# Utility Functions Section
# ------------------------------------------------------------------

def chinese_remainder_theorem (number: int, p: int, q: int, d: int) -> int: 
    ''' Resolution through Chinese Remainder Theorem '''

    ## REDUCE THE EXPOENTS
    dp = d % (p - 1)
    dq = d % (q - 1)

    ## TAKE THE INVERSES
    _, inv_p, inv_q = EEA_natural (p, q)

    ## REDUCE THE MESSAGES
    reduced_number_p = number % p
    reduced_number_q = number % q

    count_a = pow (reduced_number_p, dp, p)
    count_b = pow (reduced_number_q, dq, q)
    number = (count_a + (count_b - count_a) * inv_p)

    return (number)

def EEA_natural (a: int, b: int) -> (int, int, int): 
    ''' Return the natural results of Extended Euclidian Algorithm '''

    abs_a = abs (a)
    abs_b = abs (b)

    gcd, x, y = Theorem.Euclides (abs_a, abs_b)
    x %= abs_b
    y %= abs_a
    
    return (gcd, x, y)

def RSA_test (number: int) -> str: 
    ''' RSA tests to assess if number is PRIME ''' 

    iterator = Prime.iterator ()
    current = next (iterator)
    iterator_list = []

    ## TEST IF HAS FACTOR LOWER THAN 5000
    while (current < 5000): 
        
        iterator_list.append(current)
        if (number % current == 0): 
            return False
    
        current = next (iterator)
    
    ## TEST 10 OF THESE PRIMES AS BASIS IN MILLER-RABIN
    test_list = []
    for i in range (10): 
        test_list.append (iterator_list [randint (1, 5000) % len (iterator_list)])
    if (Prime.test_MRA (number, test_list) == 'False'): 
        return ('False')
    
    return ('inconclusive')

def random_prime (r: int) -> int: 
    ''' Return a PROBABLY (r) digits PRIME  '''

    while True: 

        random = int (randrange ((10 ** r) + 1, (10 ** r) * 100, 2))

        if (RSA_test (random) == 'inconclusive'):
            return (random)


# -------------------------------------------------------------------
# RSA Functions Section
# -------------------------------------------------------------------

def generate_keys (): 

    ## THE PRIME NUMBERS WHOSE FORM MODULO N
    p = random_prime (125)
    q = random_prime (105)

    ## THE TOTAL OF INVERSES MODULO N
    E = (p - 1) * (q - 1)
    
    e = 3
    while (True): 
        
        ## FIND SMALLER KEY WHOSE HAS INVERSE MODULO E
        gcd, d, _ = EEA_natural (e, E)
        
        ## THE PUB_KEY WAS FOUND
        if (gcd == 1): 
            break
        
        e += 2

    return (p * q, p, q, e, d)

def encrypt (text: str, e: int, modulo: int) -> list: 

    ## CHOOSE THE SIZE OF EACH SECTION LESS THAN THE MIN(p, q) 
    section_size = 101 // 3
    
    ## DECODE THE SYMBS IN TEXT
    text_symb_list = [symb_to_code (symb) for symb in list (text)]

    ## SEPARATE THE SYMBS IN SECTIONS
    text_code_list = [''.join(text_symb_list [i:i+section_size]) for i in range (0, len (text_symb_list), section_size)]

    ## EBCRYPT THE SECTIONS
    c_text = [int (code) for code in text_code_list]
    c_text = [pow (section, e, modulo) for section in c_text]

    return (c_text)

def decrypt_naive (e_text: list, d: int, modulo: int) -> str: 

    ## DECRYPT THE SECTIONS
    dt_code_sections = [str (pow (section, d, modulo)) for section in e_text]
    
    ## SEPARATE THE SECTIONS IN 3 NUMBERS AGAIN
    dt_codes_value = [section [i:i+3] for section in dt_code_sections for i in range (0, len (section), 3)]
    dt_codes_value = [int (code) for code in dt_codes_value]
    
    ## ENCODE THE TEXT
    dt_text = [code_to_symb (symb) for symb in dt_codes_value]            

    text = ''    
    for symb in dt_text: 
        text += symb
            
    return (text)

def decrypt_chinese (e_text: list, p: int, q: int, d: int) -> str: 

    ## DECRYPT THE SECTIONS WITG THE CHINESE REMAINDER THEOREM
    dt_code_sections = [str (chinese_remainder_theorem (section, p, q, d)) for section in e_text]

    ## SEPARATE THE SECTIONS IN 3 NUMBERS AGAIN
    dt_codes_value = [section [i:i+3] for section in dt_code_sections for i in range (0, len (section), 3)]
    dt_codes_value = [int (code) for code in dt_codes_value]
    
    ## DECODE THE TEXT
    dt_text = [code_to_symb (symb) for symb in dt_codes_value]            

    text = ''    
    for symb in dt_text: 
        text += symb
            
    return (text)


if (__name__ == '__main__'): 
    
    modulo, p, q, e, d = generate_keys ()

    text = input ("Text to encrypt: ")
    encrypted_text = encrypt (text, e, modulo)

    print (f"\nEncrypted text: {encrypted_text}")
    print (f"Decrypted text: {chinese_decrypt (encrypted_text, p, q, d)}\n")
