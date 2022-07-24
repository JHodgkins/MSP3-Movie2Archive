document.addEventListener('DOMContentLoaded', function() {
    // Navbar initialization
      let sidenav = document.querySelectorAll('.sidenav');
      M.Sidenav.init(sidenav);
});

function textareaLengthCheck(el) {
  let textArea = el.value.length;
  let charactersLeft = 100 - textArea;
  let count = document.getElementById('lblRemainingCount');
  count.innerHTML = "Remaining characters: " + charactersLeft;
}

// Show date on footer
let date = new Date();
document.getElementById("copyright").innerHTML = date.getFullYear();