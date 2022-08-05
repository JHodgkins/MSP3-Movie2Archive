document.addEventListener('DOMContentLoaded', function() {

// Text area countdown to show characters left to enter
function textareaLengthCheck(el) {
  let textArea = el.value.length;
  let charactersLeft = 100 - textArea;
  let count = document.getElementById('lblRemainingCount');
  count.innerHTML = "Remaining characters: " + charactersLeft;
}

// Show date on footer
let date = new Date();
document.getElementById("copyright").innerHTML = date.getFullYear();