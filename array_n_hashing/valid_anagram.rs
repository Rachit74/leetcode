// character counting approach
/*
anagram strings must have same number of frequency of each character, one way is to sort and compare the strings
another is to count characters

1. if strings s and t are not of same length then return false
2. count how many times each character appears in the first string
3. go through the second string and subtract from those counts

If any count goes negative or ends up non-zero, they're not anagrams
 */

fn is_anagram(s: String, t: String) -> bool {
    // compare lengths
    if s.len() != t.len() {
        return false
    }

    let mut count = [0;26]; // creates a fixed size array of 26 elements all intilizaed to 0
    // each index in array would represent a letter

    for ch in s.chars() {
        // ch as u8 converts char into ASCII value
        // b'a' represents byte literal for char a = 97
        // we convert ch to ASCII and subtract 97 from it to finds it's value in array index, a = 97-97 = 0, b = 98-97 = 1
        // then we convert it into usize type for array index
        // increment the count of that index by 1
        count[(ch as u8 - b'a') as usize] += 1;
    }

    // calculate index for each char and sub the count for respective indexes
    for ch in t.chars() {
        let idx = (ch as u8 - b'a') as usize;
        count[idx] -= 1;

        if count[idx] < 0 {
            return false;
        }
    }

    // verify all counts are 0
    // .all() checks if every single element satisfies an condition
    count.iter().all(|&c| c == 0)

}