use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = HashMap::new();

    // enumerate adds index to each element while iteration
    for (i, &num) in nums.iter().enumerate() {
        let complement = target - num;

        // if some value for a key is found, i.e value found for complement
        if let Some(&j) = map.get(&complement) {
            return vec![j as i32, i as i32]
        }

        // insert the num and the index into the hashmap
        map.insert(num, i);
    }

    vec![]
}