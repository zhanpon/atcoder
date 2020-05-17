use std::collections::HashSet;

use proconio::{input, marker::Usize1};

fn main() {
    input! {
        n: usize,
        m: usize,
        h: [usize; n],
        ab: [[Usize1; 2]; m],
    }

    let mut good_obs: HashSet<usize> = (0..n).collect();
    for xy in ab {
        let x = xy[0];
        let y = xy[1];

        if h[x] <= h[y] {
            good_obs.remove(&x);
        }

        if h[y] <= h[x] {
            good_obs.remove(&y);
        }
    }

    println!("{}", good_obs.len())
}
