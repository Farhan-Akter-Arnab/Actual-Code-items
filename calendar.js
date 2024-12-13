function showDateAndDay() {
    var date = new Date();
    var y = date.getFullYear();
    var month = date.getMonth();
    var dt = date.getDate();
    var d = date.getDay();
    var day = "Sunday";

    if (d == 0) {
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

    y = (y < 10) ? "0" + y : y;
    month = (month < 10) ? "0" + month : month;
    dt = (dt < 10) ? "0" + dt : dt;
    d = (d < 10) ? "0" + d : d;

    var time = dt + "." + month + "." + y + " ";
    document.getElementById("date").innerText = time;
    setTimeout(showDateAndDay, 1000);
    document.getElementById("day").innerHTML = "Today is " + day;
}
showDateAndDay();