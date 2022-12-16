# Rapport d'activité - Alexis Opolka, Lucas Simpol

Information: Chaques test certification a été effectuée deux fois,
elles sont présentes en annexe à la fin du rapport d'activité.

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

<hr>

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

démarer les 2 aparreil en appuis le bouton "power" puis laisser-les démarré.

avant de réalisé un test de ligne il faut mettre le valeur de référence.
Pour cela il faut branché les apareil celon l'un des branchement de la figure 1.
Une fois fait, sur l'accueil du menus appuisé sur le bouton option puis sur apuis
sur le bouton "définir valeur de référence" ensuite suivé les instrucion le l'unité principale.

![procedure_de_test](./src/procedure_de_test.png)

mise en place des diférente information a propo du projet

<figure>
  <img src="./src/img/dsxi/ecran-accueil.jpg"
        alt="Ecran-accueil" width="300px">
  <figcaption>L'écran d'accueil du DSXI</figcaption>
</figure>

Avant tout changement, vérifié que le projet n'ai pas déja enregisté,
si il est déjà enregisté vérifié toute les information,
si il n'est pas enregisté *(fleche 1)* appuié le la fleche,
vous changerait de page (*image 3*),
pour changé de projet appuié sur le bouton "modifier projet",
vous changerai a nous de page, parcouré la liste,
si votre projet a déjà enregistré il vous suffit de le sélectionné,
si n'est pas enregistré, appuié sur le bouton "nouveau projet".  

<figure>
  <img src="./src/img/dsxi/para_projets.jpg"
        alt="Parametrage" width="300px">
  <figcaption>Paramétrage du DSXI</figcaption>
</figure>

La flèche 2 corespond a la configuration du cable

<figure>
  <img src="./src/img/dsxi/certification-correct.jpg"
        alt="certification-correct" width="300px">
  <figcaption>certification correcte</figcaption>
</figure>

un fois sur le rapport de test donné par l'appareil *(voir figure 4)*
vous pouvez accéder à plusieurs tests effectués par le DSXI.

on fois vos test terminer vous pouvez les récupéré sur un ordinateur
disposent du logiciel LinkWare, pour cela :  
branché l'appareil avec le cable USB A  vers micro-USB B a votre ordinateur
et ouvert le logiciel.  
Ouvrez l'onglet file, sélectionné l'onglé "import from" puis sélectionné votre appareil.  
A partir de la fenêtre qui souffre vous pouvez soit choisir quelle
élément vous voulé importé ou tout importé.

## Certification du cable

![Cable-Certification](./src/dsxi-tests/img/designated-cable/Rapport-de-test-SIMPOL_OPOLKA_Page_3.png "Certification du cable")

<hr>

## Analyse de la certification

### Les informations qui sautent aux yeux

Au dessus de l'encadré bleu on peut voir que le cable testé est OK,
on le voit grace à l'encadré vert avec la coche.
Dans l'encadré bleu on peut voir les infomation du cables et les information des l'appareil.  

### L'analyse des courbes

| Catégorie             | Image                                                                                                                                                   | Analyse        |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Wire Map              | ![test-page-img-01](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0003.png "Wire Map")                | Grâce a l'image on peu vérifier si le cable est cablé corectement sur les prise femelle, on peut voir aussi il une des paire est casé car elle ne s'affichera pas.
| Insertion loss (dB)   | ![test-page-img-02](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0004.png "Insertion loss (dB)")     | représente la perte de dB sur les différente paire. La ligne rouge représente la limite maximale de perte que l'on peut admettre. <br> La dexième ligne, n'est pas une ligne mais plusieurs, elle représente la perte de chaque paire de cable en fonction de la féquence. Sur ce test on peut voir que le test est valide car on ne dépasse pas la limite maximale fixé donc sur ce test le cable est valide.
| NEXT (dB)             | ![test-page-img-03](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0005.png "NEXT (dB)")               | Next correspond a la paradiaphonie du cable *(mesure de la perturbation d'une paire sur une autre)*. <br> Sur le graphique on peut voir différentes courbes qui représentent la perte en dB de chacune des paires, la courbe rouge représente la valeur minimale de perturbation que l'on peut admettre. <br> Pour ce test on peut voir que sur la basse fréquence il y a plus de perte qu'en haute féquence. <br> Le cable peut être certifié car on ne passe pas en dessous de la valeur de référence.
| NEXT @ Remote (dB)    | ![test-page-img-04](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0006.png "NEXT @ Remote (dB)")      | Next correspond a la puissance cumulée de paraphonies du cable *(mesure de la perturbation d'une paire sur une autre)*. Sur le graphique on peut voir diffréntes courbes qui représentent la perte en dB de chacune des paires, la courbe rouge représente la valeur minimal de perturbation que l'on peut admettre. Pour ce test on peut voir que sur la basse fréquence il y a plus de perte qu'en haute féquence. <br> Le cable peut être certifié car on ne passe pas en dessous de la valeur de référence.
| ACR-F (dB)            | ![test-page-img-05](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0007.png "ACR-F (dB)")              | ACR-F est le rapport entre l'atténuation et la diaphonie au  niveau du coté distant, selon le schéma apparant, nous avons des piques a certains moment, cela signifiant que l'on a une absorption supérieur à cette fréquence, ce qui est ce que l'on veut. <br> Vu que tout est positif, on cherche la valeur la plus haute, donc plus on a une grande valeur mieux c'est.
| ACR-F @ Remote (dB)   | ![test-page-img-06](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0008.png "ACR-F @ Remote (dB)")     | Si l'ACR-F est le rapport entre l'atténuation et la diaphonie, l'ACR-F @ Remote est le rapport entre l'atténuation et la diaphonie capturé par l'unité distante. L'on peut voir que le relevé est très proche de celui capturé par l'unité principale voir même identique. <br> Cela signifie qu'il y a aucun problème au niveau du cable sur cet instance précise, où l'on a les mêmes données en début de ligne qu'en fin de câble. 
| ACR-N (dB)            | ![test-page-img-07](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0009.png "ACR-N (dB)")              | l'ARC-N est le rapport entre l'atténuation et la diaphonie. sur se grafique on peut voir plusieurs courbe représentant chaqu'une des paires, la courbe rouge represente la valeur maximale de le peut admettre, le fait que la coubre soit inverersé signifié que les résultats obtenue sont négatif. sur le grafique on peut voir que le courbe sont au dessous des norme physique donc selon se test il est certifiable.
| ACR-N @ Remote (dB)   | ![test-page-img-08](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0010.png "ACR-N @ Remote (dB)")     | l'ARC-N est le rapport entre l'atténuation et la diaphonie. sur se grafique on peut voir plusieurs courbe représentant chaqu'une des paires, la courbe rouge represente la valeur maximale de le peut admettre, le fait que la coubre soit inverersé signifié que les résultats obtenue sont négatif. sur le grafique on peut voir que le courbe sont au dessous des norme physique donc selon se test il est certifiable. vue par le module distant
| RL (dB)               | ![test-page-img-09](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0011.png "RL (dB)")                 | RL est corespond a la puissance resus par rapport a la puissance émie. le rapport et deux fois athénuation + réfléction en but de cable
| RL @ Remote (dB)      | ![test-page-img-10](./src/dsxi-tests/img/designated-cable/graphes/page-3/Rapport-de-test-SIMPOL_OPOLKA_Page_3_Image_0012.png "RL @ Remote (dB)")        | RL est corespond a la puissance resus par rapport a la puissance émie. le rapport et deux fois athénuation + réfléction en but de cable vue par le module distant

<hr>

## Autre certifications

### Liaison permanente entre le SR du 2e étage et la salle B207 de l'IUT de Béziers

Pour la troisième partie nous avons choisie de faire un teste sur l'un des cable de qui relie l'une des salle de l'iut au switch d'étage. 
Pour cela nous avons demendé les autorisation au pole maintenance pour débranché la salle B207. 
Avec les autoristaion nous avons pus prosédé au test du cable. 
Les résultat obtenue sont sensiblement les mêmes que pour le cable imposé. 
Grace au test nous pourvons dire que le cable installé pour relié la salle est certifier 

<hr>

## Annexes

### 1er test sur le cable 7

![1st-test-designated-cable](./src/dsxi-tests/img/designated-cable/pages/Rapport-de-test-SIMPOL_OPOLKA_Page_3.png "1er test sur le cable 7")

### 2e test sur le cable 7

![2nd-test-designated-cable](./src/dsxi-tests/img/designated-cable/pages/Rapport-de-test-SIMPOL_OPOLKA_Page_4.png "2e test sur le cable 7")

### 1er test sur la liaison permanente de l'IUT (SR du 2e étage -> B207)

![1st-test-permanent-link](./src/dsxi-tests/img/permanent-link/pages/Rapport-de-test-SIMPOL_OPOLKA_cable_iut_Page_3.png "1er test sur la liaison permanente de l'IUT")

### 2e test sur la liaison permanente de l'IUT (SR du 2e étage -> B207)

![2nd-test-permanent-link](./src/dsxi-tests/img/permanent-link/pages/Rapport-de-test-SIMPOL_OPOLKA_cable_iut_Page_4.png "2e test sur la liaison permanente de l'IUT")

## Copyright Alexis Opolka, Lucas Simol &copy; 2022 - All Rights Reserved
