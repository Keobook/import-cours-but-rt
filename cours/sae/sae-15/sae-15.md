# SAE-15 Traiter les données

## Les statistiques

- Acquisition
  - capteurs
  - webscrapping
- Analyse / Interprétation
  - Indicateurs
  - Graphs

### Exemple de série chifrée

|                                      |       Notes A1       |       Notes A2        |
| :----------------------------------: | :------------------: | :-------------------: |
|                                      |          10          |          18           |
|                                      |          11          |          16           |
|                                      |          9           |           2           |
|                                      |          10          |           4           |
|                                      |          12          |          11           |
|                                      |          8           |          12           |
|                                      |          10          |           7           |
|        $\frac{1}{n} \sum x_i$        |          10          |          10           |
| $\frac{1}{n} \sum (x_i - \bar{x})^2$ |         1,42         |         30,57         |
|               $\sigma$               | $\sqrt{1.42} = 1.19$ | $\sqrt{30.57} = 5.52$ |

| x <br> Maths | y <br> Reseau |
| :----------: | :-----------: |
|      12      |       8       |
|      6       |       7       |
|      13      |       8       |
|      9       |      17       |
|      2       |      20       |
|      14      |      17       |

$(x_i - \bar{x} ) (y_i - \bar{x})$

#### La moyenne

La moyenne est la somme des valeurs divisée par le nombre de valeurs.  
$\bar{x} = \frac{1}{n} \sum x_i$

#### La variance

La variance est la moyenne des écarts à la moyenne.  
${1 \over n} \sum (x_i - \bar{x})^2$

#### L'écart-type

L'écart-type est la racine de la variance.  
$\sigma = \sqrt{var(x)}$

#### La covarience

Avec deux valeurs, le produit $(x - \bar{x})(y - \bar{y})$.  
$cov(x,y) = {1 \over n} \sum (x - \bar{x})(y - \bar{y})$

#### La correlation

$r(x,y) = \frac{cov(x,y)}{\sigma x \sigma y}$

La correlation n'est pas la causalité.  
Cela veut aussi dire qu'il y a susceptiblement une raison sous-jacente.
