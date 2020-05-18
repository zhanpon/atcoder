use proconio::input;

fn main() {
    input! {
        s: String,
        t: String,
    }

    let answer = if t.starts_with(&s) { "Yes" } else { "No" };
    println!("{}", answer);
}
