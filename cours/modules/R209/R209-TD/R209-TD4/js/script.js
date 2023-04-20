
// Definition of Event handlers

$("#start-btn").on("click", function(){
  setupDateContent();

  if ($(this).html() == "Start") {
    $(this).html("Stop");
    if ($("#reverse").is(":checked")) {
      intervalID = setInterval(decrementChrono, 20)
    } else {
      intervalID = setInterval(incrementChrono, 20);
    }
    console.log("intervalID: ",intervalID)
  } else {
    $(this).html("Start");
    clearInterval(intervalID);
    intervalID = null;
    console.log("intervalID: ", intervalID)
  }
})
$("#reset-btn").on("click", function(){
  if (!intervalID) {
    setupDateContent();
  } else {
    clearInterval(intervalID);
    intervalID = null;
    $("#start-btn").html("Start");
  }
})

$("#save-btn").on("click", function(){
  $("#logs").append($("#chronometre").text()+"<br>");
})

// Definition of Functions

function setupDateContent(){
  const date = new Date();
  var [hour, minutes, seconds, milliseconds] = [
    date.getHours(),
    date.getMinutes(),
    date.getSeconds(),
    date.getMilliseconds(),
  ];

  console.log("Yay!", hour, minutes, seconds, milliseconds);

  $("#h").text(hour);
  $("#m").text(minutes);
  $("#s").text(seconds);
  $("#ms").text(milliseconds);
}

function incrementChrono(){
  var hour = Number($("#h").html());
  var minute = Number($("#m").html());
  var second = Number($("#s").html());
  var milliseconds = Number($("#ms").html());

  milliseconds += 10;

  if (milliseconds >= 1000){
    milliseconds -= 1000;
    second += 1;
  }
  if (second >= 60){
    second -= 60;
    minute += 1;
  }
  if (minute >= 60){
    minute -= 60;
    hour += 1;
  }


  String($("#ms").text(milliseconds)).padStart(2, "0");
  String($("#s").text(second)).padStart(2, "0");
  String($("#m").text(minute)).padStart(2, "0");
  String($("#h").text(hour)).padStart(2, "0");
}

function decrementChrono(){
  var hour = Number($("#h").html());
  var minute = Number($("#m").html());
  var second = Number($("#s").html());
  var milliseconds = Number($("#ms").html());

  milliseconds -= 10;

  if(milliseconds <= 0){
    milliseconds += 1000;
    second -= 1;
  }
  if(second <= 0){
    second += 60;
    minute -= 1;
  }
  if(minute <= 0){
    minute += 60;
    hour -= 1;
  }

  String($("#ms").text(milliseconds)).padStart(2, "0");
  String($("#s").text(second)).padStart(2, "0");
  String($("#m").text(minute)).padStart(2, "0");
  String($("#h").text(hour)).padStart(2, "0");
}



// Definition and Initialization of variables

var intervalID = null;
var chronoValue = 0; // Value in milliseconds
