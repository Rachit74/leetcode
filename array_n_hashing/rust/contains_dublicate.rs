use std::collections::HashSet;

fn main() {
    let arr: Vec<i32> = vec![1,2,3,4,5, 4];

    let res = contains_dublicate(arr);
    println!("{}", res);
}

fn contains_dublicate(nums: Vec<i32>) -> bool {
    let mut set: HashSet<i32> = HashSet::new();

    for num in nums {
        if set.contains(&num) {
            return false
        }
        set.insert(num);
    }
    return true
}