<!--
TO DO/THINGS TO NOTE:
    -Profile icon doesn't work
    -search bar scope dropdown
    -actual logo
    -add sidebar (https://www.w3schools.com/howto/howto_js_off-canvas.asp)
    -https://www.w3schools.com/howto/howto_js_mobile_navbar.asp
-->

<div id="banner">
    <a id="logo" href='../index.php'>Site Name</a>
    <div class="dropdown">
        <button class='dropbutton'>Create
            <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
            <a href='#'>Campaign</a>
            <a href='#'>Article</a>
            <a href='#'>Character</a>
        </div>
    </div>

    <div id="profileDropdown" class="dropdown">
        <button id="profileButton" class='dropbutton'>
            <i id="profileIcon" class="fa-solid fa-circle-user fa-2xl"></i>
        </button>
    </div>

    <div class="search-container">
        <form action="#">
            <input type="text" placeholder="Search...">
            <button type="submit"><i class="fa fa-search"></i></button>
        </form>
    </div>
            
</div>

<div id="sidebar" class="sidebar">
    <a href="javascript:void(0)" class="closebutton" onclick="closeNav()">&times;</a>
    <a href="#" class="sidebarOption">Campaign A</a>
    <div class="sidebarDiv">
        <a href="#">Articles</a>
        <a href="#">Players</a>
        <a href="#">Map</a>
    </div>
    <a href='#' class="sidebarOption">Campaign B</a>
    <div class="sidebarDiv">
        <a href="#">Articles</a>
        <a href="#">Players</a>
        <a href="#">Map</a>
    </div>
    <a href='#' class="sidebarOption">Campaign C</a>
    <div class="sidebarDiv">
        <a href="#">Articles</a>
        <a href="#">Players</a>
        <a href="#">Map</a>
    </div>
</div>

<button class="openButton" onclick="openNav()">
    <i class="fa-solid fa-bars" style="color: #ffffff;"></i>
</button>

<script>
    function openNav() {
    document.getElementById("sidebar").style.width = "200px";
    document.getElementById("banner").style.marginLeft="200px";
    document.getElementById("banner").style.paddingRight = "210px"; //
    document.getElementById("wrapper").style.marginLeft="200px";
    }

    function closeNav() {
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("banner").style.marginLeft="0";
    document.getElementById("banner").style.paddingRight = "10px";
    document.getElementById("wrapper").style.marginLeft="0";
    }


    //JS for the collapsible sidebar menus from: https://www.w3schools.com/howto/howto_js_collapsible.asp
    var coll = document.getElementsByClassName("sidebarOption");
    var i;
    for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
        content.style.display = "none";
        
        } else {
        content.style.display = "block";
        }
    });
    }
</script>