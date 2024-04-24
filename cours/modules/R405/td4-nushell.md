# R405 - NuShell in nutshell

On installe NuShell:

```sh
curl https://sh.rustup.rs -sSf | sh # On installe Rust, pour l'installation WSL, voir:https://www.rust-lang.org/tools/install
source $HOME/.cargo/env
cargo install nu --all-features
cargo install nu_plugin_formats
sudo apt install jq jc
```

## Utilisation du flux d'entrée de la commande ss

> [!NOTE]
> Pour en savoir plus sur les filtre NuShell, voir [ici](https://www.nushell.sh/commands/categories/filters.html).

1. "Parsez" le résultat de la commande `ss -tunlp` afin de créer une table des connections tcp et udp

    On fait:

    ```sh
      ss -tunlp | jc --ss | jq '.[]' | from json
    ```

    nous donnant:

    ```json
    {
      "netid": "udp",
      "state": "UNCONN",
      "recv_q": 0,
      "send_q": 0,
      "local_address": "127.0.0.53",
      "local_port": "53",
      "peer_address": "0.0.0.0",
      "peer_portprocess": "*",
      "interface": "lo",
      "local_port_num": 53
    }
    ```

    On peut aussi faire:

    ```sh
    ss -tunlp | jc --ss | from json
    ```

    nous donnant:

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬───────────────┬────────────┬──────────────┬──────────────────┬───────────┬────────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ local_address │ local_port │ peer_address │ peer_portprocess │ interface │ local_port_num │
    ├───┼───────┼────────┼────────┼────────┼───────────────┼────────────┼──────────────┼──────────────────┼───────────┼────────────────┤
    │ 0 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.53    │ 53         │ 0.0.0.0      │ *│ lo        │             53 │
    │ 1 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.1     │ 323        │ 0.0.0.0      │*                │    ❎     │            323 │
    │ 2 │ udp   │ UNCONN │      0 │      0 │ [::1]         │ 323        │ [::]         │ *│    ❎     │            323 │
    │ 3 │ tcp   │ LISTEN │      0 │   4096 │ 127.0.0.53    │ 53         │ 0.0.0.0      │*                │ lo        │             53 │
    ╰───┴───────┴────────┴────────┴────────┴───────────────┴────────────┴──────────────┴──────────────────┴───────────┴────────────────╯
    ```

2. Rejetez la colonne "peer_portprocess"

    Pour rejeter la colonne `peer_portprocess`, on fait:

    ```sh
    ss -tunlp | jc --ss | jq '.[]|del(.peer_portprocess)'
    ```

    nous donnant:

    ```json
    {
      "netid": "udp",
      "state": "UNCONN",
      "recv_q": 0,
      "send_q": 0,
      "local_address": "127.0.0.53",
      "local_port": "53",
      "peer_address": "0.0.0.0",
      "interface": "lo",
      "local_port_num": 53
    }
    ```

    On peut aussi faire:

    ```sh
    ss -tunlp | jc --ss | from json | reject peer_portprocess
    ```

    nous donnant:

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬───────────────┬────────────┬──────────────┬───────────┬────────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ local_address │ local_port │ peer_address │ interface │ local_port_num │
    ├───┼───────┼────────┼────────┼────────┼───────────────┼────────────┼──────────────┼───────────┼────────────────┤
    │ 0 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.53    │ 53         │ 0.0.0.0      │ lo        │             53 │
    │ 1 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.1     │ 323        │ 0.0.0.0      │    ❎     │            323 │
    │ 2 │ udp   │ UNCONN │      0 │      0 │ [::1]         │ 323        │ [::]         │    ❎     │            323 │
    │ 3 │ tcp   │ LISTEN │      0 │   4096 │ 127.0.0.53    │ 53         │ 0.0.0.0      │ lo        │             53 │
    ╰───┴───────┴────────┴────────┴────────┴───────────────┴────────────┴──────────────┴───────────┴────────────────╯
    ```

3. Triez par port d'écoute local ascendant

    Pour trier par port d'écoute local ascendant, on fait:

    ```sh
    ss -tunlp | jc --ss | jq 'sort_by(.local_port_num)' | from json
    ```

    nous donnant:

    ```json
    [
      {
        "netid": "udp",
        "state": "UNCONN",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "127.0.0.53",
        "local_port": "53",
        "peer_address": "0.0.0.0",
        "peer_portprocess": "*",
        "interface": "lo",
        "local_port_num": 53
      },
      {
        "netid": "tcp",
        "state": "LISTEN",
        "recv_q": 0,
        "send_q": 4096,
        "local_address": "127.0.0.53",
        "local_port": "53",
        "peer_address": "0.0.0.0",
        "peer_portprocess": "*",
        "interface": "lo",
        "local_port_num": 53
      },
      {
        "netid": "udp",
        "state": "UNCONN",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "127.0.0.1",
        "local_port": "323",
        "peer_address": "0.0.0.0",
        "peer_portprocess": "*",
        "local_port_num": 323
      },
      {
        "netid": "udp",
        "state": "UNCONN",
        "recv_q": 0,
        "send_q": 0,
        "local_address": "[::1]",
        "local_port": "323",
        "peer_address": "[::]",
        "peer_portprocess": "*",
        "local_port_num": 323
      }
    ]
    ```

    ou aussi

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬───────────────┬────────────┬──────────────┬──────────────────┬───────────┬────────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ local_address │ local_port │ peer_address │ peer_portprocess │ interface │ local_port_num │
    ├───┼───────┼────────┼────────┼────────┼───────────────┼────────────┼──────────────┼──────────────────┼───────────┼────────────────┤
    │ 0 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.53    │ 53         │ 0.0.0.0      │ *│ lo        │             53 │
    │ 1 │ tcp   │ LISTEN │      0 │   4096 │ 127.0.0.53    │ 53         │ 0.0.0.0      │*                │ lo        │             53 │
    │ 2 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.1     │ 323        │ 0.0.0.0      │ *│    ❎     │            323 │
    │ 3 │ udp   │ UNCONN │      0 │      0 │ [::1]         │ 323        │ [::]         │*                │    ❎     │            323 │
    ╰───┴───────┴────────┴────────┴────────┴───────────────┴────────────┴──────────────┴──────────────────┴───────────┴────────────────╯
    ```

4. N'affichez que les 5 premières lignes

    Pour n'afficher que les 5 première lignes, on fait:

    ```sh
    ss -tunlp | jc --ss | from json | first 5
    ```

    nous donnant:

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬───────────────┬────────────┬──────────────┬──────────────────┬───────────┬────────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ local_address │ local_port │ peer_address │ peer_portprocess │ interface │ local_port_num │
    ├───┼───────┼────────┼────────┼────────┼───────────────┼────────────┼──────────────┼──────────────────┼───────────┼────────────────┤
    │ 0 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.53    │ 53         │ 0.0.0.0      │ *│ lo        │             53 │
    │ 1 │ udp   │ UNCONN │      0 │      0 │ 127.0.0.1     │ 323        │ 0.0.0.0      │*                │    ❎     │            323 │
    │ 2 │ udp   │ UNCONN │      0 │      0 │ [::1]         │ 323        │ [::]         │ *│    ❎     │            323 │
    │ 3 │ tcp   │ LISTEN │      0 │   4096 │ 127.0.0.53    │ 53         │ 0.0.0.0      │*                │ lo        │             53 │
    ╰───┴───────┴────────┴────────┴────────┴───────────────┴────────────┴──────────────┴──────────────────┴───────────┴────────────────╯
    ```

5. Ne sélectionnez que les connexions tcp

    On peut faire:

    ```sh
    ss -tunlp | jc --ss | jq 'sort_by(.local_port_num)' | from json| where $it.netid == tcp
    ```

    nous donnant:

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬───────────────┬────────────┬──────────────┬──────────────────┬───────────┬────────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ local_address │ local_port │ peer_address │ peer_portprocess │ interface │ local_port_num │
    ├───┼───────┼────────┼────────┼────────┼───────────────┼────────────┼──────────────┼──────────────────┼───────────┼────────────────┤
    │ 0 │ tcp   │ LISTEN │      0 │   4096 │ 127.0.0.53    │ 53         │ 0.0.0.0      │ *                │ lo        │             53 │
    ╰───┴───────┴────────┴────────┴────────┴───────────────┴────────────┴──────────────┴──────────────────┴───────────┴────────────────╯
    ```

6. Sélectionnez avec "get" uniquement la variable `local_port_num` et triez les.
  Quel est le type de données retournées ? Sommez les numéros de ports entre eux.

    On fait:

    ```sh
    ss -tunlp | jc --ss | jq 'sort_by(.local_port_num)' | from json| get local_port_num | sort
    ```

    Nous donnant:

    ```sh
    ╭───┬─────╮
    │ 0 │  53 │
    │ 1 │  53 │
    │ 2 │ 323 │
    │ 3 │ 323 │
    ╰───┴─────╯
    ```

    Les données retournées sont des entiers et la structure les contenant est un tableau contenant l'indice d'apparition de la valeur.  
    Nous avons le port `53` et `323` qui nous sont notamment retournés.

7. Sans conserver les filtres précédents, créez une nouvelle table avec uniquement les colonnes `netid`, `local_address`, `local_port`.
  En déduire la différence entre "get" et "select" appliquée à une table.

     - Avec `get`, on peut faire:

        ```sh
        ss -tunlp | jc --ss | from json | get netid local_address local_port
        ```

        nous donnant:

        ```sh
        ╭───┬────────────────────╮
        │ 0 │ ╭───┬─────╮        │
        │   │ │ 0 │ udp │        │
        │   │ │ 1 │ udp │        │
        │   │ │ 2 │ udp │        │
        │   │ │ 3 │ tcp │        │
        │   │ ╰───┴─────╯        │
        │ 1 │ ╭───┬────────────╮ │
        │   │ │ 0 │ 127.0.0.53 │ │
        │   │ │ 1 │ 127.0.0.1  │ │
        │   │ │ 2 │ [::1]      │ │
        │   │ │ 3 │ 127.0.0.53 │ │
        │   │ ╰───┴────────────╯ │
        │ 2 │ ╭───┬─────╮        │
        │   │ │ 0 │ 53  │        │
        │   │ │ 1 │ 323 │        │
        │   │ │ 2 │ 323 │        │
        │   │ │ 3 │ 53  │        │
        │   │ ╰───┴─────╯        │
        ╰───┴────────────────────╯
        ```

     - Avec `select`, on peut faire:

        ```sh
        ss -tunlp | jc --ss | from json | select netid local_address local_port
        ```

        nous donnant:

        ```sh
        ╭───┬───────┬───────────────┬────────────╮
        │ # │ netid │ local_address │ local_port │
        ├───┼───────┼───────────────┼────────────┤
        │ 0 │ udp   │ 127.0.0.53    │ 53         │
        │ 1 │ udp   │ 127.0.0.1     │ 323        │
        │ 2 │ udp   │ [::1]         │ 323        │
        │ 3 │ tcp   │ 127.0.0.53    │ 53         │
        ╰───┴───────┴───────────────┴────────────╯
        ```

      On peut donc dire que `get` nous permet d'obtenir sous forme de liste/tableau les occurences et les valeurs
      d'une ou plusieurs colonnes au contraire de `select` qui nous permet d'obtenir, dans le cas d'un tableau,
      la clé ainsi que ses valeurs, nous donnant ainsi deux types de tableaux différents.

8. Utilisez la commande "each" et la liste des ports numériques pour lancer un scan nmap sur les ports d'écoute de la machine locale.

    Pour utiliser `each` and `nmap`, on fait:

    ```sh
    ss -tunlp | jc --ss | from json | each {|e| sudo nmap -sS $e.local_address --source-port $e.local_port}
    ```

    Ce qui nous donne:

    ```sh
    [sudo] password for centaurus:
    ╭───┬──────────────────────────────────────────────────────────────────╮
    │ 0 │ Starting Nmap 7.80 ( <https://nmap.org> ) at 2024-04-24 08:29 CEST │
    │   │ Nmap scan report for 127.0.0.53                                  │
    │   │ Host is up (0.0000030s latency).                                 │
    │   │ Not shown: 999 closed ports                                      │
    │   │ PORT   STATE SERVICE                                             │
    │   │ 53/tcp open  domain                                              │
    │   │                                                                  │
    │   │ Nmap done: 1 IP address (1 host up) scanned in 1.16 seconds      │
    ╰───┴──────────────────────────────────────────────────────────────────╯
    Failed to resolve "[::1]".
    WARNING: No targets were specified, so 0 hosts scanned.
    ╭───┬──────────────────────────────────────────────────────────────────╮
    │ 1 │ Starting Nmap 7.80 ( <https://nmap.org> ) at 2024-04-24 08:29 CEST │
    │   │ Nmap scan report for localhost (127.0.0.1)                       │
    │   │ Host is up (0.0000040s latency).                                 │
    │   │ All 1000 scanned ports on localhost (127.0.0.1) are closed       │
    │   │                                                                  │
    │   │ Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds      │
    │ 2 │ Starting Nmap 7.80 ( <https://nmap.org> ) at 2024-04-24 08:29 CEST │
    │   │ Nmap done: 0 IP addresses (0 hosts up) scanned in 0.02 seconds   │
    │ 3 │ Starting Nmap 7.80 ( <https://nmap.org> ) at 2024-04-24 08:29 CEST │
    │   │ Nmap scan report for 127.0.0.53                                  │
    │   │ Host is up (0.0000030s latency).                                 │
    │   │ Not shown: 999 closed ports                                      │
    │   │ PORT   STATE SERVICE                                             │
    │   │ 53/tcp open  domain                                              │
    │   │                                                                  │
    │   │ Nmap done: 1 IP address (1 host up) scanned in 1.16 seconds      │
    ╰───┴──────────────────────────────────────────────────────────────────╯
    ```

9. Créez une nouvelle colonne constituée de l'adresse `IP:PORT`. Rejetez les colonnes d'origine.

    Pour créer une nouvelle colonne, on fait:

    ```sh
    ss -tunlp | jc --ss | from json | insert "local IP:PORT" {|row| $row.local_address + ":" + $row.local_port} | reject local_address local_port local_port_num
    ```

    nous donnant:

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬──────────────┬──────────────────┬───────────┬───────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ peer_address │ peer_portprocess │ interface │ local IP:PORT │
    ├───┼───────┼────────┼────────┼────────┼──────────────┼──────────────────┼───────────┼───────────────┤
    │ 0 │ udp   │ UNCONN │      0 │      0 │ 0.0.0.0      │ *│ lo        │ 127.0.0.53:53 │
    │ 1 │ udp   │ UNCONN │      0 │      0 │ 0.0.0.0      │*                │    ❎     │ 127.0.0.1:323 │
    │ 2 │ udp   │ UNCONN │      0 │      0 │ [::]         │ *│    ❎     │ [::1]:323     │
    │ 3 │ tcp   │ LISTEN │      0 │   4096 │ 0.0.0.0      │*                │ lo        │ 127.0.0.53:53 │
    ╰───┴───────┴────────┴────────┴────────┴──────────────┴──────────────────┴───────────┴───────────────╯
    ```

10. Exportez au format csv votre dernière table et re-importer la ensuite afin de créer une nouvelle table.

    Pour exporter à un format donné, on fait:

    ```sh
    to <format>
    ```

    nous donnant, dans notre cas, la commande suivante:

    ```sh
    ss -tunlp | jc --ss | from json | insert "local IP:PORT" {|row| $row.local_address + ":" + $row.local_port} | reject local_address local_port local_port_num | to csv
    ```

    avec le résultat suivant:

    ```csv
    netid,state,recv_q,send_q,peer_address,peer_portprocess,interface,local IP:PORT
    udp,UNCONN,0,0,0.0.0.0,*,lo,127.0.0.53:53
    udp,UNCONN,0,0,0.0.0.0,*,,127.0.0.1:323
    udp,UNCONN,0,0,[::],*,,[::1]:323
    tcp,LISTEN,0,4096,0.0.0.0,*,lo,127.0.0.53:53
    ```

    On import ensuite le CSV pour former un tableau:

    ```sh
    ss -tunlp | jc --ss | from json | insert "local IP:PORT" {|row| $row.local_address + ":" + $row.local_port} | reject local_address local_port local_port_num | to csv | from csv
    ```

    nous donnant un résultat final tel que:

    ```sh
    ╭───┬───────┬────────┬────────┬────────┬──────────────┬──────────────────┬───────────┬───────────────╮
    │ # │ netid │ state  │ recv_q │ send_q │ peer_address │ peer_portprocess │ interface │ local IP:PORT │
    ├───┼───────┼────────┼────────┼────────┼──────────────┼──────────────────┼───────────┼───────────────┤
    │ 0 │ udp   │ UNCONN │      0 │      0 │ 0.0.0.0      │ *│ lo        │ 127.0.0.53:53 │
    │ 1 │ udp   │ UNCONN │      0 │      0 │ 0.0.0.0      │*                │           │ 127.0.0.1:323 │
    │ 2 │ udp   │ UNCONN │      0 │      0 │ [::]         │ *│           │ [::1]:323     │
    │ 3 │ tcp   │ LISTEN │      0 │   4096 │ 0.0.0.0      │*                │ lo        │ 127.0.0.53:53 │
    ╰───┴───────┴────────┴────────┴────────┴──────────────┴──────────────────┴───────────┴───────────────╯
    ```

## Interrogation d'une base de données sqlite avec NuShell et questions diverses

1. Ouvrez la base de données Nushell

    Pour ouvrir la base de données Nushell, on fait:

    ```sh
    ```

    > [!NOTE]
    > Pour plus d'informations sur les bases de données NuShell, voir [ici](https://www.nushell.sh/commands/categories/database.html).

2. Récupérez son schéma.
    Quel est le nombre de table SQL dans cette base de données ?

    s

3. Afficher la table "actor" avec NuShell.
4. Quel est le nombre d'acteurs (utilisez une requête SQL) ?
5. Quel et le nimbre d'acteurs dont le nom commence par `N` ?
6. Quelle est la taille cumulée des fichiers de votre user test ?
7. Quel est le moteur du serveur web du site scodoc.iutbeziers.fr et sa version ?
