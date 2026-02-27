use std::collections::HashMap;

fn main() {

    let nums: Vec<i32> = vec![3,4,5,6]; // target 7


}

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, usize> = HashMap::new();

    for (i, &num) in nums.iter().enumerate() {
        let diff = target - num;

        match map.get(&diff) {
            Some(&j) => return vec![j as i32, i as i32],
            None => {}
        }

        map.insert(num, i);
    }

    vec![]
}