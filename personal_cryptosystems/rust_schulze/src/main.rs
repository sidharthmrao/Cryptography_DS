mod rsa_utils;
mod server;
mod schulze;
mod attendance;

use attendance::AttendanceGen;

fn main() {
    let mut attend = AttendanceGen::load();
    attend.generate(None);
    attend.store_initial_hashes();

    server::initialize();
}
