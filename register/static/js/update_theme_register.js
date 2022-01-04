var element = document.body;
var form = document.getElementsByClassName("registerForm");
var hrLine = document.getElementsByClassName("hrLine");
var hrLine = document.getElementsByClassName("hrLine");
var navbar = document.getElementById("navbar");

window.addEventListener('load', (event) => {
    let theme = localStorage.getItem('currentTheme');
    
    if (theme == "dark") {
        element.classList.add("dark-mode");
        navbar.classList.remove("navbar-border");
        for(var i = 0; i < form.length; i++) {
            form[i].classList.add("formBlock");
        }
        for(var i = 0; i < hrLine.length; i++) {
            hrLine[i].classList.add("hrLineDark");
        }
    } else {
        element.classList.remove("dark-mode");
        navbar.classList.remove("navbar-border");
        for(var i = 0; i < form.length; i++) {
            form[i].classList.remove("formBlock");
        }
        for(var i = 0; i < hrLine.length; i++) {
            hrLine[i].classList.remove("hrLineDark");
        }
    }
});
