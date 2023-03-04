<?php
// Affiche les données sous forme de tableau HTML
// $data est un tableau de tableau associatif
// $limit est le nombre de lignes à afficher

function afficheDataTable($data, $limit=500) {
  if (is_array($data)) {
    printf("<table>\n");
    printf("<tr>"); 
    foreach (array_keys(current($data)) as $i=>$colName) {
      printf("<th>%s</th>",$colName);
    }
    printf("</tr>\n");
    if (sizeof($data) <= $limit) {
      foreach ($data as $i=>$row) {
        printf("<tr>"); 
        foreach ($row as $key=>$val) {
          printf("<td>%s</td>",$val);
        }
        printf("</tr>\n");
      }
    } else {
      // Display only the first $limit rows
      for ($i = 0; $i < $limit; $i++) {
        printf("<tr>"); 
        foreach ($data[$i] as $key=>$val) {
          printf("<td>%s</td>",$val);
        }
        printf("</tr>\n");
      }
    }
    printf("</table>\n");
  } else {
    printf("<h2 style='color:red;'>Erreur de données !!!</h2>\n");
  }
}
?>
