<?php
    session_start();
    $cookieName = "formCookie";
?>

<!DOCTYPE html>
<!--inspiration: https://www.bestbuy.com/site/logitech-m325-wireless-optical-mouse-silver/2577677.p?skuId=2577677-->

<html>
    <head>
        <title>Bean Crate - Product Details</title>
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/productDetails.css">
        <link rel="stylesheet" href="../css/beanSelection.css">


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

        <?php
            $productName = "beanCrate";
            $pieces = preg_split('/(?=[A-Z])/',$productName);
            $productTitle = ucfirst($pieces[0] . " " . $pieces[1]);
            
            $productPrice = "349.99";
        ?>

        <script>
            window.onload = function(){
                document.getElementById("beanSelectionDiv").style.display = "none";
            }

            function openForm() {
            document.getElementById("beanSelectionDiv").style.display = "block";
        }
    
        function closeForm() {
            document.getElementById("beanSelectionDiv").style.display = "none";
        }
        </script>


    </head>

    <body>
        <?php 
        include_once("../inc/banner.php");
        //db connection
        include("../inc/db_connection.php");
        include_once("../inc/navbar.php");?>

        

        <div id="pageBody">
            <div id="productBlock" class="pageBlock">
                <div id="productContent"> <!--includes image of product, product name, and product description-->
                    <h1 id="productTitle" class="pageBlockHeader"><?php echo $productTitle ?></h1>
                    <img id="productImg" src="../img/products/<?php echo $productName?>.png">

                    <!-- BEAN SELECTION/CHECKOUT CODE -->
                     <div class = "form-popup" id="beanSelectionDiv">
                        <form id="beanSelectionForm" action="../cart/addtocart.php" method="post" class= "form-container">
                         
                            <div class="beanCell" style="grid-area: bean1">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='2'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                                <!--<input type="checkbox" id="adzukiBean" name="adzukiBean" value="Adzuki Bean" />
                                <label for="adzukiBean" class ="selectionLabel">
                                    <img src="../img/beans/adzukiBean.jpg" class="beanSelectionImg" />
                                    <p class='beanName'>Adzuki Bean</p>
                                </label>-->
                            </div>
                            <div class="beanCell" style="grid-area: bean2">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='3'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean3">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='4'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean4">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='5'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean5">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='6'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean6">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='7'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean7">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='8'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean8">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='9'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean9">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='10'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean10">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='11'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean11">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='12'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                            <div class="beanCell" style="grid-area: bean12">
                            <?php
                                $sql = "SELECT * FROM products WHERE ProductID='13'";
                                $result = $conn->query($sql);
                                $row = $result->fetch_assoc();
                                $pname = $row["Pname"];
                                $pimage = $row["Pimage1"];
                                echo '<input type="checkbox" id="' . $pname . '" name="' . $pname . '" value="' . $pname . '" />';
                                echo '<label for="' . $pname . '" class ="selectionLabel">
                                <img src=' . $pimage . ' class="beanSelectionImg" />
                                <p class="beanName">' . $pname . '</p></label>';
                            ?>
                            </div>
                       
                        </form>
                        <input type="submit" class="btn" name ="submit" form="beanSelectionForm" value = "🛒 Add to Cart">
                        <button type="button" class="btn cancel" onclick="closeForm()">Close</button>
                       
                    </div>
                    
                    
                </div>

                <div id="productMisc"> <!--includes add to cart, price, shipping info, reviews etc.-->
                    <form id ="productForm">
                    <h2 id="productName"><?php echo $productTitle ?> </h1>
                    <h2 id="productPrice">$<?php echo $productPrice ?></h2>
                    <div id="productDescription">
                        <ul id = "listDescription"> 
                            <li><p>up to X number of different beans!</p></li>
                            <li><p>product weight: 275lbs.</p></li>
                            <li><p>Item Dimensions: 12ft x 12ft x 8ft</p></li>
                            <li><p>Free Shipping!</p></li>
                        <ul></ul>
                    </div>
                     <button type="button" id="beanSelectionButton" onclick="openForm()">Customize Now!</button>
                </form>
                </div>
            </div>

           

            <div id="reviewBlock" class="pageBlock">
                <div id="inlineReview" class="inlineBlock">
                    <h2 id="reviewBlockHeader" class="pageBlockHeader">Leave a Review</h2>

                    <div id="reviewBlockTop">
                        <div id="reviewScore">
                            <h2 id="avgStars">4.5</h2>
                            <p id="numReviews">(2,687)</p>
                            <div class="stars" style="--rating: 4.5;" aria-label="Rating of this product is # out of 5."></div>
                        </div>

                        <form id="reviewForm">
                            <textarea id="reviewText" placeholder="leave a review..." type="textarea"></textarea>
                            <input id="reviewSubmit" type="submit" value="Submit"> </div>
                        </form>
                    </div>
                </div>
            </div>


        </div>
    </body>
</html>