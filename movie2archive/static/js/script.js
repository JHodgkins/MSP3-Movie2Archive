// Calls to the textarea located on the add movie page
// Text area countdown to show characters left to enter
function textareaLengthCheck(el) {
  let textArea = el.value.length;
  let charactersLeft = 100 - textArea;
  let count = document.getElementById('lblRemainingCount');
  count.innerHTML = "Remaining characters: " + charactersLeft;
}

// Calculates the date
// Show date on footer
let date = new Date();
document.getElementById("copyright").innerHTML = date.getFullYear();
