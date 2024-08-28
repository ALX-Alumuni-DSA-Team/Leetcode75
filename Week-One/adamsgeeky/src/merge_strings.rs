pub struct Solution; // This is the solution to the problem

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::new();
        let mut index = 0;

       while index < word1.len() || index < word2.len() {
            if index < word1.len() {
                result.push(word1.chars().nth(index).unwrap());
            }
            if index < word2.len() {
                result.push(word2.chars().nth(index).unwrap());
            }
            index += 1;
        }
        result
    }
}