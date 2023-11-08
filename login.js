document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    const loginMessage = document.getElementById("login-message");

    // Send data to the server for login
    fetch("login.php", {
        method: "POST",
        body: JSON.stringify({ username, password }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                loginMessage.innerHTML = "Login successful. Redirecting...";
                window.location.href = "dashboard.html";
            } else {
                loginMessage.innerHTML = "Login failed. Check your credentials.";
            }
        });
});
