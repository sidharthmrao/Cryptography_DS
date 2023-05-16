use rsa::{Oaep, Pkcs1v15Encrypt, RsaPrivateKey, RsaPublicKey};
use rand;
use rsa::pkcs1::{EncodeRsaPrivateKey, EncodeRsaPublicKey, DecodeRsaPublicKey, DecodeRsaPrivateKey};
use sha2;

fn generate(rng: &mut rand::rngs::ThreadRng) -> (RsaPublicKey, RsaPrivateKey) {
    let bits = 2048;
    let private_key = RsaPrivateKey::new(rng, bits).expect("failed to generate a key");
    let public_key = RsaPublicKey::from(&private_key);

    public_key.write_pkcs1_der_file("data/public_key.der").expect("failed to write public key");
    private_key.write_pkcs1_der_file("data/private_key.der").expect("failed to write private key");

    return (public_key, private_key);
}

struct KeyPair {
    public_key: RsaPublicKey,
    private_key: RsaPrivateKey,
}

struct RSA {
    key_pair: KeyPair,
    rng: rand::rngs::ThreadRng,
}

impl RSA {
    fn new() -> RSA {
        let mut rng = rand::thread_rng();
        let (public_key, private_key) = generate(&mut rng);
        RSA {
            key_pair: KeyPair {
                public_key,
                private_key,
            },
            rng,
        }
    }

    fn load() -> RSA {
        let mut rng = rand::thread_rng();
        let public_key = DecodeRsaPublicKey::read_pkcs1_der_file("data/public_key.der").expect("failed to read public key");
        let private_key = DecodeRsaPrivateKey::read_pkcs1_der_file("data/private_key.der").expect("failed to read private key");

        RSA {
            key_pair: KeyPair {
                public_key,
                private_key,
            },
            rng,
        }
    }

    fn encrypt(&self, message: &str) -> Vec<u8> {
        let padding = Oaep::new::<sha2::Sha256>();
        let enc_data = self.key_pair.public_key.encrypt(&mut rand::thread_rng(), padding, message.as_bytes()).expect("failed to encrypt");
        return enc_data
    }

    fn decrypt(&self, message: &Vec<u8>) -> String {
        let padding = Oaep::new::<sha2::Sha256>();
        let dec_data = self.key_pair.private_key.decrypt(padding, message).expect("failed to decrypt");
        let data = String::from_utf8(dec_data).expect("failed to convert to string");
        return data
    }
}

fn main() {
    let rsa = RSA::load();
    let enc_data = rsa.encrypt("hello world");
    let dec_data = rsa.decrypt(&enc_data);
    println!("{}", dec_data);
}
