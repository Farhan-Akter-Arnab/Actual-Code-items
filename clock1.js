function showClock() {
    var date = new Date();
    var h = date.getHours();
    var min = date.getMinutes();
    var s = date.getSeconds();
    var session = "AM";
    var d = date.getDay();
    var day = "Sunday";

    if (h==0){
        h = 12;
    }
    if (h > 12){
        h = h - 12;
        session = "PM";
    }
    if (d==0){
        day = "Sunday";
    }
    if (d == 1) {
        day = "Monday";
    }
    if (d == 2) {
        day = "Tuesday";
    }
    if (d == 3) {
        day = "Wednesday";
    }
    if (d == 4) {
        day = "Thursday";
    }
    if (d == 5) {
        day = "Friday";
    }
    if (d == 6) {
        day = "Saturday";
    }
    h = (h < 10) ? "0" + h : h;
    min = (min < 10) ? "0" + min : min;
    s = (s < 10) ? "0" + s : s;
    d = (d < 10) ? "0" + d : d;

    var time = h + ":" + min + ":" + s + " " + session;
    document.getElementById("Clock").innerText = time;
    setTimeout(showClock, 1000);
    document.getElementById("day").innerHTML = "Today is " + day;
}
showClock();