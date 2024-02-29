<!DOCTYPE html>

<html>
    <head>
        <title>Bean Crate</title>
        <link rel="stylesheet" href="css/main.css">
        <link rel="stylesheet" href="css/homePage.css">
        <!--the below stylesheet is stolen from w3schools and is what is being used to to grab the caret symbol for the more dropdown-->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">

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
        <?php include_once("inc/banner.php");?>

        <?php include_once("inc/logoContainer.php");?>
       
        <?php include_once("inc/navbar.php");?>

        <div id="pageBody">
            <!--Account Information, Purchase History, Your Subscription(s)-->
            <div id="profileNavItems">
                <h2 id="profileNavHeader">Your Account</h2>
                <a id="profileAccountNav" class="profileButton" href='#'>Account Information</a>
                <a id="profilePurchaseHistoryNav" class="profileButton" href='#'>Purchase History</a>
                <a id="profileSubscriptionNav" class="profileButton" href='#'>Your Subscription(s)</a> 
            </div>  
        </div>
    </body>
</html>