function start(){
    console.log("common的start");
    buttonArr = [];
    localStorage.removeItem("genre");
    localStorage.removeItem("key");
    // loaddata();
}

window.addEventListener("load", start, false);