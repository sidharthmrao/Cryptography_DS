from _sha1 import sha1
from rsa_utils import decrypt
from rsa_utils import key
from Crypto.Util.number import getPrime

print(key.gen_keys(1024, getprime_func=getPrime))


def pass_hash(hash, key=""):
    return sha1((hash + key).encode("utf-8")).hexdigest()

passkey = "hashes_are_interesting"

initial_hashes = []

for i in "abcdefghijklmnopqrstuvwxyz":
    initial_hashes.append(pass_hash(i))


votes = []
