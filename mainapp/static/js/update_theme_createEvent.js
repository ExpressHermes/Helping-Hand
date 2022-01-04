var element = document.body;
var eventForm = document.getElementById("eventForm");
var navbar = document.getElementById("navbar");
var hrLineCreateEvent = document.getElementById("hrLineCreateEvent");

window.addEventListener('load', (event) => {
    let theme = localStorage.getItem('currentTheme');

    if (theme == "dark") {
        element.classList.add("dark-mode");
        eventForm.classList.add("formBlock");
        eventForm.classList.remove("border");
        navbar.classList.add("navbar-border");
        hrLineCreateEvent.classList.add("hrLine");
    } else {
        element.classList.remove("dark-mode");
        eventForm.classList.remove("formBlock");
        eventForm.classList.add("border");
        navbar.classList.remove("navbar-border");
        hrLineCreateEvent.classList.remove("hrLine");
    }
    document.getElementById("chkDiv").remove();
});