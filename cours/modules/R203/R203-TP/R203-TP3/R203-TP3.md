# Escape Game de R203

## Escape Game n°3

On active la VM `Debian11_EG3`, on ouvre le TP sur le Moodle de l'IUT et on se connecte à [cette adresse](https://moodle-but.iutbeziers.fr/moodle/course/view.php?id=179&sectionid=3066).

1. Sur votre PC désintaller le package apache2

  ```sh
  sudo apt remove apache2
  ```

2. Supprimer le répertoire /etc/apache2 et le répertoire /var/www

  ```sh
  sudo rm -rf /etc/apache2/ /var/www/
  ```

3. Installer le package apache2

  ```sh
  sudo apt install apache2
  ```

4. Si votre distribution a démarré automatique le daemon HTTPD vous pourrez vous connecter via l'interface local loopback qui est associé à l'adrese IP 127.0.0.1 et au nom localhost

  ```sh
  curl http://localhost
  ```

5. Si ce n'est pas le cas, démarrer le daemon HTTPD

  ```sh
  sudo systemctl status apache2
  ```

### Installation d'un site web

1. Récupérer sur internet le code "HTML" de la première page du site www.haribo.com

  ```sh
  wget -r -l 1 212.47.235.5
  ```

2. L'installer dans le répertoire /var/www/html de votre serveur (attention aux droits)

  > Je te laisse faire. :wink:

3. Vérifier que votre serveur fonctionne et qu'il envoie bien la page prévue

  ```sh
  curl http://localhost
  ```

4. Vérification croisée avec un de vos camarades de la salle


### Configuration d'une redirection

> On veut maintenant que votre serveur renvoie certaines requêtes vers un autre serveur

1. Pour commencer vous devez configurer que l'URL http://votre.ip/reglisse renvoie vers le site http://lareglisserie.fr



2. Vérifier que cela fonctionne

3. Procéder de même avec /mms vers mms.com

4. Procéder de même avec /carambar vers le site de carambar : carambarco.com


### Virtual Host

> En récupérant le contenu du site fra.mars.com vous devez maintenant créer un virtual host pour votre site web.

1. Copier le site /etc/apache2/sites-available/000-default et le renommer avec un nom de votre choix (voir mise en situation).

2. Désactiver le site par défaut : a2dissite 000-default.conf
3. Activer le nouveau site avec la commande a2ensite mms
4. Activer le nouveau site avec la commande a2ensite haribo
5. Faites le lien entre le site mms et votre machine locale

127.0.0.1    mms

127.0.0.1    haribo

Relancer le serveur apache2 et vérifier son fonctionnement dans le navigateur du client.  
Conclure : Comment se fait la détermination du site affiché par le serveur?
