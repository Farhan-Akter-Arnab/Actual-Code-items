var index = 0;
function carousel() {
    var i;
    var x = document.getElementsByClassName("d-block w-100");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    index++;
    if (index > x.length){
        index = 1;
    }
    x[index - 1].style.display = "block";
    setTimeout(carousel, 2000);
}
carousel();

function showTime() {
    var date = new Date();
    var h = date.getHours();
    var min = date.getMinutes();
    var s = date.getSeconds();
    var tar = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();
    var day = date.getDay();
    var day_ord = "Sunday";
    var session = "AM";

    if (h == 0) {
        h = 12;
    }
    if (h > 12) {
        h = h - 12;
        session = "PM";
    }
    if (day == 0) {
        day_ord = "Sunday";
    }
    if (day == 1) {
        day_ord = "Monday";
    }
    if (day == 2) {
        day_ord = "Tuesday";
    }
    if (day == 3) {
        day_ord = "Wednesday";
    }
    if (day == 4) {
        day_ord = "Thursday";
    }
    if (day == 5) {
        day_ord = "Friday";
    }
    if (day == 6) {
        day_ord = "Saturday";
    }
    h = (h < 10) ? "0" + h : h;
    min = (min < 10) ? "0" + min : min;
    s = (s < 10) ? "0" + s : s;
    tar = (tar < 10) ? "0" + tar : tar;
    month = (month < 10) ? "0" + month : month;
    year = (year < 10) ? "0" + year : year;

    var tarihi = tar + "." + month + "." + year + " " + day_ord;

    var time = h + ":" + min + ":" + s + " " + session + ", " + tarihi;
    document.getElementById("Mathematical_Clock").innerText = time;
    setTimeout(showTime, 1000);
}
showTime();