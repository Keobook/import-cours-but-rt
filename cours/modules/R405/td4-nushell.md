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

8. Utilisez la commande "each" et la liste des ports numériques pour lancer un scan nmap sur les ports d'écoute de la machine locale.

9. Créez une nouvelle colonne constituée de l'adresse `IP:PORT`. Rejetez les colonnes d'origine.

10. Exportez au format csv votre dernière table et re-importer la ensuite afin de créer une nouvelle table.
