<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TP-3 de R207 de Alexis Opolka</title>
  <link rel="stylesheet" href="foot-tp3.css">
</head>

<body>
  <?php

  // Require once the file that contains the function to show the table
  require_once('funcs-afficheDataTable.php');

  // The PDO of our database
  $pdo = new PDO('mysql:host=localhost;charset=utf8;dbname=db_OPOLKA', '22203995', '752277');

  // Let's initialize our variables
  if (empty($_GET['filter'])) {
    $filter = null;
  } else {
    $filter = $_GET['filter'];
  }

  // The $limitToDisplay is a dev tweak used to limit the generation of the table
  // It should not be implemented as it is now in a production environment
  if (empty($_GET['limit'])) {
    $limitToDisplay = 100;
  } else {
    $limitToDisplay = $_GET['limit'];
  }

  if ($filter == null) {
    // If the filter is empty, we don't want to filter the results
    // This request should not be edited
    $sql = "SELECT e1.nom AS 'Equipe 1', matchs.score1, matchs.score2, e2.nom AS 'Equipe 2', dateMatch AS Jour FROM matchs, equipes AS e1, equipes AS e2
    WHERE e1.id = matchs.eq1 AND e2.id = matchs.eq2
    ORDER BY e1.nom ASC;";
  } else {
    // If the filter is not empty, we want to filter the results

    // But first, we need to reconstruct the $_GET['matchs'] values into an array usable for both our sql request and our conditions
    if (empty($_GET['matchs'])) {
      $matchs = null;
    } else {
      $matchs = explode(",", $_GET['matchs']);
    }

    if ($matchs == null or sizeof($matchs) > 1) {
      // We do want to filter the results, but we don't want to filter the type of match
      $sql = "SELECT e1.nom AS 'Equipe 1', matchs.score1, matchs.score2, e2.nom AS 'Equipe 2', dateMatch AS Jour FROM matchs, equipes AS e1, equipes AS e2
      WHERE e1.id = matchs.eq1 AND e2.id = matchs.eq2
      AND (e1.nom LIKE '%" . $filter . "%' OR e2.nom LIKE '%" . $filter . "%')
      ORDER BY e1.nom ASC;";
    } else {
      // We want to filter the results and the type of match
      $matchCondition = $_GET['matchs'] == "aller" ? " e1.nom LIKE '%" . $filter . "%' " : " e2.nom LIKE '%" . $filter . "%' ";

      $sql = "SELECT e1.nom AS 'Equipe 1', matchs.score1, matchs.score2, e2.nom AS 'Equipe 2', dateMatch AS Jour FROM matchs, equipes AS e1, equipes AS e2
      WHERE e1.id = matchs.eq1 AND e2.id = matchs.eq2
      AND" . $matchCondition . "
      ORDER BY e1.nom ASC;";
    }
  }
  ?>

  <h1>Liste des Matchs</h1>

  <!-- The form used to sort/filter our results -->
  <form action="./matchs.php" method="get">
    Equipe:
    <input type="text" name="filter" id="filter-input" value="">
    <select name='filter' id='filter-dropdown'>
      <?php
      // The dropdown menu that will be used to filter the results
      // It will be generated from database
      $statement = $pdo->query("SELECT nom FROM equipes ORDER BY nom ASC;");
      $data = $statement->fetchAll(PDO::FETCH_ASSOC);
      foreach ($data as $row) {
        print("<option value='". $row['nom'] ."'>". $row['nom'] ."</option>");
      }
      ?>
    </select>
    <input type="checkbox" name="matchs" value="aller" id="match-aller"> Matchs Aller
    <input type="checkbox" name="matchs" value="retour" id="match-retour"> Matchs Retour
    <input type="button" onclick="GetValueInLine()" value="Rechercher">
  </form>
  <?php
  $statement = $pdo->query($sql);
  $data = $statement->fetchAll(PDO::FETCH_ASSOC);
  printf("Nombre de résultats: <strong>%s</strong>", count($data));
  afficheDataTable($data, $limitToDisplay);
  ?>

  <!-- A div on the upper right corner of the page letting us set if we want to have a dropdown menu or an input to type what we want to filter -->
  <div id="dev-set" class="fixed-right dev-corner">
    <h2>Dev Settings</h2>
    <form action="./matchs.php" method="get">
      <input type="radio" name="dev" value="dropdown" id="dev-dropdown" checked> Dropdown
      <input type="radio" name="dev" value="input" id="dev-input"> Input
      <br />
      <!-- The limit of results we want to see while dev -->
      <label for="dev-limit">Limit:</label>
      <input type="number" name="limit" id="dev-limit" value="100">
      <input type="button" onclick="GetValueInLine()" value="Valider">
    </form>
  </div>

</body>
<script>
  // The function that will recheck the checkboxes when the page is reloaded
  // depending on the value of the $_GET['matchs'] variable
  function recheck() {
    // The user wants to have all the results
    if (window.location.href.includes("matchs=aller,retour")) {
      document.getElementById("match-aller").checked = true;
      document.getElementById("match-retour").checked = true;
    }
    // The user wants to filter the results by the team that played at home
    if (window.location.href.includes("matchs=aller")) {
      document.getElementById("match-aller").checked = true;
    }
    // The user wants to filter the results by the team that played away
    if (window.location.href.includes("matchs=retour")) {
      document.getElementById("match-retour").checked = true;
    }
  }

  // The function that will take the value from the form and put in in 'line' as we want it to be with the php code
  // The $_GET['filter] should not be touched but the $_GET['matchs] should be arranged into an array letting
  // the user choose between "aller" and "retour" or both
  function GetValueInLine() {
    if (document.getElementById("dev-input").checked) {
      // If the user wants to use an input to filter the results
      var filter = document.getElementById("filter-input").value;
    } else {
      // If the user wants to use a dropdown menu to filter the results
      var filter = document.getElementById("filter-dropdown").value;
    }
    const matchs = () => {
      var matchs = [];
      if (document.getElementById("match-aller").checked) {
        matchs.push("aller");
      }
      if (document.getElementById("match-retour").checked) {
        matchs.push("retour");
      }
      return matchs;
    }

    var toSend = {
      filter: filter,
      matchs: matchs()
    }
    // Log the value in the console
    console.log(toSend);
    // Put the value of the form in the url and reload the page
    // Take into account the values of the dev corner
    if (document.getElementById("dev-input").checked) {
      window.location.href = "./matchs.php?filter=" + filter + "&matchs=" + matchs() + "&dev=input&limit=" + document.getElementById("dev-limit").value;
    } else {
      window.location.href = "./matchs.php?filter=" + filter + "&matchs=" + matchs() + "&dev=dropdown&limit=" + document.getElementById("dev-limit").value;
    }
  }

  // The function that will change our webpage depending of the actions taken in the dev corner
  // The function should update the values of the dev form and the values of the main form
  function TakeDevSettings() {
    if (window.location.href.includes("dev=input")) {
      // The user wants to have an input to type what he wants to filter
      document.getElementById("filter-input").style.display = "initial";
      document.getElementById("filter-dropdown").style.display = "none";
      document.getElementById("dev-input").checked = true;
    } else if (window.location.href.includes("dev=dropdown")) {
      // The user wants to have a dropdown menu to choose what he wants to filter
      document.getElementById("filter-input").style.display = "none";
      document.getElementById("filter-dropdown").style.display = "initial";
      document.getElementById("dev-dropdown").checked = true;
    } else {
      // The user just landed on the page and haven't tweaked anything
      // We just set the default values to input and 100
      document.getElementById("filter-input").style.display = "initial";
      document.getElementById("filter-dropdown").style.display = "none";
      document.getElementById("dev-input").checked = true;
      document.getElementById("dev-limit").value = 100; 
    }

    // The user wants to change the limit of results
    if (window.location.href.includes("limit=")) {
      var limit = window.location.href.split("limit=")[1];
      document.getElementById("dev-limit").value = limit;
    }
  }

  // The function to set the value of the dropdown menu and the input field to the value of the $_GET['filter'] variable
  function SetValues() {
    if (window.location.href.includes("filter=")) {
      var filter = window.location.href.split("filter=")[1].split("&")[0];
      document.getElementById("filter-input").value = filter;
      document.getElementById("filter-dropdown").value = filter;
    }
  }

  // We execute the functions when the page is loaded
  window.onload = function() {
    recheck();
    TakeDevSettings();
    SetValues();
  }
</script>

</html>
