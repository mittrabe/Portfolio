<!DOCTYPE html>

<!--==========================READ ME==========================
This code is a generic template that should likely be used for every (user) page.

The template is broken up into 4ish main chunks/divs:
    1. banner 
    2. navbar 
    3. pageBody
    4. footer
    5(ish). a separate div that houses the logo (top left)

The banner, navbar, and footer, are three sections I expect to remain consistent regardless where this is used

The pageBody div is where the individual page content can be expected to go.


When applying this template, there are a number of lines that need to be modified. Mainly the ones making directory references.

It is safe to assume that any line with a href=" " needs to be changed (once they are actually implemented) with only a few outliers:
    1. the img src line in the logo container div needs to be updated as well
    2. the second link rel="stylesheet" line does not need to be changed as it is not making a reference to the local directory.
============================================================-->

<html>
    <head>
        <title>Bean Crate - Product Details</title>
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/productList.css">
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

        

        <div id="pageBody">
            <div id="productListDisplay">
                <img src="../img/product_list.jpg" id="beanListImg" alt="Bean Product List">
        </div>
        <br />
        <a id="productDetailsButton" href="../products/productDetails.php">Product details</a>

        <?php include_once("../inc/footer.php");?>
    </body>
</html>