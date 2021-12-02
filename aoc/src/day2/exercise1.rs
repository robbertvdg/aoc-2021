use crate::utils;

pub fn exercise1() {
    let lines = utils::lines_from_file("./src/day2/input1.txt");
    let mut horizontal = 0;
    let mut depth = 0;
    for line in lines {
        let instruction= line.split(" ").collect::<Vec<&str>>();
        let amount = instruction[1].parse::<i32>().unwrap();
        match instruction[0] {
            "forward" => {
                horizontal += amount
            }
            "down" => {
                depth += amount
            }
            "up" => {
                depth -= amount
            }
            _ => {
                panic!("Wrong input")
            }

        }
    }
    println!("Day 2 exercise 1 answer: {}", horizontal * depth)
}
