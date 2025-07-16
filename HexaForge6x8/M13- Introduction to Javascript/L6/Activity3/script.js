function validate(event) {
    event.preventDefault();

    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var age = document.getElementById("age").value;
    var messageBox = document.getElementById("validation_message");

    var message;

    if (email === "") {
        message = "Enter an email.";
        messageBox.style.color = "red";
    }
    else if (password === "") {
        message = "Enter a password.";
        messageBox.style.color = "red";
    }
    else if (age === "") {
        message = "Enter an age.";
        messageBox.style.color = "red";
    }
    else {
        message = "For submitted.";
        messageBox.style.color = "green";
    }

    messageBox.innerHTML = message;
}