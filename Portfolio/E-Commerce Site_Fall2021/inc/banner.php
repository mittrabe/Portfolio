<div id="banner">
    <a id="branding" class="branding" href="../index.php">Bean Crate</a> <!--always point this to the home page index page-->

    <a id="login" class="bannerButton" href="/login/index.php">Login</a>
    <a id="signUp" class="bannerButton" href="/signup/index.php">Sign Up</a>

    <!--The code for the profileDiv (the user profile circle in the top right) is incomplete and currently nonfunctional-->
    <div id="profileDiv" class="profileDiv" style="float:right;"> 
        <button id = "profileIcon" class="profileIcon" onclick="displayProfileContent()"></button>

        <div id="profile-content" class="profile-content">
                <a href="#">Account</a>
                <a href="#">Subscriptions</a>
                <a href="#">Order History</a>
                <a href="#">Help/Support</a>
                <a href="#">Sign Out</a>
            </div>
    </div>
</div>