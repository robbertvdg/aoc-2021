use crate::utils;

pub fn exercise1() {
    let lines = utils::lines_from_file("./src/day1/input1.txt");
    let ints: Vec<i32> = lines.iter().map(|l| l.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let mut count = -1;
    let mut last_entry = 0;
    for entry in ints {
        if entry > last_entry {
            count+=1;
        }
        last_entry = entry;
    }
    println!("Answer to day 1 exercise 1 is: {}", count)
}
