<?php

// this is from this video https://www.youtube.com/watch?v=7nOFMI2yf_Q&list=PLhPyEFL5u-i0XXGLJawaTNLiXxmSp24TR&index=18

include("../../inc/db_connection.php");

$new_fname = $_GET['firstNameText'];
$new_lname = $_GET['lastNameText'];
$new_email = $_GET['emailText'];
$new_username = $_GET['usernameText'];
$new_password = $_GET['passwordText'];

$new_password = addslashes($new_password);

echo "<h2>Attempting to create new user: " . $new_fname . " " . $new_lname . " email: " . $new_email . " username: " . $new_username . "pw: " . $new_password . "</h2>";

// check if user already exists
$sql = "SELECT * FROM Users WHERE Username = '$new_username'";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    echo "The username " . $new_username . " is aready is use!";
    exit;
}

// hashes password to put it into the database
$new_password = password_hash($new_password, PASSWORD_DEFAULT);

// creates the new user
$sql = "INSERT INTO Users (Username, Fname, Lname, Password, Email) VALUES ('$new_username', '$new_fname', '$new_lname', '$new_password', '$new_email')";
$result = $conn->query($sql) or die (mysqli_error($mysqli));
if ($result) {
    echo "Created new user: " . $new_fname . " " . $new_lname . " email: " . $new_email . " username: " . $new_username;
} else {
    echo "Something went wrong and the user was not registered";
}


?>
<br/>
<a href="../../admin/admin_home.php">Return to Admin Home</a>