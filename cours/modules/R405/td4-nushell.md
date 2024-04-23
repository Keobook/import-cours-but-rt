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

3. Triez par port d'écoute local ascendant

    Pour trier par port d'écoute local ascendant, on fait:

    ```sh
    ss -tunlp | jc --ss | jq 'sort_by(.local_port_num)'
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

4. N'affichez que les 5 premières lignes

    Pour n'afficher que les 5 première lignes, on fait:

    ```sh
    ss -tunlp | jc --ss | from json | first 5
    ```

5. Ne sélectionnez que les connexions tcp
6. Sélectionnez avec "get" uniquement la variable `local_port_num` et triez les.
  Quel est le type de données retournées ? Sommez les numéros deports entre eux.
7. Sans conserver les filtres précédents, créez une nouvelle table avec uniquement les colonnes "netid" `local_address_local_port`.
  En déduire la différence entre "get" et "select" appliquée à une table.
8. Utilisez la commande "each" et la liste des ports numériques pour lancer un scan nmap sur les ports d'écoute de la machine locale.
9. Créez une nouvelle colonne constituée de l'adresse `IP:PORT`. Rejetez les colonnes d'origine.
10. Exportez au format csv votre dernière table et re-importer la ensuite afin de créer une nouvelle table.
