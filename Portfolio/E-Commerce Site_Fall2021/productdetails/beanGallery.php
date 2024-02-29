<!DOCTYPE html>
<html>
    <head>
        <title>Bean Crate</title>
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/main.css">
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
        <?php include_once("../inc/banner.php");?>
        <?php include_once("../inc/logoContainer.php");?>
        <?php include_once("../inc/navbar.php");?>

        <br /><br /><br />
        <div id="beanListPage">
            <div id="beanList">
                <img id="beanListImg" src="../img/bean_list.jpg" width="1500" height="1000" class ="beanListImg" alt="Bean product list" title="Bean product list">
            </div>
        </div>

        <?php include_once("../inc/footer.php");?>
    </body>
</html>
<!--==========================READ ME==========================
This code is a generic template that should likely be used for every (user) page.

The template is broken up into 4ish main chunks/divs:
    1. banner 
    2. navbar 
    3. pageBody
    4. footer
    5(ish). a separate div that houses the logo (top left)

The banner, navbar, and footer are simply includes/references to separate php files.

The pageBody div is where the individual page content can be expected to go.


When applying this template, all you need to modify are the directory paths within the includes() to more reflect the page you are on.
============================================================-->