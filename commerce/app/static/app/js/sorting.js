var allCards = document.querySelectorAll(".card");
function orginal() {
    document.querySelector(".row.gy-3").innerHTML = "";
    for (var i = 0; i < allCards.length; i++) {
        document.querySelector(".row.gy-3").appendChild(allCards[i].parentNode);
    }
}

document.getElementById("select").addEventListener("change", function () {
   var option = document.getElementById("select").value;

    if (option == "Low to high") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);
        sortedCards.sort(function (a, b) {
            return parseInt(a.querySelector(".price").textContent) - parseInt(b.querySelector(".price").textContent);
        });
        document.querySelector(".row.gy-3").innerHTML = "";
        for (var i = 0; i < sortedCards.length; i++) {
            document.querySelector(".row.gy-3").appendChild(sortedCards[i].parentNode);
        }


    }
    else if (option == "High to low") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);
        sortedCards.sort(function (a, b) {
            return parseInt(b.querySelector(".price").textContent) - parseInt(a.querySelector(".price").textContent);
        });
        document.querySelector(".row.gy-3").innerHTML = "";
        for (var i = 0; i < sortedCards.length; i++) {
            document.querySelector(".row.gy-3").appendChild(sortedCards[i].parentNode);
        }
    
    }
    else if (option == "Default") {
        orginal();
    }

});
