function game(){
    $("#gameContent").html=""
    var newElement = $("<div>");
    var count = 0;
    $("#gameContent").append(newElement);
    function increaseCount() {
        count++;
        newElement.text("Licznik: " + count);
    }
    setInterval(increaseCount, 1000);
}
game()