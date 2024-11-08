function myFunction() {
    var num1 = document.forms["myForm"]["num1"].value;
    var num2 = document.forms["myForm"]["num2"].value;
    var num3 = document.forms["myForm"]["num3"].value;

    var arithmean = (num1 + num2 + num3)/3;
    var geomean = (num1 * num2 * num3) ** 1/3;

    if (num1 == "") {
        alert("Please enter the first number!");
    }
    else if (num2 == "") {
        alert("Please enter the second number!");
    }
    else if (num3 == "") {
        alert("Please enter the third number!");
    }
    else {
        document.getElementById("arithmean").innerHTML = "The arithmetic mean of your numbers is " + arithmean;
        document.getElementById("geomean").innerHTML = "The geometric mean of your numbers is " + geomean;
    }
}