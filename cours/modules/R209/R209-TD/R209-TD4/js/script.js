
// Definition of Event handlers

$("#start-btn").click(function(){
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
})

