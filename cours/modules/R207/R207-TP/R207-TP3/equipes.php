<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TP-3 de R207 de Alexis Opolka</title>
  <link rel="stylesheet" href="foot.css">
</head>

<body>
  <?php

  // Require once the file that contains the function to show the table
  require_once('funcs-afficheDataTable.php');

  $tables = array(1 => 'equipes', 2 => 'equipes17_UEFA', 3 => 'equipes17_F1', 4 => 'equipes14_UEFA');
  $titres = array(1 => 'Ligue1 2018-2019', 2 => 'UEFA 2017-2018', 3 => 'Ligue1 2017-2018', 4 => 'UEFA 2014-2015');

  // The PDO of our database
  $pdo = new PDO('mysql:host=localhost;charset=utf8;dbname=db_OPOLKA', '22203995', '752277');

  // On initialise les variables
  if (empty($_GET['res'])) {
    $seasonToShow = 1;
  } else {
    $seasonToShow = $_GET['res'];
  }

  if (empty($_GET['filter'])) {
    $sql = "SELECT * FROM " . $tables[$seasonToShow] . " ORDER BY nom ASC";
  } else {
    $sql = "SELECT * FROM " . $tables[$seasonToShow] . " WHERE nom LIKE '%" . $_GET['filter'] . "%' ORDER BY nom ASC";
  }

  foreach ($titres as $key => $value) {
    printf("<a href='?res=%s'>%s</a>", $key, $value);
  }

  printf("<h1>Liste des équipes </h1>");

  if ($seasonToShow == 1) {
    $rowSigle = true;
    $headSigle = "<th>Son sigle</th>";
  } else {
    $rowSigle = "";
    $headSigle = "";
  }
  ?>

  <form action="./equipes.php" method="get">
    Equipe: 
    <input type="text" name="filter" id="filter-id">
    <input type="submit" value="Rechercher">
  </form>
  <?php
    $statement = $pdo->query($sql);
    $data = $statement->fetchAll(PDO::FETCH_ASSOC);
    printf("Nombre de résultats: <strong>%s</strong>", count($data));
    afficheDataTable($data);
  ?>
</body>

</html>
