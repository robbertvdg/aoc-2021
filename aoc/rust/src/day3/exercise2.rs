use crate::day3::exercise1::{binary_vec_to_dec, input_to_vecs};

fn is_most_common(v: &Vec<u32>, ints: Vec<Vec<u32>>, i: usize, oxygen: bool) -> bool {
    let mut zeros: u32 = 0;
    let mut ones: u32 = 0;
    for v1 in ints.iter() {
        if v1[i] == 0 {
            zeros += 1
        } else {
            ones += 1
        }
    }
    let mut most_common = 0;

    if zeros == ones {
        most_common = oxygen as u32;
    } else if (ones > zeros) & oxygen {
        most_common = 1
    } else if (ones < zeros) & !oxygen {
        most_common = 1
    }
    return v[i] == most_common;
}

pub fn get_measurement(mut ints: Vec<Vec<u32>>, oxygen: bool) -> Vec<u32> {
    let vec_len = ints[0].len();
    let mut i: usize = 0;
    while i < vec_len {
        ints = ints.clone().into_iter()
            .filter(|v|
                is_most_common(v, ints.clone(), i, oxygen)
            ).collect();
        if ints.len() == 1 {
            break;
        }
        i += 1
    }
    return ints[0].clone();
}

pub fn exercise2() {
    let ints: Vec<Vec<u32>> = input_to_vecs("./src/day3/input1.txt");
    let oxygen = get_measurement(ints.clone(), true);
    let co2scrub = get_measurement(ints.clone(), false);
    println!("Answer to day 3 exercise 2 is: {:?}", binary_vec_to_dec(oxygen) * binary_vec_to_dec(co2scrub));
}
