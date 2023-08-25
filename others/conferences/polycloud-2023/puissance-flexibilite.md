# Puissance et flexibilité du cloud - AWS

répartition mondiale des datacenters

- Le "on-premises": héberger le serveur physique par l'entreprise qui développe
- Le "cloud": On loue des serveurs chez un provider

IAAS: Infrastructure as a service
PAAS: Platform as a service
SAAS: Software as a service

AWS / Azure / GCP mais OVH / Scaleway

EC2 => VM dans la cloud

## AWS

Data -> Datalake -> Eposition (datalab) -> usages

Amazon S3 -> Scalable object storage

- Bucket -> Conteneur de stockage
- Object key -> Id de l'objet


AWS Glue -> Computing:

- Catalogue des données
- Jobs (Python)

AWS Athena -> SQL query sur des fichiers (Analytics):

On va utiliser un `crawler` afin de déterminer les données et leur index
dans un fichier de raw data.

On aura donc un schéma d'exécution tel que:

```txt
Raw data <- Crawler <- Glue <- Athena
```

Comment on s'en sert:

- Terraform
- console
- AWS SDK
- AWS CLI

On peut utiliser de l'ETL pour nettoyer des datasets
