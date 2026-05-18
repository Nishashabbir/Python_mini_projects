# Simple RSA Algorithm

# Step 1: Choose two prime numbers
p = 3
q = 11

# Step 2: Calculate n
n = p * q

# Step 3: Calculate phi
phi = (p - 1) * (q - 1)

# Step 4: Choose e
e = 7

# Step 5: Choose d
d = 3

# Message
msg = 12

print("Original Message =", msg)

# Encryption
c = (msg ** e) % n
print("Encrypted Message =", c)

# Decryption
m = (c ** d) % n
print("Decrypted Message =", m)