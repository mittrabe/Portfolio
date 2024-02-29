
<a href="../../admin/admin_home.php">Return to Admin Home</a>

<?php
include("../../inc/db_connection.php");
    $formSearch = $_GET["ticketIDText"];
    $sql = "SELECT TicketID, Topic, Issue, Replied, Modified From tickets Where TicketID LIKE '%" . $formSearch . "%'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "Ticket ID: " . $row["TicketID"] . " || " . "Subject: " . $row["Topic"] . " || " . "Description: " . $row["Issue"] . " || " . "Status: " . $row["Replied"] . " || " . "Modified: " . $row["Modified"] . "<br>";
            }
    } else {
        echo "0 results";
    }
?>

