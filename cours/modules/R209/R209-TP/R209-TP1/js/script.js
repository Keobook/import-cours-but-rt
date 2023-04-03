
var idCourbe = 0;


var jours=[1,2,3,4,5,6,7,8,9,10];
var tmin=[7.0,7.0,4.4,2.7,8.2,2.3,4.1,5.5,11.6,8.2];
var colors=["black","yellow","blue","magenta","aqua","coral","red","chartreuse"];
var wind = [68.5,79.6,42.6,64.8,50.0,18.5,18.5,38.9,38.9,35.2];

var courbe1={
  label: "Température minimum en °C",
  backgroundColor: "darkcyan",
  borderColor: "darkcyan",
  yAxisID: "yTmin",
  data: tmin,
  pointRadius: 5,
  pointHoverRadius: 10,
  fill: false,
};

var courbe2 = {
  label: "Vitesse du vent (en Km/h)",
  backgroundColor: "darkorchid",
  borderColor: "darkorchid",
  yAxisID: "yWind",
  data: wind,
  pointRadius: 5,
  pointHoverRadius: 10,
  fill: false,
};

var axeX = {
  display: true,
  scaleLabel: {
    display: true,
    labelString: "Numéro du jour"
  }
};
var axeY1 = {
  id: "yTmin",
  position: "left",
  ticks: {
    suggestedMin: 2,
    suggestedMax: 12
  },
  display: true,
  scaleLabel: {
    display: true,
    labelString: "Température en °C"
  },
  gridLines: {
    drawOnChartArea: false
  }
};
var axeY2 = {
  id: "yWind",
  position: "right",
  ticks: {
    suggestedMin: 20,
    suggestedMax: 80
  },
  display: true,
  scaleLabel: {
    display: true,
    labelString: "Vitesse en Km/h"
  }
};

var config={
  type: "line",
  data: {labels: jours, datasets: [courbe1]},
  options: {
    title: {display: true, text: "Béziers en 2007"},
    scales: {
      xAxes: [axeX],
      yAxes: [axeY1, axeY2],
    },
    tooltips: {
      mode: "index",
      intersect: false,
    }
  }
};

// On ajoute notre deuxième courbe après avoir défini config
config.data.datasets.push(courbe2);

window.onload=function() {
  var ctx=document.getElementById("canvas").getContext("2d");
  const selectRoot = document.getElementById("couleur");
  const echellesBox = document.getElementById("echelles");
  const radioBox = document.getElementById("radio-box");
  window.graph1=new Chart(ctx,config);

  // Dynamically creating the options for selecting colors
  for (i in colors.sort()) {
    var colorOption = document.createElement("option");
    colorOption.setAttribute("value", colors[i]);
    colorOption.innerHTML = colors[i];

    selectRoot.appendChild(colorOption);
  }

  // Dynamically creating the radio inputs for selecting which dataset we want
  // to act on.
  for (i in config.data.datasets) {
    const datasetIndex = document.createElement("input");
    const datasetIndexText = document.createElement("span")
    datasetIndex.setAttribute("type", "radio");
    datasetIndex.setAttribute("name", "dataset");
    datasetIndex.setAttribute("value", i);
    // Dynamically set the current dataset to checked
    if (i == idCourbe) {
      datasetIndex.setAttribute("checked", true);
    }

    datasetIndexText.appendChild(datasetIndex);
    datasetIndexText.innerHTML += "Courbe " + i;

    datasetIndexText.addEventListener("click", function(event) {
      if (event.target && event.target.matches("input[type='radio']")){
        idCourbe = event.target.value;
        console.log(`Changed dataset index: ${idCourbe} <- ${event.target.value}`)
      }
    })

    radioBox.appendChild(datasetIndexText);
  }


  // Adding EventListener on colors select
  selectRoot.addEventListener("change", function() {
    const value = this.options[this.selectedIndex].value;
    const textContent = this.options[this.selectedIndex].text;

    config.data.datasets[idCourbe].backgroundColor = colors[this.selectedIndex];
    config.data.datasets[idCourbe].borderColor = colors[this.selectedIndex];
    window.graph1.update()

    console.log(`Dataset: ${idCourbe} - Couleur ${this.selectedIndex}: ${value} -> ${textContent}`)
  })

  // Adding EventListener on échelles checkbox
  echellesBox.addEventListener("change", function() {
    const isChecked = this.checked;

    for (i in config.options.scales) {
      config.options.scales[i][0].scaleLabel.display = isChecked;
    }
    window.graph1.update()
  })
};
