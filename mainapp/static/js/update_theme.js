var element = document.body;
var navbar = document.getElementById("navbar");
var hrLine = document.getElementById("hrLine");
var eventBlock = document.getElementsByClassName("eventBlock");
var cardHeader = document.getElementsByClassName("cardHeader");
var cardBody = document.getElementsByClassName("cardBody");
var eventsInfo = document.getElementsByClassName("eventsInfo");
var changeThemeBtn = document.getElementById("changeThemeBtn");
var notInterestedBtn = document.getElementsByClassName("notInterestedBtn");

const changeThemeToDark = () => {
    element.classList.toggle("dark-mode");
    navbar.classList.add("navbar-border");
    hrLine.classList.add("hrLine");
    
    for (var i = 0; i < eventBlock.length; i++) {
        eventBlock[i].classList.add("darkEventBlock");
        cardBody[i].classList.add("cardBorder");
        cardHeader[i].classList.add("cardBorder");
    }
    for (var i = 0; i < eventsInfo.length; i++) {
        eventsInfo[i].classList.add("eventsInfoDark");
    }
    for (var i = 0; i < notInterestedBtn.length; i++) {
        notInterestedBtn[i].classList.add("notInterestedBtnDark");
    }
    changeThemeBtn.innerText = "Light Mode"
    localStorage.setItem("currentTheme", "dark"); // save theme to local storage
}

const changeThemeToLight = () => {
    element.classList.toggle("dark-mode");
    navbar.classList.remove("navbar-border");
    hrLine.classList.remove("hrLine");
    for (var i = 0; i < eventBlock.length; i++) {
        eventBlock[i].classList.remove("darkEventBlock");
        cardBody[i].classList.remove("cardBorder");
        cardHeader[i].classList.remove("cardBorder");
    }
    for (var i = 0; i < eventsInfo.length; i++) {
        eventsInfo[i].classList.remove("eventsInfoDark");
    }
    for (var i = 0; i < notInterestedBtn.length; i++) {
        notInterestedBtn[i].classList.remove("notInterestedBtnDark");
    }
    changeThemeBtn.innerText = "Dark Mode"
    localStorage.setItem("currentTheme", 'light');
}

function changeTheme() {
    let theme = localStorage.getItem('currentTheme');
    if (theme == "dark") {
        changeThemeToLight();
    } else {
        changeThemeToDark();
    }
}

window.addEventListener('load', (event) => {
    let theme = localStorage.getItem('currentTheme');

    if (theme == "dark") {
        element.classList.add("dark-mode");
        navbar.classList.add("navbar-border");
        hrLine.classList.add("hrLine");
        for (var i = 0; i < eventBlock.length; i++) {
            eventBlock[i].classList.add("darkEventBlock");
            cardBody[i].classList.add("cardBorder");
            cardHeader[i].classList.add("cardBorder");
        }
        for (var i = 0; i < eventsInfo.length; i++) {
            eventsInfo[i].classList.add("eventsInfoDark");
        }
        for (var i = 0; i < notInterestedBtn.length; i++) {
            notInterestedBtn[i].classList.add("notInterestedBtnDark");
        }
        changeThemeBtn.innerText = "Light Mode"
    } else {
        element.classList.remove("dark-mode");
        navbar.classList.remove("navbar-border");
        hrLine.classList.remove("hrLine");
        for (var i = 0; i < eventBlock.length; i++) {
            eventBlock[i].classList.remove("darkEventBlock");
            cardBody[i].classList.remove("cardBorder");
            cardHeader[i].classList.remove("cardBorder");
        }
        for (var i = 0; i < eventsInfo.length; i++) {
            eventsInfo[i].classList.remove("eventsInfoDark");
        }
        for (var i = 0; i < notInterestedBtn.length; i++) {
            notInterestedBtn[i].classList.remove("notInterestedBtnDark");
        }
        changeThemeBtn.innerText = "Dark Mode"
    }
});

document.addEventListener('click', function (e) {
    if (document.activeElement.toString() == '[object HTMLButtonElement]') {
        document.activeElement.blur();
    }
});
