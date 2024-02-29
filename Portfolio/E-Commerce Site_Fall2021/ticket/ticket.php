<?php
session_start();
$cookieName = "formCookie";

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Submit Ticket</title>
        <link rel = "stylesheet" href = "../css/contact.css">
        <link rel = "stylesheet" href = "../css/main.css">

    </head>
    <body>
        <?php include_once("../inc/banner.php");?>
        <?php include_once("../inc/navbar.php");?>

            <div id="header">
                <h1 id ="contactFormHeader" class="contactFormHeader">Need Help?</h1>
            </div>
            <div id="contactForm">
                <form id="contactFields" name="contactFields" method="post">
                    <h2 id="fistName">no you don't</h2>

                    <a id="homeButton" href="../../index.php">Our site is flawless</a> 
                </form>

                
            </div>


    </body>
</html>