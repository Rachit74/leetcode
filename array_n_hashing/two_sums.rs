use std::collections::HashMap;

/// Finds two numbers in the array that add up to the target.
/// Returns their indices as a vector [index1, index2].
/// 
/// Assumes exactly one solution exists and you can't use the same element twice.
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    // Key: number from the array, Value: its index
    let mut map = HashMap::new();

    // Loop through the array with both index and value
    for (i, &num) in nums.iter().enumerate() {
        // The number we need to find to reach the target
        let complement = target - num;

        // Check if we've already seen the complement earlier
        if let Some(&j) = map.get(&complement) {
            // Found it! Return the stored index and current index
            return vec![j as i32, i as i32];
        }

        // Haven't seen this number yet, store it for future lookups
        map.insert(num, i);
    }

    // Should never reach here (problem guarantees a solution exists)
    vec![]
}