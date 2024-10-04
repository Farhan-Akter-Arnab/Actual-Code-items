function validate(e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgBox = document.getElementById("message").value;

    let message = ''
    if (email === '') {
        message = 'Please enter an email!';
        msgBox.style.color = red;
    } else if (password === '') {
        message = 'Password should be at least 8 characters long!';
        msgBox.style.color = red;
    } else if (age === '') {
        message = 'Age must be between 12 and 200'
        msgBox.style.color = red;
    }

    else {
        message = 'Login succesful!'
        msgBox.style.color = green;
    }

    msgBox.innerText = message;
}