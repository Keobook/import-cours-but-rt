---
Author: Alexis Opolka
Subject: Cloud - Kernel Virtualization Machine
Company: IUT de Béziers
Copyright: All Rights Reserved
---

## 4 - Création de machines virtuelles K-VMs

1. ### 4.1 - Création de VMs avec virt manager

    On active le service `serial-getty`:

    ```sh
    systemctl enable serial-getty@ttyS0
    systemctl start serial-getty@ttyS0
    ```

    > **Note:**  
    > J'ai installé une VM Centos-8 (`CentOS-Stream-8-20230429.0-x86_64-dvd1.iso`).

    1. Récupérez des informations sur le node KVM depuis le `shell`.

        Pour récupérer des informations sur le node KVM, on peut faire:

        ```sh
        virsh nodeinfo
        ```

        ce qui nous donne:

        ```txt
        CPU model:           x86_64
        CPU(s):              12
        CPU frequency:       1898 MHz
        CPU socket(s):       1
        Core(s) per socket:  6
        Thread(s) per core:  2
        NUMA cell(s):        1
        Memory size:         15772444 KiB
        ```

    2. Listez les domaines (comprendre les K-VMs) actifs de votre noeud Kvm.

        Pour lister les domaines actifs, on peut faire:

        ```sh
        virsh list --state-running
        ```

        Ce qui nous donne:

        ```txt
        Id   Name                 State
        ------------------------------------

        2    cloud-vm1-centos-8   running
        ```

    3. Listez les domaines actifs et inactifs de votre noeud Kvm.

        - Pour lister les domaines actifs, nous pouvons simplement faire:

          ```sh
          virsh list
          ```

          ou

          ```sh
          virsh list --state-running
          ```

        - Pour lister les domaines inactifs, nous pouvons faire:

          ```sh
          virsh list --inactive
          ```

          Ce qui nous donne:

          ```txt
          Id   Name       State

          ---------------------------

          - debian11   shut off
          ```

    4. Démarrez la K-VM

        Pour démarrer la K-VM, nous pouvons faire:

        ```sh
        virsh start <domain-URI>
        ```

        Où l'on reçoit simplement le message suivant:

        ```txt
        Domain '<domain-URI>' started
        ```

        > **Note:**  
        > On peut vérifier en faisant:
        >
        > ```sh
        > virsh list
        > ```
        >
        > Et voir que notre domain a maintenant l'état de lancé:
        >
        > Si l'on lance mon domaine `debian11`, on obtient:
        >
        > ```sh
        > (base) centaurus@centaurustasie:~1$ sudo virsh start debian11
        >
        > Domain 'debian11' started
        >
        > (base) centaurus@centaurustasie:~$ sudo virsh list
        > Id   Name                 State
        > ------------------------------------
        >
        > 2    cloud-vm1-centos-8   running
        > 3    debian11             running
        >```

    5. Faites en sorte que cette K-VM démarre automatiquement au démarrage de l'hôte.

        Pour démarrer automatiquement une K-VM au démarrage de la machine hôte, on peut faire:

        ```sh
        virsh autostart <domain-URI>
        ```

        > **Note:**  
        > Pour désactiver l'`autostart`, on peut faire:
        >
        > ```sh
        > virsh autostart --disable <domain-URI>
        > ```

    6. Récupérez des informations sur la K-VM (en interrogeant son "domain").

        Pour récupérer des informations sur la K-VM, on peut faire:

        - Lister les blocs de stockage:

            ```sh
            virsh domblklist <domain-URI>
            ```

            Ce qui nous donne, dans le cas de `cloud-vm1-centos-8`:

            ```txt
            Target   Source
            ------------------------------------------------------------

            vda      /var/lib/libvirt/images/cloud-vm1-centos-8.qcow2
            sda      -
            ```

        - Statistiques des blocs de stockage:

            ```sh
            virsh domblkstat <domain-URI> <type> --human
            ```

            > **Note:**  
            > On utilise le paramètre `human` afin d'obtenir une sortie
            > qui est lisible et compréhensible par un humain.

            Ce qui nous donne, pour le `vda` de `cloud-vm1-centos-8`:

            ```txt
            Device: vda
            number of read operations:      27565
            number of bytes read:           1647045632
            number of write operations:     2737
            number of bytes written:        206557696
            number of flush operations:     552
            total duration of reads (ns):   5806104452
            total duration of writes (ns):  1909577486
            total duration of flushes (ns): 2540435358
            ```

        - Lister les interface Réseaux:

          Pour lister les interfaces réseaux de la K-VM, on peut faire:

          ```sh
          virsh domiflist <domain-URI>
          ```

          Ce qui nous donne, pour `cloud-vm1-centos-8`:

          ```txt
          Interface   Type      Source    Model    MAC
          -------------------------------------------------------------
            vnet1       network   default   virtio   52:54:00:4b:f7:a1
          ```

        - Statistiques d'une interface réseau:

          Pour obtenir les statistiques d'une interface réseau, on peut faire:

          ```sh
          virsh domifstat <domain-URI> <interface>
          ```

          Ce qui nous donne, pour `vnet1` de `cloud-vm1-centos-8`:

          ```txt
          vnet1 rx_bytes 682623
          vnet1 rx_packets 14358
          vnet1 rx_errs 0
          vnet1 rx_drop 0
          vnet1 tx_bytes 18515
          vnet1 tx_packets 112
          vnet1 tx_errs 0
          vnet1 tx_drop 0
          ```

        - Statistiques sur la mémoire de la K-VM

          Pour obtenir des statistiques sur la mémoire d'une KVM, on peut faire:

          ```sh
          virsh dommemstat <domain-URI>
          ```

          Ce qui nous donne, pour `cloud-vm1-centos-8`:

          ```txt
          actual 2097152
          swap_in 0
          swap_out 0
          major_fault 306
          minor_fault 140189
          unused 1605172
          available 1820504
          usable 1575820
          last_update 1699603428
          disk_caches 84288
          hugetlb_pgalloc 0
          hugetlb_pgfail 0
          rss 2098296
          ```

    7. Faites un "graceful shutdown" de la K-VM.
        Redémarrez là, puis forcez l'arrêt de la machine.

        Pour faire un graceful shutdown, on fait:

        ```sh
        virsh shutdown <domain-URI> --mode acpi
        ```

        On la redémarre en faisant:

        ```sh
        virsh start <domain-URI>
        ```

        > **Note:**  
        > Dans le cas d'un reboot pendant que le domaine est encore
        > actif, on peut faire:
        >
        > ```sh
        > virsh reboot <domain-URI> --mode <mode>
        > ```
        >
        > Le `mode` à préférer peut être `acpi`, d'après moi.

        On peut forcer l'arrêt de la machine en faisant:

        ```sh
        virsh destroy <domain-URI>
        ```

1. ### 4.2 - Création d'une K-VM Debian avec virt-install

    1. Bâtissez une K-VM Debian en utilisant la commande virt-install à partir d'une iso minimal et une console SPICE.

        Elle aura les caractéristiques suivantes:

         - 1 VCPU
         - 1024 Go de RAM
         - 5 Gigas de disque.

        On fait:

        ```sh
        virt-install \
          --name cloud-guest-alpine \
          --memory 1024 \
          --vcpus 1 \
          --disk size=5 \
          --cdrom ./src/.images/alpine-virt-3.18.4-x86_64.iso \
          --os-variant alpinelinux3.18
        ```

    1. Récupérer des informations sur la vm ( virsh dominfo/schedinfo/domifilist/domvlklist/vcpucount ...)

        - dominfo:

          ```txt
          Id:             1
          Name:           cloud-guest-alpine
          UUID:           a61d94ba-c57c-4a06-835c-c25d458a0c04
          OS Type:        hvm
          State:          running
          CPU(s):         1
          CPU time:       4.6s
          Max memory:     1048576 KiB
          Used memory:    1048576 KiB
          Persistent:     yes
          Autostart:      disable
          Managed save:   no
          Security model: none
          Security DOI:   0
          ```

        - domiflist:

          ```txt
           Interface   Type   Source   Model    MAC
          ---------------------------------------------------------
           - user   -        virtio   52:54:00:c2:c0:a7
          ```

        - domblkist:

          ```txt
           Target   Source
          ------------------------------------------------------------------------------------------------------------------------------------------
          vda      /home/centaurus/.local/share/libvirt/images/cloud-guest-alpine.qcow2
          sda      /home/centaurus/Documents/depots/iut-related/import-cours-but-rt/cours/modules/Cloud/src/.images/alpine-virt-3.18.4-x86_64.iso
          ```

        - vcpucount:

          ```txt
          maximum      config         1
          maximum      live           1
          current      config         1
          current      live           1
          ```

    1. Attribuez à froid deux V-CPUs à cette K-VM.

      - On arrête d'abord la VM:

        ```sh
        virsh shutdown cloud-guest-alpine --mode acpi
        ```

      - On attribue deux VCPUs au domaine `cloud-guest-alpine`:

        ```sh
        virsh setvcpus cloud-guest-alpine 2 --maximum --config
        virsh setvcpus cloud-guest-alpine 2 --config
        ```

      - On relance la VM et on regarde les VCPUs alloués:

        ```sh
        virsh start cloud-guest-alpine
        virsh vcpucount cloud-guest-alpine
        ```

        Ce qui nous donne:

        ```txt
        maximum      config         2
        maximum      live           2
        current      config         2
        current      live           2
        ```

        On peut donc voir que nous avons bien attribué à froid deux V-CPUs à cette K-VM.

1. ### 4.3 - Création de VMs avec virt-builder

    1. virt-builder permet de créer rapidement une VM à partir d'une image téléchargée sans avoir à la construire.  
        Utilisez cette commande afin de personnaliser l'image de centos-8
        (taille 10G, password=root)[^1].  
        Utilisez-la ensuite pour créer une VM avec virt-manager à partir de cette image modifiée ou utilisez virt-install.

        On peut faire:

        ```sh
        virt-builder <linux-image> -o <output-file> --root-password <password-selector>:<password-argument> --size <filesize>
        ```

        Avec l'image `centos-8.0`, l'output en tant `test.img`, le `root-password` en tant que `password` et de la valeur `root`
        et une taille d'image de `10G`:

        ```sh
        virt-builder centos-8.0 -o test.img --root-password password:root --size 10G
        ```

        ```sh
        [   1.1] Downloading: <http://builder.libguestfs.org/centos-8.0.xz>
        [   1.9] Planning how to build this image
        [   2.0] Uncompressing
        [   5.3] Resizing (using virt-resize) to expand the disk to 10.0G
        [  41.6] Opening the new disk
        [  52.6] Setting a random seed
        [  52.6] Setting passwords
        [  53.6] SELinux relabelling
        [  69.2] Finishing off
                          Output file: test.img
                          Output size: 10.0G
                        Output format: raw
                    Total usable space: 9.3G
                            Free space: 8.1G (86%)
        ```

        On installe dès à présent la vm via `virt-install`:

        ```sh
        virt-install --name test-guest --memory 1024 --vcpus 1 --disk size=5 --cdrom ./test.img --os-variant centos8
        ```

        [^1]: On peut être ammenés à positionner la variable `LIBGUESTFS_BACKEND=direct`.

1. ### 4.4 - Création de VMs avec virt-customize

    L'autre format de disque de VM est `qcow2`.

    1. Utilisez `virt-customize` afin de modifier l'image `qcow2` debian 11 avec un mot de passe `root`.  
        Utilisez-la ensuite pour créer une VM avec virt-manager à partir de cette image modifiée.

        On fait:

        ```sh
        virt-customize -a /var/lib/libvirt/images/debian11.qcow2 --root-password password:root
        ```

        Ce qui nous donnne:

        ```sh
        [   0.0] Examining the guest ...
        [  16.5] Setting a random seed
        [  16.5] Setting passwords
        [  17.5] SELinux relabelling
        [  17.6] Finishing off
        ```

        Puis pour créer une VM à partir de cette image modifiée:

        ```sh
        virt-install --name debian11.1 --ram 2048 --vcpus 2 --disk path=/var/lib/libvirt/images/debian11.qcow2,size=10 --graphics spice --osinfo debian11 --cdrom ./src/.images/debian-11.7.0-amd64-netinst.iso
        ```

## 5 - Découverte de l'architecture KVM

1. ### 5.1 - Gestion du réseau

    1. Listez les bridges virtuels de la machine avec brctl et virsh ?
        Quel est le nom du bridge utilisé par la K-VM Debian créée précédemment ?

        - Avec `virsh`:

          - Lister les réseaux

              ```sh
              virsh net-list
              ```

              Ce qui nous donne:

              ```txt
              Name      State    Autostart   Persistent
              --------------------------------------------
              default   active   yes         yes
              ```

          - Avoir plus de détails sur un réseau en question:

              ```sh
              virsh net-dumpxml <network-name>
              ```

              Ce qui nous donne, avec `default`:

              ```xml
              <network>
                <name>default</name>
                <uuid>2643e40d-0448-4529-b5f2-07f2cfc022d6</uuid>
                <forward mode='nat'>
                  <nat>
                    <port start='1024' end='65535'/>
                  </nat>
                </forward>
                <bridge name='virbr0' stp='on' delay='0'/>
                <mac address='52:54:00:d6:18:d1'/>
                <ip address='192.168.122.1' netmask='255.255.255.0'>
                  <dhcp>
                    <range start='192.168.122.2' end='192.168.122.254'/>
                  </dhcp>
                </ip>
              </network>
              ```

        - Avec `brctl`:

          > **Note:**  
          > `brctl` du paquet `bridge-utils` est déprécié,
          > voir les notes du `manpages` [disponible pour Debian](https://manpages.debian.org/testing/bridge-utils/brctl.8.en.html).

          On peut faire:

          ```sh
          ip link show type bridge
          ```

          Ce qui nous donne:

          ```txt
          4: mpqemubr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default qlen 1000
              link/ether 52:54:00:60:f6:b1 brd ff:ff:ff:ff:ff:ff
          6: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default qlen 1000
              link/ether 52:54:00:d6:18:d1 brd ff:ff:ff:ff:ff:ff
          7: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
              link/ether 02:42:ce:48:10:59 brd ff:ff:ff:ff:ff:ff
          8: br-2df60dc5cd5a: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
              link/ether 02:42:92:b5:9f:c5 brd ff:ff:ff:ff:ff:ff
          9: br-91e058177582: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
              link/ether 02:42:2b:07:a0:5f brd ff:ff:ff:ff:ff:ff
          10: br-ead98bf895a1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
              link/ether 02:42:d0:56:fc:a1 brd ff:ff:ff:ff:ff:ff
          ```

          On retrouve bien notre réseau `default` détecté avec `virsh`:

          ```txt
          6: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default qlen 1000
              link/ether 52:54:00:d6:18:d1 brd ff:ff:ff:ff:ff:ff
          ```

    2. Faites un petit schéma de l'accès de la K-VM au réseau de la salle.
        Quel est le principe apppliqué et l'outil utilisé par KVM pour metre en oeuvre cet accès au réseau.

        ```mermaid
        flowchart LR

        vm[K-VM] --- h[host]
        h --- ext[External Network]

        ```

    3. Créez un nouveau bridge appelé `monbridge`.
        Pour cela "dumpez" la configuration du "défault network" afin de générer un nouveau fichier et modifiez-le afin de créer le nouveau réseau.

        On dump la configuration par défaut:

        ```sh
        virsh net-dumpxml default > ./new-default.xml
        ```

        Pour créer un nouveau réseau, on fait:

        ```sh
        virsh net-create ./new-default.xml
        ```

        > **Note:**  
        > On doit modifier les valeurs suivantes:
        >
        > - name
        > - uuid
        > - bridge:name
        > - ip:address
        > - ip.dhcp.range:start et ip.dhcp.range:end

    4. Rattachez la K-VM Debian à monBridge.

        Pour rattacher la K-VM Debian à `monbridge`, on peut faire:

        ```sh
        virsh edit <domain-URI>
        ```

        puis pour vérifier, on peut faire:

        ```sh
        virsh domiflist debian11
        ```

        Ce qui nous donne:

        ```txt
         Interface   Type      Source      Model    MAC
        ---------------------------------------------------------------
         vnet4       network   monbridge   virtio   52:54:00:a1:b6:2f
        ```

        La debian a bien changé de réseaux.

    5. Créez deux K-VMs en la rattachant à des interfaces macvtap.
        Explorez les différents modes de ce type de réseau.

        On fait:

        ```sh
        virsh net-define ./macvtap-def.xml
        virsh net-start macvtap-net
        ```

        On fait ensuite:

        ```sh
        virt-install --name netguest-1 --memory 1536 --vcpus 1 --disk size=5 --cdrom ./test.img --os-variant centos8 --network network:macvtap-net,model=virtio;
        virt-install --name netguest-2 --memory 1536 --vcpus 1 --disk size=5 --cdrom ./test.img --os-variant centos8 --network network:macvtap-net,model=virtio
        ```

1. ### 5.2 - Migration d'une K-VM d'un noeud KVM à l'autre

    Créez une nouvelle VM dans VMWareWorkstation ainsi qu'une nouvelle K-VM bâtie sur le pool de
    stockage NFS v4. Avec l'aide de virt-manager migrez la K-VM d'un noeud à l'autre.
    Vos VMs doivent être mises à l'heure avec le protocole NTP indispensable pour NFS.

    Avant tout, on crée notre VM qui nous servira de serveur NFS:

    ```sh
    virt-install \
      --name nfs-server \
      --memory 1024 \
      --vcpus 1 \
      --disk size=5 \
      --cdrom ./src/.images/CentOS-Stream-8-20230429.0-x86_64-dvd1.iso \
      --os-variant alpinelinux3.18
    ```

    On suit le tutoriel suivant: [linuxize.com](https://linuxize.com/post/how-to-install-and-configure-an-nfs-server-on-centos-8/)

    - Installation du serveur NFS (CentOS 8):

        ```sh
        sudo dnf install nfs-utils
        sudo systemctl enable --now nfs-server
        sudo cat /proc/fs/nfsd/versions
        sudo mkdir -p /srv/nfs4/{backups,www}
        sudo mount --bind /opt/backups /srv/nfs4/backups
        sudo mount --bind /var/www /srv/nfs4/www
        sudo exportfs -ra

        ### Firewall
        sudo firewall-cmd --new-zone=nfs --permanent
        sudo firewall-cmd --zone=nfs --add-service=nfs --permanent
        sudo firewall-cmd --zone=nfs --add-source=10.202.0.0/16 --permanent
        sudo firewall-cmd --reload
        ```

    - Installation du client NFS (Debian 11):

        ```sh
        sudo apt-get install nfs-common
        sudo mkdir -p /nfs/www
        sudo mount -t nfs -o vers=4 10.202.0.106:/backups /nfs/backups
        ```

    Après cela, nous faisons la migration:

1. ### 5.3 - Clonage d'une K-VM et gestion du stockage

    1. Listez les pools de la machine.

        ```sh
        virsh pool-list
        ```

    1. Créer un clone

        ```sh
        virt-clone
        ```

    1. Créer un nouveau disque

        ```sh
        sudo qemu-img create -f raw test 2G
        ```

## 6 - Utilisation de KClI

kcli est un package Python qui p ermet d'automatiser la gestion des K-VMs.

1. En vous inspirant de la documentation suivante [karmab/kcli](https://github.com/karmab/kcli) utilisez-le p our manipuler une VM debian9.

    - On installe kcli:

        ```sh
        curl -s https://raw.githubusercontent.com/karmab/kcli/main/install.sh | bash
        ```

    - On met en place les permissions pour lui permettre de créer des VMs:

        ```sh
        sudo setfacl -m u:centaurus:rwx /var/lib/libvirt/images
        ```

    - On installe une VM:

        ```sh
        kcli create vm -i debian11 testvm
        ```

    > **Note:**  
    > On peut créer une VM vide:
    >
    > ```sh
    > kcli local create vm -P uefi=true -P start=false -P memory=20480 -P numcpus=16 -P disks=[50,50] -P nets=[default] empty-me
    > ```

> **Note:**  
> Voici des liens de documentation intéressants:
>
> - [libguestfs/virt-builder](https://libguestfs.org/virt-builder.1.html)

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
