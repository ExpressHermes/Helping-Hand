var element = document.body;
var eventForm = document.getElementById("eventForm");
var hrLineCreateEvent = document.getElementById("hrLineCreateEvent");

window.addEventListener('load', (event) => {
    let theme = localStorage.getItem('currentTheme');

    if (theme == "dark") {
        element.classList.add("dark-mode");
        eventForm.classList.add("formBlock");
        eventForm.classList.remove("border");
        hrLineCreateEvent.classList.add("hrLine");
    } else {
        element.classList.remove("dark-mode");
        eventForm.classList.remove("formBlock");
        eventForm.classList.add("border");
        hrLineCreateEvent.classList.remove("hrLine");
    }
});

window.addEventListener('load', (event) => {
    document.getElementById("changeThemeBtn").remove();
});