use std::collections::HashMap;

fn top_K_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut map = HashMap::new();

    for num in &nums {
        // find map key for num and increase the value (freq) by 1, if not found then insert key and value
        // .or_insert returns an refrence, hence we need to derefrence
        *map.entry(*num).or_insert(0) += 1;
    }

    // we use bucket sort
    // we create 7 buckets, which is equal to max possible frequency
    // each bucket is a vec and each index of the vector represnets frequency of num
    let mut buckets = vec![Vec::new(); nums.len() + 1];

    // place elements in bucket by frequency
    for (num, freq) in map {
        buckets[freq as usize].push(num);
    }

    let mut results = Vec::new();

    // we iterate in reverse to get higest freq elements first and iterate as long as length of results is k
    for bucket in buckets.into_iter().rev() {
        for num in bucket {
            results.push(num);
            if results.len() == k as usize {
                return results;
            }
        }
    }

    results
}