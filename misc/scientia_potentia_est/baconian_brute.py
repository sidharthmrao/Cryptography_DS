import string
from itertools import zip_longest

ciphertext_old = "001010111001001001110110100001"
ciphertext = "1001001101101001010110100101011010101101001001011001001001100110011011001010"
ciphertext_new = ciphertext.replace("0", "2").replace("1", "0").replace("2", "1")
for i in zip_longest(*[iter(ciphertext_new)]*5, fillvalue=""):
    i = int("".join(i), 2)
    print(string.ascii_lowercase[i-1], end="")

ciphertext2 = ciphertext.replace("0", "-").replace("1", ".")
ciphertext3 = ciphertext.replace("0", ".").replace("1", "-")
ciphertext4 = ciphertext[::-1].replace("0", "-").replace("1", ".")
ciphertext5 = ciphertext[::-1].replace("0", ".").replace("1", "-")
print(ciphertext2)
print(ciphertext3)
print(ciphertext4)
print(ciphertext5)
