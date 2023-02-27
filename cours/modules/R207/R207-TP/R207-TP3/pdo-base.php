<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TP-2 de R207 de Alexis Opolka</title>
  <link rel="stylesheet" href="foot.css">
</head>

<body>
  <?php
    // On initialise les variables
    $seasonToShow = $_GET['res'];
    if($seasonToShow == null) $seasonToShow = 1;
    $tables = array(1 => 'equipes', 2 => 'equipes17_UEFA', 3 => 'equipes17_F1', 4 => 'equipes14_UEFA');
    $titres = array(1 => 'Ligue1 2018-2019', 2 => 'UEFA 2017-2018', 3 => 'Ligue1 2017-2018', 4 => 'UEFA 2014-2015');

    foreach ($titres as $key => $value) {
      printf("<a href='?res=%s'>%s</a>", $key, $value);
    }

    printf("<h1>Liste des équipes - %s</h1>", $titres[$seasonToShow]);

  if ($seasonToShow == 1) {
    $rowSigle = true;
    $headSigle = "<th>Son sigle</th>";
  } else {
    $rowSigle = "";
    $headSigle = "";
  }
  ?>
  <table>
    <?php
    printf("
      <tr>
        <th>Nom de l'équipe</th>"
        . $headSigle .
        "<th> Son groupe</th>
        <th>Ses points</th>
        <th>Matchs joués </th>
        <th>Matchs gagnés </th>
        <th>Matchs perdus </th>
        <th>Matchs nuls </th>
        <th>Buts marqués </th>
        <th>Buts encaissés </th>
      </tr>");
    try {
      $pdo = new PDO('mysql:host=localhost;charset=utf8;dbname=db_OPOLKA', '22203995', '752277');
      $statement = $pdo->query("SELECT * FROM ". $tables[$seasonToShow] ." ORDER BY nom ASC");
      while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
        printf("
        <tr>
          <td>" . $row['nom'] . "</td>");
        if ($rowSigle === true) {
          printf("<td> <img src='./logos/" . $row['sigle'] . ".png' alt='Logo de l&apos;équipe de " . $row['nom'] . "' class='logos'> </td>");
        }
        printf(
          "<td>" . $row['groupe'] . "</td>
          <td>" . $row['points'] . "</td>
          <td>" . $row['joues'] . "</td>
          <td>" . $row['gagnes'] . "</td>
          <td>" . $row['perdus'] . "</td>
          <td>" . $row['nuls'] . "</td>
          <td>" . $row['marques'] . "</td>
          <td>" . $row['encaisses'] . "</td>
        </tr>");
      }
      $statement->closeCursor();
    } catch (Exception $e) {
      printf("ERREUR : %s !!!\n", $e->getMessage());
    }
    ?>
  </table>
</body>

</html>
