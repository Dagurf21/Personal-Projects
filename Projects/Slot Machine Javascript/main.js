// 1. Deposit some money
// 2. Determine number of lines to bet on
// 3. Collect a bet amount
// 4. Spin the slot machine
// 5. CHeck if the user won
// 6. Give the user their winnigs
// 7. Play again ?


// Collect the deposit
// function deposit() {
//  return 1
// }

const prompt = require("prompt-sync")();

const deposit = () => {

    while (true){
        const depositAmount = prompt("Enter a deposit amount: "); // Get input from user
        const numberDepositAmount = parseFloat(depositAmount); // Take str and convert to float and store in variable
        
        // if user input is not a number OR (||) the user amount is less then or equal to 0
        if (isNaN(numberDepositAmount) || numberDepositAmount <= 0) {
            console.log("Invalid deposit amount, try again");
        } else {
            return numberDepositAmount;
        }
    }
};
    
const getNumberOfLines = () => {
    while (true) {
        const lines = prompt("Enter the number of lines to bet on (1-3): ");
        const numberOfLines = parseFloat(lines);
        if (isNaN(numberOfLines) || numberOfLines <= 0 || numberOfLines > 3) {
            console.log("Invalid number of lines, try again.");
        } else {
            return numberOfLines;
        }
    }
};

const getBet = (balance, lines) => {
    while(true) {
        const bet = prompt("Enter the bet per line: ");
        const numberBet = parseFloat(bet);

        if (isNaN(numberBet) || numberBet <= 0 || numberBet > balance / lines) {
            console.log("Invalid bet, try again.");
        } else {
            return numberBet;
        }
    }
};



let balance = deposit();
const numberOfLines = getNumberOfLines();
const bet = getBet(balance, numberOfLines);