function showTime() {
    var date = new Date();
    var h = date.getHours();
    var min = date.getMinutes();
    var s = date.getSeconds();
    var session = "AM";

    if (h == 0){
        h = 12;
    }
    if (h > 12){
        h = h - 12;
        session = "PM";
    }
     h =  (h < 10) ? "0" + h : h;
     min = (min < 10) ? "0" + min : min;
     s = (s < 10) ? "0" + s : s;

    var time = h + ":" + min + ":" + s + " " + session;
    document.getElementById("MyClockDisplay").innerText = time;
    setTimeout(showTime, 1000);
}
showTime();