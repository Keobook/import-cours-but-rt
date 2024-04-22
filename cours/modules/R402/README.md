# R402 - Transmissions Numériques avancées

## TD 1

- Faux
- Vrai tant que $\frac{f}{2} > f_max$
- $n f_e$: Pas forcément
- Valence: Vrai (3 bits par symbole => 8 de valence ($\exp2$))
- Rapidité de modulation: $D = nR$ où D = bits/s et R = symbole/s => Faux
- IES: Vrai (Interférences Entre Symboles)
- Largeur de bande du canal impose le choix de la rapidité de modulation: Vrai
- Prob. d'erreur augmente avec la valence: Vrai
- \+ de bruit, + $R_{\frac{S}{B}}$ est grand: Faux
- Le canal 1, dont le $R_{\frac{S}{B}}$ vaut 30 dB, a une capacité plus grande que le canal 2 dont le $R_{\frac{S}{B}}$ vaut 35 dB: Faux
- Capacité d'un canal est proportionnelle à la bande passante du canal: Vrai
- Modulation est obligatoire: Faux
- 3 type de modulation numérique: Fréquence, Amplitude et Phase => Vrai
- Sur une constellation, on peut lire de modulation utilisée: Vrai
- Démodulation synchrone, multiplier le signal par la fréquence de la porteuse: Vrai

Multiplexage:

- Multiplexage temporel
- Multiplexage fréquentiel

$u_1(t) = A \sin(\omega t + cf)$  
$u(t) = A (\sin(\omega t) + \sin(\omega t + cf))$

### Exercice 1

1. Exprimer la puissance en dB et dBm d'un émetteur de 2 W.

    $P = 2 \text{ W} = 2000 \text{ mW}$  
    $P_{(db)} = 10 \log2 = 3 \text{ dB}$  
    $P_{(dBm)} = 10 \log2000$  
    $= 33 dBm$

1. $P_r(d) = P_e G_e G_r (\frac{\lambda}{4 \pi d})^2$

    $\lambda = \frac{C}{f} = \frac{3.10^8}{900.10^6}$  
    $= 0.33$ m

    Pour

    $P_r = P_e G_e G_r (\frac{\lambda}{4 \pi d})^2$  
    $= 2 (\frac{0.33}{4 \pi \times 500})^2$
    $=5.52 mW$

1. Distance émetteur-récepteur

    - Multipliée par 2

      Si $d \text{ est } \times 2$ => $\frac{P_r}{4}$

    - Multipliée par 10

      Si $d \text{ est } \times 10$ => $\frac{P_r}{100}$

1. Expliquer expression "on perd 20 dB par décade"

    ...

1. GSM

    ...

## TD 2 - OFDM

### Préparation

  - 16 QAM =>
    - V = 16
    - n = 4
  - 3 porteuses

    On aura donc une coupure tous les $n$ (donc tous les 4 bits)
    où l'on aura une alterance de 3 porteuses différentes:

    | 1 n | 2 n | 3 n | 4 n |
    | --- | --- | --- | --- |
    | f1  | f2  | f3  | f1  |

    Avec $\varDelta f = R$

  - Un débit de 10 Mbits/s

    - Sans OFDM, $t_{bit} = 0.1 \mu s$
    - Avec OFDM, $t_{bit} = 0.3 \mu s$  
      $ITE = 1.2 \mu s$

  - Rapidité de modulation ($R$) de $200 \text{MBd}$

    $\varDelta t = \frac{2}{3.10^8} = 0,67 . 10^{-8} = 6.7 \text{ns}$  
    $ITE = \frac{1}{R} = \frac{1}{200 . 10^6} = 0,5 . 10^{-8} = 5 ns$

    Il y aura une interférence entre symboles puisque R recevra le symbole
    2 en même temps que le symbole 1 après réfléxion de E.

    On allonge donc l'ITE avec OFDM afin de s'assurer que le symbole 2
    arrivera après le symbole 1 après réfléxion.

    > [!NOTE]
    > C'est une peu la technique du "Il Vaut mieux devenir une tortue
    > que de s'efforcer d'entrainer l'autre à devenir un lièvre."

  - Méthode de transmission utilisée en ADSL et le procédé OFDM

    Avec l'OFDM on utilise des porteuses orthogonales, elles
    peuvent donc se chevaucher, on peut en mettre plus sur une
    une même bande passante.

    Avec l'OFDM tous les canaux ont la même valance, contrairement
    à l'ADSL.

### Exercice 1

  1. Dans quels cas est-il intéréssant de l'utiliser (OFDM) ?

      Dans la communication aérienne (dans l'air)

  1. OFDM.durée-symbole = $224 \mu s$:

      1. espacement entre porteuse

        $\varDelta f = R = \frac{1}{224 . 10^{-6}} = 4464$ Hz

      1. Ecart entre les deux porteuses extrêmes

        $\varDelta f_{total} = 1702 \times 4464 = 7.6$ MHz

  1. Intervalle de garde. Pourquoi ? Durée maximale ?

      - Pourquoi Intervalle de garde: Pour complètement supprimer les IES entre chemins.

          $IG \leq \frac{1}{4} ITE$

      - Durée maximale

        $D_{1p} = \frac{q}{ITE \times IG}$  
        $D = N_p \frac{q}{ITE \times IG}$

        Si l'on veut augmenter le débit, il faudra augmenter le nombre de porteuses.

  1. Intérêt d'augmenter la durée du symbole OFDM ?

      Empêcher la perturbation entre symboles (symbole 2 reçu avant réflexion symbole 1)

  1. Si chaque symbole possède q bits, quel est le débit pour chaque porteuse ? le débit local ?

Dans le mode 8K, on utilise le procédé OFDM avec 6817 porteuses espacées de 1116 HZ ($= R$).

Intérêt + porteuses, ITE plus grand, intervalle + petit, porteuses + proches, + précision nécessaire

1. Rappeler le débit d'un canal de télévision après les CCE

    $D = 39 \text{MBits/s}$

1. Ce flux de données est partagé en 6408 flux (transmis avec 6048 porteuses)
    1. Débit de chaque porteuse ?

        $D_{1p} = 6448 \text{ bits/s} = \frac{39 . 10^6}{6048}$

    1. A quoi peuvent servir les porteuses "manquante" ?

        Elles vont servir comme bandes de fréquence de garde.
        Elles peuvent aussi être utilisée pour des informations
        annexes sans perturber les bandes de fréquence principales.

    1. Largeur spectrale d'une porteuse ?

        $OS_{1p} = 2 \times 1116 = 2232$ Hz

    1. Rapidité de modulation maximale pour chaque porteuse ?

        $R = 1116$ Bd

    1. Comparer au débit: conclure et proposer une modulation possible

        $D = nR \rArr n = \frac{D}{R} = \frac{6448}{1116} \rArr n = 6$

        > [!NOTE]
        > On ne trouve pas un entier, on est donc obligé d'arrondir à 6.

    1. Donner alors la rapidité de modulation réelle pour chaque et la durée réelle d'un symbole

        $R_{réelle} = \frac{D}{6} = \frac{6448}{6}$  
        $= 1074$ Bd

        $\lrArr T_s = 931 \mu s$

        $T_u = \frac{1}{R} = \frac{1}{1116} = 896 \mu s$

        $IG = 931 - 896 = 35 \mu s$

        > [!NOTE]
        > R Correspond à $T_u$ la durée utile d'un symbole.

1. Calculer la durée utile d'un symbole OFDM. En déduire alors la durée de l'intervalle de garde.
  A quelle distance cela correspond-il ?

### Exercice 2

1. Qu'est-ce qu'un symbole OFDM ?
2. De quoi est composée une trame OFDM ?
3. Représenter une Trame OFDM en faisant apparaître les paramètre $IG$, $Tu$ et $Ts$.

    | $T_s$ | $T_s$ |
    | ----- | ----- |
    | $T_u$ | $IG$  |

4. s

5. Pour éviter l'interférence entre symboles, on augmente l'IG.
6. Mode 2K, IG de 1/16:

    - $T_u$: $224 \mu s$
    - $IG$: $14 \mu s$
    - $T_s$: $238 \mu s$

7. $BP = 8 \text{ MHz}$

    $R = \frac{1}{224 . 10^{-6}} = 4464 \text{ Bd}$

    $N_p = \frac{8 .10^6}{4464} = 1792 porteuses$

8. 16-QAM, débit Maximal ?

    $D_{1p} = \frac{4}{238 . 10^{-6}} = 16.8 \text{ kbits/s}$  
    $D_g = 1792 \times 16.8 . 10^3$
    $= 30.1 \text{Mbits/s}$  

9. Le débit réel maximum

    $28.6 \text{ Mbits/s} = D_{Réel} = 1705 \times 16,8 . 10^3$

10. Déterminer le débit utile de la transmission

    $D_u = \frac{3}{4} (1705 - 17) \times 16,8 . 10^3$  
    $= 21.3 \text{ Mbits/s}$

### Exercice 3

Mode 8k  
$IG = 56 \mu s$  
$T_u = 896 \mu s$

1. $D = 30 \times 600 \times 800 \times 8 = 115.2 \text{Mbits/s}$

2. $R = \frac{1}{T_u} = \frac{1}{896.10^{-6}} = 1116 \text{ Bd}$  
    $OS_{1p} = 2R = 2 \times 1116 = 2232 \text{ Hz}$  
    $N_p = \frac{8.10^6}{1116} = 7168 \text{ porteuses}$

3. $D_{1p} = \frac{115 . 10^6}{6817}$  
    $16.9 \text{ kbits/s}$

    $D = nR \rArr n = \frac{D}{R} = \frac{16,9 . 10^3}{1116}$  
    $\rArr n = 16$

4. La modulation utilisée est une 64-QAM. Déterminer le taux de compression nécessaire du flux vidéo.

    $T_x = \frac{16}{6} = 2.67$

    $D = \frac{6}{T_u \times IG}$

### Exercice 4

$D = 2 \text{ Mbits/s}$

1. On utilise 128 porteuses. Débit de chaque porteuse ?

    $D_{1p} = \frac{2 . 10^6}{128} = 15625 \text{ kbits/s}$  
    $R = \frac{D}{n} = \frac{15625}{4} = 3.9 \text{ kBd}$

    $OS = [500 \text{ kHz}; 500 . 10^3 + 128 \times 3,9 .10^3]$  
    $= [500 \text{ kHz}; 1 \text{ MHz}]$

## TD 3 - CDMA

### Exercice 1

Débit $D = 0.1 Mbits/s$, on utilise le code `0011010110`

1. Voir le cours pour CDMA
1. Suite envoyée ?

    - Pour un 1:

        On utilise le code comme tel (0011010110)

    - Pour un 0:

        On utilise l'inverse (1100101001)

1. ...
1. ...
1. ...

1. Que devient la bande de fréquence utilisée ?

    Elle est étalée de 10

### Exercice 2

1. On propose la méthode CDMA
1. ($I_1 + C_1$) + ($I_2 + C_2$)

### Exercice 3

Montrer que les codes $C_1$ et $C_2$ sont orthogonaux.

- $C_1$: `+1+1-1-1+1+1-1-1`
- $C_2$ `+1+1+1+1-1-1-1`

> [!NOTE]
> Pour qu'ils soient orthogonaux, il nous faut avoir un résultat égal à 0.

### Exercice 4

1. Quel est le débit en chips/s du signal après étalement ?

    $D = 256 \times 30 000$  
    $= 7680 kchips/s$

2. Quelle est alors la durée d'un chip ?

    $$
        V = 4, n=2 \\
        R = \frac{D}{2} = 3840 . 10^3 symbole / s
    $$

3. La modulation utilisée est une modulation Q-PSK.
    Quelle est la rapidité de modulation du signal modulé ? Comment obtient-on un tle signal ?
    Représenter le synoptique par un schéma-bloc.
4. Représenter les spectres des signaux:
   - $e(t)$ signal numérique initial;
   - $s_e(t)$ signal étalé;
   - $s_m(t)$ signal modulé;
