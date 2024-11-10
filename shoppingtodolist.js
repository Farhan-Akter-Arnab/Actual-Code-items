var myForm = document.getElementById("myForm");
var myInput = document.getElementById("myInput");
var myItem = document.getElementById("myItem");
myForm.addEventListener("submit",
function(event){
        event.preventDefault()
        createItem(myInput.value)
})
function createItem(inputItems){
    var items = `<li>${inputItems}
    <button onclick="deleteElement(this)" style="background-color: red; color: white; padding: 5px; font-weight: bold;">Delete</button></li>`
    myItem.insertAdjacentHTML("beforeend", items)
    myInput.value=""
    myInput.focus()
}
function deleteElement(ElementToDelete){
    ElementToDelete.parentElement.remove()
}