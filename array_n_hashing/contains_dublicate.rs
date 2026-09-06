use std::collections::HashSet;

fn contains_dublicate(nums: Vec<i32>) -> bool {
    let mut set = HashSet::new();
    for num in nums {
        // set.insert returns false if a dublicated value is inserted
        // this is used to return early rather than length comparision
        if !set.insert(num) {
            return true;
        }
    }

    false
}