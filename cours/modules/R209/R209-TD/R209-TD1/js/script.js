
// Definition of functions
function checkCombinations(code,combination) {
  bp=0;
  mp=0;
  console.log("Code : "+code.toString());
  console.log("Combination: "+combination.toString());
  var check=code.slice();// A copy-pasta
  // BP
  for (k in check) {
    if (combination[k]==check[k]) {
      bp++;
      check[k]=-1;// Marque BP
    }
  }
  // MP
  for (i in combination) {
    if (combination[i]>=0) {
      for (j in check) {
        if (j!=i&&check[j]>=0) {// Case different and not checked
          if (combination[i]==check[j]) {
            mp++;
            check[k]=-2;// Marque BP
            break;
          }
        }
      }
    }
  }
  console.log("BP : "+bp+" MP : "+mp);
}

function newCode(tab) {
  for (let figure in tab) {
    tab[figure] = Math.floor(Math.random()*8);
  }
  console.log(tab);
  document.getElementById("code").innerHTML = tab.toString();
  newCombination();
}

function changeColor(btn) {
  var colors=["rouge","jaune","vert","bleu","orange","blanc","violet","fuchsia"];
  const colorIndex = (Number(btn.innerHTML) % colors.length) + 1
  const btnIndex = Number(btn.id.slice(-1)) - 1;

  combination[btnIndex] = colorIndex;

  console.log(btn.innerHTML, colorIndex, btnIndex, btn.id, btn.id.slice(-1))

  btn.setAttribute("class", colors[colorIndex]);
  btn.innerHTML = colorIndex;
}

function newCombination(){
  const gameRoot = document.getElementById("game");
  const lineHolder = document.createElement("div");
  const buttonLine = document.createElement("span");

  // Creating & initializing the 3 buttons
  // <button onclick="changeColor(this)">0</button>
  var btn1 = document.createElement("button");
  btn1.addEventListener("click", func => {
    changeColor(btn1);
  })
  btn1.innerHTML = "0";
  btn1.id = "btn-1";

  var btn2 = document.createElement("button");
  btn2.addEventListener("click", func => {
    changeColor(btn2);
  })
  btn2.innerHTML = "1";
  btn2.id = "btn-2";

  var btn3 = document.createElement("button");
  btn3.addEventListener("click", func => {
    changeColor(btn3);
  })
  btn3.innerHTML = "2";
  btn3.id = "btn-3";

  // Creating & initializing the results span DOM elements
  var spanLeft = document.createElement("span");
  spanLeft.innerHTML = "-";
  spanLeft.classList.add("bp");

  var spanRight = document.createElement("span");
  spanRight.innerHTML = "-";
  spanRight.classList.add("mp");

  // Creating & initializing the validation button
  var endButton = document.createElement("button");
  endButton.textContent = "OK";
  endButton.addEventListener("click", func => {
    verif(endButton);
  })

  // Appending the elements to form the line
  buttonLine.appendChild(btn1);
  buttonLine.appendChild(btn2);
  buttonLine.appendChild(btn3);

  buttonLine.appendChild(spanLeft);
  buttonLine.appendChild(spanRight);

  buttonLine.appendChild(endButton);

  // Adding the line of buttons to our Holder div
  lineHolder.appendChild(buttonLine);
  // Then setting it all in the document via our root div
  gameRoot.appendChild(lineHolder);
}

function verif(btn) {
  var childs=btn.parentNode.childNodes;
  for (k in childs) {
    if (childs[k].tagName == 'BUTTON') childs[k].disabled = true;
  }
}

// Variables definition
var bp = 0, mp = 0;
var table = [0,0,0];
var combination = [0, 0, 0]



// Scripting area
newCode(table);
