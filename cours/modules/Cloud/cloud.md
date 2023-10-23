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

## [TD 1](./cloud-td1.md)

## [TP 1](./cloud-td1.md)

## Copyright &copy; 2023 Alexis Opolka - All Rights Reserved
