async function product(a,b) {
    let response = await a*b;
    display(response);
}
function display(math) {
    document.getElementById("result").innerHTML = math;
}
product(86.6, 15);