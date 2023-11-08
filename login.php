<?php
// Handle login request
$data = json_decode(file_get_contents("php://input"));
$username = $data->username;
$password = $data->password;

// Database connection
$conn = new mysqli("localhost", "root", "Nightowl@123", "userdb");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT password FROM users WHERE username = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $username);
$stmt->execute();
$stmt->bind_result($hashed_password);
$stmt->fetch();

if (password_verify($password, $hashed_password)) {
    $response = ["success" => true];
} else {
    $response = ["success" => false];
}

echo json_encode($response);
$conn->close();
