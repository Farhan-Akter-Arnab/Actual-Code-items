window.onload = function() {
    var value = 0;
    var appendValue = document.getElementById("value");
    var buttonIncr = document.getElementById("button-increment");
    var buttonDecr = document.getElementById("button-decrement");
    var buttonReset = document.getElementById("button-reset");
    
    buttonIncr.onclick = function() {
        value = value + 1;
        appendValue.innerHTML = value;
    }
    buttonDecr.onclick = function() {
        value = value - 1;
        appendValue.innerHTML = value;
    }
    buttonReset.onclick = function() {
        value = 0;
        appendValue.innerHTML = value;
    }
}