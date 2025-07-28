// 1. Deposit some money.
// 2. Determine number of lines to bet on.
// 3. Collect a bet amount.
// 4. Spin the slot machine.
// 5. Check if the user won.
// 6. Give the user their money.
// 7. Play again

const prompt = require("prompt-sync")();

const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

const SYMBOL_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

const deposit = () => {  //This is the newer version which is used by the people
    while (true){

        const depositAmount = prompt("Enter a deposit amount: ");
        const numberDepositAmount = parseFloat(depositAmount);

        if (isNaN(numberDepositAmount) || numberDepositAmount <= 0 ) {
            console.log("Invalid deposit amount, try again")
        } 
        else{
            return numberDepositAmount;
        };
}
}; 

const getNumberOfLines = () => {
    while (true){

        const lines = prompt("Enter number of lines you want to bet on (Max Lines 3):  ");
        const numberOfLines = parseFloat(lines);

        if (isNaN(numberOfLines) || numberOfLines > 3 ) {
            console.log("Invalid number of lines, try again")
        } 
        else{
            return numberOfLines;
        }
}
}; 

const getBet = (balance, lines) => {
    while (true){

        const bet = prompt("Enter the total bet: ");
        const numberOfBet = parseFloat(bet);

        if (isNaN(numberOfBet) || numberOfBet <= 0 || numberOfBet > (balance / lines)) {
            console.log("Invalid bet, try again")
        } 
        else{
            return numberOfBet;
        }
    }
}; 

const spin = () => {
    const symbols = [];
    for ([symbol, count] of Object.entries(SYMBOLS_COUNT)){
        for (let i = 0; i < count; i++){
            symbols.push(symbol);
        }
    }


    const reels = [];
    for (let i = 0; i < COLS; i++) {
        reels.push([]);
        const reelSymbols = [...symbols];

        for (let j = 0; j < ROWS; j++){
            const randomIndex = Math.floor(Math.random() * reelSymbols.length);
            const selectedSymbol = reelSymbols[randomIndex];
            reels[i].push(selectedSymbol);
            reelSymbols.splice(randomIndex, 1);
        }
    }
    return reels;
};

const transpose = (reels) => {
    const rows  =[];
    for (let i = 0; i < ROWS;  i++) {
        rows.push([]); 
        for (let j = 0; j < COLS; j++){
            rows[i].push(reels[j][i])
        }
        return rows
    }

}

const printRows = (rows) => {
    for (const row of rows) {
        let rowString = "";
        for (const [i, symbol] of rows.entries()) {
            rowString += symbol
            if (i != rows.length -1){
                rowString+= " | "
            }
        }
    console.log(rowString)
    }
}


let balance  =  deposit();
const numberOfLines = getNumberOfLines();
const bet = getBet(balance, numberOfLines)
const reels = spin();
const rows = transpose(reels);
printRows(rows)