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

- Biphase Unipolaire
  - 0: valeur constante
  - 1: front descendant[^4]
- Biphase bipolaire (Manchester)
  - 0: front montant[^5]
  - 1: front descendant

  > **Note:**  
  > On change de tension pendant l'ITE, plus précisemment à sa moitié.
- Manchester différentiel
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

## TD 1

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

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
