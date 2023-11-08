document.getElementById("signup-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const username = document.getElementById("signup-username").value;
    const password = document.getElementById("signup-password").value;
    const signupMessage = document.getElementById("signup-message");

    // Send data to the server for registration
    fetch("signup.php", {
        method: "POST",
        body: JSON.stringify({ username, password }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                signupMessage.innerHTML = "Signup successful. You can now login.";
            } else {
                signupMessage.innerHTML = "Signup failed. Try a different username.";
            }
        });
});
