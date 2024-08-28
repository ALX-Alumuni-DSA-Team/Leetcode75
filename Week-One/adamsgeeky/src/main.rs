// Date: 10/10/2021
// Author: AdamsGeeky
// Problem Source: https://leetcode.com/problems/merge-strings-alternately/

// Import the modules
mod merge_strings;
use merge_strings::Solution;

fn main() {
    // Test 
    let word1 = String::from("abc");
    let word2 = String::from("pqr");
    let result = Solution::merge_alternately(word1.clone(), word2.clone());
    println!("Merged: {}",result); 

    let word1 = String::from("ab");
    let word2 = String::from("pqrs");
    let result = Solution::merge_alternately(word1.clone(), word2.clone());
    println!("Merged: {}",result); 

    let word1 = String::from("abcd");
    let word2 = String::from("pq");
    let result = Solution::merge_alternately(word1.clone(), word2.clone());
    println!("Merged: {}",result);
}