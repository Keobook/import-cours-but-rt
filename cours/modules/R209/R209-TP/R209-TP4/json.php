<?php 
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json; charset=utf-8');

  //URL of targeted site  
  $url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220.json";  
  $ch = curl_init();  

  // set URL and other appropriate options  
  curl_setopt($ch, CURLOPT_URL, $url);  
  curl_setopt($ch, CURLOPT_HEADER, 0);  
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);  

  // grab URL and pass it to the browser  

  $output = curl_exec($ch);  

  echo($output)?$output:http_response_code(404);

  // close curl resource, and free up system resources  
  curl_close($ch);  
  exit(0);
?>
