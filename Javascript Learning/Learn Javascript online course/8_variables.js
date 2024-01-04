/////////
// Let //
/////////

// When first declaring variable have to have let
// ex. 1
// This is okay
let age = 19
age = 12

// ex. 2
// This is not okay
age = 19
age = 12

// ////////
// Const //
///////////

// When there is a variable with const you can not change it later-
// This is okay
// ex.1
const some_int = 15
console.log(some_int)

// This is not! okay
// ex.2
const some_str = "15"
some_str = "123"
console.log(some_str)