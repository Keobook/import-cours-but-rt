---
Author:
  Alexis O.
  Mathys D.
  Thibault Garcia
Company: IUT de Béziers
Subject: R402-TP - OFDM
Copyright: All Rights Reserved
---

# R402 - TP1 - OFDM

## Préparation

1. Expliquer le principe de l’OFDM pour un signal numérique de débit 3 kbits/s utilisant 3 porteuses.  
    On fera un schéma explicatif en s’appuyant sur le signal numérique 0 1 1 1 0 1 0 0 1 0 0 1 1

    OFDM est principe où l'on transmet simultanément plusieurs symboles
    en parallèle sur différentes porteuses

    ![schema-preparation](./src/tp1/schema-preparation.jpg)

1. Quel est alors le débit de chaque porteuse ?

    $$
        D_p = \frac{3 \times 10^{3}}{3} = 1 \text{ kbit/s}
    $$

1. Quel espace entre porteuses faut-il choisir si on utilise des modulations de valence 2 ? Pourquoi ?

    $$
        R = \frac{D_p}{n} \\
        R = \frac{1 \times 10^3}{1} \\
        R = 1 \text{ kBd}
    $$

## Manipulation, partie émetteur

- Générer grâce à la carte **Audio Oscillator** une horloge de fréquence 1 kHz.  
    Cette carte commande deux cartes **Sequence Generator** qui délivrent trois signaux numériques à 1 kbits/s

    | &nbsp;          | &nbsp; |
    | --------------- | ------ |
    | X rouge-carte 1 | Num1   |
    | Y rouge         | Num 2  |
    | X rouge-carte 2 | Num 3  |

    Dans la pratique, comme vous l’avez montré précédemment, ces trois signaux numériques proviennent
    d'un seul et même signal utile de débit 3 kbits/s

- Visualiser le signal numérique Num1 (sortie X rouge) en fonction du temps ; quel est le code utilisé ?  
    Mesurer la durée de l’ITE.  
    Que vaut la rapidité de modulation ?

    ![signal-num1](./src//tp1/signal-num1.jpg)

    Le code **NRZ Unipolaire** est utilisé, nous avons un $ITE = 1 \text{ ms}$ et nous avons une rapidité de modulation de
    $\frac{1}{ITE} = 1$ kBd.

- Visualiser le spectre du signal numérique; en particulier mesurer son occupation spectrale (premier lobe).

    Le spectre du signal numérique est:

    ![spectre-num1](./src//tp1/spectre-num1.jpg)

    Son occupation spectrale, notamment au niveau de son premier lobe
    est de $1$ kHz.

- Grâce à un filtre **LPF**, éliminer les lobes secondaires.  
  Pourquoi est-il raisonnable de couper les lobes secondaires ?  
  Observer alors le signal numérique en sortie du filtre. Que peut-on dire ?

    Il est raisonnable de couper les lobes secondaires car cela nous permet ainsi de ne pas empiéter sur les fréquences voisines.

    ![signal-num1-filtre-lpf](./src/tp1/signal-num1-filtre-lpf.jpg)

  > [!NOTE]
  > Faire vérifier par l'enseignant

  > [!CAUTION]
  > Pour simplifier le montage final, on supprimera dorénavant le filtre LPF.

- Générer, grâce à 1 autre carte  **Audio Oscillator**  et un GBF,  deux signaux sinusoïdaux de fréquence respective 2 kHz et 3 kHz (soyez extrêmement précis dans les réglages) et d'amplitude 2 V.

  > [!NOTE]
  > Faire vérifier vos premiers réglages par l'enseignant.

- Moduler le premier signal numérique Num1 avec la porteuse de fréquence 1kHz (première carte **Audio Oscillator**). Observer le spectre de ce signal.

    ![spectre-num1-module](./src/tp1/spectre-num1-module.jpg)

    On voit que l'étalement spectrale a diminué car nous venons de multiplier le signal numérique 1 avec
    une porteuse à la même fréquence que le signal.

- Moduler le deuxième signal numérique Num2 avec la porteuse de fréquence 2 kHz et le troisième signal numérique Num3 avec la porteuse de fréquence 3 kHz

    - Num2

      ![spectre-num2-module](./src/tp1/spectre-num2-module.jpg)

    - Num3

      ![spectre-num3-module](./src//tp1//spectre-num3-module.jpg)

- Observer les spectres de ces signaux modulés

    - Num2

      On peut observer que le signal s'est bien déplacé à la fréquence de sa porteuse, $2$ kHz.

    - Num3

      On peut observer à nouveau que le signal s'est bien déplacé à la fréquence de sa porteuse, $3$ kHz.

- Représenter les spectres de ces trois signaux modulés sur un même graphe (trois couleurs différentes).  
    Que remarque-t-on ? Expliquer le choix des valeurs de fréquence des différentes porteuses ?

    ![spectre-num-1-2-3-module](./src/tp1/spectre-num123-module.png)

    où

    | couleur                                    | Spectre de signal  |
    | ------------------------------------------ | ------------------ |
    | <span style="color:orangered">rouge</span> | signal numérique 1 |
    | <span style="color:green">vert</span>      | signal numérique 2 |
    | <span style="color:magenta">rose</span>    | signal numérique 3 |

    > [!NOTE]
    > Faire vérifier vos résultats par l'enseignant.

- Grâce à deux cartes  **Adder** (gain unitaire), ajouter ces trois signaux.  
    Observer et relever le spectre du signal OFDM.  
    Quelle est son occupation spectrale ? Conclure

    ![spectre-signal-additionne](./src/tp1/spectre-signal-additionne.jpg)

    Son occupation spectrale est de $4$ kHz, on peut donc en conclure
    que l'OFDM nous permet d'obtenir une occupation spectrale qui combine l'entièreté
    des OS des différentes porteuses, elle est donc plus étendue.

    > [!NOTE]
    > Faire vérifier vos résultats par l'enseignant.

## Manipulation, partie récepteur

- En réception, que doit-on faire pour régénérer les signaux numériques ?  
    On représentera les différentes étapes sur un schéma-bloc en précisant, pour chaque filtre, les valeurs de leur bande passante.

    ```mermaid
    %%{init: {"flowchart": {"htmlLabels": false}} }%%
    flowchart LR

    st("Signal émis") --> filtre("Filtre Passe Bas à 2 * fréquence porteuse (2khz)") --> mult("Multiplication avec la porteuse") ---> so("Signal originel")
    ```

On souhaite retrouver le signal numérique Num1 (porté par la porteuse à 1 kHz).

- Filtrer le signal OFDM avec la carte  **Tuneable LPF**  pour ne récupérer que la bande de fréquences correspondant au signal 1.  
    On précisera les limites de cette bande de fréquences.  
    Ensuite, multiplier le signal filtré avec la porteuse à 1 kHz.

    - Retrouve-t-on le signal numérique ?

        Non

    - Quelle est l'autre étape nécessaire ?

        Nous devons ajouter un filtre passe bas, à nouveau, avec une fréquence de coupure à 1 kHz.

- Réaliser le filtrage.

    ![spectre-num1-demodule](./src/tp1/spectre-num1-demodule.jpg)

    > [!NOTE]
    > Faire vérifier vos résultats par l'enseignant.

- Pour obtenir un signal « propre » on utilisera la carte **Comparator**.  
    Cette carte régénère le signal filtré en le comparant à une tension constante de référence **DC**.

- Régler la valeur de la tension constante à appliquer à l’entrée de la carte **Comparator**.  
    Il s’agit de la valeur du Seuil de décision du signal reçu.

- Retrouver le signal régénéré

    ![spectre-signal-regenere](./src/tp1/spectre-signal-regenere.jpg)

- Afficher sur l’oscilloscope également le signal Num1 initial et vérifier qu’il a bien été régénéré sans erreur.

    ![signal-regenere-initial.jpg](./src/tp1/signal-regenere-initial.jpg)

    > [!NOTE]
    > On peut constater un léger retard sur le signal régénéré car il passe physiquement
    > par plusieurs filtres sur la baie Tims.

    > [!NOTE]
    > Faire vérifier vos résultats par l'enseignant.

## Logiciel WinIQSim

On utilise le logiciel WINIQSIM étudié au semestre précédent.  
Lancer WINIQSIM et sélectionner dans « system » la configuration « multicarrier ».

Choisir dans l'émetteur :

  - Data Source : PRBS 15
  - une modulation 64-QAM (elle sera effective pour chaque porteuse) ;
  - un débit des symboles (symbol rate) de 2 MHz (pour chaque porteuse) ;
  - un filtre de Gauss (B.T = 0,5) ;
  - un nombre de symboles = 10 000.

Pour le récepteur, choisir de recevoir 1 porteuse.

- Relever le spectre du signal ; donner son occupation spectrale et son amplitude.  
    Attention, l'échelle horizontale (en fréquence) utilise comme variable la fréquence normalisée (f-fP)/R.  
    De plus, ce logiciel est bien plus précis qu'un oscilloscope ; on limitera l'occupation spectrale à -30 dB par rapport à la valeur maximale

    ![winiqsim-](./src/tp1/winiqsim-1porteuse.png)

    - Son occupation spectrale: 2R
    - Son amplitude: 30 dB

Pour le récepteur, choisr maintenant de recevoir 6 porteuses (State ON, Mod ON, Data PRSB).

- Si on veut respecter le critère de Nyquist, quel doit être l'espacement entre les porteuses ?

    On doit avoir un espacement de $2R$ entre les porteuses.

- Régler l'espace entre porteuses de manière à respecter le critère de Nyquist
- Visualiser le spectre d'amplitude, vérifier qu'il y a bien étalement de spectre et mesurer la largeur de bande obtenue.
    Relever également son amplitude et conclure.

    ![winiqsim-6porteuse](./src/tp1/winiqsim-6porteuses.png)

    Il y a bien étalement de spectre, la largeur de bande obtenue est de $-3$ à $3$ R, ce qui nous donne $6$ MHz de largeur de bande.  
    Nous avons toujours une amplitude de 30 dB.

    On peut donc conclure que lorsque l'on ajoute des porteuses, notre amplitude reste la même à contrario
    de la largeur de bande qui, elle, est modifiée.

- Visualiser la constellation. Que constate-t-on ?

    ![winiqsim-constellation](./src/tp1/winiqsim-constellation.jpg)

    On peut constater que la constellation est "parfaite".

- Modifier l'espace entre porteuses pour le prendre égal à $1.3 \times débit$ des symboles puis $2 \times débit$ des symboles.  
    Visualiser dans les deux cas le spectre et la constellation.  
    Que constate-t-on ? Conclure

    - $1.3 \times débit$

        - Spectre:

            ![winiqsim-1.3-spectre](./src/tp1/winiqsim-1.3-spectre.png)

        - Constellation

            ![winiqsim-1.3-constellation](./src/tp1/winiqsim-1.3-constellation.png)

    - $2 \times débit$

        - Spectre:

            ![winiqsim-2-spectre](./src/tp1/winiqsim-2-spectre.png)

        - Constellation

            ![winiqsim-2-constellation](./src/tp1/winiqsim-2-constellation.png)

    On peut constater que l'on a une occupation spectrale plus grande ($8 MHz$), de $4$ à $4$ R.
