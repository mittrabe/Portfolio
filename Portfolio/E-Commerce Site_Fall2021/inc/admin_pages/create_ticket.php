<?php
include("../../inc/db_connection.php");
    $newTicketFname = $_GET["requesterFNameText"];
    $newTicketLname = $_GET["requesterLNameText"];
    $newTicketEmail = $_GET["requesterEmailText"];
    $newTicketUsername = $_GET["requesterUsernameText"];
    $newTicketPriority = $_GET["requesterPriorityText"];
    $newTicketGroup = $_GET["requesterGroupText"];
    $newTicketSubject = $_GET["requesterSubjectText"];
    $newTicketDescription = $_GET["requesterDescriptionText"];
    $sql = "INSERT INTO tickets (Topic, Issue, Priority, Collection, Username, Email, Fname, Lname)
    VALUES ('$newTicketSubject', '$newTicketDescription', '$newTicketPriority', '$newTicketGroup', '$newTicketUsername', '$newTicketEmail', '$newTicketFname', '$newTicketLname')";
    $result = $conn->query($sql);
?>