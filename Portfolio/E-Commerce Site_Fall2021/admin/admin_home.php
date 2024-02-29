<!DOCTYPE html>
<html>
    <head>
        <title>Bean Crate</title>
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/admin_home.css">
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
        <?php include_once("../inc/admin_pages/admin_banner.php");?>
        <?php include_once("../inc/admin_pages/admin_navbar.php");?>
        <?php include("../inc/db_connection.php");?>

        <div id="adminHomeTop">

                <!-- ACCOUNT SECTION -->
            <div id="quickNewAccount">
                <!-- Header -->
                <h1>Quick Make Account</h1> <br />
            <form action="../inc/admin_pages/create_user.php">
                <!-- First Name -->
                <label for="firstNameText">Requester First Name:</label>
                <input type="text" id="firstNameText" name="firstNameText" placeholder="First Name..." />
                <br />
                <!-- Last Name -->
                <label for="lastNameText">Requester Last Name:</label>
                <input type="text" id="lastNameText" name="lastNameText" placeholder="Last Name..." />
                <br />
                <!-- Email -->
                <label for="emailText">Requester Email:</label>
                <input type="email" id="emailText" name="emailText" placeholder="email@email.com..." />
                <br />
                <!-- Username -->
                <label for="usernameText">Requester Username:</label>
                <input type="text" id="usernameText" name="usernameText" placeholder="Username..." />
                <br />
                <!-- Password -->
                <label for="passwordText">Requester Username:</label>
                <input type="password" id="passwordText" name="passwordText" placeholder="Password..." />
                <br />
                <input type="submit" value="Create">
            </form>
            </div>
        </div>

            <!-- TICKET SECTION -->
        <div id="ticketPanel">
            <!-- Header -->
            <h1>User Tickets</h1><br />
            <input type="button" value="View Ticket">
            <br />
            <div>
            <!--lookup ticket-->
            <form action="../inc/admin_pages/ticket_search.php">
                Ticket ID search: 
                <input type="text" name="ticketIDText"><br/>
                <input type="submit" value="Submit">
            </form>
        </div>
        <hr/>
        <div>
            <!--new ticket creation-->
            <form action="../inc/admin_pages/create_ticket.php">
                Ticket Requester First Name: 
                <input type="text" name="requesterFNameText"><br/>
                Ticket Requester Last Name: 
                <input type="text" name="requesterLNameText"><br/>
                Ticket Requester Email: 
                <input type="text" name="requesterEmailText"><br/>
                Ticket Requester Username: 
                <input type="text" name="requesterUsernameText"><br/>
                Ticket Priority: 
                <input type="text" name="requesterPriorityText"><br/>
                Ticket Group: 
                <input type="text" name="requesterGroupText"><br/>
                Ticket Subject: 
                <input type="text" name="requesterSubjectText"><br/>
                Ticket Description: 
                <input type="text" name="requesterDescriptionText"><br/>
                <input type="submit" value="Submit">
            </form>
        </div>
        </div>

    </body>
</html>
