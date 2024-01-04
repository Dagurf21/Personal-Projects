const language = "JavaScript"

// NOTE ! you cannot use minus numbers inside the brackets use .at() to get minus index
let first_char = language[0]; // First character
let second_char = language[1]; // Second character
let third_char = language[2]; // Third character

// Combining with length
let second_to_last = language[ language.length - 2 ]; // "p" bc. 10 - 2 = 8

// At certain index
let first_index = language.charAt(0)      // "J"
let second_index = language.charAt(1)     // "a"
let last_index = language.charAt(-1)      // "t"
let nexr_last_index = language.charAt(-2) // "p"