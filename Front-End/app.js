var canvas = document.getElementById('Canvas');
var context = canvas.getContext("2d");
var img = document.getElementById("image");
var text = document.getElementById("text");
var input = document.getElementById("upload");
var button = document.getElementById("button");
var submit = document.getElementById("submit");

//image input
function handleImageUpload() {
var image = document.getElementById("upload").files[0];

    var reader = new FileReader();

    reader.onload = function(e) {
        img.src = e.target.result;
        img.classList.remove("hidden");
        button.classList.remove("hidden");
        canvas.classList.remove("hidden");
        submit.classList.remove("hidden");
        img.classList.add("hidden");
        input.classList.add("hidden");
    }

    reader.readAsDataURL(image);

} 

var Marker = function () {
    this.mImg = new Image();
    this.mImg.src = "http://www.clker.com/cliparts/K/2/n/j/Q/i/blue-dot-md.png"
    this.Width = 10;
    this.Height = 10;
    this.XPos = 0;
    this.YPos = 0;
}

var Markers = new Array();

var mouseClicked = function (mouse) {
    // Get current mouse coords
    var rect = canvas.getBoundingClientRect();
    var mouseXPos = (mouse.x - rect.left);
    var mouseYPos = (mouse.y - rect.top);

    console.log("Marker added");
    console.log(Markers);

    var marker = new Marker();
    marker.XPos = mouseXPos - (marker.Width / 2);
    marker.YPos = mouseYPos - marker.Height;

    Markers.push(marker);
}

// Add mouse click event listener to canvas
canvas.addEventListener("mousedown", mouseClicked, false);

var firstLoad = function () {
    context.font = "15px Arial";
    context.textAlign = "center";
}

firstLoad();

var main = function () {
    draw();
};

var draw = function () {
    // Clear Canvas
    context.fillStyle = "#000000";
    context.fillRect(0, 0, canvas.width, canvas.height);

    // Draw map
    context.drawImage(img, 0, 0, 768, 538);

    // Draw markers
    for (var i = 0; i < Markers.length; i++) {
        var tempMarker = Markers[i];
        // Draws marker
        context.drawImage(tempMarker.mImg, tempMarker.XPos, tempMarker.YPos, tempMarker.Width, tempMarker.Height);

        // Calculate postion
        var text = "Postion (X:" + tempMarker.XPos.toFixed(2) + ", Y:" + tempMarker.YPos.toFixed(2);

        // Draws a box
        var textMeasurements = context.measureText(text);
        context.fillStyle = "#D3D3D3";
        context.globalAlpha = 0.7;
        context.fillRect(tempMarker.XPos - (textMeasurements.width / 2), tempMarker.YPos - 15, textMeasurements.width, 20);
        context.globalAlpha = 1;

        // Draw position
        context.fillStyle = "#000000";
        context.fillText(text, tempMarker.XPos, tempMarker.YPos);
    }
    
};

setInterval(main, (1000 / 60)); // Refresh 60 times a second

function submit() {

}