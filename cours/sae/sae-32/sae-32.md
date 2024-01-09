# SAE-32 - Développer une application communicante

## Descriptif générique

Partant de l’analyse d’un cahier des charges fourni, le professionnel R&T développe une application communicante permettant l’échange et la sauvegarde de données.  
La réalisation de ce projet contient les étapes suivantes :

- Analyser le cahier des charges fourni et répondre à celui-ci en mentionnant les technologies à utiliser et éventuellement leur impact environnemental et économique ;
- Développer une application client/serveur ;
- Authentifier les utilisateurs ;
- Sauvegarder les données échangées ;
- Concevoir une interface graphique, une application mobile ou une interface Web.

## A propos

Le contenu déposé sur le rendu Moodle n'est pas la version finale du projet, du à des problèmes de dernière minute.
C'est tout du moins la version la plus avancée qui se trouve être stable.

Vous pouvez trouver la version finale ainsi que sa fiche d'installation et de tests dans vos mails avec comme objet: `[SAE-32 ALEXIS OPOLKA + MATHYS DOMERGUE] - Version Finale (Livre Mon Colis + Livre Mon Colis Backend)` et téléchargeable via la page de releases du dépôt GitHub [@alexis-opolka/livre-mon-colis/](https://github.com/alexis-opolka/livre-mon-colis/releases) ayant comme titre `Release: [SAE-32] FINAL RELEASE` et comme tag `2.0.0`.

> **Note:**  
> Cette note de `A propos` n'est pas présente afin de me dédouaner du retard de la version finale déposée mais a pour but de vous informer afin qu'aucun malentendu ne soit créé.
>
> Je comprends et j'assume le fait que le vrai dépôt sera en retard et j'accepterai toute pénalité liée à ce fait.  
> Je tiens seulement, en ma qualité d'étudiant, à fournir un travail à la hauteur de mes capacités et des attentes.

## Installation

### Prérequis

Pour pouvoir installer correctement l'application, vous devez avoir d'installé:

- NodeJS
- Python
- Docker
- Git

Vous pouvez ensuite lancer le script [./install.sh](./install.sh)

## Commentaire

### Répartition des tâches

| Alexis                             | Mathys                              |
| ---------------------------------- | ----------------------------------- |
| Serveur Python + Fin Client NextJS | Début Client NextJS + Client Python |

### Fonctionnalités non implémentées

En ce qui concerne les fonctionnalités non implémentées, il y a principalement, de manière non-exhaustive:

- le chiffrement TLS
- le chiffrement du mot de passe (ou autres données sensibles) lors des transactions client/serveur
- Une résilience accrue coté serveur au niveau de la gestion  de la BDD et du SGBD.
- Un script d'installation en bonne et due forme

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
