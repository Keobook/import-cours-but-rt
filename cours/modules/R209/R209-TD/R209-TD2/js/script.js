
// Functions definition
function createHLine(echiquier) {
  var case1=document.createElement("div");
  case1.setAttribute("class","numeroHV");
  echiquier.appendChild(case1);
  for(var j=0;j<8;j++) {
    var case2=document.createElement("div");
    case2.setAttribute("class","numeroH");
    case2.innerHTML=lettres[j].toUpperCase();
    echiquier.appendChild(case2);
  }
  case1=document.createElement("div");
  case1.setAttribute("class","numeroHV");
  echiquier.appendChild(case1);
}
function createEchiquier(echiquier) {
  createHLine(echiquier);
  // First loop, we're creating the numbers
  // on the sides of the game
  for(var i=8;i>0;i--) {
    var case1=document.createElement("div");
    case1.setAttribute("class","numeroV");
    case1.innerHTML=i;
    echiquier.appendChild(case1);
    // Second loop, we're creating each cell
    // of the board, line by line
    for(var j=0;j<8;j++) {
      var case2=document.createElement("div");
      const cellId = lettres[j]+i;
      case2.setAttribute("class", `${(j+i)%2 == 0 ? "blanc" : "noir"}`);
      case2.setAttribute("id", cellId);

      if (noirs[cellId ]!= undefined ) {
        case2.innerHTML = noirs[cellId];
      } else if (blancs[cellId] != undefined) {
        case2.innerHTML = blancs[cellId];
      }

      echiquier.appendChild(case2);
    }
    case1=document.createElement("div");
    case1.setAttribute("class","numeroV");
    case1.innerHTML=i;
    echiquier.appendChild(case1);
  }
  createHLine(echiquier);
}

// Var definition
var coup=0;
var joueur=["1","2","1","2","1","2","1","2","1","1","2"];
var debut=["e2","e7","g1","b8","f1","a7","b5","g8","e1","h1","f8"];
var fin=["e4","e5","f3","c6","b5","a6","a4","f6","g1","f1","e7"];

var lettres=["a","b","c","d","e","f","g","h"];
var noirs={"a8":"&#9820;","b8":"&#9822;","c8":"&#9821;","d8":"&#9819;","e8":"&#9818;","f8":"&#9821;","g8":"&#9822;","h8":"&#9820;",
           "a7":"&#9823;","b7":"&#9823;","c7":"&#9823;","d7":"&#9823;","e7":"&#9823;","f7":"&#9823;","g7":"&#9823;","h7":"&#9823;"};
var blancs={"a2":"&#9817;","b2":"&#9817;","c2":"&#9817;","d2":"&#9817;","e2":"&#9817;","f2":"&#9817;","g2":"&#9817;","h2":"&#9817;",
           "a1":"&#9814;","b1":"&#9816;","c1":"&#9815;","d1":"&#9813;","e1":"&#9812;","f1":"&#9815;","g1":"&#9816;","h1":"&#9814;"};

// Js Scripting
const echiquier = document.getElementById("echiquier");
createEchiquier(echiquier);

// Event listener on "Next" button
document.getElementById("next").addEventListener("click", func => {
  var tries = document.getElementById("coup");
  const history = document.getElementById("history");
  var tryNumber = Number(tries.innerHTML);

  // Creating a new line of history
  if (tryNumber < joueur.length){
  const newHistoryLine = document.createElement("p");
  newHistoryLine.innerHTML = `Coup ${tryNumber+1} (Joueur ${joueur[tryNumber]}) : ${debut[tryNumber]}-${fin[tryNumber]}`;

  // We add the next movement
  document.getElementById(fin[tryNumber]).innerHTML = document.getElementById(debut[tryNumber]).innerHTML;
  document.getElementById(debut[tryNumber]).innerHTML = "";

  history.appendChild(newHistoryLine);
  tries.innerHTML = tryNumber + 1;
  }
})

// Event listener on "Previous" button
document.getElementById("prev").addEventListener("click", func => {
  var tries = document.getElementById("coup");
  const history = document.getElementById("history");
  var tryNumber = Number(tries.innerHTML) - 1 ;

  if (tryNumber >= 0){
    tries.innerHTML = tryNumber;

    // We remove the last move
    document.getElementById(debut[tryNumber]).innerHTML = document.getElementById(fin[tryNumber]).innerHTML;
    document.getElementById(fin[tryNumber]).innerHTML = "";

    history.removeChild(history.lastChild);
  }

})
