<?php
    session_start();
    $cookieName = "formCookie";
?>

<?php include_once("../inc/error_reporting.php");?>

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

        <script>
            window.onload = function cartOnLoad(){

                populateCart();
            } 

            function getListFromCookie(){
                var cartList = [];
                    allItems = getCartCookie();
                    allItems = allItems.replace(/['"]+/g, '');
                    allItems = allItems.replace("]", '');
                    allItems = allItems.substring(9);
                    const cartArray = allItems.split(",");
                    cartList.push(cartArray);
                return cartList;
            }

            function populateCart(){
                var cart = [];
                cart = getListFromCookie();
                
                
                cartString = String(cart);
                    var completeCart = cartString.split(":");
                    completeCart.pop();
                    
                    var finalCart = [];
                    var arr = [];
                    for (let i = 0; i < completeCart.length; i++) {
                        var cartItemName = "";
                        var cartItemBeans = [];
                        arr = completeCart[i].split(",");
                        for (let j = 0; j < arr.length; j++) {
                            if(j == 0){
                                cartItemName = arr[j];
                            }
                            else {
                                cartItemBeans.push(arr[j]);    
                            }
                        } 
                        finalCart.push([cartItemName, cartItemBeans]);
                        
                    }
                    addItemsToCart(finalCart);  
            }

            function addItemsToCart(cartArray){
                var count = 1;
                cartArray.forEach(function(item){
                    document.getElementById("cartItemList").innerHTML += getCartDiv(item);
                    document.getElementById("item").setAttribute("id","item" + count);
                    var newItemId = "item" + count;
                    document.getElementById("product").setAttribute("id","product" + count);
                    document.getElementById("productName").setAttribute("id","productName" + count);
                    document.getElementById("beanList").setAttribute("id","beanList" + count);
                    document.getElementById("removeFromCart").setAttribute("id", "removeFromCart" + count);
                    //document.getElementById("removeFromCart").setAttribute("onclick", function(){removeItem(document.getElementById("" + newItemId))} );

                    document.getElementById("product" + count).src = "../img/products/" + item[0] + ".png";
                    document.getElementById("productName" + count).innerHTML = item[0];
                    document.getElementById("beanList" + count).innerHTML = item[1];
                    count += 1;
                });

            }

            function getCartDiv(item){
                return `<div class="cartItem" id="item">
                            <div class="cartItemBox">
                                <img id="product" class="cartItemImg" src="" />
                                <h4 id="productName" class="cartItemName"></h4>
                            </div>
                            <div class="cartItemMisc">
                                <h3 class="cartItemPrice">$$$</h3>
                                <button id="removeFromCart" class="removeButton" onclick = "removeItem(this);">Remove</button>
                            </div>
                            <hr style="width: 100%;">
                            <div class="beansIncluded">
                                <h4 class="cartItemBeanHeader">Beans Selected:</h4>
                                <p id="beanList" class="cartItemBeanList"></p>
                            </div>
                        </div>;`
            }

            function getCartCookie() {
                var cartList = [];
                var theCookies = document.cookie.split('|');
                var aString = '';
                for (var i = 1; i <= theCookies.length; i++) {
                    if(theCookies[i-1].substring(0,8) == "cartItem"){
                        cartList.push(theCookies[i-1]);
                    }
                }
                return cartList[0];
            }

            btns = document.getElementsByClassName("removeButton");
            for (var i = 0; i < btns.length; i++) {
                btns[i].addEventListener("click", function () {
                    //btns[i].parentNode.remove();
                    alert("test");
                });
            }
            
            function removeItem(clickedButton){
                clickedButton.parentNode.parentNode.remove();
            }

           
        </script>

    </head>

    <body>

        <?php include_once("../inc/banner.php");?>
       
        <?php include_once("../inc/navbar.php");?>

        <div id="pageBody">
            <div id="checkoutBlock" class="pageBlock">
                <h1 id="checkoutHeader" class="pageBlockHeader">Order Summary</h1>
                <div id="checkoutSubBlock">
                    <div id="orderInfo">
                        <h3 id="cartTotal" class="summaryElement">Original Price: $$$</h3>
                        <h3 id="shippingCost" class="summaryElement">Shipping: $$$</h3>
                        <hr style="width:14em; margin-left: 5px;">
                        <h3 id="finalTotal">Final Total: $$$</h3>
                    </div>
                    <div id="checkoutButtonDiv">
                        <a id="checkoutButton" href="#">Checkout</a>
                    </div>
                </div>
            </div>

            <div id="cartBlock" class="pageBlock">
                <h1 id="cartHeader" class="pageBlockHeader">Your Cart</h1>
                <div id="cartItemList">
            
                    
            


                </div>

            </div>
        </div>


        </div>
    </body>
</html>