use crate::rsa_utils::RSA;

mod rsa_utils;
mod server;
mod schulze;

fn main() {
    server::initialize();
}
