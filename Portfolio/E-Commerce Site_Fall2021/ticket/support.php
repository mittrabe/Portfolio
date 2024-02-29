<!DOCTYPE html>
<html>
    <head>
        <title>Bean Crate: Support</title>
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/support.css">
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
        <!-- Default Page Info Call -->
        <?php include_once("../inc/banner.php");?>
        <?php include_once("../inc/logoContainer.php");?>
        <?php include_once("../inc/navbar.php");?>
        <br />
        <!-- Ticket Page Data -->
        <div id="TicketPageBody">
    
            <!-- Header -->
            <h1 id="frqHeader">
                Frequently Asked Questions
            </h1>
            <!-- FRQ Section -->
            <div id="frq">
                <ul>
                    <!-- Unordered list for the bulleted questions -->
                    <li>How do I do yadda yadda yadda?</li>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac congue ligula. Fusce pellentesque, 
                        quam id feugiat hendrerit, ipsum neque consequat magna, id finibus purus ipsum eget neque. Quisque facilisis 
                        facilisis egestas. Nulla tincidunt faucibus nunc, sed rhoncus velit rutrum ac. 
                    </p>
                    <li>Do you sell yadda yadda yadda?</li>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac congue ligula. Fusce pellentesque, 
                        quam id feugiat hendrerit, ipsum neque consequat magna, id finibus purus ipsum eget neque. Quisque facilisis 
                        facilisis egestas. Nulla tincidunt faucibus nunc, sed rhoncus velit rutrum ac. 
                    </p>
                </ul>  
            </div>
        
            <!-- Header -->
            <h1 id="ticketHeader">
                Submit a Support Ticket
            </h1>
            <div id="ticket">
                <div id="ticketInfo">
                    <!-- First Name -->
                    <label for="firstNameText">Requester First Name:</label>
                    <input type="text" id="firstNameText" name="firstNameText" placeholder="First Name..." />
                    <br />
                    <!-- Last Name -->
                    <label for="lastNameText">Requester Last Name:</label>
                    <input type="text" id="lastNameText" name="lastNameText" placeholder="Last Name..." />
                    <br />
                    <!-- Priority -->
                    <label for="priotityDropdown">Priority:</label>
                    <select name="priotityDropdown" id="priotityDropdown">
                        <option value="noSelection">----</option>
                        <option value="Low">Low</option>
                        <option value="Medium">Medium</option>
                        <option value="High">High</option>
                    </select>
                    <br />
                    <!-- Contact Fields -->
                    <!-- Email -->
                    <label for="emailText">Requester Email:</label>
                    <input type="email" id="emailText" name="emailText" placeholder="email@email.com..." />
                    <br />
                    <!-- Username -->
                    <label for="usernameText">Requester Username:</label>
                    <input type="text" id="usernameText" name="usernameText" placeholder="If you have an account..." />
                    <br />
                    <!-- Group -->
                    <label for="groupDropdown">Group:</label>
                    <select name="groupDropdown" id="groupDropdown">
                        <option value="noSelection">----</option>
                        <option value="Passwords">Passwords</option>
                        <option value="Refund">Refund</option>
                        <option value="Website">Website</option>
                    </select>
                    <br />

                </div>
                <div id="ticketMessage">
                    <!-- Message Subject -->
                    <label for="subjectText">Subject:</label>
                    <input type="text" id="subjectText" name="subjectText" placeholder="Message Subject..." />
                    <br />
                    <!-- Message -->
                    <label for="messageText">Description:</label>
                    <textarea class="longInput" cols="74" rows="10" id="messageText" name="messageText" placeholder="Message..." ></textarea>
                    <br />
                </div>
                <!-- Submit and Cancel Buttons -->
                <div id="ticketButtons">
                    <input type="button" value="Cancel">
                    <input type="button" value="Submit">
                </div>
            </div>
        </div>
        <!-- Footer -->
        <?php include_once("../inc/footer.php");?>
    </body>
</html>