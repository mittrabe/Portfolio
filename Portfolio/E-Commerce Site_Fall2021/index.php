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

       
        <?php include_once("inc/navbar.php");?>

        

        <div id="pageBody">
            <div id="landingPage" class="mainPageSection">
                <img id="beanLogo" class="center" src="img/beanLogo3.png" style="width:20em; height:20em;">
                <h1 id="slogan">Beans Made Easy</h1>
                <p id="missionStatement">Bean Crate is a subscription-based, monthly bean service that allows users to mix and match beans to find the perfect match for them. We strive to provide each user with a revolutionary bean experience the likes of which they have never seen.</p>
            </div>
            <div id="productDisplay" class="mainPageSection">
                <!--Number of beans offered, Different tiers of beans, different products/plans, Worldwide Shipping-->
                <h1 id="productHeader" style="grid-area: header">Products</h1>

                <a id="beanBox" class="productIcon" style="grid-area: box"><img src="img/products/beanBoxSoon.png" class="productPng"></a>
                <a id="beanBucket" class="productIcon" style="grid-area: bucket"><img src="img/products/beanBucketSoon.png" class="productPng"></a>
                <a href='productdetails/index.php' id="beanCrate" class="productIcon" style="grid-area: crate"><img src="img/products/beanCrate.png" class="productPng"></a>
                
                <a id="beanBoxTitle" class="productTitle" style="grid-area: boxTitle">Bean Box</h3>
                <a id="beanBucketTitle" class="productTitle" style="grid-area: bucketTitle">Bean Bucket</h3>
                <a href='productdetails/index.php' id="beanCrateTitle" class="productTitle" style="grid-area: crateTitle">Bean Crate</h3>
            </div>

            <div id="discover" class="mainPageSection">
                <!--takes you to the bean gallery-->
               <a id="discoverButton" href="#">Discover</a>
            </div>

            <div id="navigationSection" class="mainPageSection">
                    <!--History/About, Contact Us, Leave a Review-->
                <img id="navImg1" class="navImg" src="img/decorativeImg/beanBowls.jpg" style="grid-area:img1">

                <div id="aboutCell" class="navHeader" style="grid-area: about">
                    <h2 id="aboutTitle">About Us/History</h2>
                    <p id="aboutText" class="navText">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <a id="aboutLink" class="navLink" href="/about/about.php">Read More</a>
                </div>

                <img id="navImg2" class="navImg" src="img/decorativeImg/greenBeans2.jpg" style="grid-area:img2">

                <div id="contactCell" class="navHeader" style="grid-area: contact">
                    <h2 id="contactTitle">Contact Us</h2>
                    <p id="contactText" class="navText">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    <a id="contactLink" class="navLink" href="contact/index.php">Contact Us </a>
                </div>

                <img id="navImg3" class="navImg" src="img/decorativeImg/assortedBeans.jpg" style="grid-area:img3">

                <div id="reviewCell" class="navHeader" style="grid-area: leaveReview">
                    <h2 id="reviewTitle">Need Help? </h2>
                    <p id="reviewText" class="navText">If you want to get into contact with our quality support team, click bellow to submit a support ticket!</p>
                    <a id="reviewLink" class="navLink" href="/ticket/ticket.php">Submit a Ticket</a>
                </div>

            </div>

            <div id="reviews" class="mainPageSection">
                <!--Code for implementing stars: https://css-tricks.com/five-methods-for-five-star-ratings/-->

                <h2 id="reviewHeader" class="reviewSectionText">Reviews</h2>
                <img id="reviewQuote" class="reviewSectionText" src="img/decorativeImg/quotationMark.png" style="filter: invert(100%);">
                <p id="reviewMessage">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>  
            </div>
            
            <div id="misc" class="mainPageSection">
                
            </div>
        </div>
    </body>
</html>