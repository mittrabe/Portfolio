<?php
session_start();
$cookieName = "formCookie";
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Contact Form</title>
        <link rel = "stylesheet" href = "assets/main.css">

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

        // define variables and set to empty values
        $firstName = $lastName = $email = $confirmEmail = $contactReason = "";
        $firstError = $lastError = $emailError = $confirmError = $contactError = "";

        if (isset($_POST['submit'])) {
            $firstName = test_input($_POST["firstName"]);
            $lastName = test_input($_POST["lastName"]);
            $email = test_input($_POST["email"]);
            $confirmEmail = test_input($_POST["confirmEmail"]);
            $contactReason = test_input($_POST["contactReason"]);
            $phoneTextPref = $_POST["textPreference"];
            $phoneCallPref = $_POST["callPreference"];
            $emailPref = $_POST["emailPreference"];
            $companyName = $_POST["companyName"];
            $timeZone = $_POST["timeZone"];
            $requestPriority = $_POST["requestPriority"];

            $formSubmission = "firstName: " . $firstName . "\n\r"
                            . "lastName: " . $lastName . "\n\r" 
                            . "email: " . $email . "\n\r"   
                            . "phone number: " . $phoneNum . "\n\r"
                            . "phoneTextPref: " . $phoneTextPref ."\n\r"
                            . "phoneCallPref: " . $phoneCallPref . "\n\r"
                            . "emailPref: " . $emailPref . "\n\r"
                            . "companyName: " . $companyName . "\n\r"
                            . "timeZone: " . $timeZone . "\n\r"
                            . "contactReason: " . $contactReason . "\n\r"
                            . "requestPriority: " . $requestPriority;






            $requiredFields = array();
            array_push($requiredFields, $firstName, $lastName, $email, $confirmEmail, $contactReason);

            $firstError = $lastError = $emailError = $confirmError = $contactError = "none";
            $errorClasses = array();
           
            if(validate_fields($requiredFields)){
                setcookie($cookieName, $firstName . "," . $lastName . "," . $email . "," . $phoneNumber . "," . $phoneTextPref . "," . $phoneCallPref . "," . $emailPref . "," . $companyName . "," . $timeZone . "," . $contactReason . "," . $requestPriority);
                $to="mrabehl1@cord.edu";
                $subject="mittrabe Contact Form Submission";
                mail($to,$subject,$formSubmission);
                header("location: thanks.php");
                exit();
            }
            else{
                echo "<p> <font color=white>[SERVER ERROR] Invalid or Missing Fields</font> </p>";
                foreach ($errorClasses as $error){
                    if($error == 0){$firstError = " error";}
                    if($error == 1){$lastError = " error";}
                    if($error == 2){$emailError = " error";}
                    if($error == 3){$confirmError = " error";}
                    if($error == 4){$contactError = " error";}
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
        <div id="header">
            <h1 id ="contactFormHeader" class="contactFormHeader">Contact Me</h1>
        </div>
        <div id="contactForm">
            <form id="contactFields" onsubmit="CheckRequiredSubmissions();" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" name="contactFields" method="post"> 
                <input placeholder="First Name*" type="text" id="firstName" name="firstName" class="requiredElement  <?php echo $firstError; ?>"/>
                <input placeholder="Last Name*" type="text" id="lastName" name="lastName" class="requiredElement <?php echo $lastError; ?>"/>
                <br />

                <input placeholder="Email Address*" type="text" id="email" name ="email" class="requiredElement <?php echo $emailError; ?>"/>
                <input placeholder="Confirm Email Address*" type="text" id="confirmEmail" name ="confirmEmail" class="requiredElement <?php echo $confirmError; ?>"/>
                <input placeholder="Phone Number: (xxx) xxx-xxxx" onkeyup="GetPhoneFormat('phoneNum')" type="text" id="phoneNum" name="phoneNum"/>

                <script>
                    //Code for phone number formatting taken from: 
                    //https://stackoverflow.com/questions/8139531/set-american-phone-number-format-automatically
                    function GetPhoneFormat(id) {
                        var str = document.getElementById(id).value;
                        if (str.length == 3) {
                            var ind = str.substring(0, 3);
                            document.getElementById(id).value = '('+ind+')' + " ";
                        }
                        if (str.length == 9) {
                            var ind = str.substring(0, 9);
                            document.getElementById(id).value = ind+'-';
                        }
                    }
                </script>
                <br />


                <p id="prefContact" class="formHeader">Preferred Contact</p>

                <input type="checkbox" id="phoneTextPref" name="textPreference" value="Phone(text) Preferred" />
                <label class="contactPreference" for="phoneTextPref">Phone (Text)</label>
                <br />
                <input type="checkbox" id="phoneCallPref" name="callPreference" value="Phone(call) Preferred" />
                <label class="contactPreference" for="phoneCallPref">Phone (Call)</label>
                <br />
                <input type="checkbox" id="emailPref" name="emailPreference" value="Email Preferred" />
                <label class="contactPreference" for="emailPref">Email</label>
                <br />

                <input placeholder="Company Name (if any)" type="text" id="companyName" name ="companyName" />

                <select placeholder="Time Zone" id="timeZone" name="timeZone">
                    <option>Select Time Zone</option>
                    <option>Greenwich Mean Time (UTC+00)</option>
                    <option>Universal Coordinated Time (UTC+00)</option>
                    <option>European Central Time (UTC+1)</option>
                    <option>Eastern European Time (UTC+2)</option>
                    <option>Central African Time (UTC+2)</option> 
                    <option>(Arabic) Egypt Standard Time (UTC+3)</option>
                    <option>Eastern African Time (UTC+3)</option>
                    <option>Gulf Standard Time (UTC+4)</option>
                    <option>Afghanistan Time (UTC+4:30)</option>
                    <option>Pakistan Standard Time (UTC+5)</option>
                    <option>India Standard Time (UTC+5:30)</option>
                    <option>Bangladesh Standard Time (UTC+6)</option>
                    <option>Vietnam Standard Time (UTC+7)</option>
                    <option>China Standard Time (UTC+8)</option>
                    <option>Japan Standard Time (UTC+9)</option>
                    <option>Australia Central Time (UTC+9:30)</option>
                    <option>Australia Eastern Time (UTC+10)</option>
                    <option>Solomon Standard Time (UTC+11)</option>
                    <option>New Zealand Standard Time (UTC+12)</option>
                    <option>Midway Islands Time (UTC-11)</option>
                    <option>Hawaii Standard Time (UTC-10)</option>
                    <option>Alaska Standard Time (UTC-9)</option>
                    <option>Pacific Standard Time (UTC-8)</option>
                    <option>Phoenix Standard Time (UTC-7)</option>
                    <option>Mountain Standard Time (UTC-7)</option>
                    <option>Central Standard Time (UTC-6)</option>
                    <option>Eastern Standard Time (UTC-5)</option>
                    <option>Atlantic Standard Time (UTC-4)</option>
                    <option>Canada Newfoundland Time (UTC-3:30)</option>
                    <option>Argentina Standard Time (UTC-3)</option>
                    <option>Fernando de Noronha Time (UTC-2)</option> 
                    </select>
                <br />

                <input placeholder="Your Message*" type="textarea" id="contactReason" name ="contactReason" class="requiredElement <?php echo $contactError; ?>" />
                <br />

                <p id="requestImportance" class="formHeader">Request Importance/Priority</p>
                
                <input type="radio" id="lowPriority" name="requestPriority" value="low" />
                <label class = "radioLabel" for="lowPriority">Low</label>
                <br />
                <input type="radio" id="mediumPriority" name="requestPriority" value="medium" />
                <label class = "radioLabel" for="mediumPriority">Medium</label>
                <br />
                <input type="radio" id="highPriority" name="requestPriority" value="high" />
                <label class = "radioLabel" for="highPriority">High</label>
                <br />
                
                <input id="submit" name="submit" type="submit" class="rainbow-text" value="Submit">
                
            </form>

            
        </div>

    </body>
</html>