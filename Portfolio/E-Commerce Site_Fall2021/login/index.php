<?php
session_start();
$cookieName = "formCookie";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Bean Crate - Login</title>
        <link rel = "stylesheet" href = "../css/login.css">
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
        $username = $password = "";
        $usernameError = $passwordError = "";

        if (isset($_POST['submit'])) {
            $username = test_input($_POST["username"]);
            $password = test_input($_POST["password"]);
            $password = addslashes($password);

            $requiredFields = array();
            array_push($requiredFields, $username, $password);

            $usernameError = $passwordError = "none";
            $errorClasses = array();
           
            // validate password and hash https://stackoverflow.com/questions/14624509/single-result-from-database-using-mysqli
            if(validate_fields($requiredFields)){
                $sql = "SELECT * FROM Users WHERE Username = '$username'";
                $result = $conn->query($sql);
                if ($result->num_rows > 0) {
                    $row = $result->fetch_assoc();
                    $hash = $row["Password"];
                    $isadmin = $row["IsAdmin"];
                    // verifies hash in the db
                    if (password_verify($password, $hash)) {
                        
                        //this section was to see if the user was an admin but it sent every user to the admin page so i gave up
                        if ($isadmin == "1") {
                            header('Location: ../../admin/admin_home.php');
                            exit();
                        } else {
                            header('Location: ../../index.php');
                            exit();
                        }
                        setcookie($cookieName, $username . "," . $password);
                        header("location: ../index.php");
                        exit();

                    } else {
                        echo "<p> <font color=white>[SERVER ERROR] passwords do not match</font> </p>";
                        exit();
                    }
                } else {
                    echo "<p> <font color=white>[SERVER ERROR] no user with that username</font> </p>";
                    exit();
                }
                
            }
            else{
                echo "<p> <font color=white>[SERVER ERROR] Invalid or Missing Fields</font> </p>";
                foreach ($errorClasses as $error){
                    if($error == 0){$usernameError = " error";}
                    if($error == 1){$passwordError = " error";}
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

        <div id="results">
            
        </div>

        <div id="header">
            <h1 id ="contactFormHeader" class="contactFormHeader">Login</h1>
        </div>
        <div id="contactForm">
            <form id="contactFields" onsubmit="CheckRequiredSubmissions();" action="" name="contactFields" method="post">  
                <input placeholder="Username*" type="text" id="username" name="username" class="requiredElement  <?php echo $usernameError; ?>"/>
                <input placeholder="Password*" type="password" id="password" name="password" class="requiredElement <?php echo $passwordError; ?>"/>
                
                
                <input id="submit" name="submit" type="submit" class="rainbow-text" value="Sign-In">
                
            </form>

            
        </div>

    </body>
</html>