//make the size chart button toggle the size chart image
//normally it is hidden
const showsizechartbtn = document.querySelector(".showsizechart");
const sizechartimg = document.querySelector(".sizechart");
sizechartimg.style.display = "none";
showsizechartbtn.onclick = toggleImg;

function toggleImg() {
    if (sizechartimg.style.display == "none") {
        sizechartimg.style.display = "block";
        showsizechartbtn.innerText = "hide size chart";
    } else {
        sizechartimg.style.display = "none";
        showsizechartbtn.innerText = "check size chart";
    }
}