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

  // The PDO of our database
  $pdo = new PDO('mysql:host=localhost;charset=utf8;dbname=db_OPOLKA', '22203995', '752277');

  // On initialise les variables

  if ($_GET['filter'] == null) {
    $sql = "SELECT e1.nom AS 'Equipe 1', matchs.score1, matchs.score2, e2.nom AS 'Equipe 2', dateMatch AS Jour FROM matchs, equipes AS e1, equipes AS e2 ORDER BY e1.nom ASC";
  } else {
    $sql = "SELECT e1.nom AS 'Equipe 1', matchs.score1, matchs.score2, e2.nom AS 'Equipe 2', dateMatch AS Jour FROM matchs, equipes AS e1, equipes AS e2 WHERE nom LIKE '%" . $_GET['filter'] . "%' ORDER BY e1.nom ASC";
  }

  printf("<h1>Liste des matchs </h1>");

  ?>

  <form action="./index.php" method="get">
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
