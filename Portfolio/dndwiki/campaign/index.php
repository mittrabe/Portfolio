<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Campaign Home</title> <!-- Title of the tab in browser -->
        
        <h1>Home</h1>

        <?php include_once("../inc/banner.php");?>
        <link rel="stylesheet" href="../css/bannerCSS.css" />

        <!-- FontAwesome Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <!-- <link rel="stylesheet" href=""> <-- Link for CSS style sheet for page -->
        <link rel="stylesheet" href="../css/campaigns.css" />


    </head>

    <body>
        <div class="container">
            <div id="mainNavigation" class="subSeciton"> <!-- main navigation box for Campaign Homepage -->
                <h2>Main Section Navigation</h2> <!-- will need to rename this section to something else -->
                <p>What would you like to know?</p>
                <ul style="list-style-type: none;"> <!-- Makes the list below into an actual list -->
                    <li><a href="#">World</a></li> <!-- be a link to a template page for wiki information for now i suppose -->
                    <li><a href="#">Campaign Story</a></li>
                    <li><a href="#">People</a></li>
                    <li><a href="#">Items/Things</a></li>
                    <li><a href="#">Player Info/Notes</a></li> <!-- Link to article style page for players to keep notes for themselves on if they want, if unused can be removed -->
                </ul>
            </div>   

            <div id="sideRightNavigation" class="subSeciton"> <!-- section for links for other players to see information on the other players in the campaign with them, possibly edited by the player who's character it is? -->
                <h2>Character Information</h2>
                <p>Catch up on important information on your party mates!</p>
                <ul style="list-style-type: none;"> <!-- Makes the list below into an actual list -->
                    <li><a id="tTipP1" href="#" title="isaac">Player Character Name 1</a></li>
                        <span class="toolTipText">Player1Name</span> <!-- Adding a tool tip so players can know the actual person they are playing the game with and their character name -->
                    <li><a id="tTipP2" href="#">Player Character Name 2</a></li>
                        <span class="toolTipText">Player2Name</span>
                    <li><a id="tTipP3" href="#">Player Character Name 3</a></li>
                        <span class="toolTipText">Player3Name</span>
                    <li><a id="tTipP4" href="#">Player Character Name 4</a></li>
                        <span class="toolTipText">Player4Name</span>
                    <li><a id="tTipP5" href="#">Player Character Name 5</a></li>
                        <span class="toolTipText">Player5Name</span>
                    <li><a id="tTipP6" href="#">Player Character Name 6</a></li>
                        <span class="toolTipText">Player6Name</span>
                    <li><a id="tTipP7" href="#">Player Character Name 7</a></li>
                        <span class="toolTipText">Player7Name</span>
                    <li><a id="tTipP8" href="#">Player Character Name 8</a></li>
                        <span class="toolTipText">Player8Name</span>
                </ul>
            </div> 

            <div id="worldLore" class="subSeciton"> <!-- section for the world's lore and whatever -->
                <h2>World & Lore</h2> 
                <p>Oh boy lore time!</p>
                <ul style="list-style-type: none;"> <!-- Makes the list below into an actual list -->
                    <li><a href="#">World</a></li> <!-- be a link to a template page for wiki information for now i suppose -->
                    <li><a href="#">Campaign Story</a></li>
                    <li><a href="#">People</a></li>
                    <li><a href="#">Items/Things</a></li>
                    <li><a href="#">Player Info/Notes</a></li> <!-- Link to article style page for players to keep notes for themselves on if they want, if unused can be removed -->
                </ul>
            </div>   
        </div>
    </body>
</html>