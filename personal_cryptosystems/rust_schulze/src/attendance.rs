use std::fs::{File, OpenOptions};
use std::io::{Read, Write};
use sha2::{Sha256, Digest};
use rand::distributions::{Alphanumeric, DistString};

#[derive(Debug)]
pub struct AttendanceUtil {
    session_gen: Vec<String>,
    password: String
}

impl AttendanceUtil {
    pub fn new(password: String) -> AttendanceUtil {
        AttendanceUtil {
            session_gen: Vec::new(),
            password,
        }
    }

    pub fn load() -> AttendanceUtil {
        let mut password = String::new();
        let mut initial_hashes: Vec<String> = Vec::new();

        let pass_file = File::open("data/attendance_password");
        let hash_file = File::open("data/attendance_hashes");

        match pass_file {
            Ok(mut file) => {
                file.read_to_string(&mut password).unwrap();
            },
            Err(_) => {
                let mut file = File::create("data/attendance_password").unwrap();
                password = AttendanceUtil::generate_password();
                file.write_all(password.as_bytes()).unwrap();
            }
        }

        match hash_file {
            Ok(mut file) => {
                let mut unsplit_initial_hashes = String::new();
                file.read_to_string(&mut unsplit_initial_hashes).expect("failed to read attendance hashes");

                if unsplit_initial_hashes == "" {
                    return AttendanceUtil::new(password);
                } else {
                    for hash in unsplit_initial_hashes.split("\n") {
                        if hash != "" {
                            initial_hashes.push(hash.to_string());
                        }
                    }
                }
            },
            Err(_) => {
                File::create("data/attendance_hashes").unwrap();
            }
        }

        AttendanceUtil {
            session_gen: initial_hashes,
            password,
        }
    }

    pub fn generate(&mut self, prev: Option<String>) -> String {
        return match prev {
            Some(prev) => {
                let mut hasher = Sha256::new();
                let to_hash = prev.to_string() + &self.password.to_string();
                let to_hash = to_hash.as_bytes();

                hasher.update(to_hash);
                let mut hasher = hasher.finalize().to_vec().iter().map(|x| format!("{:02x}", x)).collect::<String>();
                hasher.truncate(6);
                hasher
            },
            None => {
                let to_hash = Alphanumeric.sample_string(&mut rand::thread_rng(), 6).to_string() + &self.password.to_string();
                let to_hash = to_hash.as_bytes();

                let mut hasher = Sha256::new();
                hasher.update(to_hash);
                let mut resp = hasher.finalize().to_vec().iter().map(|x| format!("{:02x}", x)).collect::<String>();
                resp.truncate(6);
                self.session_gen.push(resp.clone());
                self.store_initial_hashes();
                resp
            }
        }
    }

    pub fn generate_password() -> String {
        Alphanumeric.sample_string(&mut rand::thread_rng(), 6)
    }

    pub fn store_initial_hashes(&self) {
        let mut file = OpenOptions::new()
            .write(true)
            .truncate(true)
            .open("data/attendance_hashes").unwrap();
        for hash in &self.session_gen {
            file.write_all(hash.as_bytes()).unwrap();
            file.write_all(b"\n").unwrap();
        }
    }

    pub fn check_hash_chain(&mut self, mut chain: Vec<String>) -> i32 {
        let mut count = 0;

        let mut prev = chain.get(0).unwrap().to_string();
        chain.remove(0);

        if self.session_gen.contains(&prev) {
            count += 1;
            self.session_gen.remove(self.session_gen.iter().position(|x| x == &prev.to_string()).unwrap());
            self.store_initial_hashes();
        } else {
            return count;
        }

        for hash in chain {
            let gen_hash = self.generate(Some(prev));
            if gen_hash == hash {
                count += 1;
            } else {
                break;
            }
            prev = gen_hash;
        }

        return count;
    }
}

#[derive(Debug)]
struct AttendanceSets {
    pub attendance_hashes: Vec<String>,
    password: String
}

