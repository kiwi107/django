var allCards = document.querySelectorAll(".card");
function orginal() {
    document.querySelector(".row.gy-3").innerHTML = "";
    for (var i = 0; i < allCards.length; i++) {
        document.querySelector(".row.gy-3").appendChild(allCards[i].parentNode);
    }
}



document.getElementById("select2").addEventListener("change", function () {
    var option2 = document.getElementById("select2").value;

    if (option2 == "Male") {
        orginal();
        var maleCards = document.querySelectorAll(".male");
        document.querySelector(".row.gy-3").innerHTML = "";
        for (var i = 0; i < maleCards.length; i++) {
            document.querySelector(".row.gy-3").appendChild(maleCards[i].parentNode);
        }
    }
    else if (option2 == "Female") {
        orginal();
        var femaleCards = document.querySelectorAll(".female");
        document.querySelector(".row.gy-3").innerHTML = "";
        for (var i = 0; i < femaleCards.length; i++) {
            document.querySelector(".row.gy-3").appendChild(femaleCards[i].parentNode);
        }

    }
    else {
        orginal();
    }

});










