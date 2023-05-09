if ($args.Length -eq 1) {
  Write-Host "Reference to get: $args.json"
  curl.exe "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_$args.json"
}
