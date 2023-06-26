# Administrer - Portfolio S2

- SAE-11

## Composantes essentielles

- <details>

  <summary>

  ### En communiquant avec les clients et les différents acteurs impliqués

  </summary>

  Il est important de savoir communiquer efficacement et de manière pertinente
  avec des clients et les différents acteurs impliqués afin permettre aux
  informations nécessaires d'être transmises.

  - Dans le cadre professionnel / associatif, j'ai du communiquer avec les
    dirigeantes de l'association, qui sont aussi mes clientes, principalement
    sur des questions de style et rendu.

    J'ai utlisé principalement les SMS car c'était un des seuls moyens de communication
    que l'on partage, en plus des addresses mails du nom `firstname.lastname@petitspapiersdarchitecture.fr`..

  - Dans le cadre de la SAE-12, j'ai eu à communiquer avec mon client, qui était
    aussi le professeur chargé de m'évaluer, sur la forme et le fond des livrables attendus.

  </details> <div class="page" />
- <details>

  <summary>

  ### En choisissant les solutions et technologies adaptées

  </summary>

  Choisir les technologies adaptées sont primordiales à la réussite d'un projet.  
  Tout projet peut se voir échouer ou être rempli de problèmes seulement à cause
  d'une mauvais technologie employée.

  - Dans le cadre de la SAE-21, j'ai dû revoir les technologies employées par le
    professeur, qu'elles aient été obligée ou non.

    J'ai dû, 48h avant la date de rendu initiale, revoir mon architecture et infrastructure
    réseau car le routeur qui nous avait été obligé d'utiliser ne pouvait servir à faire
    ce qui était demandé. J'ai alors testé quelques autres routeurs plus récents et ceux
    faisant partie du tutoriel partagé par le professeur. J'ai fini par en utiliser un
    où je m'étais assuré de sa capacité à effectuer la tâche et d'être compatible avec
    mon réseau.

    Dans un autre cas, le choix du logiciel, de décider de partir sur du Cisco Packet Tracer
    a montré être compliqué de par sa nature d'émulateur et non de simulateur.

    J'ai dû, tout au long du projet, balancer erreurs d'émulation et restriction logicielle.
    J'avais tenté de faire un DNS-relay mais c'est impossible de le faire sur Cisco Packet Tracer
    car la fonctionnalité n'est pas prise en charge. J'ai eu des tests de connexion entre
    les deux bouts de mon tunnel VPN qui ont échoué car les paquets ARP se sont simplement
    volatilisé durant leur voyage car j'avais trop de communications en même temps pour
    Packet Tracer.

    En dernier cas, l'utilisation de liens cuivres dans un projet ayant pour vocation
    de se projeter dans un futur où je suis technicien Réseaux et Télécommunications.

    J'ai réfléchi avec un regard critique sur la situation actuelle de l'infrastructure réseau
    et j'ai décidé d'utiliser des liens fibres et non cuivrés sur mon schéma car un futur où
    la plupart des réseaux sont fibrés ne me semble ni loin ni inatteignable.

  </details> <div class="page" />
- <details>

  <summary>

  ### En respectant les principes fondamentaux de la sécurité informatique

  </summary>

  La sécurité est un élément crucial, surtout dans le domaine de l'informatique
  et l'est encore plus dans le domaine du réseau et des télécommunications.

  - Dans le cadre de la SAE-21, j'ai eu à configurer un réseau d'entreprise.
    Dans les spécificités techniques, il a été mentionné l'utilisation de VLANs
    et les règles de communication entre eux.

    Une de ces règles a été le fait que le VLAN du service technique soit capable
    de communiquer avec tous les autres VLANs au sein du réseau interne sans que les
    autres VLANs puissent être initiateurs d'une connexion avec une machine du VLAN
    technique. Cela a impliqué la recherche d'une règle de politique de VLAN permettant
    les communications initiées par une partie, et donc la réponse de l'autre partie, et
    ne permettant pas les communications initiées par l'autre partie.

    Dans le cas de la SAE-21, j'ai décidé d'utiliser une règle ICMP interdisant tout trafic ICMP
    sauf les paquets `ECHO REPLY` des VLANs n'étant pas le VLAN du service technique.  
    Ainsi, le service technique pouvait être initiateur d'une communication vers les autres
    mais ne se retrouvait jamais à répondre à une requête d'autres VLANs.

  - Dans le cadre de la SAE-24, j'ai eu à administrer une VM Ubuntu, hébergée chez [Scaleway](https://www.scaleway.com/).

    J'ai eu à mettre à jour les clés SSH utilisées par mes collègues ainsi que de vérifier que les ports sortants et entrants
    étaient bien ceux dont qui devaient l'être. J'ai aussi regardé les logs `journalctl` chaque jour afin de m'assurer du bon
    fonctionnement de la VM et des services installés dessus.

  </details> <div class="page" />
- <details>

  <summary>

  ### En utilisant une approche rigoureuse et méthodique (démarche scientifique)

  </summary>

  Utiliser une approche rigoureuse et méthodique est, pour la plupart du temps,
  nécessaire à la bonne résolution de problèmes.

  - Dans le cadre de la SAE-21, j'ai dû développer un réseau
    pour une entreprise, en prenant en compte les besoins
    de l'entreprise, une DMZ, le réseau FAI et des sites distants.

    Afin de s'assurer de ne pas perdre le fil de la conception,
    j'ai créé un schéma réseau avant de commencer le montage réseau
    sur Cisco Packet Tracer.

    <div style="text-align: center; color: rgb(180, 180, 180)">

    ![sae21-schema-reseau](../../sae-21/src/img/schema-reseau.drawio.svg)
    <span style="border-bottom: 1.5px solid rgb(180, 180, 180);"> *Schéma réseaux fait lors de la SAE-21* </span>

    </div>

    J'ai ensuite construit et testé le réseau block par block en suivant le schéma
    imaginé initialement.

  - Dans le cadre de la SAE-12, j'ai dû travailler sur des outils d'installation, voir de débogage,
    du réseau. Et pour ce faire, j'ai eu à utiliser une approche méthodique consistant à:

    - Vérifier la connexion physique (i.e. Est-ce que c'est branché ?)
    - Vérifier l'état de la négociation du lien (e.g. Mii-Tool)
    - Vérifier l'état de la carte réseau (e.g. l'utilitaire `ip`)
    - Vérifier le DHCP / Vérifier l'adresse IP fixe
    - Vérifier la gateway par défaut (i.e. `ping 8.8.8.8`)

  </details> <div class="page" />
- <details>

  <summary>

  ### En assurant une veille technologique

  </summary>

  Dans le milieu de l'informatique, il est nécessaire d'assurer une
  veille technologique d'autant plus que les technologies évoluent rapidement.

  - Dans le cadre personnel, j'effectue depuis plusieurs années une veille technologique
    dans le domaine de l'informatique, cela a commencé, et l'est toujours, par pur intérêt intellectuel
    d'apprendre et de connaître ce qui se fait, comment ça se fait, etc.

    Cela m'a amené à suivre régulièrement les publications sur [Microsoft Research](https://www.microsoft.com/en-us/research/),
    [Google Research](https://research.google/pubs/) ou encore [Spotify R&D](https://research.atspotify.com/publication/).

    J'écoute les podcasts de la EFF (Electronic Frontier Foundation), [How to Fix the Internet](https://open.spotify.com/show/4UAplFpPDqE4hWlwsjplgt?si=7f7d58e8f22343d3),
    de GitHub, [The ReadME Podcast](https://open.spotify.com/show/660KitvdJDX2vUmioAbwSQ?si=57ff36a67a5449a9),
    de Spotify, [NerdOut@Spotify](https://open.spotify.com/show/5eXZwvvxt3K2dxha3BSaAe?si=7ddbef4e537048e0) ou encore
    de Gitpod, [DevXPod](https://open.spotify.com/show/3zOACmbvoA5qxAqGYGxgMe?si=086442ede40049f0).

    En plus de cela, j'esaie au maximum de suivre les conférences et sommets de l'informatique tels que
    le [GitHub Universe](https://githubuniverse.com/), la conférence [Google I/O](https://io.google/) mais
    j'ai aussi participé à [Polycloud](https://polycloud.fr/), en présentiel cette fois-ci.

    Je me retrouve, des fois voir la plupart du temps, à sauter de projets en projets sur GitHub jusqu'à finir à tomber sur
    de nouveaux projets et / ou de nouvelles technologies.

  - Dans le cadre professionnel, je me dois de me tenir au courant des derniers changements sur les
    technologies et services que j'utilise ce qui fait que j'écoute les derniers podcasts [Reactiflux](https://open.spotify.com/show/4g3Le83YfsMeI8Fq3cpPeH?si=ddcc8e2536254922),
    les publications de DigitalOcean ou de Google, pour la Google Cloud Platform (GCP) et autres.

  </details> <div class="page" />

## Apprentissages critiques

- <details>

  <summary>

  ### Comprendre l'architecture et les fondements des systèmes numériques, les principes du codage de l'information, des communications et de l'Internet

  </summary>

  - Dans le cadre de la SAE-12 et de la SAE-15, j'ai du travailler avec des architectures différentes,
    des principes hétérogènes que ce soit sur la manière de communiquer ou simplement de fonctionner.

    Tout comme chaque langage de programmation à son paradigme qui lui est propre.

    J'ai eu à comprendre le fonctionnement des différentes instances Windows ou Linux, leur principe
    de fonctionnement ainsi que la manière dont leur I/O était organisé.

  - Dans le cadre de la SAE-24, j'ai dû comprendre comment fonctionnait le protocole MQTT ainsi
    que toute l'architecture dans laquelle il est utilisé. J'ai aussi dû comprendre quels étaient
    les principes derrière le protocole LoRaWan.

    Sans oublier de parler du fait que j'ai dû comprendre comment fonctionnait les capteurs utilisés
    aussi bien que les micro-controlleurs.

  </details> <div class="page" />
- <details>

  <summary>

  ### Configurer les fonctions de base du réseau et des systèmes usuels

  </summary>

  - Dans le cadre de la SAE-21, j'ai eu à concevoir puis développer un réseau
    d'entreprise comprenant un DHCP, un DNS, un serveur Web ainsi qu'une distinction
    entre DMZ et réseau privé (local), où un filtre NAT à d'ailleurs été mis en place
    à la jonction des deux zones.

    J'ai du configuer le DHCP afin qu'il puisse être par VLAN et avoir des pools
    d'adressage différents.

    J'ai du configurer des règles afin que les services techniques ne puissent pas
    avoir accès à plus loin que leur réseau local soit par des règles de politique
    de VLAN soit par la manière dont ils intéragissent avec le réseau (i.e. Adresse IP).

  </details> <div class="page" />
- <details>

  <summary>

  ### Maîtriser les rôles et les principes fondamentaux des systèmes d’exploitation

  </summary>

  Maîtriser les rôles et les principes fondamentaux des systèmes d'exploitation permettent
  d'aborder des problèmes d'administration avec un recul pouvant permettre la résolution
  plus rapides de ceux-ci ou de découvrir un problème sous jacent racine du problème auquel
  on est confronté.

  - Dans le cadre de la SAE-11, j'ai pu travailler sur une campagne de sensibilisation sur
    la cybersécurité. J'ai donc du savoir les principes fondamentaux d'un système d'exploitation (OS)
    afin de pouvoir réfléchir et aider à réaliser une campagne pour prôtéger ces dits OS.

  - Dans le cadre de la SAE-12, j'ai du connaître les principes fondamentaux des systèmes d'exploitation
    afin de savoir quelles commandes requiert d'être en administrateur pour Windows ou super-utilisateur pour Linux.

    Comment fonctionne et comment intéragissement les composants matériels avec, d'un coté l'Active Directory pour Windows,
    de l'autre coté les chemins root et les chemins non root.

  - Dans le cadre de la SAE-23, vu que le projet incluait le déploiement avec Docker de l'application,
    j'ai dû installer Docker et le faire passer en mode non-root en ajoutant docker dans des groups
    avec des capabilities et des cgroups permettant à Docker et à ses containers de fonctionner sans
    avoir besoin d'être super-utilisteur.

  </details> <div class="page" />
- <details>

  <summary>

  ### Identifier les dysfonctionnements du réseau local et des réseaux de campus

  </summary>

  Savoir identifier les dysfonctionnements d'un réseau local ou d'un réseau de campus
  est primordial que ce soit à petite échelle ou à plus grande échelle.

  - Dans le cadre de la SAE-21, j'ai été confronté à des problèmes, comme la plupart
    de mes pairs, notamment sur la mise en place d'un VPN.  
    J'ai aussi dû créer des tests unitaires, requis dans le cadre de la SAE.

    En ce qui concerne la mise en place du VPN, il s'est avéré que les VPNs obligatoires
    n'étaient pas compatibles avec le travail demandé car ils étaient en EOL (End Of Life)
    et le support au sein de l'émulateur était déprécié.  
    Cependant, cela m'a permis de m'améliorer en débogage et en identification de dysfonctionnements
    réseaux en utilisant la capacité de l'émulateur de passer de `temps réel` à `simulation` et
    ainsi de voir où ils se retrouvaient être détruits et d'investiguer puis de définir les causes
    de ces dysfonctionnements.

    En ce qui concerne les tests unitaires, il a fallu identifier les différents dysfonctionnements
    possibles du réseau local lorsque l'on fait le test et s'assurer qu'ils ne puissent pas perturber
    le résultat de ceux-ci s'ils ne sont pas concernés par ce dysfonctionnement en particulier.

  - Dans le cadre de la SAE-12, j'ai dû créer une documentation sur l'installation d'un poste de bureautique
    dans un réseau.

    J'ai donc été obligé de penser aux possibles dysfonctionnements dans le réseau capables de rendre nulls
    les commandes effectuées ou venir perturber leur résultat.

    Si le serveur DHCP tombe, nous n'obtenons pas d'adresse IP via un bail DHCP, il ne sera donc pas possible
    de ping le serveur DNS de Google `8.8.8.8` pour tester la bonne configuration.  
    J'ai alors dû identifier ces dysfonctionnements possibles et les prendre en compte lors de la rédaction
    de la documentation.

  </details> <div class="page" />
- <details>

  <summary>

  ### Installer un système d’exploitation, linux et windows, par différents moyens

  </summary>

  On peut installer sur une machine un ou plusieurs systèmes d'exploitations.  
  D'où la plupart des bootloader sont capables de gérer différentes entrées.

  - Dans le cadre personnel, j'ai eu à manipuler des installations et des entrées
    GRUB que ce soit sur ma machine ou sur la machine d'amis que j'ai aidé à dépanner.

    Par exemple, dans le cas d'un dual boot, il est plus intéressant d'installer Windows
    puis d'installer Linux (avec GRUB) en second, car lors de l'installation de GRUB, la
    distribution Linux scanne normalement toutes les entrées BIOS de systèmes d'exploitations
    présents sur la machine et crée les entrées GRUB correspondantes.

    J'ai déjà eu à faire un dual boot sur ma machine, et c'est ma situation actuelle de par
    mon besoin d'utiliser des outils présents seulement sur Windows et d'autres outils seulement
    sous Linux.  
    J'ai eu à installer d'abord Windows puis Linux me simplifiant ainsi la création des entrées
    GRUB correspondantes aux entrées BIOS sur un système UEFI. Dans le cas où Linux a été installé
    avant, j'ai pu utiliser `os-prober` et `update-grub`.

    Dans le cas où `os-prober` détecte Windows mais qu'`update-grub` n'arrive pas à créer une entrée
    dans le GRUB, je l'ai faite manuellement dans `/etc/grub.d/`:

    ```sh
    menuentry "Windows 11"{
      insmod part_gpt
      search --set=root --fs-uuid <partition-UUID>
      chainloader /EFI/Microsoft/Boot/bootmgfw.efi
    }
    ```

  - Dans le cadre universitaire, que ce soit durant les SAE-12, SAE-15, ou durant
    certaines ressources telles que R202, j'ai eu à installer des VMs, des machines
    physiques et dans le cloud, avec des hyperviseurs tels que ESXi.

    J'ai eu entre les mains des images dites `netinstall` où l'image `.iso` est petite
    car l'on télécharge depuis Internet la plupart des paquets que l'on va avoir besoin.  
    Mais aussi des images de développement, d'Insiders ou encore des images normales
    avec une taille allant de 2Go jusqu'à 8Go.

    <div style="text-align: center; color: rgb(180, 180, 180)">

    ![windows-insiders-preview](./src/windows-insiders-iso.png)
    <span style="border-bottom: 1.5px solid rgb(180, 180, 180);">
      *Screenshot montrant la liste des choix d'ISO de Windows Insiders*
    </span>
    </div>

    <div style="text-align: center; color: rgb(180, 180, 180)">

    ![fedora-normal-isos](./src/fedora-isos.png)
    <span style="border-bottom: 1.5px solid rgb(180, 180, 180);">
      *Screenshot montrant la liste des choix d'ISO de Fedora*
    </span>
    </div>

    <div style="text-align: center; color: rgb(180, 180, 180)">

    ![fedora-netinstall](./src/fedora-netinstall.png)
    <span style="border-bottom: 1.5px solid rgb(180, 180, 180);">
      *Screenshot montrant la version NetInstall de Fedora*
    </span>
    </div>

  </details> <div class="page" />
- <details>

  <summary>

  ### Installer un poste de bureautique en réseau

  </summary>

  Installer un système d'exploitation sur une machine, c'est bien,
  faire en sorte qu'elle puisse communiquer avec le réseau, c'est mieux.

  - Dans le cadre de la SAE-12, j'ai dû travailler et me documenter sur
    la mise en réseau d'un poste de bureautique que ce soit sous Linux
    ou Windows.

    Sous Linux, on utilisera des utilitaires tels que `mii-tool`, `ip` et autres,
    alors que sous Windows, on utilisera plutôt les utilitaires PowerShell tels que
    `Get-NetIpAdress`, `Set-NetIpAdress`, etc.

    J'ai donc dû me documenter et créer une documentation sur les procédures et les
    équivalents tout en faisant attention de souligner les spécificités de chaque OS.

    > **Note**:  
    > J'ai d'ailleurs toujours mon issue d'ouverte sur le dépôt de la documentation
    > des utilitaires réseaux de Microsoft.

    En plus de simplement faire de la documentation, j'ai mis en pratique ce que j'ai
    appris en appliquant les commandes sur mon propre ordinateur car il était sous Windows
    au moment de cette SAE. Cela m'a d'ailleurs bien aidé et m'a permit de me familiariser
    avec l'administration réseau sur Windows.

  - Dans le cadre de la SAE-21, j'ai du interconnecter des machines dans des VLANs différents
    de manière dynamique, c'est à dire avec un DHCP, à moins que quelqu'un préfère le système
    APIPA à un DHCP, mais je doute qu'en standalone ce soit un choix très judicieux dans la plupart des cas.

    J'ai du créer un pool par VLAN sur le routeur par défaut en spécifiant un pool par sous-interface
    afin que chaque VLAN ait son pool d'adresses et sa gateway par défaut.

    En ce qui concerne le DNS, j'ai, au départ, configuré un DNS dans le réseau privé de l'entreprise
    ayant comme vocation d'être un DNS-relay mais il s'est avéré impossible de la faire avec Cisco
    Packet Tracer, ainsi donc, tous les FQDN ont été centralisés en un seul serveur DNS et son adresse
    IP a été insérée dans la configuration de chaque bails du serveur DHCP.

  </details>

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
