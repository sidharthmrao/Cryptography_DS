use std::fs::OpenOptions;
use std::io::Write;
use serde::Deserialize;
use crate::attendance::AttendanceUtil;
use crate::rsa_utils::RSA;

#[derive(Deserialize, Debug)]
pub struct Vote {
    pub vote_string: Vec<u8>,
    pub attendance_string: Vec<u8>,
}

impl Vote {
    pub fn decode(&mut self) -> DecodedVote {
        let rsa = RSA::load();
        let decrypted_vote = rsa.decrypt(&self.vote_string);
        let decrypted_attendance = rsa.decrypt(&self.attendance_string);

        return DecodedVote::new(decrypted_vote, decrypted_attendance);
    }
}

#[derive(Deserialize, Debug)]
pub struct DecodedVote {
    pub vote_string: String,
    pub attendance_string: String,
    pub weightage: u32,
}

impl DecodedVote {
    pub fn new(decrypted_vote: String, decrypted_attendance: String) -> DecodedVote {
        DecodedVote {
            vote_string: decrypted_vote,
            attendance_string: decrypted_attendance,
            weightage: 0,
        }
    }

    pub fn encode(&self) -> Vote {
        let rsa = RSA::load();
        let encrypted_vote = rsa.encrypt(&self.vote_string);
        let encrypted_attendance = rsa.encrypt(&self.attendance_string);

        return Vote {
            vote_string: encrypted_vote,
            attendance_string: encrypted_attendance,
        }
    }

    pub fn determine_weightage(&mut self, attendance: &mut AttendanceUtil) {
        self.weightage = attendance.check_hash_chain(self.attendance_string.split(",").map(str::to_string).collect::<Vec<String>>()) as u32;
    }

    pub fn write_to_file(&self, file_name: &str) {
        let mut file = OpenOptions::new()
            .append(true)
            .open(file_name)
            .unwrap();

        file.write_all((self.vote_string.clone() + " " + &self.weightage.to_string()).as_bytes()).unwrap();
        file.write_all("\n".as_bytes()).unwrap();
    }
}
