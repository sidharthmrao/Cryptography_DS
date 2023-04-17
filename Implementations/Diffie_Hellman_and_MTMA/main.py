from dataclasses import dataclass
from mtma_test import mtma


@dataclass
class Actor:
    __private_key: int
    __shared_secret: int = None
    public_key: int = None

    def gen_public_key(self, p, g):
        self.public_key = (g ** self.__private_key) % p

    def gen_shared_secret(self, other_actor, p):
        self.__shared_secret = (other_actor.public_key ** self.__private_key) % p

    def encode_message(self, msg: str):
        encrypted = [int(ord(char) * self.__shared_secret) for char in msg]

        return encrypted

    def decode_message(self, msg: list):
        decrypted = [chr(int(char / self.__shared_secret)) for char in msg]

        return "".join(decrypted)


class Adversary:
    def __init__(self, msg: list, p: int, g: int, actor_1: Actor, actor_2: Actor):
        self.p = p
        self.g = g
        self.actor_1 = actor_1
        self.actor_2 = actor_2
        self.msg = msg

    def decode_message(self):
        iters, b = mtma(p, g, self.actor_2.public_key)
        secret_key = (self.actor_1.public_key ** b) % p

        decrypted = [chr(int(char / secret_key)) for char in self.msg]

        return iters, "".join(decrypted)


message = "Hi Ryan!"
p = 13921  # prime
g = 433  # primitive root

alice = Actor(41)
bob = Actor(245)

alice.gen_public_key(p, g)
bob.gen_public_key(p, g)

alice.gen_shared_secret(bob, p)
bob.gen_shared_secret(alice, p)

encoded_message = alice.encode_message(message)
decoded_message = bob.decode_message(encoded_message)

print(encoded_message)

alice = Adversary(encoded_message, p, g, alice, bob)
# print(alice.decode_message())

total_tries = 0
for i in range(100):
    total_tries += alice.decode_message()[0]

print(total_tries / 100)
