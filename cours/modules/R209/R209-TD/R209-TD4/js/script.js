
// Definition of Event handlers

$("#start-btn").on("click", function(){
  setupDateContent();

  if ($(this).html() == "Start") {
    $(this).html("Stop");
    if ($("#reverse").is(":checked")) {
      intervalID = setInterval(decrementChrono, chronoInterval, chronoInterval)
    } else {
      intervalID = setInterval(incrementChrono, chronoInterval, chronoInterval);
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
  // On either case, we reset to 0 our chronometer
  chronoValue = 0;
  // Then we wipe the logs off the log area
  $("#logs").html("");
})

$("#save-btn").on("click", function(){
  let chronoFinal = new Date();
  chronoFinal.setTime(chronoValue);
  let chronoFinalDisplayed = `${String(chronoFinal.getHours()).padStart(2, "0")}:${String(chronoFinal.getMinutes()).padStart(2, "0")}:${String(chronoFinal.getSeconds()).padStart(2, "0")}:${String(chronoFinal.getMilliseconds()).padStart(3, "0")}`;

  console.log(chronoValue, chronoFinal.getTime());

  $("#logs").append($("#chronometre").text() + "(Chronomètre: " + chronoFinalDisplayed +") <br>");
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

function incrementChrono(valueToIncrement){

  var hour = Number($("#h").html());
  var minute = Number($("#m").html());
  var second = Number($("#s").html());
  var milliseconds = Number($("#ms").html());

  // Increment our display
  milliseconds += valueToIncrement;

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

  // Increment our real chronometer
  chronoValue = incrementChronoValue(chronoValue, chronoInterval)

  $("#ms").text(String(milliseconds).padStart(3, "0"));
  $("#s").text(String(second).padStart(2, "0"));
  $("#m").text(String(minute).padStart(2, "0"));
  $("#h").text(String(hour).padStart(2, "0"));
}

function decrementChrono(valueToDecrement){

  var hour = Number($("#h").html());
  var minute = Number($("#m").html());
  var second = Number($("#s").html());
  var milliseconds = Number($("#ms").html());

  // Decrement our display
  milliseconds -= valueToDecrement;

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

  // Increment our real chronometer
  chronoValue = incrementChronoValue(chronoValue, chronoInterval);

  $("#ms").text(String(milliseconds).padStart(3, "0"));
  $("#s").text(String(second).padStart(2, "0"));
  $("#m").text(String(minute).padStart(2, "0"));
  $("#h").text(String(hour).padStart(2, "0"));
}

function incrementChronoValue(chronometreReference, intervalToUpdate){
  chronometreReference += intervalToUpdate;

  return chronometreReference;
}

// Definition and Initialization of variables

var intervalID = null;
var chronoValue = 0; // Value in milliseconds
var chronoInterval = 20; // Value to wait between each interval in chronometer
