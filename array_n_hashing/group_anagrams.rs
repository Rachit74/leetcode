use std::collections::HashMap;

/// Groups words that are anagrams of each other.
/// 
/// Anagrams are words with the same letter counts (e.g., "eat" and "tea").
fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    // Key: [a-z] letter frequency array, Value: all words matching that pattern
    let mut map: HashMap<[i32; 26], Vec<String>> = HashMap::new();

    for s in strs {
        // Count occurrences of each letter in the current word
        let mut count = [0; 26]; // index 0 = 'a', 1 = 'b', ..., 25 = 'z'

        for ch in s.chars() {
            // Convert 'a' to 0, 'b' to 1, etc.
            count[(ch as u8 - b'a') as usize] += 1;
        }

        // All anagrams share the same count array, so they'll go in the same bucket
        map.entry(count).or_insert_with(Vec::new).push(s);
    }

    // Return all buckets as a list of word groups
    map.into_values().collect()
}