use serde::Deserialize;
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
}

impl DecodedVote {
    pub fn new(decrypted_vote: String, decrypted_attendance: String) -> DecodedVote {
        DecodedVote {
            vote_string: decrypted_vote,
            attendance_string: decrypted_attendance,
        }
    }
}
