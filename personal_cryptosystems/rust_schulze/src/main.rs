mod rsa_utils;
use rsa_utils::RSA;

fn main() {
    let rsa = RSA::load();
    let enc_data = rsa.encrypt("hello world");
    let dec_data = rsa.decrypt(&enc_data);
    println!("{}", dec_data);
}
