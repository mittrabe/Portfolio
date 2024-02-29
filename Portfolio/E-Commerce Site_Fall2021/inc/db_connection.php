<?php
//php from w3schools.com
$servername = "localhost";
$username = "u374748074_Admin";
$password = "A1pHaNum3RIk";
$dbname = "u374748074_beanCrateDB";

// connection creation
$conn = new mysqli($servername, $username, $password, $dbname);

//check connection
/*if ($conn->connect_error) {
    die("Connection Failed: " . $conn->connect_error);
}
echo "Connected successfully";

/*
$sql = "INSERT INTO tickets (Topic, Issue, Priority, Collection, Username, Email, Fname, Lname, Replied)
VALUES ('Test', 'This is a test to see if the server is connecting correctly', '0', '0', 'local_admin', 'localadmin@notrealemail.com', 'local', 'admin', 'No'";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}*/

//$conn->close();

?>