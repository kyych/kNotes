function addNote(){
    var inputBox = document.createElement("DIV");
    inputBox.className = "inputDiv";
    // btn.innerHTML = "CLICK ME";
    var content = document.createElement("INPUT")
    var button = document.createElement("BUTTON")
    button.className= "btn";
    button.id = "button".concat();
    button.innerHTML = "SUBMIT";

    button.onclick = function(){
        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function(){
            if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status === 200) {
                console.log(xhttp.responseText);
              }
        };

        xhttp.open("POST", '/note/add', true);
        // xhttp.send("note=".concat());
        xhttp.send()

    };

    // document.body.appendChild(btn);
    inputBox.appendChild(content);
    inputBox.appendChild(button);
    document.body.appendChild(inputBox);
}


function getNotes(username){
    console.log(username);
}