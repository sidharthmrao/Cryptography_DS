mod rsa_utils;
mod server;
mod schulze;
mod attendance;

use attendance::AttendanceUtil;

fn main() {
    let mut attend = AttendanceUtil::load();

    server::initialize(&mut attend);
}
