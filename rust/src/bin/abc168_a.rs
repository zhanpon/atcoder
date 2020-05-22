use proconio::input;

fn main() {
    input! {
        n: String,
    }

    let last_char = n.chars().last().unwrap();
    let answer = match last_char {
        '3' => "bon",
        '0' | '1' | '6' | '8' => "pon",
        _ => "hon",
    };

    println!("{}", answer);
}