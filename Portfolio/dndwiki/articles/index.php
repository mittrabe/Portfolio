<!--
TO DO/THINGS TO NOTE:
    -Hyperlink feature all kinds of useless
    -add tag feature
    -tab indenting doesn't work when in a bullet/number list
-->

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Rich Text Editor</title>
        <!-- FontAwesome Icons -->
        <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
        />
        <!-- Google Fonts -->
        <link
        href="https://fonts.googleapis.com/css2?family=Poppins&display=swap"
        rel="stylesheet"
        />
        <!-- Stylesheet -->
        <link rel="stylesheet" href="../css/articlecss.css" />
        <link rel="stylesheet" href="../css/bannerCSS.css" />
    </head>

    <body>
        <?php include_once("../inc/banner.php");?>
        
        <div id="wrapper">
            <div id="headerBlock">
                <div id="titleDiv" style="float:left;margin-right:40px;">
                    <label id="titleLabel" class="headerLabel" for="articleTitleText">Article Title</label>
                    <input type="text" id="articleTitleText" class="headerText" name="articleTitleText" />
                </div>

                <div id="typeDiv" style="float:left;">
                    <label id="typeLabel" class="headerLabel" for="articleTypeDropdown">Article Type</label>
                    <select id="articleTypeDropdown" class="headerText">
                        <option value="Null"></option>
                        <option value="Person">Person</option>
                        <option value="Place">Place</option>
                        <option value="Thing">Thing</option>
                    </select>
                </div>

                <!-- invisibleDiv who's only purpose is to push down the miscHeaderDiv a line -->
                <div id=fakeDiv style="float:left;">
                    <label id="invisibleLabel" class="headerLabel" for="articleTitleText">ㅤㅤㅤㅤㅤㅤ</label>
                </div>

                <div id="miscHeaderDiv" style ="float:left;">
                    <button id="publicPrivateButton" class="miscButtons" style="float:right; margin-left:10px;">
                        <img id="publicPrivateImage" src="privateIcon.png" class="buttonImage"/>
                    </button>
                    <button id="unhiddenHiddenButton" class="miscButtons" style="float:right; margin-left:10px;">
                        <img id="unhiddenHiddenImage" src="hiddenIcon.png" class="buttonImage"/>
                    </button>
                    <button id="tagButton" class="miscButtons" style="float:right;">
                        <img id="tagImage" src="tagIcon.png" class="buttonImage"/>
                    </button>
                </div>
                
            </div>
            
        
            <!-- CODE FROM: https://codingartistweb.com/2022/04/rich-text-editor-with-javascript/ -->
            <div id="articleTextbox" class="container">
                <div class="toolbar">
                    <!-- Text Format -->
                    <button class="bold toolbar-button format" title="Bold">
                        <i class="fa-solid fa-bold"></i>
                    </button>
                    <button class="italic toolbar-button format" title="Italic">
                        <i class="fa-solid fa-italic"></i>
                    </button>
                    <button class="underline toolbar-button format" title="Underline">
                        <i class="fa-solid fa-underline"></i>
                    </button>
                    <button class="strikethrough toolbar-button format" title="Strikethrough">
                        <i class="fa-solid fa-strikethrough"></i>
                    </button>
                    <button class="superscript toolbar-button script" title="superscript">
                        <i class="fa-solid fa-superscript"></i>
                    </button>
                    <button class="subscript toolbar-button script" title="subscript">
                        <i class="fa-solid fa-subscript"></i>
                    </button>

                    <!-- List -->
                    <button class="insertOrderedList toolbar-button" title="Ordered List">
                        <div class="fa-solid fa-list-ol"></div>
                    </button>
                    <button class="insertUnorderedList toolbar-button" title="Unordered List">
                        <i class="fa-solid fa-list"></i>
                    </button>

                    <!-- Undo/Redo -->
                    <button class="undo toolbar-button" title="Undo">
                        <i class="fa-solid fa-rotate-left"></i>
                    </button>
                    <button class="redo toolbar-button" title="Redo">
                        <i class="fa-solid fa-rotate-right"></i>
                    </button>

                    <!-- Link -->
                    <button class="createLink adv-toolbar-button" title="Hyperlink">
                        <i class="fa fa-link"></i>
                    </button>
                    <button class="unlink toolbar-button" title="Unlink">
                        <i class="fa fa-unlink"></i>
                    </button>

                    <!-- Alignment -->
                    <button class="justifyLeft toolbar-button align" title="Justify Left">
                        <i class="fa-solid fa-align-left"></i>
                    </button>
                    <button class="justifyCenter toolbar-button align" title="Justify Center">
                        <i class="fa-solid fa-align-center"></i>
                    </button>
                    <button class="justifyRight toolbar-button align" title="Justify Right">
                        <i class="fa-solid fa-align-right"></i>
                    </button>
                    <button class="justifyFull toolbar-button align" title="Justify Full">
                        <i class="fa-solid fa-align-justify"></i>
                    </button>
                    <button class="indent toolbar-button spacing" title="Indent">
                        <i class="fa-solid fa-indent"></i>
                    </button>
                    <button class="outdent toolbar-button spacing"title="Outdent">
                        <i class="fa-solid fa-outdent"></i>
                    </button>

                    <!-- Headings -->
                    <select class="formatBlock adv-toolbar-button" title="Headings">
                        <option value="H1">H1</option>
                        <option value="H2">H2</option>
                        <option value="H3">H3</option>
                        <option value="H4">H4</option>
                        <option value="H5">H5</option>
                        <option value="H6">H6</option>
                    </select>

                    <!-- Font -->
                    <select class="fontName adv-toolbar-button" title="Font Names"></select>
                    <select class="fontSize adv-toolbar-button" title="Font Size"></select>

                    <!-- Color -->
                    <div class="input-wrapper">
                        <label class="foreIcon"><i class="fa fa-palette"></i></label>
                        <input type="color" class="foreColor adv-toolbar-button" title="Font Color"/> <!-- style="visibility: hidden" -->
                    </div>
                    <div class="input-wrapper">
                        <label class="backIcon"><i class="fa-solid fa-fill-drip"></i></label>
                        <input type="color" class="backColor adv-toolbar-button" title="Highlight Color"/>
                    </div>
                </div>
                <div class="textarea" contenteditable="true"></div>
            </div>
            
            <div id="dmTextbox">
                <button type="button" class="collapsible">DM Text</button>
                <div class="content">
                    <div class="toolbar">
                        <!-- Text Format -->
                        <button class="bold toolbar-button format">
                            <i class="fa-solid fa-bold"></i>
                        </button>
                        <button class="italic toolbar-button format">
                            <i class="fa-solid fa-italic"></i>
                        </button>
                        <button class="underline toolbar-button format">
                            <i class="fa-solid fa-underline"></i>
                        </button>
                        <button class="strikethrough toolbar-button format">
                            <i class="fa-solid fa-strikethrough"></i>
                        </button>
                        <button class="superscript toolbar-button script">
                            <i class="fa-solid fa-superscript"></i>
                        </button>
                        <button class="subscript toolbar-button script">
                            <i class="fa-solid fa-subscript"></i>
                        </button>

                        <!-- List -->
                        <button class="insertOrderedList toolbar-button">
                            <div class="fa-solid fa-list-ol"></div>
                        </button>
                        <button class="insertUnorderedList toolbar-button">
                            <i class="fa-solid fa-list"></i>
                        </button>

                        <!-- Undo/Redo -->
                        <button class="undo toolbar-button">
                            <i class="fa-solid fa-rotate-left"></i>
                        </button>
                        <button class="redo toolbar-button">
                            <i class="fa-solid fa-rotate-right"></i>
                        </button>

                        <!-- Link -->
                        <button class="createLink adv-toolbar-button">
                            <i class="fa fa-link"></i>
                        </button>
                        <button class="unlink toolbar-button">
                            <i class="fa fa-unlink"></i>
                        </button>

                        <!-- Alignment -->
                        <button class="justifyLeft toolbar-button align">
                            <i class="fa-solid fa-align-left"></i>
                        </button>
                        <button class="justifyCenter toolbar-button align">
                            <i class="fa-solid fa-align-center"></i>
                        </button>
                        <button class="justifyRight toolbar-button align">
                            <i class="fa-solid fa-align-right"></i>
                        </button>
                        <button class="justifyFull toolbar-button align">
                            <i class="fa-solid fa-align-justify"></i>
                        </button>
                        <button class="indent toolbar-button spacing">
                            <i class="fa-solid fa-indent"></i>
                        </button>
                        <button class="outdent toolbar-button spacing">
                            <i class="fa-solid fa-outdent"></i>
                        </button>

                        <!-- Headings -->
                        <select class="formatBlock adv-toolbar-button">
                            <option value="H1">H1</option>
                            <option value="H2">H2</option>
                            <option value="H3">H3</option>
                            <option value="H4">H4</option>
                            <option value="H5">H5</option>
                            <option value="H6">H6</option>
                        </select>

                        <!-- Font -->
                        <select class="fontName adv-toolbar-button"></select>
                        <select class="fontSize adv-toolbar-button"></select>

                        <!-- Color -->
                        <div class="input-wrapper">
                            <label class="foreIcon"><i class="fa fa-palette"></i></label>
                            <input type="color" class="foreColor adv-toolbar-button"/> <!-- style="visibility: hidden" -->
                        </div>
                        <div class="input-wrapper">
                            <label class="backIcon"><i class="fa-solid fa-fill-drip"></i></label>
                            <input type="color" class="backColor adv-toolbar-button"/>
                        </div>
                    </div>
                    <div id="dmTextarea" class="textarea" contenteditable="true"></div>
                </div>
            </div>
        </div>
        

    <!--Script-->
    <!--JS for the collapsible DM textbox from: https://www.w3schools.com/howto/howto_js_collapsible.asp -->
    <script>
    var coll = document.getElementsByClassName("collapsible");
    var dmDiv = document.getElementById("dmTextbox");
    var i;

    for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
        content.style.display = "none";
        dmDiv.style.top = "80%";
        
        } else {
        content.style.display = "block";
        dmDiv.style.top = "107%";
        }
    });
    }
    </script>

    <script src="articlesjs.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  </body>
</html>
