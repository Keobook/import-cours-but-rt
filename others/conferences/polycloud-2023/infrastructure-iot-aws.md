# Architecture pour l'IoT avec AWS et des cartes STM32 (Viveris)

de Nicolas Bruot

- Communication entre appareils IoT -> MQTT
- Architecture Cloud:
  - Serverless
  - AWS

## Problématiques de l'IoT

- en Temps réel
- Bcp de petits messages à traiter
- Transformation et analyse de données
- Diversité d'appareils
- Besoin de gérer la maintenance du parc

## Architecture d'ingestion et d'exposition de données de capteurs

- Collecter des données
- API REST
- Affichage en temps réel
- Archiver automatiquement les données anciennes

Contraintes:

- Architecture avec grande capacité d'ingestion
- IaC

STM32 B-U585I-IOT02A

Service Serverless : FaaS

Pas d'infrastructure à gérer
Scaling de zéro jusqu'aux pics de demande
S'il n'est pas utilisée -> 0 € / mois

DynamoDB en mode "on-demand capacity" est serverless

Services utilisés:

- IoT Core
- S3: Stockage
- Lambda: Calcul à la demande
- DynamoDB: SGBD
- API Gateway: Création de l'API
- Kinesis & Kinesis Data Firehose: Gestion de flux de données (Routeur et switch ?)

(site de démo)[iot.bruot.org]

### IoT Core

Service AWS
Connexion, authentification
Comm: MQTT, HTTPS

MQTT:

c'est un broker, de couche 7 OSI

### Lambda

Support de nombreux de langages

Déclemenchement par des événements
Intégration avec AWS CloudWatch native pour le logging

Elle va cacher du code si l'on appelle plusieurs fois la même fonction,
attention à l'initialisation à l'intérieur de fcts.

### DynamoDB

BD NoSQL clé-valeur adaptée au cloud
Latence <1ms; Supporte > 10 millions req/s

### AWS Kynesis

Collecte, traite et analyse les flux de données

Fait pour:

- Données en mouvment
- Petits, mais nombreux messages

On gère l'archivage via des TTLs, par DATETIME (ou TIMESTAMP), probablement.

### IaC

Déployer deux architectures similaires: dev et prod

Permet des modifications incrémentables

Outils:

- AWS CloudFormation
- AWS CDK + CloudFormation
- Terraform

C'est important d'utiliser de l'IaC
Les projets sont sur GitHub ! ^-^
