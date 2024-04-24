# R405 - Automatisation

- RUNDECK
- Ansible, Puppet, Chef, Rudder
- IaC => Vagrant, Packer, Docker, Terraform, OpenTofu

> [!NOTE]
> HereDoc

```bash
cat << StPushou\
Vénérez le Saint Pouchou ! \
J'ai dit: Vénérez le Saint Pouchou $(whoami) ! \
StPushou\
```

## Ansible

- fichiers de configuration
- hosts
- modules Ansibles
- transport SSH
- Playbook
- Templates
- Facts
- Rôles
- collections

## TD 1

1. Que font ces oneliners ou ces scripts BASH ? Ecrivez ce que vous pensez voir en sortie de la commande ou du script BASH.

   1. Cette ligne `DATE=$(date); echo $DATE` donne comme résultat le retour de la date système, en prenant la locale.

      ```sh
      Thu Apr 4 10:25:24 AM CEST 2024
      ```

   1. Cette ligne `cat /etc/passwd |wc -l` renvoie le nombre de lignes du fichier `/etc/passwd`

      ```sh
      48
      ```

   1. Cette ligne `find /var/log -type f -name *.log -exec ls -alh {} \;` renvoie tous les fichiers comprenant l'extension `.log` dans le répertoire `/var/log`

      ```sh
      -rw-------. 1 root root 37K Feb 20 19:13 /var/log/anaconda/anaconda.log
      -rw-------. 1 root root 4.0K Feb 20 19:13 /var/log/anaconda/dbus.log
      -rw-------. 1 root root 0 Nov  1 02:15 /var/log/anaconda/dnf.librepo.log
      -rw-------. 1 root root 120 Nov  1 02:15 /var/log/anaconda/hawkey.log
      -rw-------. 1 root root 4.3M Feb 20 19:13 /var/log/anaconda/journal.log
      -rw-------. 1 root root 94K Nov  1 02:15 /var/log/anaconda/ks-script-_g54h3h4.log
      -rw-------. 1 root root 0 Nov  1 02:15 /var/log/anaconda/ks-script-gxy2ckvo.log
      -rw-------. 1 root root 12K Feb 20 19:13 /var/log/anaconda/packaging.log
      -rw-------. 1 root root 4.8K Feb 20 19:13 /var/log/anaconda/program.log
      -rw-------. 1 root root 878K Feb 20 19:13 /var/log/anaconda/storage.log
      find: ‘/var/log/audit’: Permission denied
      find: ‘/var/log/chrony’: Permission denied
      find: ‘/var/log/gdm’: Permission denied
      find: ‘/var/log/httpd’: Permission denied
      find: ‘/var/log/libvirt’: Permission denied
      find: ‘/var/log/ppp’: Permission denied
      find: ‘/var/log/private’: Permission denied
      find: ‘/var/log/samba’: Permission denied
      find: ‘/var/log/speech-dispatcher’: Permission denied
      find: ‘/var/log/sssd’: Permission denied
      find: ‘/var/log/swtpm/libvirt/qemu’: Permission denied
      -rw-------. 1 root root 4.9K Apr  4 08:03 /var/log/boot.log
      -rw-r--r--. 1 root root 508K Apr  4 09:54 /var/log/dnf.librepo.log
      -rw-r--r--. 1 root root 227K Apr  4 09:54 /var/log/dnf.rpm.log
      -rw-r--r--. 1 root root 263K Apr  4 09:54 /var/log/dnf.log
      -rw-r--r--. 1 root root 1010 Mar 31 17:29 /var/log/nvidia-installer.log
      -rw-r--r--. 1 root root 1.8K Apr  4 08:03 /var/log/akmods/akmods.log
      -rw-r--r--. 1 root root 2.8K Apr  4 09:54 /var/log/hawkey.log
      ```

   1. L'alias `cds` nous permet d'accéder directement au répertoire `/Users/pouchou/ownCloud/cours\ iut\ 2/cours\ iut/latex/inc/scripts` sans avoir à faire un `cd` et d'entrer le répertoire en question.

      ```sh
      alias cds='cd /Users/pouchou/ownCloud/cours\ iut\ 2/cours\ iut/latex/inc/scripts'
      ```

   1. Cette ligne `echo 111-{aa,bb,cc}+{xx,yy,zz}-222` va imprimer sur la console une suite de termes qui vont itérer
      entre `aa`, `bb` et `cc` pour la première entrée et `xx`, `yy`, `zz` pour la deuxième de la forme suivante: `111-[XX]+[YY]-222`.

      ```sh
      111-aa+xx-222 111-aa+yy-222 111-aa+zz-222 111-bb+xx-222 111-bb+yy-222 111-bb+zz-222 111-cc+xx-222 111-cc+yy-222 111-cc+zz-222
      ```

   1. De la boucle suivante:

      ```sh
      MESSAGE="hello world"
      for i in "$MESSAGE"; do echo $i; done
      hello world
      for i in $MESSAGE; do echo $i; done
      hello
      word
      ```

      On peut retenir que le résultat change puisque lors de la première boucle, nous utilisons la variable entre guillemets, nous avons donc
      créé une nouvelle structure/variable comportant le message, dans la deuxième boucle, nous utilisons la variable directement, nous pouvons
      donc plus facilement la découper avec le séparateur <kbd>espace</kbd>.

   1. De la commande suivante:

      ```sh
      cp dirname-et-basename.sh dirname-et-basename.sh.bak
      ```

      on peut la simplifier tel que:

      ```sh
      cp dirname-et-basename.sh{,.bak}
      ```

   1. Avec la commande:

      ```sh
      ps -ef
      ```

      On obtient le PID de notre process bash, faire

      ```sh
      kill -9 $$
      ```

      va tuer le process bash sur lequel nous avons exécuté la commande car `$$` dans bash est notre dernière sortie d'exécution, en l'occurence `4022`.

   1. La commande suivante:

      ```sh
      ping -c1 localhost && { echo succes;} || { echo pasglop; }
      ```

      va "pinger" le FQDN enregistré sur la machine `localhost` et en fonction de la sortie positive ou négative (graĉe au `&&`)
      va imprimer sur la console soit `succes` si nous avons réussi ou `pasglop` si la commande a retourné un code d'erreur.

1. Explorons `$*` et `$@`: quels résultats donnent les scripts suivants ?

    1. le résultat de la commande suivante:

      ```sh
      ./loopargs1.sh un deux trois quatre
      ```

      renvoie:

      ```txt
      un
      deux
      trois
      quatre

      un
      deux
      trois
      quatre

      un deux trois quatre

      un
      deux
      trois
      quatre
      ```

      dans le cas de la troisième boucle avec `$*`, on peut voir que le fait
      de créer une nouvelle variable nous permet d'afficher en une ligne le contenu,
      au contraire de `$@` qui ne fait pas de différentiations.

1. Solutions pour lire un fichier

   1. Découverte de IFS

      1. Le script suivant

          ```sh
          mkdir "repertoire avec espace"{1,2} &>/dev/null && touch "fichier "{1,2} \
          & > /dev/null || echo -e "rep et fichiers presents"
          for n in $(ls) ; do echo $n ; done
          echo -e "-------------------"
          echo -e "Avec IFS modifié"
          IFS=$'\n'; for n in $(ls) ; do echo $n ; done
          ```

          fera:

          - la création des répertoires `repertoire avec espace1` et `repertoire avec espace2` tout en supprimant toute sortie console (`&> /dev/null`).
          - Si la création des répertoires s'effectue bien, il créera les fichiers `fichier 1` et `fichier 2`.
          - Il affichera ensuite les entrées (fichiers et dossiers) du répertoire courant d'exécution
          - Il affichera deux lignes avec du contenu arbitraire ("---..." et "Avec IFS ...")
          - Puis affichera à nouveau les fichiers du répertoire courant d'exécution en changeant l'IFS en `$'\n'`, ce qui va permettre de ne pas sauter
            de lignes entre le contenu d'une ligne même avec des espaces mais de sauter des lignes après le contenu.

      1. Que fait ce script ?

          Le script suivant fait:

          ```sh
          #!/bin/bash
          _file="${1:-/dev/null}" # Sécurité en cas d'erreur
          while IFS= read -r line
          do
          echo "$line"
          done < "$_file"
          ```

          - Il définit la variable `_file` comme étant `/dev/null`
          - Une boucle tant que (`while`) permet de lire du contenu avec `read -r line` en tant que condition, puis est attribuée à la variable `line`
          - Si la condition renvoie vrai, imprimer sur la console la variable `line`, qui est la ligne exécutée
          - Lire la valeur de `_file`, qui est nulle.

          > [!NOTE]
          > Le séparateur (IFS) sera soit null soit " ".

   1. Que fait ce script ?

      ```sh
      # !/bin/bash
      while IFS= read -r line
      do
      echo "$line"
      done < "/etc/passwd"
      ```

      Ce script fait:

      - Une boucle tant que permet de lire du contenu puis d'attribuer la valeur à la variable `line`
      - Si la conditiion est vraie, imprimer sur la console la valeur de `line`
      - Lire le contenu de `/etc/passwd`

      1. On rappelle que les champs de /etc/passwd sont séparés par ’ :’ A quoi sert IFS ?

            IFS nous permet de définir la séparation utilisée pour l'affichage console et ainsi donc
            de pouvoir séparer des chaines de caractères en liste de chaines.

          > [!NOTE]
          > Le séparateur (IFS) sera soit null soit " ".

   1. Que fait ce script ?

      ```sh
      #/bin/bash
      IFS=:
      while read login mdp uid gid gecos home shell;
      do echo "${gecos:=undef} > login $login (home : $home, shell : $shell)" ;
      done < /etc/passwd
      ```

      - On définit l'IFS comme étant le caractère `:`
      - Une boucle tant que permet de lire du contenu puis attribue la valeur des champs aux variables suivantes: `login`, `mdp`, `uid`, `gid`, `gecos`, `home` et `shell`
      - Si la condition est vraie, imprimer sur la console une ligne contenant une expression arbitraire mais avec une condition que si `gecos` si trouve être vide, imprimer `undef` à la place
      - Lire le contenu de `/etc/passwd`

      > [!NOTE]
      > Le séparateur (IFS) sera ":".

## TD 2

1. Commande AT

    1. Donner la syntaxe pour effectuer une commande différée répondant aux critères suivants:
         1. A 3h10 du matin

             ``

         2. A 3h10 de l'après-midi

         3. Le 21 janvier 2048 à 5h27

         4. Dans 20 min.

         5. Dans 3 jours

         6. Dans 3 jours et un mail est envoyé à l'utilisateur

         7. A 3h10, lancer le script /home/user/script
    1. Quelle est la commande permettant de voir la liste des taches en attente ?
    1. Quelle est la commande permettant de supprimer une tache en attente ?
    1. Dans quel dossier sont stockées les taches en attente ?
    1. Regarder le contenu et le nom d’un des fichiers de taches en attente (après avoir créé une ou 2 taches)

1. CRON

## <center> AT </center>

1) a) at 03:10 AM ou at 03:10
   b) at 03:10 PM ou at 15:10
   c) at 05:25 21.01.48
   d) at now + 20min
   e) at now + 3 days
   f) at -m now + 3 days
   g) at 03:10 -f /home/user/script
2) atq ou at -l
3) atrm id ou at -r id
4) Le dossier est /var/spool/cron/

## <center> CRON </center>

1. ...
   1. /var/spool/cron/crontabs
   1. ...

      | donnée   | répertoire        |
      | -------- | ----------------- |
      | heures   | /etc/cron.hourly  |
      | jours    | /etc/cron.daily/  |
      | semaines | /etc/cron.weekly/ |
      | mois     | /etc/cron.monthly |

   1. utilisateur qui execute la commande
   1. ils sont lancés à l'heure et la date précisé dans l'execution de la commande
   1. run-parts execute les scripts se situant dans le dossier.

1. ...

## TD 3

...

## TD 4

## TP Ansible

...
