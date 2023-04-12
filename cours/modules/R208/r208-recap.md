# Récapitulatif du cours de R208 sur la structuration des données

## Qu'est-ce que la structuration des données

La structuration des données est une notion important lorsque l'on parle d'interactions entre plusieurs services
tel que des APIs, bases de données ou encore seulement si l'on veut stocker des données dans des fichiers.

## Le langage XML

Le langage XML est un langage de balisage qui a la même structure que du HTML:

```xml
<main id="1" statut="exemple" />
```

où
- `main` est la balise
- `id` et `statut` sont des attributs

### Retour sur le TP de R208

> **Note**:  
> Je vais plus me concentrer sur les points du TP
> qui peuvent être mal compris, plus que refaire le TP de A à Z.

On suppose que le module `etree` de `lxml` est importé.

```py
  from lxml import etree
```

#### 1 - flux instantané

##### 1.1 - Nombre de points de vente

  On doit créer un script python affichant le nombre de points de vente, aussi appelés PDV.

  ```py
  ### On `parse` le fichier
  tree = etree.parse('./src/instant/instant.xml')
  ```

  Pour donner le nombre de PDV, on a deux méthodes,
  soit on utilise l'expression XPATH `count()`

  ```py
  nbr = int(tree.xpath("count(/pdv_liste/pdv)"))
  ```

  soit on utilise la fonction Python `len()`

  ```py
  nbr = len(tree.xpath("/pdv_liste/pdv"))
  ```

  La première méthode, on utilise l'expression `count()` dans XPATH,
  le nombre ressort en `float` donc si l'on veut un entier,
  on doit utiliser `int()` afin de le transformer.  
  Avec cette méthode, nous n'avons que le nombre,
  on ne pourra pas utiliser les éléments pour d'autres utilisations.

  La deuxième méthode, on utilise la fonction `len()` sur XPATH,
  qui nous renvoie en fait une liste de tous les éléments du fichier.  
  De base, le `len` ne nous renvoie pas de `float`
  (ce qui est normal, compliqué d'avoir 12.5 éléments dans une liste).  
  On peut en plus réutiliser notre liste d'éléments pour de futures utilisations.

##### 1.2 - Des informations détaillées sur le PDV autre

  Dans le cas où l'on a besoin d'informations détaillées sur une donnée
  minoritaire, nos conditions de filtrage vont être dans le négatif.  
  Donc, au lieu d'avoir une expression XPATH avec `attribut="valeur"`,
  on aura une expression XPATH avec `not(attribut="valeur")`.

  Cela peut évidemment varier selon les cas, mais dans notre cas,
  on veut des informations sur un PDV qui est ni routier, ni autoroutier.

> **Explication**:  
> Ici, on utilise une expression XPATH afin de filtrer nos résultats
> Le crochet nous permet d'émettre une expression de filtrage à 
> l'élement sur lequel on travaille, en l'occurence /pdv_liste/pdv.  
> Le "@" devant pop signifie que l'on veut un attribut de l'élement
> au lieu de chercher dans ses enfants, XPATH regardera alors sur la
> même ligne au lieu de regarder sur les lignes plus en bas.  
> On utilise donc une condition à la négative:  
> A ce niveau, on reste sur une expression très littérale.
> "Je veux tous les éléments pdv, enfant de pdv_liste, n'ayant pas
> comme valeur d'attribut pop 'R' ou 'A'".  
> Il nous sortira donc tous les éléments pdv ayant pour valeur
> autre chose que 'A' ou 'R'.

  On peut donc avoir comme code:

  ```py
  autres_pdv = tree.xpath("/pdv_liste/pdv[not(@pop='R') and not(@pop='A')]")

  ### Dans ce cas précis, nous n'avions pas besoin d'utiliser une
  ### liste car nous avions qu'un seul élement mais c'est un
  ### bon réflexe à avoir de boucler quand on travaille avec une
  ### liste.
  for pdv in autres_pdv:
    pop, id, cp = pdv.get("pop"), pdv.get("id"), pdv.get("cp")
    print(f'Un PDV autre a comme informations: \n\t- POP: {pop} \n\t- ID: {id} \n\t- CP: {cp}')
  ```

##### 1.7 - Combien de stations proposent du SP98 dans l'Hérault

A cette question, il faut comprendre que l'on veut filtrer
deux fois.

Une fois où l'on veut compter que les stations dans l'Hérault,
puis les stations qui servent du SP98.

Le mieux est d'utiliser une expression XPATH, à nouveau.

> **Explication**:  
> On va utiliser la fonction `starts-with` afin de filtrer pour l'Hérault.
> On l'utilise de la même manière que nos conditions `not` précédentes
> Elle fonctionne avec deux paramètres, le premier est la variable
> que l'on va chercher, en l'occurence c'est un attribut donc on met `@cp`
> puis on met entre guillemets ce par quoi on veut filtrer.
> C'est la même utilisation que la méthode `startswith()` de Python.
> 
> Après que l'on ait filtré sur les PDVs, on filtre les éléments `prix`.
> Vu que c'est une valeur fixe, il y a soit `SP98`, soit autre chose, on
> peut faire une simple condition, on écrit alors `@nom='SP98'`.

```py
nbr = len(tree.xpath("/pdv_liste/pdv[starts-with(@cp, '34')]/prix[@nom='SP98']"))

### Pour le total, on a juste besoin de ne pas mettre l'élement prix
### dans l'expression XPATH. (à revoir la formulation)
total = len(tree.xpath("/pdv_liste/pdv[starts-with(@cp, '34')]"))
```


## Le langage JSON

Le langage JSON est un langage de formattage et de stockage de données par paires.

Un exemple de fichier JSON:

```json
{
  "titre": "Un fichier d'exemple JSON",
  "auteur": "alexis-opolka",
  "site-web": "https://alexis-opolka.dev",
  "donnees": {
    "date": {
      "jours": ["lundi", "mardi", "mercredi"]
    },
  }
}
```

Dans cet exemple, `titre` est la clé et `Un fichier d'exemple JSON` est la valeur.  
La structure est équivalente à un dictionnaire Python.

### Retour sur le TD de R208

> **Note**:  
> Je traiterais le TD jusqu'à ce que je considère que l'expliquer
> pas à pas n'est plus pertinent.

#### 2 - Affichez les 3 premiers enregistrements du fichier `eve.json`

On doit implémenter en Python l'équivalent de la commande en-dessous.

```sh
cat eve.json | jq --slurp '.[:3]'
```

> **Explication:**  
> On affiche le contenu du fichier `eve.json` via `cat` puis
> on redirige la sortie vers `jq` (préalablement installé) avec
> l'option `slurp` et on affiche les 3 premières entrées (`'.[:3]'`).  
> Il faut s'imaginer que le slurp nous crée une liste avec
> chaque entrée puis on ne décide d'en afficher que trois.

On a un processus équivalent à:

- Etape 1: Notre cat affiche le fichier
  ```txt
  <Entrée 1>
  <Entrée 2>
  <Entrée 3>
  <Entrée 4>
  ```
- Etape 2: On redirige la sortie vers jq en mode --slurp
  ```txt
  [<Entrée 1>, <Entrée 2>, <Entrée 3>, <Entrée 4>]
  ```
- Etape 3: On coupe notre liste à l'indice n°3
  ```txt
  [<Entrée 1>, <Entrée 2>, <Entrée 3>]
  ```
- Etape 4: On affiche nos entrées sous forme de JSON (et colorisées en passant)
  ```txt
  {
    <Entrée 1>,
    <Entrée 2>,
    <Entrée 3>
  }
  ```

Ca, c'est ce qui s'est passé avec `JQ`, maintenant, on doit le faire en Python.

On utilise deux bibliothèques en Python afin d'avoir le même résultat: `json` et `rich`.

On crée une liste, que j'ai décidé d'appeler `records`.

```py
records = []
```

puis on utilise un bloc `with` où l'on ouvre le fichier en lecture:

```py
with open("eve.json", "rt") as fin: ### Fin comme Fichier entrant (File in)
  for json_data in fin:
    enregistrement = json.loads(json_data)
    records.append(enregistrement)
```

> **Explication**:  
> On utilise le block `with` car il nous permet de ne pas nous préoccuper
> de la fermeture du fichier après coup.  
> On boucle ensuite dans notre fichier, c'est à dire
> que l'on itère à chaque ligne.  
> Ensuite, on attribue à la variable `enregistrement` la ligne
> actuelle sous forme de dictionnaire en utilisant la
> librairie `json`.  
> Puis on ajoute à notre liste `records` notre enregistrement.

Après avoir construit notre liste contenant ainsi tous nos
enregistrements, on peut les afficher.  
Deux choix s'offrent à nous:

- On affiche que les trois directement avec un print, on fera
  cela en une ligne.  
  Point négatif, on ne pourra faire que cette action.

  ```py
  print(records[:3])
  ```

  > **Note**:  
  > Il est possible de substituer la valeur `3`
  > par une variable de son choix.

- On affiche une ligne par une ligne dans une boucle.  
  Point positif, on peut ajouter d'autres actions lors de l'affichage.  
  Point négatif, ça risque de prendre plus de temps vu que l'on affiche
  notre liste un par un.

  ```py
  for record in record[:3]:
    print(record)
  ```

  > **Note**:  
  > Il est possible de substituer la valeur `3`
  > par une variable de son choix.

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
