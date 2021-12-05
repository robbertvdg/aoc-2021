use crate::utils;

pub fn input_to_vecs(input: &str) -> Vec<Vec<u32>>{
    let lines = utils::lines_from_file(input);
    let mut ints: Vec<Vec<u32>> = Vec::new();
    for line in lines {
        ints.push(line.chars()
            .map(| l | l.to_digit(10).unwrap_or(0))
            .collect())
    }
    return ints;
}

pub fn binary_vec_to_dec(input: Vec<u32>) -> isize {
    let mut binary_string = String::new();
    let mut i = 0;

    while i < input.len() {
        binary_string.push_str(&*input[i].to_string());
        i+=1;
    }
    return isize::from_str_radix(&*binary_string, 2).unwrap();
}

pub fn exercise1(){

    let ints: Vec<Vec<u32>> = input_to_vecs("./src/day3/input1.txt");
    let len_ints: u32 = ints.len() as u32;
    let mut sums: Vec<u32> = Vec::new();
    for v in ints {
        if sums.len() == 0 {
            sums = v;
        } else {
            sums = sums.iter().zip(v.iter()).map(|(&a, &b)| a + b).collect::<Vec<u32>>();
        }
    }
    let gamma: Vec<u32> = sums.iter().map(|s|(s> &(len_ints / 2)) as u32).collect();
    let epsilon: Vec<u32> = sums.iter().map(|s|(s< &(len_ints / 2)) as u32).collect();
    let gamma_dec = binary_vec_to_dec(gamma);
    let epsilon_dec = binary_vec_to_dec(epsilon);

    println!("Answer to day 3 exercise 1 is: {}",  gamma_dec*epsilon_dec);
}
