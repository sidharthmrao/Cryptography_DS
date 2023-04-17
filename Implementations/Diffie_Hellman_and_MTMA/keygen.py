p = 23
g = 5

alice_secret_a = 4

A = (g**alice_secret_a) % p

bob_secret_b = 3

B = (g**bob_secret_b) % p

alice_secret = (B**alice_secret_a) % p
bob_secret = (A**bob_secret_b) % p

print(alice_secret)
print(bob_secret)