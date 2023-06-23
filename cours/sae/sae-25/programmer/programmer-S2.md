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

> **Note**:  
> Augmenter la taille des sections et les lier entre elles

## Composantes essentielles

### En étant à l’écoute des besoins du client et des différents acteurs impliqués

J'ai pu et dû, de nombreuses fois, être à l'écoute des besoins
d'un client, qu'il soit interne ou externe, et de différents acteurs
impliqués dans un projet.  
Dans le cadre de la SAE-23, j'ai dû être à l'écoute des besoins
de mon binôme, qui était aussi le client interne du projet,
et des besoins requis par le cahier des charges.

J'ai donc dû adapater mon travail en fonction de ces besoins,
que ce soit au niveau de la conception, du développement ou
encore des fonctionnalités développées.  
A plusieurs reprises, j'ai dû modifier des fonctionnalités,
les étoffer ou les réduire afin qu'elles correspondent aux
besoins de mon binôme et du cahier des charges.

Plusieurs outils m'ont permis de communiquer avec eux, tels que:

- Discord
- Slack
- Services mails (Gmail / Zimbra)
- GitHub

### En utilisant une approche rigoureuse et méthodique (démarche scientifique)

Afin de pouvoir programmer, ou toute autre tâche nécessitant
de la méthodologie et une démarche scientifique, il est important
d'aborder le problème de manière rigoureuse et méthodique.

Dans le cadre de la SAE-21, j'ai dû développer un réseau
pour une entreprise, en prenant en compte les besoins
de l'entreprise, une DMZ, le réseau FAI et des sites distants.  
Afin de s'assurer de ne pas perdre le fil de la conception,
j'ai créé un schéma réseau avant de commencer le montage réseau
sur Cisco Packet Tracer.

![sae21-schema-reseau](../../sae-21/src/img/schema-reseau.drawio.svg)

Ayant déjà préparé le schéma réseau et les accès de chacuns (par Groupes),
j'ai pu commencer le montage, et par la suite, faire les tests
me permettant de valider ou non, le bon fonctionnment de mon réseau.  
Cependant, avoir une approche rigoureuse et méthodique ne suffit pas.
Dans le cas de Cisco Packet Tracer, je me suis vu confronté
à des limitions propes à l'outil, qui m'ont obligé à revoir
mon schéma réseau de manière incrémentale et itérative afin
d'obtenir un réseau fonctionnel.

### En choisissant les outils et l’environnement de développement adaptés

De part mon expérience, j'ai pu apprendre à utiliser de nombreux
outils et environnements de développement.

Dans le cadre étudiant, du BUT R&T, j'ai pu utiliser des outils
et des environnements de développement tels que [GitHub](https://github.com), [Visual Studio Code](https://code.visualstudio.com),
[Visual Studio](https://visualstudio.microsoft.com), [GitKraken](https://gitkraken.com) ou d'autres encore.

Par exemple, pour la SAE-23, vu que j'ai dû développer une application web contenant une API en TypeScript et NextJS, j'ai utilisé:

- GitHub pour stocker le code source en ligne
- GitHub Projects pour gérer les tâches à effectuer
- Visual Studio Code en tant qu'IDE
- GitKraken et Git pour contrôler les versions du code source

  > **Note**:  
  > GitKraken est une interface graphique pour Git
  > qui, d'après moi, permet dans certaines situations
  > de mieux comprendre les conflits et de les résoudre.

- Docker pour build et lancer l'application construite
- Postman pour développer et tester l'API
- ESLint pour vérifier la syntaxe du code source

Plus récemment, dans le cadre de la SAE-24 je travaillais
dans une équipeé

Dans d'autres cadres et dans d'autres projets, j'ai pu utiliser
beaucoup d'autres outils et environnements de développement
tel que [GitLab](https://gitlab.com), [BitBucket](https://bitbucket.org), [AWS](https://aws.amazon.com), [GCP](https://console.cloud.google.com), [Azure DevOps](https://dev.azure.com), etc.

Ce qui m'a permis d'apprendre les fonctionnalités de base de
ces outils et environnements de développement, mais aussi
de me sentir à l'aise avec l'idée d'être confronté à un nouvel
outil.

### En intégrant les problématiques de sécurité

La sécurité est un élément essentiel dans le développement d'une
application, qu'elle soit interne ou externe.

Dans le cadre de la SAE-23, j'ai dû développer une application web
qui permettait de gérer et de suivre les données récoltées par
les Banzaii. Il était donc important d'avoir une gestion des
comptes utilisateurs et de leurs permissions.

A cela, s'ajoute le système d'authentification qui ne doit pas
transmettre les données de l'utilisateur, notamment le mot de passe,
en clair. Et encore d'autres problématiques de sécurité liées à l'accès de l'API, à l'accès des pages, etc.

J'ai donc dû mettre en place un système d'authentification et de 
double authentification prenant en compte les problématiques de
sécurité qu'une application unipage peut avoir.  
J'ai aussi dû mettre en place une gestion des droits d'accès
et d'affichages de certains éléments de l'application.  
Qui, dans le cas de la SAE-23 et du fait que ce soit une 
application démonstrative, n'est pas complètement poussée
notamment dû au court lapse de temps donné entre le début
du projet et son rendu, ne me permettant pas, ainsi qu'à
mon binôme, d'obtenir un résultat convenable ainsi que la
prise en compte et la mise en place de solutions pour
différents problèmes qu'ils soient techniques, sécuritaires
ou autres.


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
A contrario, je vais qualifier les langages `PHP`, `JavaScript` avec `NodeJS`,
les langages de bases de données comme `MySQL`, `PostgreSQL`, `Flux (de InfluxDB)`, etc.
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

Dans le cas de la SAE-23, j'ai dû travailler avec des données au format JSON
où l'on avait des données qui étaient séparées en plusieurs fichiers et qui
devaient contenir un historique des données.

Si l'on prend par exemple les données considérées comme externes, j'avais une
structure équivalente à celle ci-dessous:

```json
{
  "id": "<ID-du-Banzaii>",
  "data": [
    {
      "type": "<Type-de-donnée>",
      "description": "<Description-des-données>",
      "timeline": [
        {
          "value": "<valeur>",
          "timestamp": "<timestamp>"
        },
        {
          "value": "<valeur>",
          "timestamp": "<timestamp>"
        }
      ]
    }
  ]
}
```

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
la [SAE-15](https://github.com/alexis-opolka/sae-15-data/), la [SAE-12](https://github.com/alexis-opolka/sae-12/), la [SAE-21](https://github.com/alexis-opolka/sae-21/), la [SAE-23](https://github.com/alexis-opolka/Mon-Banzaii/) ou encore simplement pour [mes
cours](https://github.com/alexis-opolka/import-cours-but-rt/).  
J'ai aussi eu l'occasion d'utiliser GitHub pour des projets personnels ou pour contribuer à des projets open-source tels
que [Ren'Py](https://github.com/renpy/renpy), [Code OSS](https://github.com/microsoft/vscode/), la [documentation GitHub](https://github.com/github/docs/), etc.

Vous pouvez par exemple voir ci-dessous, comment la SAE-23 a été organisée de manière collaborative en utilisant les GitHub Projects.

![sae23-github-boards](./src/sae-23-boards.png)
