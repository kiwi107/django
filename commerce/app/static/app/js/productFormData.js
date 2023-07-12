var form = document.querySelector('form');
var buttonGroupColor = document.querySelector('.colorGrp');
var buttonGroupSize = document.querySelector('.sizeGrp');
var counterPlus = document.querySelector('.plus');
var counterMinus = document.querySelector('.minus');

//default quantity
document.getElementById('selectedquantity').value = 1;


counterPlus.addEventListener('click', function (event) {
    var counterNumber = document.querySelector('.number');
    document.getElementById('selectedquantity').value = counterNumber.innerText;


});

counterMinus.addEventListener('click', function (event) {
    var counterNumber = document.querySelector('.number');
    document.getElementById('selectedquantity').value = counterNumber.innerText;

});






// Add event listener to the button group

buttonGroupColor.addEventListener('click', function (event) {
    var clickedButton = event.target;

    // Check if a button was clicked
    if (clickedButton.classList.contains('btn-check')) {
        // Get the selected color name and ID
        var selectedColorName = clickedButton.nextElementSibling.innerText;
        var selectedColorId = clickedButton.id.replace('color', '');

        // Update the hidden input field in the form
        var hiddenInput = document.getElementById('selectedColor');
        hiddenInput.value = selectedColorName;


    }
});
buttonGroupSize.addEventListener('click', function (event) {
    var clickedButton = event.target;

    // Check if a button was clicked
    if (clickedButton.classList.contains('btn-check')) {
        // Get the selected color name and ID
        var selectedSizeName = clickedButton.nextElementSibling.innerText;
        // var selectedSizeId = clickedButton.id.replace('size', '');

        // Update the hidden input field in the form
        var hiddenInput = document.getElementById('selectedSize');
        hiddenInput.value = selectedSizeName;


    }
});






