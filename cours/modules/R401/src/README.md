---
Author: Alexis Opolka
Subject: Infrastructure de sécurité
---

# R401 - Infrastructure de sécurité

## TP 3 - Proxy

1. ### - Questions Préliminaires

    1. Rappelez quel est le rôle d'un proxy direct

        Le rôle d'un proxy direct est d'authentifier le traffic
        de clients du réseau comme étant originel de son adresse IP.

        Cela permet de masquer l'adresse des machines utilisateurs sur
        le traffic internet.

    2. Quelle différence faites-vous avec le proxy inverse ?

        Le proxy inverse est principalement utilisé pour sécuriser des connexions
        serveurs. Il est utilisé comme machine hôte du traffic serveur-client
        afin d'empêcher d'exposer sur internet le serveur en question.

    3. Citez quelques exemples de solutions permettant de réaliser ces fonctions.

        Nginx, Apache et tout serveur web permettant de gérer du traffic entrant et sortant.

1. ### Proxy direct

    On met en place l'infrastructure nécessaire au TP:
