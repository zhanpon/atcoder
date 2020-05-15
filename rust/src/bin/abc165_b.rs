use proconio::input;

fn main() {
    input! {
        x: i64,
    }

    let mut year: i64 = 0;
    let mut balance: i64 = 100;
    while balance < x {
        year += 1;
        balance += balance / 100;
    }

    println!("{}", year);
}
