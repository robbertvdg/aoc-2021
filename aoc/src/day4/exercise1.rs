use crate::utils;

pub struct Board {
    pub(crate) board: Vec<Vec<i32>>
}

pub trait BingoBoard {
    fn has_bingo(&self) -> bool;
    fn cross_number(& mut self, number: i32);
}

impl BingoBoard for Board {
    fn has_bingo(&self) -> bool {
        if self.board.clone().into_iter()
            .filter(|v|v.iter().sum::<i32>() == -5).collect::<Vec<Vec<i32>>>().len() > 0 {
            return true;
        }
        let mut bingo = false;
        for i in 0..self.board.len() {
            let vert_bingo = self.board.clone().into_iter().filter(|v|v[i] == -1).collect::<Vec<Vec<i32>>>().len();
            if vert_bingo == self.board.len() {
                bingo = true;
            }
        }
        return bingo;
    }

    fn cross_number(&mut self, number: i32) {
        let mut new_board : Vec<Vec<i32>> = Vec::new();
        for v in self.board.clone() {
            let mut new_v : Vec<i32> = Vec::new();
            for el in v {
                if el == number {
                    new_v.push(-1);
                }
                else {
                    new_v.push(el);
                }
            }
            new_board.push(new_v)
        }
        self.board = new_board;
    }
}

pub fn read_input(input: &str) -> (Vec<i32>, Vec<Board>){
    let lines = utils::lines_from_file(input);
    let mut start = true;
    let mut input_sequence: Vec<i32> = Vec::new();
    let mut board: Vec<Vec<i32>> = Vec::new();
    let mut boards: Vec<Board> = Vec::new();
    for line in lines {
        if start {
            input_sequence = line.split(",").map(|l| l.parse::<i32>().unwrap()).collect::<Vec<i32>>();
            start = false;
        } else {
            if line == "" {
                if board.len() == 5 {
                    boards.push( Board { board: board.clone()});
                    board = Vec::new();
                }
            } else {
                board.push(line.split(" ")
                    .into_iter()
                    .filter(|el|el != &"").collect::<Vec<&str>>()
                    .iter()
                    .map(|l| l.parse::<i32>().unwrap()).collect::<Vec<i32>>())
            }
        }

    }
    return (input_sequence, boards)
}

pub fn summed_value(board: Vec<Vec<i32>>) -> i32 {
    let mut sum: i32 = 0;
    for v in board {
        for el in v {
            if el != -1 {
                sum += el;
            }
        }
    }
    return sum;
}

pub fn exercise1(){
    let (inputs, mut boards) = read_input("./src/day4/input1.txt");
    let mut winning_board: Vec<Vec<i32>> = Vec::new();
    let mut last_number = 0;
    'outer: for input in inputs {
        for i in 0..boards.len() {
            boards[i].cross_number(input);
            if boards[i].has_bingo() {
                winning_board = boards[i].board.clone();
                last_number = input;
                break 'outer;
            }
        }
    }
    println!("Answer to day 4 exercise 1 is: {:?}",  summed_value(winning_board) * last_number);
}
