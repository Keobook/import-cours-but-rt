---
Author: Alexis Opolka
Copyright: All Rights Reserved
Subject: Spécialisation Cloud
Company: IUT de Béziers
---

# BUT-RT2 - Spécialisation Cloud

Cloud / On-Premise

FinOps -> Coûts du projet

On doit:

- Virtualiser
- Containeriser

## La virtualisation

Ça date des années 80.

- Améliorer le taux d'occupation des serveurs et des équipements
- S'isoler de l'architecture physique (rester sur une version ancienne, ex: Redhat AS7, avec de nouveaux équipements)
- Une façon de gérer la haute disponibilité, la répartition de charge et la sécurité. PRA et PCA
- Faire du provisionning
- [PowerCLI (VMWare)](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-F02D0C2D-B226-4908-9E5C-2E783D41FE2D.html)

Il faut toujours prendre 3 machines physiques (voir petite) plus
que 2 machines (plus moyennes).

> **Note:**  
> On appelle ça de l'analyse marginale.

### Les limites de la virtualisation

- ROI pas si évident que ça
- Perf
- Complexité
- Couts (pour 100k€ de machines, 100k€ de licences)

### Deux types de virtualisation

> **Warning:**  
> La containerisation n'est pas de la virtualisation.

- L'hyperviseur (VmWare, KVM, Wen, Hyper V)
- Un hyperviseur repose soit sur le Kernel Linux soit sur un Kernel durcit dit bare-metal

| Hyperviseur                                                       | Container                                                                                                               |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Un machine hôte supporte l'hyperviseur qui gère les VM et devices | Un kernel qui gère les processus, on a une "illusion" d'une machine indépendante                                        |
| Chaque VM à son OS                                                | Chaque container partage le même kernel, fonctionne sur le principe d'un chroot, isolement graĉes aux briques du kernel |

Dans les container (et dans le cloud), on parle de serveurs multi-tenants.

### Virtio

### Libvirt

- Virsh
- Spice

## La containerisation

Les containers apportent de la sécurité.

On peut faire tourner des VMs dans des containers.

## Le cloud

- ### Cloud Public

  AWS/GCP/Azure -> infrastructure partagée par tout le monde

- ### Managed Cloud Services

  Infrastructure gérée par le Provider

- ### Services Sécurité Cloud

- ### Hosting et Cloud Privé

  Payement par Compute en interne

- ### Transformation Cloud

  Architecte (AWS) -> migration On-Premise -> Cloud

Dites bonjour au SRE

Le kernel n'est pas porté par le conteneur.
Observability
Platform Engineering

- On-demand self-service
- Broad Network access
- Resource pooling
- Rapid elasticity
- Measured service

La IAM est une des caractéristiques du cloud.

## Build & Run

IaC

Capex --> Investissement --> Coûts fixes
Lopex --> Coûts variables

## TDs

!!!include(./cloud-td1.md)!!!

## TPs

!!!include(./cloud-tp1.md)!!!

!!!include(./cloud-tp2.md)!!!

## Virtualisation

- Deux parties:

  - Processeur
  - Hyperviseur

Kernel-Space / User-Space

Hyperviseur va traîter les requêtes Kernel-Space de la VM
après les avoir reçues du CPU (qui les lui a transférées)

On peut être de base en `VM_NON_ROOT`, dans le cas d'exécution `Kernel-Space`
on fait une `VM_EXIT`[^1] puis on charge le contexte de l'hyperviseur.

[^1]: Process qui va nous permettre de save le contexte de la VM puis de le quitter

Afin d'utiliser des périphériques, on crée un buffer FIFO/FILO bi-directionnel permettant
de transférer les paquets/instructions entre la VM et l'Hyperviseur.

Sur KVM, le paquet permettant de créer les buffers, est `virt-io`,
sur VmWare, c'est `VM Tools`.

En ce qui concerne la mémoire, le processus ne connait qu'une adresse
mémoire, elle est ensuite indexée dans une table `PT` (Patch Table) afin d'obtenir
l'adresse physique.  
Il existe une `TLB` afin de cacher le process et d'accélerer le tout.

Dans le cas de la virtualisation, on translate cette notion vers l'hyperviseur,
on utilise d'ailleurs le `IOMMU` dans ce process.

En ce qui concerne les flux réseaux, sur les serveurs il existe les SRIOV
(on virtualise les cartes réseaux). <-- Meilleures performances

Avec NPAR, on peut diviser la bande passante.

L'hyperviseur fait du Ballooning (Gonfler un "ballon" afin de récupérer de
la RAM non utilisée par un process mais par un cache).  
C'est conditionnel à l'inactivité d'une VM.
