# Wifi mesh

## TD sur le wifi

1.  Après s'être connecté au raspberry-pi via ssh, on peut trouver notre interface réseau.

```sh
iw phy1 info | grep mesh
```

On a comme sortie:

![mesh-support](./src/mesh-support.png)

On peut donc utiliser le mode vu q'il apparaît comme supporté.

2. On peut ensuite scanner les canaux utilisés

```sh
ip link set state down dev wlan1
iw wlan1 set type mesh
ip link set state up dev wlan1
sudo iw wlan1 scan | grep Primary
```

4. On joint ensuite le réseau mesh

```sh
iw wlan1 mesh join rtbz
```
5. On peut dump les différentes stations connectées

```sh
iw wlan1 station dump
```

Et les chemins

```sh
iw wlan1 mpath dump
```

7. Pour capturer les paquets 802.11, on fait :

```sh
sudo ifconfig wlan1 promisc
sudo tcpdump -i wlan1 -e -v --monitor-mode | tee monitor-wifimesh.log | grep 802.11
```

On a en sortie:

![capture-802_11](./src/capture-802_11.png)

## TP sur le wifi et un ESP


