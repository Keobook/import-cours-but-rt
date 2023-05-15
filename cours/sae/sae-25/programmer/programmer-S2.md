# Programmer - Portfolio S2

- [Programmer - Portfolio S2](#programmer---portfolio-s2)
  - [Composantes essentielles](#composantes-essentielles)
    - [En étant à l’écoute des besoins du client et des différents acteurs impliqués](#en-étant-à-lécoute-des-besoins-du-client-et-des-différents-acteurs-impliqués)
    - [En utilisant une approche rigoureuse et méthodique (démarche scientifique)](#en-utilisant-une-approche-rigoureuse-et-méthodique-démarche-scientifique)
    - [En choisissant les outils et l’environnement de développement adaptés](#en-choisissant-les-outils-et-lenvironnement-de-développement-adaptés)
    - [En intégrant les problématiques de sécurité](#en-intégrant-les-problématiques-de-sécurité)
  - [Apprentissages critiques](#apprentissages-critiques)
    - [Utiliser un système informatique et ses outils](#utiliser-un-système-informatique-et-ses-outils)
    - [Lire, comprendre, exécuter, corriger et modifier un programme](#lire-comprendre-exécuter-corriger-et-modifier-un-programme)
    - [Comprendre et traduire un algorithme, dans un langage et pour un environnement donné](#comprendre-et-traduire-un-algorithme-dans-un-langage-et-pour-un-environnement-donné)
    - [Connaître l’architecture et les technologies d’un site Web](#connaître-larchitecture-et-les-technologies-dun-site-web)
    - [Adapter le format de stockage et de transport des données au besoin de l’application](#adapter-le-format-de-stockage-et-de-transport-des-données-au-besoin-de-lapplication)
    - [S’intégrer dans un environnement propice au développement et au travail collaboratif](#sintégrer-dans-un-environnement-propice-au-développement-et-au-travail-collaboratif)


## Composantes essentielles

### En étant à l’écoute des besoins du client et des différents acteurs impliqués

lorem ipsum

### En utilisant une approche rigoureuse et méthodique (démarche scientifique)

lorem ipsum

### En choisissant les outils et l’environnement de développement adaptés

lorem ipsum

### En intégrant les problématiques de sécurité

En développant le site pour l'association Petits Papiers d'Architecture,
j'ai dû implanter ce que l'on appelle des Linter qui sont appellés avant d'envoyer le code sur le dépôt GitHub
afin d'éviter des erreurs de syntaxe puisque l'environnement de développement
(accessible à l'adresse: [dev.petitspapiersdarchitecture.fr](http://dev.petitspapiersdarchitecture.fr))
se compile et est publié à chaque nouveau push sur le dépôt.

## Apprentissages critiques

### Utiliser un système informatique et ses outils

lorem ipsum

### Lire, comprendre, exécuter, corriger et modifier un programme

lorem ipsum

### Comprendre et traduire un algorithme, dans un langage et pour un environnement donné

lorem ipsum

### Connaître l’architecture et les technologies d’un site Web

L'architecture d'un site web se compose principalement de deux éléments :

- Le front-end
- Le back-end

Bien souvent, le front-end caractérise tout ce qui va se passer sur le client.  
Le back-end caractérise, quant à lui, tout ce qui va se passer que ce soit sur
les serveurs ou au niveau de l'infrastruture.

Je vais donc qualifier les langages de balisage tel que `HTML, XML, XHTML`,
les langages de style tel que `CSS, SCSS`,
et les langages de programmation tel que `JavaScript et TypeScript`
comme étant des langages de front-end.  
A contrario, je vais qualifier les langages PHP, JavaScript avec NodeJS,
les langages de bases de données comme MySQL, PostgreSQL, Flux (de InfluxDB), etc.
comme étant des langages de back-end.

Aux langages, je peux y ajouter les frameworks et les librairies qui, eux,
sont bien plus nombreux.  
Pour n'en citer qu'une infime partie :  

- Pour les framework, nous avons `ReactJS`, `VueJS`.
- Pour les librairies, nous avons `JQuery`, `Bootstrap`, `Leaflet`.


En ce qui concerne les serveurs web, je peux citer les deux majoritaires
du marché étant `Apache` et `Nginx`.  

### Adapter le format de stockage et de transport des données au besoin de l’application

Lors de la SAE-15, je devais créer un programme qui permettait de
récolter des données sur l'API de la ville de Montpellier afin de pouvoir
analyser et interpréter les données d'occupations des parkings à voitures
et vélos de la ville.

Pour ce faire, je devais récupérer les données au format XML et en GBFS.  
J'ai donc préféré, avec mon binôme, d'utiliser le format CSV qui nous permettait
facilement d'enregistrer en plus des données la date et l'heure de la requête
effectuée et d'ainsi construire un historique des données.

Ce n'est que plus tard, où je me suis penché sur l'analyse de données en utilisant
InfluxDB et Grafana que je me suis rendu compte qu'il était plus préférable
de travailler directement en Flux (le langage d'InfluxDB) au lieu d'avoir
à tout transformer en CSV puis y traduire en Flux.  

Malgré cet inconvénient (et travail en plus), le fait d'avoir déjà tout normalisé dans un format précis et d'une manière déterminée
a permis, à mon binôme et à moi, d'importer les données récoltées
dans la base de données pour ensuite sortir des graphes.

### S’intégrer dans un environnement propice au développement et au travail collaboratif

Avant tout, on se doit de définir qu'est-ce qu'un environnement
propice au développement puis qu'est-ce qu'un environnement propice
au travail collaboratif.

D'après moi, un environnement propice au développement est un
environnement qui permet à un développeur ou à une équipe
de pouvoir se concentrer sur le code en s'occupant des points
sensibles et/ou techniques de tous projets.  
C'est à dire que l'environnement doit notamment avoir un logiciel 
de gestion de version, un focus sur la codebase, un environnement
de build et de déploiement, la possibilité de faire du CI/CD.

Un environnement propice au travail collaboratif, de ce que j'en 
pense, doit permettre de discuter sur des problèmes dans des fils
de discussion dédiés, un système de tickets, un système afin
de pouvoir trier et catégoriser les informations.

Ainsi, d'après moi, un environnement propice au développement
et au travail collaboratif doit avoir l'ensemble des points
cité ci-dessus, ou du moins, la majorité.  
Il a donc un focus sur le code avec un logiciel de gestion de 
version, la possibilité de créer des tickets (aussi appelés issues)
où la discussion peut se faire à part du code, un système de labels,
etc.


Il existe plusieurs environnements qui sont propices au développement et au travail collaboratif.  
Je peux citer les plus connus qui sont GitHub, GitLab et BitBucket.  

Etant utilisateur de GitHub depuis 2019-2020, j'ai eu l'occasion
d'utiliser GitHub que ce soit pour des projets scolaires tels que
la [SAE-15](https://github.com/alexis-opolka/sae-15-data/), la [SAE-12](https://github.com/alexis-opolka/sae-12/), la [SAE-21](https://github.com/alexis-opolka/sae-21/) ou encore simplement pour [mes
cours](https://github.com/alexis-opolka/import-cours-but-rt/).  
J'ai aussi eu l'occasion d'utiliser GitHub pour des projets personnels ou pour contribuer à des projets open-source tels
que [Ren'Py](https://github.com/renpy/renpy), [Code OSS](https://github.com/microsoft/vscode/), la [documentation GitHub](https://github.com/github/docs/), etc.
