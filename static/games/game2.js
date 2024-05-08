function game(){
    $("#gameContent").html=""
    var newElement = $("<div>");
    var letter = 'A'; 
    $("#gameContent").append(newElement);
    
    function changeLetter() {
        if (letter === 'Z') {
            letter = 'A';
        } else {
            letter = String.fromCharCode(letter.charCodeAt(0) + 1);
        }
        newElement.text("Aktualna literka: " + letter);
    }

    setInterval(changeLetter, 1000);
}

game();