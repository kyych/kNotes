function addNote(){
    var inputBox = document.createElement("DIV");
    inputBox.className = "inputDiv";
    // btn.innerHTML = "CLICK ME";
    var content = document.createElement("INPUT")
    var button = document.createElement("BUTTON")
    button.className= "btn";
    button.innerHTML = "CLICK ME";
    // document.body.appendChild(btn);
    inputBox.appendChild(content);
    inputBox.appendChild(button);
    document.body.appendChild(inputBox);
}