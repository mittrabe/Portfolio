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

        <?php
            $productName = "beanCrate";
            $adzukiBean = $_POST["adzukiBean"];
            $anasaziBean = $_POST["anasaziBean"];
            $appaloosaBean = $_POST["appaloosaBean"]; 
            $azufradoBean = $_POST["azufradoBean"];
            $blackEyedPeas = $_POST["blackEyedPeas"];
            $blackBean = $_POST["blackBean"];
            $blackTurtleBean = $_POST["blackTurtleBean"];
            $blackValentineBean = $_POST["blackValentineBean"];
            $bolitaBean = $_POST["bolitaBean"];
            $borlottiBean = $_POST["borlottiBean"];
            $butterBean = $_POST["butterBean"];
            $calypsoBean = $_POST["calypsoBean"];

        ?>

        <script>
            window.onload = function asdf(){

                updateCart();
            } 

            function updateCart(){
                fillCart();
                
                
            }
            function fillCart() {
                var productName = "<?php echo $productName; ?>";
                var adzukiBean = "<?php echo $adzukiBean; ?>";
                var anasaziBean = "<?php echo $anasaziBean; ?>";
                var appaloosaBean = "<?php echo $appaloosaBean; ?>";
                var azufradoBean = "<?php echo $azufradoBean; ?>";
                var blackEyedPeas = "<?php echo $blackEyedPeas; ?>";
                var blackBean = "<?php echo $blackBean; ?>";
                var blackTurtleBean = "<?php echo $blackTurtleBean; ?>";
                var blackValentineBean = "<?php echo $blackValentineBean; ?>";
                var bolitaBean = "<?php echo $bolitaBean; ?>";
                var borlottiBean = "<?php echo $borlottiBean; ?>";
                var butterBean = "<?php echo $butterBean; ?>";
                var calypsoBean = "<?php echo $calypsoBean; ?>";


                var productInfo = [productName, adzukiBean, anasaziBean, appaloosaBean, azufradoBean, blackEyedPeas, blackBean, blackTurtleBean, blackValentineBean, bolitaBean, borlottiBean, butterBean, calypsoBean];

                var cookieInfo = []
                productInfo.forEach(function(item){
                    if(item != ""){
                        cookieInfo.push(item);
                    }
                });

                //Used to append the preexisting cookie/cart items into the end of the new cookie
                var allItems = "";
                if (document.cookie.indexOf('cartItem=') != -1) {
                    allItems = getCartCookie();
                    allItems = allItems.replace(/['"]+/g, '');
                    allItems = allItems.replace("]", '');
                    allItems = allItems.substring(9);
                }

                var cartItem = cookieInfo + ":" + allItems;
                var json_str = JSON.stringify(cartItem);
                setCookie('cartItem', json_str, '7', '/cart/','beancrate.shop',1); // This cookie last for 7 days

                redirectToCart();
            }


            function setCookie(cname, cvalue, exdays) {
                var d = new Date();
                d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
                var expires = "expires="+d.toUTCString();
                document.cookie = "|" + cname + "=" + cvalue + ";" + ";domain=beancrate.shop;path=/;expires";
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

            function redirectToCart(){
                window.location.replace("index.php");
            }
        </script>

    </head>

</html>