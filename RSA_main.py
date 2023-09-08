from RSA_bases import *

# ------------------------------------------------------------------
# Utility Functions Section
# ------------------------------------------------------------------

def chinese_remainder_theorem (number: int, p: int, q: int, d: int) -> int: 
    ''' Resolution through Chinese Remainder Theorem '''

    ## REDUCE THE EXPOENTS
    dp = d % (p - 1)
    dq = d % (q - 1)

    ## TAKE THE INVERSES MODULO N
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

def symb_to_code (symbol: str) -> str: 
    ''' Take one symbol and return its code number as str '''
    
    dct = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
    '5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
    '-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
    'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
    'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
    's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
    'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
    'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
    'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
    'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
    'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
    'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
    'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
    'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
    ':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
    '%': 235, '@': 236, ' ': 237, '\n': 238, "'": 245}
    
    return (str (dct [symbol]))

def code_to_symb (code: int) -> str: 
    ''' Take one code number and return its symbol value '''

    dct = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
    116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
    124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
    132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
    139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
    147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
    155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
    163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
    171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
    178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
    186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
    194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
    212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
    219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
    227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
    235: '%', 236: '@', 237: ' ', 238: '\n', 245: "'"}
    
    return (str (dct [code]))
    
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
    ''' Return a PROBABLY random (r) numbers PRIME   '''

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

    ## ENCRYPT THE SECTIONS
    c_text = [int (code) for code in text_code_list]
    c_text = [pow (section, e, modulo) for section in c_text]

    return (c_text)

def decrypt_naive (e_text: list, d: int, modulo: int) -> str: 

    ## DECRYPT THE SECTIONS
    dt_code_sections = [str (pow (section, d, modulo)) for section in e_text]
    
    ## SEPARATE THE SECTIONS IN 3 NUMBERS AGAIN
    dt_codes_value = [section [i:i+3] for section in dt_code_sections for i in range (0, len (section), 3)]
    dt_codes_value = [int (code) for code in dt_codes_value]
    
    ## DECODE THE TEXT
    dt_text = [chr (symb) for symb in dt_codes_value]            

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
    
    n, p, q, e, d = generate_keys ()

    text = input ("Text to encrypt: ")
    encrypted_text = encrypt (text, e, n)

    print (f"\nEncrypted text: {encrypted_text}")
    print (f"Decrypted text: {decrypt_chinese (encrypted_text, p, q, d)}\n")