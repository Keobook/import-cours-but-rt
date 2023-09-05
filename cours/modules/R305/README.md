# R305 - Chaînes de transmissions numériques

Pourquoi numérique ?

- C'est + simple de le stocker
- C'est + facile de transmettre car le récepteur sait ce qu'il doit recevoir (0 ou 1),
  il pourra donc régénerer un signal "parfait" même en recevant un signal bruité.

```mermaid

Données numériques

```

##

Dépend du canal de transmission:

- filaire
  Signal est électrique, la bande passante du canal est de la forme [0, $f_{max}$]
- hertzien
  
- Optique

Transmission en bande de base => sans modulation

### Notions élémentaires

Un bit est représenté par une tension, cette tension est maintenue pendant un certain temps.

- ITE: Intervall de Temps Elementaire
- R: Rapidité de modulation (en Baud)

$R = \frac{1}{ITE}$

### Classification des codes

|              | Unipolaire                                                                               | Bipolaire                                                                                                                                          | AMI[^3]                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Code NRZ[^1] | Un seul niveau de tension                                                                | Deux niveaux de tension (e.g -5 => 0, +5 => 1), la valeur moyenne ~= 0                                                                             | On alterne, pour la valeur de 1, entre une valeur négative et une valeur positive. On a donc une valeur moyenne = 0          |
| Code RZ[^2]  | Un seul niveau de tension, remise à zéro à la moitié de l'ITE de toute valeur non nulle. | Deux niveaux de tension (e.g -5 -> 0 => 0, +5 -> 0 => 1). A nouveaux, nous avons une remise à zéro à la moitié de l'ITE de toute valeur non nulle. | On alterne entre une valeur positive et négative où l'on a une remise à zéro à la moitié de l'ITE de toute valeur non nulle. |
| Code Biphase |

RZ, surtout bipolaire nous permet de garder l'horloge

Transmissions synchrone: transmission TV pendant longtemps et continuellement, le signal devrait pouvoir donner l'horloge.  
Transmission asynchrone: transmission courte et espacée dans le temps

[^1]: Non Remis à Zéro
[^2]: Remis à zéro
[^3]: Alternate Mark Inversion

#### Code Biphase

- ##### Biphase Unipolaire

  - 0: valeur constante
  - 1: front descendant[^4]

- ##### Biphase bipolaire (Manchester)

  - 0: front montant[^5]
  - 1: front descendant

  > **Note:**  
  > On change de tension pendant l'ITE, plus précisemment à sa moitié.

- ##### Manchester différentiel

  - 0: même symbol que l'ITE précédent
  - 1: symbole opposé au symbole de l'ITE précédent

  | 0   | 1   | 1   | 0   | 1   |
  | --- | --- | --- | --- | --- |
  | FM  | FD  | FM  | FM  | FD  |

[^4]: Valeur positive à valeur négative
[^5]: Valeur négative à valeur positive

#### Code à mémoire HDB3

- Bit de bourrage:
  - S'assure que la valeur moyenne du signal codé est nulle.
  - Il vaut 0, -5 ou +5 de manière à ce que la valeur moyenne du signal, après lui, soit nulle.
- Bit de viol:
  - Permet au récepteur de reconnaître la suite de 4 zéros
  - viole l'alternance
  - donc identique au dernier symbole non nul.

| 0     | 1   | 0    | 1   | 1   | 0 (Bit de Bourrage) | 0    | 0    | 0 (Bit de viol) |
| ----- | --- | ---- | --- | --- | ------------------- | ---- | ---- | --------------- |
| nulle | +5  | null | -5  | +5  | -5 (Valeur Bas)     | null | null | -5              |

On utilise le bit de bourrage et de viol dès qu'on a 4 zéros d'affilé, bourrage en première position, viol en dernière.

Le principe de ce code est qu'il soit tout le temps en valeur moyenne = 0.

##### Code à mémoire Miller

- 0:
  - pas de transition au milieu de l'ITE
  - au début de l'ITE, conserve le même niveau de tension si le symbole précédent était un 1
  - ne le conserve pas sinon
- 1:
  - transition au milieu de l'ITE
  - au début de l'ITE, conserve le même niveau de tension que le symbole précédent

### Choix d'un code

- Les critères dépendent principalement du support de transmission
- Il dépend ausis de contraintes économiques
  - facilité de mise en oeuvre
  - immunité aux bruits

Bande passante: Bande de fréquence - bande du canal

<details>

<summary>

## TD 1

</summary>

### 1. Code du RNIS

- NRZ AMI inversé
  - 0: +5 ou -5
  - 1: 0

1. Que vaut l'ITE ?

   ITE = $\frac{1}{64.10^3}$ = 15.625 ms

2. En mode DATA, tracer le signal correspondant à la transmission du mot "Hello" ("A"=65, "a"=97, en ASCII)

    | H   | e   | l   | o   |
    | --- | --- | --- | --- |
    | 72  | 101 | 108 | 111 |

    | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 1   | 1   | 0   | 0   |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | +5  | -5  | +5  | 0   | -5  | +5  | 0   | -5  | 0   | +5  | 0   | -5  | +5  | 0   | 0   | -5  | +5  |

3. Que vaut la valeur moyenne du signal pour ce mot ? Généraliser

    La valeur moyenne du signal = 0.

4. Reprendre la question précédente avec un code NRZ unipolaire inversé. Généraliser.

    - NRZ Unipolaire inversé
      - 0: +5
      - 1: 0

    La valeur moyenne vaut ~$\frac{0.75}{2}$.

### 2. Code HDB 3

1011 1000 0000 0001 0100 0011 0000 1010 0010 0001

1. Représenter cette suite en utilisant un codage NRZ AMI

    | 1   | 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 1   |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | +   | 0   | -   | +   | -   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | +   | 0   | -   | 0   | 0   | 0   | 0   | +   | -   | 0   | 0   | 0   | 0   | +   | 0   | -   | 0   | 0   | 0   | +   | 0   | 0   | 0   | 0   | -   |

2. Quel est l'inconvéniant de ce codage ?

    On risque de perdre l'horloge.

3. On décide d'utiliser un code HDB3. Représenter le signal en utilisant ce codage.

    | 1011  | 1000 | 0000 | 0001 | 0100    | 0011    | 0000 | 1010  | 0010 | 0001   |
    | ----- | ---- | ---- | ---- | ------- | ------- | ---- | ----- | ---- | ------ |
    | +0-+  | -000 | -+00 | +00- | 0+-0    | 0-+-    | +00+ | -0+0  | 00-0 | 00-+   |
    | \____ | B___ | VB__ | V___ | \_\_B\_ | \_V\_\_ | B__V | \____ | ___B | _\_V\_ |

    > **Note:**  
    > Le bit de bourrage doit faire en sorte que la
    > valeur moyenne du bit suivant soit nulle, il
    > peut donc être null, si nécessaire.

4. Expliquer l'intérêt du bit de viol ?

    Il permet de retrouver la suite de 4 zéros sans avoir
    à envoyer une tension nulle trop longtemps.

5. Quel est l'intérêt du bit de bourrage ?

    Il permet d'avoir une valeur moyenne nulle.

### 3. Code RZ bipolaire

1. On considère le codage RZ bipolaire, rappeler son principe.

    On fait un retour à zéro à la moitié de l'ITE de chaque valeur non-nulle.

    - 0: +- 5 -> 0
    - 1: +5 -> 0

2. Représenter le signal-valeur absolue de ce code ?

    - 0: +5 -> 0
    - 1: +5 -> 0

3. A quel signal correspond-il ?

    Cela correspond à l'horloge.

4. Quel est l'intérêt de récupérer l'horloge en réception ?

    On sait comment décoder le signal.

### 4. Code Manchester

1. Préciser le problème que l'on peut rencontrer si on se trompe lorsqu'on connecte les paires d'émission et de réception.

    On recevra un 1 à la place d'un zéro et inversement.

2. Rappeler le principe du codage Manchester différentiel.

    La valeur moyenne = 0.
    Il garde l'horloge.

3. Montrer qu'il peut résoudre ce problème.

    Vu que l'on inverse tout, on pourra tout de même retrouver nos valeurs.

### 5. Code [Miller](#code-à-mémoire-miller)

Représenter la valeur 8AF3 avec le code Miller.

8    A    F    3  
1000 1010 1111 0011  

| 1   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FD  | B   | H   | B   | FM  | H   | FD  | B   | FM  | FD  | FM  | FD  | B   | H   | FD  | FM  |

> **Note:**  
>
> - FD: Front Descendant, voir [^4].
> - FM: Front Montant, voir [^5].
> - B: Niveau Bas
> - H: Niveau Haut

</details>

<details>

<summary>

## TD 2

</summary>

1. Décodage de codes numériques, tel un récepteur

    1. Signal 1: [HdB3](#code-à-mémoire-hdb3)
       - ITE: 1 carreaux
       - Rapidité de modulation: 500 000 bauds
       - Décodage:

          | 1   | 1   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   |
          | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
          |     |     |     |     |     | B   |     |     | V   |     | B   |     |     | V   |     |     |     | B   |     |     | V   |     |     |     |     |     |     | B   |     |     | V   |

    1. Signal 2: [Code de Miller](#code-à-mémoire-miller)

        - ITE: 2 carreaux
        - Rapidité de modulation: 1 / ITE = 250k bauds
        - Décodage:

          | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 0   | 1   | 1   |
          | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
          |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |

    1. Signal 3: [Code Manchester Différentiel](#manchester-différentiel)

        - ITE:
        - Rapidité de modulation: bauds
        - Décodage:

          | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 1   |
          | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
          |     |     |     |     |     |     |     |     |     |     |     |     |     |     |

1. Coder le signal 3 avec le code RZ unipolaire puis Manchester

    - [RZ Unipolaire](#classification-des-codes)

    - [Manchester](#biphase-bipolaire-manchester)

</details>

<details>
<summary>

## TD 3

</summary>

1. Exercice 1

   1. Donner les caractéristiques électriques du signal

       - Niveau haut: 0
       - Niveau bas: -4
       - tension de repos: 0

   2. Cela ne peut pas être du NRZ AMI car l'on a pas 3 niveaux de tension.

   3. Peut-il alors s'agir des codes: Pourquoi ?

      - RZ Bipolaire: :x:

        Le signal n'a pas 3 niveaux de tensions

      - RZ AMI: :x:

        Le signal n'a pas 3 niveaux de tensions.

      - Biphase Unipolaire: :x:

        Le signal n'a pas 3 niveaux de tensions.

   4. Si l'on sait que le débit est égal à 10Mbits/s, pourquoi peut-on dire qu'il ne s'agit pas des codes NRZ Unipolaire ou Bipolaire ?

      D = 10 Mbits/s
      ITE = $\frac{1}{D}$ = $0.1\mu$s

      Ce n'est pas possible que ce soit du NRZ unipolaire, il ne pourrait pas changer de débit durant la transmission.  
      Ainsi donc, le RZ Unipolaire et le NRZ Bipolaire ne peuvent pas marcher pour la même raison.

      Il nous reste donc le [Biphase Bipolaire](#biphase-bipolaire-manchester).

      Si on suit les schémas, le Biphase Bipolaire semble être le signal que l'on cherche.

1. Exercice 2

   1. Quelle est la durée du préambule ? Quelle est la durée du délimiteur de trame ?

       - Préambule: 7*8 bits = 56 bits soit $5.6\mu$s.
       - Délimiteur: 8 bits = $0.8\mu$s.

   2. Pourquoi envoie-t-on cette suite de bits en début de transmission ?

      Pour obtenir l'horloge du signal.

   3. Décoder le signal reçu.

      | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
      | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |

   4. Comment est codé le 1 ? le 0 ?

      - 1: front montant
      - 0: front descendant

   5. Quelle est l'adresse MAC destinataire ?

      C'est l'adresse de broadcast: `ffffff`

</details>

## Cours (suite)

### Choix d'un code, partie 2

- Dépend principalement de la Bande Passante du canal.
- On étudie donc **la densité spectrale de puissance** du code: répartition moyenne de la puissance en fonction de la fréquence.
  Elle indique *l'occupation spectrale*[^6] du code.

[^6]: Bande de fréquence qui transporte 90% de la puissance totale du code.

### Densité spectrale de différents codes

- #### Code NRZ Unipolaire

  - Une raie à f=0
    - Beaucoup d'énergie en très basse fréquence
      et pas du tout à la fréquence de l'horloge
  - Pas d'énergie pour f = R
  - OS[^6] faible
    - Beaucoup d'énergie, à nouveau, dans les très basses fréquences
    - L'OS occupe 1R

- #### Code Manchester

  - Pas d'énergie à f = 0
  - De l'énergie pour f = R
    - Le récepteur pourra reconstituer l'horloge
  - OS[^6] plus large
    - L'OS occupe 2R

  Dans le cas où l'on veut faire du manchester mais que notre canal est trop petit,
  on peut diminuer R (R = $\frac{1}{ITE}$), c'est à dire augmenter l'ITE, donc aller moins vite dans la transmission
  du signal, donc la rapidité de modulation est diminuée.

### Caractéristiques importantes des codes

- #### Occupation Spectrale

  - Largeur de la bande de fréquence occupée
  - amplitude des composantes basse fréquence et f = 0

- #### Densité des 

### Transmission asynchrone

Chaque caractère est émis de façon irrégulière dans le temps.  
Transmission qui n'est pas en continu.

### Transmission synchrone

Émetteur et récepteur sont cadencés à la même horloge:

- nécessité donc pour le récepteur de "recevoir" l'horloge du signal

$P_{BF}$: part de la puissance totale contenue

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
