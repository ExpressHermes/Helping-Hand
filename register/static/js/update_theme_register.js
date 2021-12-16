var element = document.body;
var form = document.getElementsByClassName("registerForm");
var hrLine = document.getElementsByClassName("hrLine");

window.addEventListener('load', (event) => {
    let theme = localStorage.getItem('currentTheme');
    
    if (theme == "dark") {
        element.classList.add("dark-mode");
        for(var i = 0; i < form.length; i++) {
            form[i].classList.add("formBlock");
        }
        for(var i = 0; i < hrLine.length; i++) {
            hrLine[i].classList.add("hrLineDark");
        }
    } else {
        element.classList.remove("dark-mode");
        for(var i = 0; i < form.length; i++) {
            form[i].classList.remove("formBlock");
        }
        for(var i = 0; i < hrLine.length; i++) {
            hrLine[i].classList.remove("hrLineDark");
        }
    }
});
