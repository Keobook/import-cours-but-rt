# R404 - Données cellulaires

Antennes 5G: FUll Dimension MIMO

<details><summary>

## TD 1

</summary>

1. Niveau de réception GSM-DCS
   1. Quelle est la fréquence du signal ?

      $F_L = 1710.2 + 0.2 (622 - 512)$ \
      $F_L = 1732.2 \textit{MHz}$ MS -> BTS \
      $F_U = F_L + 95 = 1827.2 \textit{MHz}$ BTS - > MS

   2. Quelle est la puissance reçue en W ?

      $P_{\omega} = 31.6 pW$ \
      $P_R = 10^{\frac{-75}{10}} mW$ \
      $P_R = 3.16 10^{-8} mW$

   3. Quelle est la tension correspondante sur une charge de 100 $\omega$

      $P = U . I = \frac{U^2}{R}$

      $U = \sqrt{P . R}$ \
      $= \sqrt{31.6 * 10^{-12} * 100}$ \
      $\equiv 56.2 \mu V$

   4. La BTS est de classe M1. Quelle est sa puissance d'émission ?

      **32 dBm** ou **1.6**

      \> 27

      > [!NOTE]
      > Colone DCS

   5. Le gain de l'antenne d'émission est de 17 dBi et de 0 dBi pour le mobile.  
      Quel est l'affaiblissement du signal mesuré ?

      $P_R = P_E + G_E + G_R - (\textsf{Pertes Affaiblissement})$  

      |           |          |       |       |
      | --------- | -------- | ----- | ----- |
      | $-75$ dBm | $32$ dBm | 17 dB | 0 dBi |

   6. <br />

      $A = 40 \log d - 20 \log(20 * 1.7) + 20 + \frac{1827.2}{40} + 0.18 * \frac{1827.2}{40} + 0.18 * \frac{80}{100} - 0.34(20 - 1.7)$  
      $40 \log d = 124 - 28.972$  
      $d = 10^{\frac{95.028}{40}} = 237.5$ m

      > [!NOTE]
      > Où $20 \log(20 * 1.7) + 20 + \frac{1827.2}{40} + 0.18 * \frac{1827.2}{40} + 0.18 * \frac{80}{100} - 0.34(20 - 1.7)$ = $28.972$ dB

      ![reponse-question-6](./src/src/reponse-question-6.jpg)

   7. En utilisant le modèle anglais (cf. annexe), estimer la distance entre le mobile et la BTS ($h_e = 20$ m et $h_r = 1.7$ m).

      $d_2 = 837.5$ m  
      $P_{R_2} = 32 + 17 +0 - (40 \log d2 + 28.972)$  
      $P_{R_2} = - 96.89 dBm$

   8. ...

      Sensibilité $-102$ dBm

      -96 > -102 => OK

   9. ...

      $P_{R_3} = -102 dBm$

      ![reponse-question-9](./src/src/reponse-question-9.jpg)

</details>
<details>

<summary>

## TD 2

</summary>

1. ### Délais de propagation

   $$

      t_2 = \frac{d}{C} = 1.07 \mu s

   $$

2. ### TA en GSM/DCS

$$

{MS}_1 TA=5 \\
{MS}_2 TA=9

$$

</details>
