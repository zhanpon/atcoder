use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
    }

    let mut snukes = HashSet::new();
    for _ in 0..k {
        input! {
            d: usize,
            a: [i32; d]
        }

        for x in a {
            snukes.insert(x);
        }
    }

    println!("{}", n - snukes.len());
}
