var values = [5, 0.25, 0.085, 30, 10, 2.548];
document.getElementById("info").innerHTML = "The values are " + values;
function kmtom(value) {
    return value * 1000;
}
var obtained = values.map(kmtom);
document.getElementById("kmtom").innerHTML = "The converted values from km to m are: " + obtained;