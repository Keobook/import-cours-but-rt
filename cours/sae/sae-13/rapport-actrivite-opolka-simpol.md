# Rapport d'activité - Alexis Opolka, Lucas Simpol

Information: Chaques test de certification a été effectué deux fois,
ils sont présents en annexe à la fin du rapport d'activité.

## Spécificités du cable

Cable: 7 - F/FTP Cat.6a 550 MHz 4P LSOH-FR TOURET 500m IVOIRE

Vendu par le fabriquant par 500m mais est disponible en plus petite taille.
C'est du fil de cuivre, l'isolant est polyétilène

LSOH-FR: Low Smoke "Zero" Halogen Retardateur de flamme

| Donnée                                  | Valeur                  |
|-----------------------------------------|-------------------------|
| Diamètre                                | 7,30mm                  |
| Poids/Km                                | 53 Kg/Km                |
| Tension max de pose                     | 98 Newton               |
| Application (max)                       | 10G Base-T              |
| Résistance                              | 146,4 &ohm;/Km          |
| Vitesse de propagation nominale (NVP)   | 78%                     |
| Affaiblissement de couplage             | &lt;= 70 dB             |

<hr>

## mise en garde pour l'utilisation

| &nbsp;                                | &nbsp;                                                                              |
|---------------------------------------|-------------------------------------------------------------------------------------|
| ![logo-1](./src/img/logos/logo_1.png) | avertissement : risque d'incendie, d'électrocution ou de dommage corporels.         |
| ![logo-2](./src/img/logos/logo_2.png) | avertissement : risque de dommage ou de destruction de l'équipement ou du logiciel. |
| ![logo-3](./src/img/logos/logo_3.png) | avertissement : consultez la documentation destinée a l'utilisateur.                |
| &nbsp;                                | &nbsp;                                                                              |

<div style="page-break-after: always"></div>

## Mode D'emploi

Avant de mettre en route l'appareil, vérifier dans le sac que l'ensemble est complet, cela comprend:

- <span style="color: orange">1</span> unité principale
- <span style="color: orange">1</span> unité distante
- <span style="color: orange">2</span> cordon de charge
- <span style="color: orange">2</span> adaptateurs de lien permannent (pour prise femelle)
- <span style="color: orange">2</span> adaptateurs de canau
- <span style="color: orange">1</span> cordon de référence
- <span style="color: orange">2</span> pairs d'écouteurs
- <span style="color: orange">1</span> cable USB AB / USB A
- <span style="color: orange">1</span> mode d'emploi

### utilisation

Démarer les 2 appareils en appuyant le bouton "power" puis laissez-les démarrer.

Avant de réaliser un test de certification sur la ligne, il faut définir la valeur de référence.  
Pour cela il faut brancher les appareils selon l'un des branchements de *la procédure de test*.  
Une fois fait, sur l'accueil du menu appuyez sur le bouton option puis
sur le bouton "définir valeur de référence" ensuite suivez les instrucions de l'unité principale.

<figure>
  <img src="./src/img/procedure_de_test.png" alt="Procedure de test" width="300px">
  <figcaption>La procédure de test</figcaption>
</figure>

<div style="page-break-after: always"></div>

#### mise en place des différentes informations à propos du projet

<figure>
  <img src="./src/img/dsxi/ecran-accueil.jpg" alt="Ecran-accueil" width="300px">
  <figcaption>L'écran d'accueil du DSXI</figcaption>
</figure>

#### Avant tous tests

1. vérifier que le projet n'ait pas déjà été enregistré
    1. S'il est déjà enregistré, vérifier toutes les informations
    1. S'il n'est pas déjà enregistré, appuyer sur la flèche *(flèche 1)*,  
      vous changerez de page *(voir Paramétrage du DSXI)*. <figure> <img src="./src/img/dsxi/para_projets.jpg" alt="Parametrage" width="300px"> <figcaption>Paramétrage du DSXI</figcaption></figure>
      Pour changer de projet, appuyez sur le bouton "modifier projet".  
      Vous arriverez sur la page où tous les projets enregistrés sont listés.
        1. Votre projet a déjà été enregistré: il vous suffit de le sélectionner.
        1. Votre projet n'est pas enregistré: appuyez sur le bouton "nouveau projet" puis entrez le nom de votre projet.
        1. Paramétrer le câble:
            1. Appuyer sur l'onglet désigné par la flèche 2 *(voir paramétrage du DSXI)*
            1. Une liste déroulante s'affiche avec les différents câbles possibles:
                1. Votre câble apparaît: le sélectionner
                1. Votre câble n'apparaît pas: Recherchez-le par fabriquant
1. Le paramétrage étant fini, revenir à l'accueil, pour cela appuyez sur le bouton physique **"HOME"**.
1. Vous pouvez maintenant effectuer le test.

<figure>
  <img src="./src/img/dsxi/certification-correct.jpg"
        alt="certification-correct" width="300px">
  <figcaption>certification correcte</figcaption>
</figure>

un fois sur le rapport de test donné par l'appareil *(voir figure 4)*
vous pouvez accéder à plusieurs tests effectués par le DSXI.

on fois vos test terminer vous pouvez les récupéré sur un ordinateur disposent du logiciel LinkWare, pour cela :  
branché l'appareil avec le cable USB A vers micro-USB B a votre ordinateur et ouvert le logiciel.  
Ouvrez l'onglet file, sélectionné l'onglet "import from" puis sélectionné votre appareil.  
A partir de la fenêtre qui souffre vous pouvez soit choisir quel élément vous voulé importé ou tout importé.

<div style="page-break-after: always"></div>

## Certification du cable n°7

***Se référer aux annexes 1 et 2***

![Cable-Certification](./src/dsxi-tests/img/designated-cable/pages/designated-cable-page-3.png "Certification du cable")

<hr>

## Analyse de la certification

### Les informations qui sautent aux yeux

Au dessus de l'encadré bleu on peut voir que le cable testé est OK,
on le voit grace à l'encadré vert avec la coche.
Dans l'encadré bleu on peut voir les infomation du cables et les information des l'appareil.  

### L'analyse des courbes

| Catégorie             | Image                                                                                                                                                   | Analyse        |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Wire Map              | ![test-page-img-01](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-wire-map.png "Wire Map")                | Grâce a l'image on peu vérifier si le cable est cablé corectement sur les prise femelle, on peut voir aussi il une des paire est casé car elle ne s'affichera pas.
| Insertion loss (dB)   | ![test-page-img-02](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-insetion-loss.png "Insertion loss (dB)")     | représente la perte de dB sur les différente paire. La ligne rouge représente la limite maximale de perte que l'on peut admettre. <br> La dexième ligne, n'est pas une ligne mais plusieurs, elle représente la perte de chaque paire de cable en fonction de la féquence. Sur ce test on peut voir que le test est valide car on ne dépasse pas la limite maximale fixé donc sur ce test le cable est valide.
| NEXT (dB)             | ![test-page-img-03](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-next.png "NEXT (dB)")               | Next correspond a la paradiaphonie du cable *(mesure de la perturbation d'une paire sur une autre)*. <br> Sur le graphique on peut voir différentes courbes qui représentent la perte en dB de chacune des paires, la courbe rouge représente la valeur minimale de perturbation que l'on peut admettre. <br> Pour ce test on peut voir que sur la basse fréquence il y a plus de perte qu'en haute féquence. <br> Le cable peut être certifié car on ne passe pas en dessous de la valeur de référence.
| NEXT @ Remote (dB)    | ![test-page-img-04](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-next-at-remote.png "NEXT @ Remote (dB)")      | Next correspond a la puissance cumulée de paraphonies du cable *(mesure de la perturbation d'une paire sur une autre)*. Sur le graphique on peut voir diffréntes courbes qui représentent la perte en dB de chacune des paires, la courbe rouge représente la valeur minimal de perturbation que l'on peut admettre. Pour ce test on peut voir que sur la basse fréquence il y a plus de perte qu'en haute féquence. <br> Le cable peut être certifié car on ne passe pas en dessous de la valeur de référence.
| ACR-F (dB)            | ![test-page-img-05](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-acr-f.png "ACR-F (dB)")              | ACR-F est le rapport entre l'atténuation et la diaphonie au  niveau du coté distant, selon le schéma apparant, nous avons des piques a certains moment, cela signifiant que l'on a une absorption supérieur à cette fréquence, ce qui est ce que l'on veut. <br> Vu que tout est positif, on cherche la valeur la plus haute, donc plus on a une grande valeur mieux c'est.
| ACR-F @ Remote (dB)   | ![test-page-img-06](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-acr-f-at-remote.png "ACR-F @ Remote (dB)")     | Si l'ACR-F est le rapport entre l'atténuation et la diaphonie, l'ACR-F @ Remote est le rapport entre l'atténuation et la diaphonie capturé par l'unité distante. L'on peut voir que le relevé est très proche de celui capturé par l'unité principale voir même identique. <br> Cela signifie qu'il y a aucun problème au niveau du cable sur cet instance précise, où l'on a les mêmes données en début de ligne qu'en fin de câble.
| ACR-N (dB)            | ![test-page-img-07](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-acr-n.png "ACR-N (dB)")              | l'ARC-N est le rapport entre l'atténuation et la diaphonie. sur se grafique on peut voir plusieurs courbe représentant chaqu'une des paires, la courbe rouge represente la valeur maximale de le peut admettre, le fait que la coubre soit inverersé signifié que les résultats obtenue sont négatif. sur le grafique on peut voir que le courbe sont au dessous des norme physique donc selon se test il est certifiable.
| ACR-N @ Remote (dB)   | ![test-page-img-08](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-acr-n-at-remote.png "ACR-N @ Remote (dB)")     | l'ARC-N est le rapport entre l'atténuation et la diaphonie. sur se grafique on peut voir plusieurs courbe représentant chaqu'une des paires, la courbe rouge represente la valeur maximale de le peut admettre, le fait que la coubre soit inverersé signifié que les résultats obtenue sont négatif. sur le grafique on peut voir que le courbe sont au dessous des norme physique donc selon se test il est certifiable. vue par le module distant
| RL (dB)               | ![test-page-img-09](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-rl.png "RL (dB)")                 | RL est corespond a la puissance resus par rapport a la puissance émie. le rapport et deux fois athénuation + réfléction en but de cable
| RL @ Remote (dB)      | ![test-page-img-10](./src/dsxi-tests/img/designated-cable/graphes/page-3/designated-cable-page-3-rl-at-remote.png "RL @ Remote (dB)")        | RL est corespond a la puissance resus par rapport a la puissance émie. le rapport et deux fois athénuation + réfléction en but de cable vue par le module distant

<hr>

## Autre certifications

### Liaison permanente entre le SR du 2e étage et la salle B207 de l'IUT de Béziers

***Se référer aux annexes 3 et 4***

Pour la troisième partie nous avons choisie de faire un teste sur l'un des cable qui relie l'une des salle de l'iut (B207) au switch d'étage.  
Pour cela nous avons demandé les autorisations au pôle maintenance et à Mr. Pujas pour débrancher la salle B207 et ouvrir l'armoire de brassage.  
Avec les autoriations nous avons pu procédé au test du cable (liaison permanente).  
Les résultats obtenus sont sensiblement les mêmes que pour le cable imposé.  
Grace au test nous pouvons dire que le cable installé pour relier la salle est certifiable et certifié, tout comme le cable imposé.

<div style="page-break-after: always"></div>

## Annexes

### Annexe 1 - 1er test sur le cable 7

![1st-test-designated-cable](./src/dsxi-tests/img/designated-cable/pages/designated-cable-page-3.png "1er test sur le cable 7")

<div style="page-break-after: always"></div>

### Annexe 2 - 2e test sur le cable 7

![2nd-test-designated-cable](./src/dsxi-tests/img/designated-cable/pages/designated-cable-page-4.png "2e test sur le cable 7")

<div style="page-break-after: always"></div>

### Annexe 3 - 1er test sur la liaison permanente de l'IUT (SR du 2e étage -> B207)

![1st-test-permanent-link](./src/dsxi-tests/img/permanent-link/pages/permanent-link-page-3.png "1er test sur la liaison permanente de l'IUT")

<div style="page-break-after: always"></div>

### Annexe 4 - 2e test sur la liaison permanente de l'IUT (SR du 2e étage -> B207)

![2nd-test-permanent-link](./src/dsxi-tests/img/permanent-link/pages/permanent-link-page-4.png "2e test sur la liaison permanente de l'IUT")

## Copyright Alexis Opolka, Lucas Simpol &copy; 2022 - All Rights Reserved

Ces tests on été effectué avec des DSXI, appareils de certification frabiqués par FLUKE Networks &reg;.
