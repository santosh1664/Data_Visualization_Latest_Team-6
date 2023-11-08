<?php
// Handle signup request
$data = json_decode(file_get_contents("php://input"));
$conn = new mysqli("localhost", "root", "Nightowl@123", "userdb");
$username = $data->username;
$password = password_hash($data->password, PASSWORD_BCRYPT);

// Database connection
$conn = new mysqli("nightowlspace.com", "root", "Nightowl@123", "userdb");
var_dump($conn);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO users (username, password) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $username, $password);

if ($stmt->execute()) {
    $response = ["success" => true];
} else {
    $response = ["success" => false];
}

//echo json_encode($response);
$conn->close();
