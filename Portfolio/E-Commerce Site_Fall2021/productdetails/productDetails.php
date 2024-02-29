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
    </head>

    <body>
        <?php include_once("../inc/banner.php");?>

        <?php include_once("../inc/logoContainer.php");?>
       
        <?php include_once("../inc/navbar.php");?>

        

        <div id="pageBody">
            <div id="productBlock" class="pageBlock">
                <div id="productContent"> <!--includes image of product, product name, and product description-->
                    <h1 id="productTitle" class="pageBlockHeader">Product Name</h1>
                    <img id="productImg" src="../img/products/beanImg.png">

                    <!-- BEAN SELECTION/CHECKOUT CODE -->
                     <div class = "form-popup" id="beanSelectionForm">
                        <form action="" class= "form-container">
                            <div class="beanCell" style="grid-area: bean1">
                                <input type="checkbox" id="adzukiBean" name="adzukiBean" value="Adzuki Bean" />
                                <label for="adzukiBean" class ="selectionLabel">
                                    <img src="../img/beans/adzukiBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Adzuki Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean2">
                                <input type="checkbox" id="anasaziBean" name="anasaziBean" value="Anasazi Bean" />
                                <label for="anasaziBean" class = "selectionLabel">
                                    <img src="../img/beans/anasaziBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Anasazi Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean3">
                                <input type="checkbox" id="appaloosaBean" name="appaloosaBean" value="Appaloosa Bean" />
                                <label for="appaloosaBean" class = "selectionLabel">
                                    <img src="../img/beans/appaloosaBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Appaloosa Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean4">
                                <input type="checkbox" id="azufradoBean" name="azufradoBean" value="Azufrado Bean" />
                                <label for="azufradoBean" class = "selectionLabel">
                                    <img src="../img/beans/azufradoBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Azufrado Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean5">
                                <input type="checkbox" id="blackEyedPeas" name="blackEyedPeas" value="Black-Eyed Bean" />
                                <label for="blackEyedPeas" class = "selectionLabel">
                                    <img src="../img/beans/black_EyedPeas.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Black-Eyed Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean6">
                                <input type="checkbox" id="blackBean" name="blackBean" value="Black Bean" />
                                <label for="blackBean" class = "selectionLabel">
                                    <img src="../img/beans/blackBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Black Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean7">
                                <input type="checkbox" id="blackTurtleBean" name="blackTurtleBean" value="Black Turtle Bean" />
                                <label for="blackTurtleBean" class = "selectionLabel">
                                    <img src="../img/beans/blackTurtleBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Black Turtle Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean8">
                                <input type="checkbox" id="blackValentineBean" name="blackValentineBean" value="Black Valentine Bean" />
                                <label for="blackValentineBean" class = "selectionLabel">
                                    <img src="../img/beans/blackValentineBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Black Valentine Bean</p>
                                </label>
                            </div>

                            <div class="beanCell" style="grid-area: bean9">
                                <input type="checkbox" id="bolitaBean" name="bolitaBean" value="Bolita Bean" />
                                <label for="bolitaBean" class = "selectionLabel">
                                    <img src="../img/beans/bolitaBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Bolita Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean10">
                                <input type="checkbox" id="borlottiBean" name="borlottiBean" value="Borlotti Bean" />
                                <label for="borlottiBean" class = "selectionLabel">
                                    <img src="../img/beans/borlottiBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Borlotti Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean11">
                                <input type="checkbox" id="butterBean" name="butterBean" value="Butter Bean" />
                                <label for="butterBean" class = "selectionLabel">
                                    <img src="../img/beans/butterBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Butter Bean</p>
                                </label>
                            </div>
                            <div class="beanCell" style="grid-area: bean12">
                                <input type="checkbox" id="calypsoBean" name="calypsoBean" value="Calypso Bean" />
                                <label for="calypsoBean" class = "selectionLabel">
                                    <img src="../img/beans/calypsoBean.jpg" class="beanSelectionImg"/>
                                    <p class='beanName'>Calypso Bean</p>
                                </label>
                            </div>
                        </form>
                        <button type="submit" class="btn" form="beanSelectionForm">🛒 Add to Cart</button>
                        <button type="button" class="btn cancel" onclick="closeForm()">Close</button>
                    </div>
                    
                    <div id="productDescription">
                        <ul id = "listDescription"> 
                            <li><p>up to X number of different beans!</p></li>
                            <li><p>product weight: xxx</p></li>
                            <li><p>Item Dimensions: # x # x #</p></li>
                            <li><p>other misc. information</p></li>
                            <li><p>other misc. information</p></li>
                        <ul></ul>
                    </div>
                </div>

                <div id="productMisc"> <!--includes add to cart, price, shipping info, reviews etc.-->
                    <form id ="productForm">
                    <h2 id="productName">Product Name</h1>
                    <h2 id="productPrice">$##.##</h2>
                    <h2 id="selectedBeansHeader">Order with these beans?</h2>
                    <div id="chosenBeans"> 
                        <ul id="selectedBeans"> <!-- This is just a filler list and should be filled with the beans they selected (not sure how exactly we want to list them (via image or text))-->
                            <li><p>bean1</p></li>
                            <li><p>bean2</p></li>
                            <li><p>bean3</p></li>
                            <li><p>bean4</p></li>
                            <li><p>bean5</p></li>
                            <li><p>bean6</p></li>
                            <li><p>bean7</p></li>
                            <li><p>bean8</p></li>
                            <li><p>bean9</p></li>
                            <li><p>bean10</p></li>
                        </u1>
                    </div>
                     <button type="button" id="beanSelectionButton" onclick="openForm()">Customize Now!</button>
                </form>
                </div>
            </div>

            <div id="compareBlock" class="pageBlock">
                <div id="inlineCompare" class="inlineBlock">
                    <h2 id="compareBlockHeader" class="pageBlockHeader">Compare to Other Products</h2>
                    <!--Here's a site I found that describes a way to dynamically create/add divs: https://www.techiedelight.com/dynamically-create-div-javascript/ -->
                    <div id="productComparison" style="grid-template-columns: repeat(6, 350px); ">
                        <div id="rowNames" class="gridElement">
                            <img class=" rowLabel compareImg gridItem oddGrid"> 
                            <h3 id="productLabel" class="rowLabel gridItem evenGrid">Product Name</h3>
                            <h3 id="priceLabel" class="rowLabel gridItem oddGrid">Price</h3>
                            <h3 id="beanLabel" class="rowLabel gridItem evenGrid">Number of Beans</h3>
                        </div>
                        <div class="gridElement">
                            <img class="compareImg gridItem oddGrid" src="../img/products/beanImg.png" href='#'>
                            <h3 class="productCell gridItem evenGrid" >Product Name</h3>
                            <h3 class="priceCell gridItem oddGrid">Price</h3>
                            <h3 class="beanCell gridItem evenGrid">Number of Beans</h3>
                        </div>
                        <div class="gridElement">
                            <img class="compareImg gridItem oddGrid" src="../img/products/beanImg.png" href='#'>
                            <h3 class="productCell gridItem evenGrid" >Product Name</h3>
                            <h3 class="priceCell gridItem oddGrid">Price</h3>
                            <h3 class="beanCell gridItem evenGrid">Number of Beans</h3>
                        </div>
                        <div class="gridElement">
                            <img class="compareImg gridItem oddGrid" src="../img/products/beanImg.png" href='#'>
                            <h3 class="productCell gridItem evenGrid" >Product Name</h3>
                            <h3 class="priceCell gridItem oddGrid">Price</h3>
                            <h3 class="beanCell gridItem evenGrid">Number of Beans</h3>
                        </div>
                        <div class="gridElement">
                            <img class="compareImg gridItem oddGrid" src="../img/products/beanImg.png" href='#'>
                            <h3 class="productCell gridItem evenGrid" >Product Name</h3>
                            <h3 class="priceCell gridItem oddGrid">Price</h3>
                            <h3 class="beanCell gridItem evenGrid">Number of Beans</h3>
                        </div>
                        <div class="gridElement">
                            <img class="compareImg gridItem oddGrid" src="../img/products/beanImg.png" href='#'>
                            <h3 class="productCell gridItem evenGrid" >Product Name</h3>
                            <h3 class="priceCell gridItem oddGrid">Price</h3>
                            <h3 class="beanCell gridItem evenGrid">Number of Beans</h3>
                        </div>
                        
                    </div>
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

        <?php include_once("../inc/footer.php");?>
    </body>
</html>