use crate::utils;

pub fn exercise2() {
    let lines = utils::lines_from_file("./src/day1/input1.txt");
    let ints: Vec<i32> = lines.iter().map(|l| l.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let mut window: Vec<i32> = vec![];
    let mut count = -1;
    let mut last_sum = 0;
    for entry in ints {
        if window.len() < 3 {
            window.push(entry)
        } else {
            window.remove(0);
            window.push(entry);
        }
        let sum: i32 = window.iter().sum();
        if (window.len() == 3) & (sum > last_sum) {
            count += 1
        }
        last_sum = sum
    }
    println!("Answer to day 1 exercise 2 is: {}", count)
}
