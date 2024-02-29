<?php
    session_start();
?>

<?php include_once("../inc/error_reporting.php");?>

<script>
    window.onload = function cookieRemove(){
        deleteCookie();
    } 

    function deleteCookie(){
        var d = new Date();
        d.setTime(d.getTime() + (-100 * 24 * 60 * 60 * 1000));
        var expires = "expires="+d.toUTCString();
        document.cookie = "|" + "cartItem" + "=" + "" + ";" + ";domain=beancrate.shop;path=/;expires";
    }
</script>

<!DOCTYPE html>

<html>
    <head>
        <title>Bean Crate - Cart</title>
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/cart.css">

        <script> 
            
            function displayProfileContent(){
                document.getElementById("profile-content").style.display= "block";
            }
        
        //CODE FROM: https://codepen.io/marizawi/pen/YgaaMp
        //I'd was unable to figure out how to get the displayProfileContent feature to be built in directly into this eventListener
        window.addEventListener('mouseup',function(event){
            var profContent = document.getElementById('profile-content');
            var profIcon = document.getElementById("profileIcon");
            //event.target.parentNode is what prevents the dropdown from closing when clicking on items in the dropdown list. not sure if we want this or not
            if(event.target != profContent && event.target.parentNode != profContent && event.target != profIcon){
                profContent.style.display = 'none';
            }
        });        
        </script>


    </head>

    <body>

        <?php include_once("../inc/banner.php");?>
       
        <?php include_once("../inc/navbar.php");?>

        <div id="pageBody">
            <div id="checkoutBlock" class="pageBlock">
                <h1 id="orderConfirmationHeader" class="pageBlockHeader">Order Confirmation</h1>
            </div>
            <h2 id="confirmationMessage">Your order has been submited!</h3>

        </div>
    </body>
</html>