document.addEventListener('DOMContentLoaded', function() {
    // Navbar initialization
      let sidenav = document.querySelectorAll('.sidenav');
      M.Sidenav.init(sidenav);
});

// Show date on footer
let date = new Date();
document.getElementById("copyright").innerHTML = date.getFullYear();