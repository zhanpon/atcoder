use std::io;

fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();

    stdin.read_line(&mut buf).unwrap();
    let n: usize = buf.trim().parse().unwrap();
    buf.clear();

    stdin.read_line(&mut buf).unwrap();
    let s = buf.trim();

    if n % 2 != 0 {
        println!("No");
        return
    }

    let m = n / 2;

    let former = &s[..m];
    let latter = &s[m..];
        
    if former == latter {
        println!("Yes");
    } else {
        println!("No");
    }
}
