// Int to string

let a = 156;
let b = 153_123;

let a_string = a.toString();
let b_string = b.toString();

// String to int
let c = "42";
let c_int = Number.parseInt(str, 10); // Number.parseInt(string, radix)
// radix == base of numerical system

let d = "123abc";
let e = "5 meters";

let d_int = Number.parseInt(d, 10) // 123
let e_int = Number.parseInt(e, 10) // 5