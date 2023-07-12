//quantity counter
const plus = document.querySelector(".plus");
const minus = document.querySelector(".minus");
const number = document.querySelector(".number");

plus.onclick = function () {
    let count = parseInt(number.innerHTML);
    count++;
    number.innerHTML = count;
}

minus.onclick = function () {
    let count = parseInt(number.innerHTML);
    if (count > 1) {
        count--;
        number.innerHTML = count;
    }
}
