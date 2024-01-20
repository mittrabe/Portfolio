let unhidHidImage = document.getElementById("unhiddenHiddenImage");
let unhidHidButton = document.getElementById("unhiddenHiddenButton");
let pubPrivImage = document.getElementById("publicPrivateImage");
let pubPrivButton = document.getElementById("publicPrivateButton");

//CODE TAKEN FROM: https://codingartistweb.com/2022/04/rich-text-editor-with-javascript/
let toolbarButtons = document.querySelectorAll(".toolbar-button");
let advancedToolbarButton = document.querySelectorAll(".adv-toolbar-button");
let fontName = document.querySelectorAll(".fontName");
let fontSizeRef = document.querySelectorAll(".fontSize");
let writingArea = document.querySelectorAll(".textarea");
let linkButton = document.querySelectorAll(".createLink"); 
let alignButtons = document.querySelectorAll(".align");
let spacingButtons = document.querySelectorAll(".spacing");
let formatButtons = document.querySelectorAll(".format");
let scriptButtons = document.querySelectorAll(".script");




//have the public/private and hidden/unhidden buttons toggle their icon on click
unhidHidButton.addEventListener("click", () => {
    if (unhidHidImage.getAttribute('src') === "hiddenIcon.png"){
        unhidHidImage.setAttribute('src', "unhiddenIcon.png");
    }
    else{
        unhidHidImage.setAttribute('src', "hiddenIcon.png");
    }
});
pubPrivButton.addEventListener("click", () => {
    if (pubPrivImage.getAttribute('src') === "privateIcon.png"){
        pubPrivImage.setAttribute('src', "publicIcon.png");
    }
    else{
        pubPrivImage.setAttribute('src', "privateIcon.png");
    }
});

//List of fontlist
let fontList = [
  "Arial",
  "Verdana",
  "Times New Roman",
  "Garamond",
  "Georgia",
  "Courier New",
  "cursive",
];

//Initial Settings
const initializer = () => {
  //function calls for highlighting buttons
  //No highlights for link, unlink,lists, undo,redo since they are one time operations
  highlighter(alignButtons, true);
  highlighter(spacingButtons, true);
  highlighter(formatButtons, false);
  highlighter(scriptButtons, true);

  //create options for font names
  fontName.forEach((fontDropdown) => {
    fontList.map((value) => {
      let option = document.createElement("option");
      option.value = value;
      option.innerHTML = value;
      fontDropdown.appendChild(option); 
    });
  });


  //fontSize allows only till 7
  fontSizeRef.forEach((fontSizeDropdown) => {
    for (let i = 1; i <= 7; i++) {
      let option = document.createElement("option");
      option.value = i;
      option.innerHTML = i;
      fontSizeDropdown.appendChild(option);
    }
    //default font size
    fontSizeDropdown.value = 3;
  });
  
};


//main logic
const modifyText = (command, defaultUi, value) => {
    console.log("test");
  //execCommand executes command on selected text
  document.execCommand(command, defaultUi, value);
};



//For basic operations which don't need value parameter
toolbarButtons.forEach((button) => {
  button.addEventListener("click", () => {
    modifyText(button.classList.item(0), false, null);
  });
});


//options that require value parameter (e.g colors, fonts)
advancedToolbarButton.forEach((button) => {
  button.addEventListener("change", () => {
    modifyText(button.classList.item(0), false, button.value);

    //It is probably not efficient to do this here and I should probably make it its own action listener/function
    //Changing the color of the color icons to match the selected color
    if(button.classList.item(0) === "foreColor"){
      document.querySelectorAll(".foreIcon").item(0).style.color = button.value;
    }
    else if(button.classList.item(0) === "backColor"){
      document.querySelectorAll('.backIcon').item(0).style.color = button.value;
    }
  });
});


//link
linkButton.forEach((linkbtn) => {
  linkbtn.addEventListener("click", () => {
    let userLink = prompt("Enter a URL");
    //if link has http then pass directly else add https
    if (/http/i.test(userLink)) {
      modifyText(linkbtn.classList.item(0), false, userLink);
    } else {
      userLink = "http://" + userLink;
      modifyText(linkbtn.classList.item(0), false, userLink);
    }
  });
});



//Highlight clicked button
const highlighter = (className, needsRemoval) => {
  className.forEach((button) => {
    button.addEventListener("click", () => {
      //needsRemoval = true means only one button should be highlight and other would be normal
      if (needsRemoval) {
        let alreadyActive = false;
        //If currently clicked button is already active
        if (button.classList.contains("active")) {
          alreadyActive = true;
        }
        //Remove highlight from other buttons
        highlighterRemover(className);
        if (!alreadyActive) {
          //highlight clicked button
          button.classList.add("active");
        }
      } else {
        //if other buttons can be highlighted
        button.classList.toggle("active");
      }
    });
  });
};
//Remove clicked button highlight
const highlighterRemover = (className) => {
  className.forEach((button) => {
    button.classList.remove("active");
  });
};

//Indents text on 'Tab' & Outdents text on 'Shift'+'Tab'
//Resource: 
//  https://stackoverflow.com/questions/15237304/jquery-content-editable-indent
//  https://stackoverflow.com/questions/59310818/javascript-outdent-text-in-contenteditable
writingArea.forEach((area) => {
  area.addEventListener('keydown', (e) => {
    if(e.key === 'Tab' && e.shiftKey){
      e.preventDefault();
      //document.execCommand("outdent");
      modifyText('outdent',true,null);
    } else if(e.key === 'Tab'){
      e.preventDefault(); 
      modifyText('indent',true,null);
    }
  });
});



window.onload = initializer();