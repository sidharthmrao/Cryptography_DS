use std::fmt::format;
use std::{fs, thread};
use std::io::{BufRead, BufReader, Read, Write};
use std::net::{TcpListener, TcpStream};
use serde::Deserialize;
use serde_json;
use crate::schulze::Vote;
use threadpool::ThreadPool;

pub fn initialize() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        })
    }
}

pub fn handle_connection(mut stream: TcpStream) {
    let mut buf_reader = BufReader::new(&mut stream);

    let request_line = buf_reader.by_ref().lines().next().unwrap().unwrap();

    let mut status_line = "";
    let mut contents = "";
    let mut length = 0;

    if request_line == "POST /votes HTTP/1.1" {
        let mut request = buf_reader.lines().into_iter();
        let mut request_body: Vec<String> = vec!();

        let mut begin_pushing: bool = false;

        for line in request.by_ref() {
            let line = line.unwrap();

            if line == "{" {
                begin_pushing = true;
                request_body.push(line);
            } else if line == "}" {
                request_body.push(line);
                break;
            } else if begin_pushing {
                request_body.push(line);
            }
        }

        let body = request_body.concat();

        let mut vote: Vote = serde_json::from_str(&body).unwrap();
        println!("{:?}", vote.decode());

        status_line = "HTTP/1.1 200 OK";
        contents = "OK";
        length = contents.len();
    } else {
        status_line = "HTTP/1.1 502 Bad Gateway";
        contents = "Bad Gateway";
        length = contents.len();
    }

    stream.write_all(&*format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}").as_bytes()).unwrap();
}
