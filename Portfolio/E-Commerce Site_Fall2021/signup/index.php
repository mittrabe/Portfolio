<?php
session_start();
$cookieName = "formCookie";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Bean Crate - Signup</title>
        <link rel = "stylesheet" href = "../css/signup.css">
        <link rel = "stylesheet" href = "../css/main.css">

        <script>
            //CLIENT SIDE VALIDATION 
            function CheckRequiredSubmissions(){
                var requiredElement = document.getElementsByClassName("requiredElement");
                var validForm = true;
                const invalid = [];

                for(var i=0; i < requiredElement.length; i++){
                    if(requiredElement[i].value == ""){
                        validForm = false;
                        invalid.push(requiredElement[i]);
                    }
                    if(requiredElement[i].value != ""){
                        requiredElement[i].style.borderColor = "rgba(180, 154, 9, 0.719)";
                    }

                }
                if(requiredElement[2].value != requiredElement[3].value){
                    validForm = false;
                    invalid.push(requiredElement[2]);
                    invalid.push(requiredElement[3]);
                }
                if(validForm == true){
                    document.getElementById("contactFields").action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>";
                }
                else if(validForm == false){
                    alert("[ERROR] Invalid or Missing Fields");
                    for(var i=0; i < invalid.length; i++){
                        invalid[i].style.borderColor = "rgba(230, 119, 119, 0.781)";
                    }
                    event.preventDefault(); //prevents form from submitting/page from reloading when required fields are missing
                }
                
            }
        </script>
        <?php
        //SERVER-SIDE VALIDATION

        //db connection
        include("../inc/db_connection.php");
        
        // define variables and set to empty values
        $username = $password = $email = $confirmPasswordError =  "";
        $usernameError = $passwordError = $emailError = $confirmPasswordError = "";

        if (isset($_POST['submit'])) {
            $username = test_input($_POST["username"]);
            $password = test_input($_POST["password"]);
            $email = test_input($_POST["email"]);
            $confirmPassword = test_input($_POST["confirmPassword"]);


            $requiredFields = array();
            array_push($requiredFields, $username, $password, $email, $confirmPassword);

            $usernameError = $passwordError = $emailError = $confirmPasswordError = "none";
            $errorClasses = array();
           
            if(validate_fields($requiredFields)){
                $sql = "SELECT * FROM Users WHERE Username = '$username'";
                $result = $conn->query($sql);
                if ($result->num_rows > 0) {
                    echo "<p> <font color=white>[SERVER ERROR] The username is already in use</font> </p>";
                    exit();
                } else {
                    setcookie($cookieName, $username . "," . $password . "," . $email . "," . $confirmPassword);
                    // hashes password to put it into the database
                    $password = password_hash($password, PASSWORD_DEFAULT);
                    // creates the new user
                    $sql = "INSERT INTO Users (Username, Password, Email) VALUES ('$username', '$password', '$email')";
                    $result = $conn->query($sql) or die (mysqli_error($mysqli));
                    header("location: ../index.php");
                    exit();
                }
            }
            else{
                echo "<p> <font color=white>[SERVER ERROR] Invalid or Missing Fields</font> </p>";
                foreach ($errorClasses as $error){
                    if($error == 0){$usernameError = " error";}
                    if($error == 1){$passwordError = " error";}
                    if($error == 2){$emailError = " error";}
                    if($error == 3){$confirmPasswordError = " error";}
                }
            }
        }
        
        
        function test_input($data) {
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
        }

        function validate_fields($required){
            global $errorClasses;

            $valid = true;
            $invalidCount = 0;
            foreach($required as $key => $field){
                if(empty($field)){
                    $valid = false;
                    $errorClasses[$invalidCount] = $key; 
                    $invalidCount++;
                }
            }
            return $valid;
        }
        ?>



        <style> 
            input:focus, textarea:focus, select:focus{
                outline: none;
                
            }
            

        </style>
    </head>
    <body>
        <?php include_once("../inc/banner.php");?>

       
        <?php include_once("../inc/navbar.php");?>

        <div id="header">
            <h1 id ="contactFormHeader" class="contactFormHeader">Signup</h1>
        </div>
        <div id="contactForm">
            <form id="contactFields" onsubmit="CheckRequiredSubmissions();" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" name="contactFields" method="post">  
                <input placeholder="Username*" type="text" id="username" name="username" class="requiredElement  <?php echo $usernameError; ?>"/>
                <input placeholder="email*" type="text" id="email" name="email" class="requiredElement  <?php echo $emailError; ?>"/>
                <input placeholder="Password*" type="password" id="password" name="password" class="requiredElement <?php echo $passwordError; ?>"/>
                <input placeholder="Confirm Password*" type="password" id="confirmPassword" name="confirmPassword" class="requiredElement <?php echo $confirmPasswordError; ?>"/>
                
                
                <input id="submit" name="submit" type="submit" class="rainbow-text" value="Sign-In">
                
            </form>

            
        </div>

    </body>
</html>