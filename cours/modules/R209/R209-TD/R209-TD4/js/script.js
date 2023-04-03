const date = new Date();

const [hour, minutes, seconds, milliseconds] = [
  date.getHours(),
  date.getMinutes(),
  date.getSeconds(),
  date.getMilliseconds(),
];

document.getElementById("start-btn").addEventListener("click", func => {
  document.getElementById("h").innerHTML = hour;
  document.getElementById("m").innerHTML = minutes;
  document.getElementById("s").innerHTML = seconds;
  document.getElementById("ms").innerHTML = milliseconds;
})
