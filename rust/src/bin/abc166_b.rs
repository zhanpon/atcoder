use std::collections::HashSet;

use proconio::{input, marker::Usize1};

fn main() {
    input! {
        n: usize,
        k: usize,
        d: [[u32]; k],
    }

    let snukes: HashSet<u32> = d.into_iter().flatten().collect();
    let ans = n - snukes.len();
    println!("{}", ans);
}
