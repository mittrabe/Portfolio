<?php
session_start();
$cookieName = "formCookie";

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Thank You</title>
        <link rel = "stylesheet" href = "../css/contact.css">
        <link rel = "stylesheet" href = "../css/main.css">

    </head>
    <body>
        <?php include_once("../inc/banner.php");?>
        <?php include_once("../inc/navbar.php");?>

        <?php
            if(isset($_COOKIE[$cookieName])){

                
            
        ?>
            <div id="header">
                <h1 id ="contactFormHeader" class="contactFormHeader">Thank You</h1>
            </div>
            <div id="contactForm">
                <form id="contactFields" name="contactFields" method="post">

                <?php
                    $pieces = explode(",", $_COOKIE[$cookieName]);
                    $firstName = $pieces[0];
                ?>
                    <h2 id="fistName">Thank you for your submission, <?php echo $firstName; ?>. </h2>

                    <a id="homeButton" href="../../index.php">Home</a> 
                </form>

                
            </div>
        <?php

            }
        ?>

    </body>
</html>