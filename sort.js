var numbers = [50, -27.5, 19, 89, 403, 1000, 6283];
document.getElementById("question").innerHTML = "The numbers are : " + numbers;
function ascending () {
    numbers.sort(function(a,b) {return a - b});
    document.getElementById("ascend").innerHTML = numbers;
}
function descending () {
    numbers.sort(function(a,b) {return b - a});
    document.getElementById("descend").innerHTML = numbers;
}
function transform (num) {
    return ((num + 5) * (num - 10))/2.25;
}
var narray = numbers.map(transform);
var newarray = narray.sort(function(a,b) {return a - b});
document.getElementById("modify").innerHTML = newarray;