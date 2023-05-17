import rsa

def generate():
    (public_key, private_key) = rsa.newkeys(512)
    open("files/public_key.pem", "w").write(public_key.save_pkcs1().decode("utf-8"))
    open("files/private_key.pem", "w").write(private_key.save_pkcs1().decode("utf-8"))

class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.load()

    def load(self):
        self.public_key = rsa.PublicKey.load_pkcs1(open("files/public_key.pem", "rb").read())
        self.private_key = rsa.PrivateKey.load_pkcs1(open("files/private_key.pem", "rb").read())

    def encrypt(self, message):
        return rsa.encrypt(message.encode("utf-8"), self.public_key)

    def decrypt(self, message):
        return rsa.decrypt(message, self.private_key).decode("utf-8")
