<?php
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json; charset=utf-8');

  if (isset($_GET["ref"])) {
    $reference = $_GET["ref"];
  } else {
    $reference = null;
  };

  $statusCode = null;

  if (is_null($reference)) {
    @shell_exec("curl -o ./data2.json 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_GeolocCompteurs.geojson'");
    $r = @file_get_contents('.\data2.json');
    echo($r)?$r:http_response_code(404);
    exit(0);
  } else {
    $path = "./temp/". $reference .".json";
    @shell_exec("pwsh ./curl-me.ps1 ". $reference ."");
    $r = @file_get_contents($path);
    echo($r)?$r:http_response_code(404);
    exit(0);
  }
?>
