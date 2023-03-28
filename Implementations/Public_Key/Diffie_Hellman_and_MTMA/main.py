from dataclasses import dataclass


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
        msg = msg.encode("utf-8")
        c = b""
        for byte in msg:
            c += bytes([byte ^ self.__shared_secret])

        return c

    def decode_message(self, msg: bytes):
        m = b""
        for byte in msg:
            m += bytes([byte ^ self.__shared_secret])

        return m.decode("utf-8")


message = "Hi Ryan!"
p = 23
g = 5

alice = Actor(4)
bob = Actor(3)

alice.gen_public_key(p, g)
bob.gen_public_key(p, g)

alice.gen_shared_secret(bob, p)
bob.gen_shared_secret(alice, p)

encoded_message = alice.encode_message(message)
decoded_message = bob.decode_message(encoded_message)

print(encoded_message)
print(decoded_message)
