var num;
var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var stopped = true;
var t;

function change() {
    var random = Math.floor(Math.random()*10);
    num.innerHTML = nums[random];
}
function stopstart() {
    if (stopped) {
        stopped = false;
        t = setInterval(change, 180);
    } else {
        clearInterval(t);
        stopped = true;
    }
    if (nums%2 != 1) {
        stopped = false;
        t = setInterval(change, 180);
    } else {
        clearInterval(t);
        stopped = true;
    }
}
window.onload = function() {
    num = document.getElementById("num");
    stopstart();
}