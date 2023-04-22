<?php
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json; charset=utf-8');

  @shell_exec("pwsh .\curl-test.ps1");
  $r = @file_get_contents('.\data.json');
  echo($r)?$r:http_response_code(404);
  exit(0);
?>
