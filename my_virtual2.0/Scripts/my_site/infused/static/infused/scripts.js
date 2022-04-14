$("#search").keyup(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
    }
});

function openContent(evt, openContent) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(openContent).style.display = "block";
    evt.currentTarget.className += " active";
}

function ExitAlert() {
    alert("Вы вышли из своей учётной записи!");
}
