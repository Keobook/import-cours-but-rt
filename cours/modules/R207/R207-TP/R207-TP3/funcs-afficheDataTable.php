<?php
// Affiche les données sous forme de tableau HTML
// $data est un tableau de tableau associatif
function afficheDataTable($data) {
  if (is_array($data)) {
    printf("<table>\n");
    printf("<tr>"); 
    foreach (array_keys(current($data)) as $i=>$colName) {
      printf("<th>%s</th>",$colName);
    }
    printf("</tr>\n");
    foreach ($data as $i=>$row) {
      printf("<tr>"); 
      foreach ($row as $key=>$val) {
        printf("<td>%s</td>",$val);
      }
      printf("</tr>\n");
    }
    printf("</table>\n");
  } else {
    printf("<h2 style='color:red;'>Erreur de données !!!</h2>\n");
  }
}
?>
