<?php
session_start();
$cookieName = "formCookie";

?>

<html>
    <body>
        <?php

            $firstName = $_POST["firstName"];
            $lastName = $_POST["lastName"];
            $email = $_POST["email"]; 
            $phoneNum = $_POST["phoneNum"];
            $phoneTextPref = $_POST["textPreference"];
            $phoneCallPref = $_POST["callPreference"];
            $emailPref = $_POST["emailPreference"];
            $companyName = $_POST["companyName"];
            $timeZone = $_POST["timeZone"];
            $contactReason = $_POST["contactReason"];
            $requestPriority = $_POST["requestPriority"];

            $formSubmission = "firstName: " . $firstName . "\n\r"
                            . "lastName: " . $lastName . "\n\r" 
                            . "email: " . $email . "\n\r"   
                            . "phone number: " . $phoneNum . "\n\r"
                            . "phoneTextPref: " . $phoneTextPref ."\n\r"
                            . "phoneCallPref: " . $phoneCallPref . "\n\r"
                            . "emailPref: " . $emailPref . "\n\r"
                            . "companyName: " . $companyName . "\n\r"
                            . "timeZone: " . $timeZone . "\n\r"
                            . "contactReason: " . $contactReason . "\n\r"
                            . "requestPriority: " . $requestPriority;


                $to="mrabehl1@cord.edu";
                $subject="mittrabeContactForm";
                mail($to,$subject,$formSubmission); 

                setcookie($cookieName, $firstName . "," . $lastName . "," . $email . "," . $phoneNumber . "," . $phoneTextPref . "," . $phoneCallPref . "," . $emailPref . "," . $companyName . "," . $timeZone . "," . $contactReason . "," . $requestPriority);
                header("location: thanks.php");
            
        ?>
    </body>
</html>