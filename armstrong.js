function armstrong(num) {
    const numString = num.toString();
    const numDigits = numString.length;
    let sum = 0;

    for (let digits of numString) {
        sum += Math.pow(parseInt(digits), numDigits);
    }
    if (numString == sum) {
        document.write(numString + " is an Armstrong number <div>");
    }
    else {
        document.write(numString + " is not an Armstrong number <div>");
    }
}
armstrong(153)
armstrong(370)
armstrong(10)