# Compétence: Administrer - S1 BUT RT

## Composentes essentielles

### En communiquant avec des clients et les différents acteurs impliqués

### En choisissant les solutions et technologies adaptées

Lors de multiples occasions, j'ai eu à décider quelle technologie à utiliser, plusieurs exemples me viennent à l'esprit.  
Comme premier exemple, lors de la création du site de l'association dont je suis directeur technique, Petits Papiers d'Architecture, les contraintes étaient les suivantes:

- Avoir un site multipages car propice à plusieurs types de contenus dont:
  - Le référencement d'articles de type blog
  - Le référencement de podcasts publiés
  - Une galerie de photos prises lors de voyages et projets de l'association
- Ne pas perdre l'esthétisme d'un "site vitrine" pour l'association et ses projets
- Etre multilangue

Une contrainte supplémentaire à été d'utiliser un langage facile à apprendre et à utiliser puisque certaines publications doivent être faites par des personnes n'étant pas du milieu du dévelopement web / logiciel en injectant du code dans le code source.  
Ainsi donc, plusieurs choix ont été possibles dans la panoplie de langages et framework pensés pour le web.  

Après quelques dissertations, il a été décidé d'utiliser un stack NextJS comprenant:

- Un langage relativement explicite: JavaScript (JS) + TypeScript (TS), TS est privilegié afin d'avoir une architecture plus typée et moderne.

- Un framework: ReactJS, permet une simplicité sur l'appel d'éléments complets coupés en plus petits éléments offrant une meilleur maintenabilité sur le long terme du code source en plus de permettre une facilité à ajouter des éléments (plus ou moins complexes) par des personnes non accoutumées au milieu. NextJS, permet d'avoir une incorporation de ReactJS et TypeScript dans un site multipage.

- Un milieu de collaboration: GitHub. Un environnement de collaboration gratuit où les fonctionnalités les plus basiques sont présentes et faciles à reconnaitre. Des GitHub Actions, ont été mises en place afin de permettre la compilation du code source et l'envoi aux serveurs qui hébergent le nom de domaine et la version de production.

- Des gestionnaires:
  - **Git**, logiciel de contrôle des versions, permet de contrôler les ajouts à la base de code source, revenir sur des versions antérieurs en cas de cassage d'une version, décentraliser le travail effectué dans plusieurs branches spécifiques.
    - *development* pour le code source de développement (nightly version),
    - *main* pour le code mis en production, mis à jour seulement avec des versions stables.
  - **Yarn**, gestionnaire de paquets spécifiques au dépot en concordence avec le fichier "package.json" et la gestion de leur versions, il est aussi utiliser pour lancer des scripts spécifiques au code source tel que:
    - La compilation du code source afin d'être envoyé en production (yarn build),
    - Le démarrage de l'environnement de développement (yarn dev / start).

### En respectant les principes fondamentaux de la sécurité informatique

Suivant l'exemple donné ci-dessus

### En utilisant une approche rigoureuse et méthodique (démarche scientifique)

### En assurant une veille technologique

## Les aprentissages critiques

### Comprendre l'architecture et les fondements des systèmes numériques, les principes du codage de l'information et de l'internet

### Configurer les fonctions de base du réseau et des systèmes usuels

### Maîtriser les rôles et les principes fondamentaux des systèmes d'exploitation

### Identifier les dysfonctionnements du réseau local et des réseaux de campus

### Installer un système d'exploitation, linux et windows, par différents moyens

### Installer un poste de bureautique en réseau
