function addNote(){
    var btn = document.createElement("DIV");
    btn.className = "inputDiv";
    // btn.innerHTML = "CLICK ME";
    var content = document.createElement("INPUT")
    var button = document.createElement("BUTTON")
    button.innerHTML = "CLICK ME";
    // document.body.appendChild(btn);
    btn.appendChild(content);
    btn.appendChild(button);
    document.body.appendChild(btn);
}