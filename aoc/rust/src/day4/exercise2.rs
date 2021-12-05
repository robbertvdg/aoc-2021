use crate::day4::exercise1::{read_input, BingoBoard, summed_value};

pub fn exercise2(){
    let (inputs, mut boards) = read_input("./src/day4/input1.txt");
    let mut last_board: Vec<Vec<i32>> = Vec::new();
    let mut last_number = 0;
    'outer: for input in inputs {
        let mut to_remove: Vec<usize> = Vec::new();
        for i in 0..boards.len() {
            boards[i].cross_number(input);
            if boards[i].has_bingo() {
                if boards.len() == 1 {
                    last_board = boards[i].board.clone();
                    last_number = input;
                    break 'outer;
                }
                else {
                    to_remove.push(i)
                }
            }
        }
        for i in to_remove.into_iter().rev() {
            boards.remove(i);
        }
    }
    println!("Answer to day 4 exercise 2 is: {:?}",  summed_value(last_board) * last_number);
}