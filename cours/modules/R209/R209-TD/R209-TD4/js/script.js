
// Definition of Event handlers

$("#start-btn").on("click", function(){
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

  incrementChrono()
})

// Definition of Functions

function incrementChrono(){
  var hour = Number($("#h").html());
  var minute = Number($("#m").html());
  var second = Number($("#s").html());
  var milliseconds = Number($("#ms").html());

  milliseconds += 10;

  String($("#ms").text(milliseconds)).padStart(2, "0");
  String($("#s").text(minute)).padStart(2, "0");
  String($("#m").text(second)).padStart(2, "0");
  String($("#h").text(hour)).padStart(2, "0");
}
