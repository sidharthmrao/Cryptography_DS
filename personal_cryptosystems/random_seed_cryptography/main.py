import random


class F:
    def __init__(self, filepath: str):
        self.filepath = filepath
        seed = open(self.filepath, "r").read()
        self.r = random.Random(seed)

    def encrypt(self, m):
        m = m.encode("utf-8")
        c = b""
        for byte in m:
            c += bytes([byte ^ self.r.getrandbits(8)])

        new_seed = self.gen_new_seed()
        open(self.filepath, "w").write(str(new_seed))

        self.r = random.Random(new_seed)

        return c

    def decrypt(self, c):
        m = b""
        for byte in c:
            m += bytes([byte ^ self.r.getrandbits(8)])

        new_seed = self.gen_new_seed()
        open(self.filepath, "w").write(str(new_seed))

        self.r = random.Random(new_seed)

        return m.decode("utf-8")

    def gen_new_seed(self):
        return self.r.getrandbits(32)
