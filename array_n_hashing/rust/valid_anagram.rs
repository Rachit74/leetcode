use std::collections::HashMap;

fn main() {
    let res = valid_anagarm("race".to_string(), "race".to_string());
    println!("{}", res);

}

fn valid_anagarm(s1: String, s2: String) -> bool {
    if !(s1.len() == s2.len()) {
        return false
    }
    let mut map: HashMap<char, i32> = HashMap::new();

    for c in s1.chars() {
        *map.entry(c).or_insert(0) += 1;
    }

    for c in s2.chars() {
        match map.get_mut(&c) {
            Some(count) => {
                *count -= 1;
                if *count < 0 {
                    return false
                }
            }
            None => return false,
        }
    }
    

    // println!("{:#?}", map);
    return true
}