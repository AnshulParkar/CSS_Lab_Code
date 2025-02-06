# Function to calculate the GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse using the Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Step 1: Define functions for generating n and phi(n)
def calculate_n(p, q):
    return p * q

def calculate_phi(n, p, q):
    return (p - 1) * (q - 1)

# Step 2: Generate public exponent e (we are using 7 as e in this case)
def choose_e(phi_n):
    e = 7  # Given in the problem
    while e >= phi_n or gcd(e, phi_n) != 1:  # Ensure gcd(e, phi(n)) == 1
        e = 7  # Fixed e as 7
    return e

# Step 3: Calculate the private exponent d (modular multiplicative inverse of e mod phi(n))
def calculate_d(e, phi_n):
    return mod_inverse(e, phi_n)

# Step 4: RSA encryption and decryption functions
def encrypt(plaintext, e, n):
    ciphertext = [pow(char, e, n) for char in plaintext]
    return ciphertext

def decrypt(ciphertext, d, n):
    plaintext = [pow(char, d, n) for char in ciphertext]
    return plaintext  # Return integer values directly, no conversion to characters

# Step 5: Example usage
def rsa_example(p, q):
    n = calculate_n(p, q)
    phi_n = calculate_phi(n, p, q)
    
    # Public exponent e is given as 7
    e = choose_e(phi_n)
    
    # Private exponent d
    d = calculate_d(e, phi_n)
    
    print(f"Public key (n, e): ({n}, {e})")
    print(f"Private key (n, d): ({n}, {d})")
    
    # Example encryption and decryption with plaintext as integer 88 (ASCII value of 'X')
    plaintext = [88]  # Plaintext is just the integer 88 (ASCII value of 'X')
    
    print(f"Plaintext: {plaintext}")
    
    ciphertext = encrypt(plaintext, e, n)
    print(f"Encrypted: {ciphertext}")
    
    decrypted_text = decrypt(ciphertext, d, n)
    print(f"Decrypted: {decrypted_text}")

# Example primes p and q
p = 17  # First prime number
q = 11  # Second prime number

# Run the RSA example
rsa_example(p, q)
