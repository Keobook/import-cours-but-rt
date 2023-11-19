# Cloud - Vagrant

1. ## I - Vagrant

   1. ### 1.1 - Création d'une première VM Ubuntu

      Pour créer une première VM via Vagrant, on fait:

      1. Créer un répertoire Vagrant à la racine de votre compte

          ```sh
          mkdir -p ~/vagrant/VM1
          ```

      1. Placez-vous dans ce répertoire:

          ```sh
          cd ~/vagrant/VM1
          ```

      1. Dans VM1, on tape:

          ```sh
          vagrant init ubuntu/xenial64
          vagrant up --provider virtualbox
          ```

          On obtient:

          ```sh
          ### vagrant init
          A `Vagrantfile` has been placed in this directory. You are now
          ready to `vagrant up` your first virtual environment! Please read
          the comments in the Vagrantfile as well as documentation on
          `vagrantup.com` for more information on using Vagrant.

          ### vagrant up
          Bringing machine 'default' up with 'virtualbox' provider...
          ==> default: Box 'ubuntu/xenial64' could not be found. Attempting to find and install...
              default: Box Provider: virtualbox
              default: Box Version: >= 0
          ==> default: Loading metadata for box 'ubuntu/xenial64'
              default: URL: https://vagrantcloud.com/ubuntu/xenial64
          ==> default: Adding box 'ubuntu/xenial64' (v20211001.0.0) for provider: virtualbox
              default: Downloading: https://vagrantcloud.com/ubuntu/boxes/xenial64/versions/20211001.0.0/providers/virtualbox/unknown/vagrant.box
          Download redirected to host: cloud-images.ubuntu.com
          ==> default: Successfully added box 'ubuntu/xenial64' (v20211001.0.0) for 'virtualbox'!
          ==> default: Importing base box 'ubuntu/xenial64'...
          ==> default: Matching MAC address for NAT networking...
          ==> default: Checking if box 'ubuntu/xenial64' version '20211001.0.0' is up to date...
          ==> default: Setting the name of the VM: VM1_default_1700213129510_46713
          Vagrant is currently configured to create VirtualBox synced folders with
          the `SharedFoldersEnableSymlinksCreate` option enabled. If the Vagrant
          guest is not trusted, you may want to disable this option. For more
          information on this option, please refer to the VirtualBox manual:

            https://www.virtualbox.org/manual/ch04.html#sharedfolders

          This option can be disabled globally with an environment variable:

            VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

          or on a per folder basis within the Vagrantfile:

            config.vm.synced_folder '/host/path', '/guest/path', SharedFoldersEnableSymlinksCreate: false
          ==> default: Clearing any previously set network interfaces...
          ==> default: Preparing network interfaces based on configuration...
              default: Adapter 1: nat
          ==> default: Forwarding ports...
              default: 22 (guest) => 2222 (host) (adapter 1)
          ==> default: Running 'pre-boot' VM customizations...
          ==> default: Booting VM...
          ==> default: Waiting for machine to boot. This may take a few minutes...
              default: SSH address: 127.0.0.1:2222
              default: SSH username: vagrant
              default: SSH auth method: private key
              default: Warning: Connection reset. Retrying...
              default: Warning: Remote connection disconnect. Retrying...
              default: 
              default: Vagrant insecure key detected. Vagrant will automatically replace
              default: this with a newly generated keypair for better security.
              default: 
              default: Inserting generated public key within guest...
              default: Removing insecure key from the guest if it's present...
              default: Key inserted! Disconnecting and reconnecting using new SSH key...
          ==> default: Machine booted and ready!
          ==> default: Checking for guest additions in VM...
              default: The guest additions on this VM do not match the installed version of
              default: VirtualBox! In most cases this is fine, but in rare cases it can
              default: prevent things such as shared folders from working properly. If you see
              default: shared folder errors, please make sure the guest additions within the
              default: virtual machine match the version of VirtualBox you have installed on
              default: your host and reload your VM.
              default: 
              default: Guest Additions Version: 5.1.38
              default: VirtualBox Version: 7.0
          ==> default: Mounting shared folders...
              default: /vagrant => /root/Vagrant/VM1
          ```

      1. Démarrez la VM avec `vagrant up`

          Voir la partie précédente.

      1. Pour se loguer sur la VM, on fait:

          ```sh
          vagrant ssh
          ```

          On obtient:

          ```txt
          Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-210-generic x86_64)

          * Documentation:  <https://help.ubuntu.com>
          * Management:     <https://landscape.canonical.com>
          * Support:        <https://ubuntu.com/advantage>

          UA Infra: Extended Security Maintenance (ESM) is not enabled.

          0 updates can be applied immediately.

          45 additional security updates can be applied with UA Infra: ESM
          Learn more about enabling UA Infra: ESM service for Ubuntu 16.04 at
          <https://ubuntu.com/16-04>

          New release '18.04.6 LTS' available.
          Run 'do-release-upgrade' to upgrade to it.
          ```

           - Ses interfaces réseaux sont:

             ```txt
             1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
                 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
             2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
                 link/ether 02:be:82:6b:cc:1d brd ff:ff:ff:ff:ff:ff
             ```

      1. On se place dans le répertoire de la VM.

         - Quel est le type de disque ?

            Pour savoir, nous faisons un `ls`, nous obtenons:

            ```txt
            Logs
            ubuntu-xenial-16.04-cloudimg-configdrive.vmdk
            ubuntu-xenial-16.04-cloudimg.vmdk
            VM1_default_1700213129510_46713.vbox
            VM1_default_1700213129510_46713.vbox-prev
            ```

            Nous pouvons voir que la boxe Vagrant utilise du `VMDK` avec
            le provider `VirtualBox`.

1. ## II - Vagrant Customisation VM et construction d'image

    1. ### 2.1 Customisation de l'instance - Partie 1

         1. La commande suivante:

            ```sh
            egrep -v -e"\#|^$" Vagrantfile
            ```

            nous retourne:

            ```Vagrantfile
            Vagrant.configure("2") do |config|
              config.vm.box = "ubuntu/xenial64"
            end
            ```

            Le `egrep` nous permet de grep le `Vagrantfile` et d'exclure
            tous les commentaires du fichier afin d'obtenir que les commandes
            de configuration.

         1. Editer le fichier Vagranfile et décommenter les lignes en rapport avec vm.provision :

             Après avoir décommenter les lignes en question, nous obtenons maintenant:

             ```Vagrantfile
             Vagrant.configure("2") do |config|
               config.vm.box = "ubuntu/xenial64"
               config.vm.provision "shell", inline: <<-SHELL
                 apt-get update
                 apt-get install -y apache2
               SHELL
             end
             ```

         1. Prouvez que vous avez bien un serveur Web qui tourne dans la VM en montrant :
               1. Que le service apache2 est actif (quelle commande avez-vous tapé ?).

                   Pour savoir si le service est actif sous Ubuntu, on fait:

                     ```sh
                     systemctl status apache2
                     ```

                   On obtient:

                   ```txt
                   ● apache2.service
                     Loaded: not-found (Reason: No such file or directory)
                     Active: inactive (dead)
                   ```

                   Le service est donc en l'occurence non chargé (donc non installé) et il n'est pas actif.  
                   Nous le lançons donc avec:

                   ```sh
                   apt-get install apache2
                   systemctl start apache2
                   ```

                   Nous voyons donc que le serveur apache tourne bien:

                   ```txt
                   ● apache2.service - LSB: Apache2 web server
                   Loaded: loaded (/etc/init.d/apache2; bad; vendor preset: enabled)
                   Drop-In: /lib/systemd/system/apache2.service.d
                           └─apache2-systemd.conf
                   Active: active (running) since Fri 2023-11-17 09:54:53 UTC; 21s ago
                     Docs: man:systemd-sysv-generator(8)
                   CGroup: /system.slice/apache2.service
                           ├─12378 /usr/sbin/apache2 -k start
                           ├─12381 /usr/sbin/apache2 -k start
                           └─12382 /usr/sbin/apache2 -k start

                   Nov 17 09:54:51 ubuntu-xenial systemd[1]: Starting LSB: Apache2 web server...
                   Nov 17 09:54:52 ubuntu-xenial apache2[12353]:  *Starting Apache httpd web server apache2
                   Nov 17 09:54:52 ubuntu-xenial apache2[12353]: AH00558: apache2: Could not reliably determine the server's fully qualifi
                   Nov 17 09:54:53 ubuntu-xenial apache2[12353]:*
                   Nov 17 09:54:53 ubuntu-xenial systemd[1]: Started LSB: Apache2 web server.
                   Nov 17 09:55:04 ubuntu-xenial systemd[1]: Started LSB: Apache2 web server.
                   ```

               2. Que le programme apache2 écoute bien sur le port 80 (utilisez netstat du paquet net-tools)

                   On utilise donc `netstat` en faisant:

                     ```sh
                     netstat -tunlp
                     ```

                     Ce qui nous donne:

                     ```txt
                     Active Internet connections (only servers)
                     Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
                     tcp        0      0 0.0.0.0:22              0.0.0.0:*LISTEN      1283/sshd
                     tcp6       0      0 :::80                   :::*                    LISTEN      12378/apache2
                     tcp6       0      0 :::22                   :::*LISTEN      1283/sshd
                     udp        0      0 0.0.0.0:68              0.0.0.0:*                           871/dhclient
                     ```

                     `Apache2` écoute donc bien sur le port 80.

               3. En téléchargeant la page d’accueil (comment ? Quelle commande avez-vous tapé ?)

                   Pour télécharger la page d'accueil, on peut faire:

                   ```sh
                   curl http://127.0.0.1:80/
                   ```

                   On obtient donc:

                   ```html
                   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                   <html xmlns="http://www.w3.org/1999/xhtml">
                     <!--
                       Modified from the Debian original for Ubuntu
                       Last updated: 2014-03-19
                       See: https://launchpad.net/bugs/1288690
                     -->
                     <head>
                       <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                       <title>Apache2 Ubuntu Default Page: It works</title>
                       <style type="text/css" media="screen">
                     * {
                       margin: 0px 0px 0px 0px;
                       padding: 0px 0px 0px 0px;
                     }

                     body, html {
                       padding: 3px 3px 3px 3px;

                       background-color: #D8DBE2;

                       font-family: Verdana, sans-serif;
                       font-size: 11pt;
                       text-align: center;
                     }

                     div.main_page {
                       position: relative;
                       display: table;

                       width: 800px;

                       margin-bottom: 3px;
                       margin-left: auto;
                       margin-right: auto;
                       padding: 0px 0px 0px 0px;

                       border-width: 2px;
                       border-color: #212738;
                       border-style: solid;

                       background-color: #FFFFFF;

                       text-align: center;
                     }

                     div.page_header {
                       height: 99px;
                       width: 100%;

                       background-color: #F5F6F7;
                     }

                     div.page_header span {
                       margin: 15px 0px 0px 50px;

                       font-size: 180%;
                       font-weight: bold;
                     }

                     div.page_header img {
                       margin: 3px 0px 0px 40px;

                       border: 0px 0px 0px;
                     }

                     div.table_of_contents {
                       clear: left;

                       min-width: 200px;

                       margin: 3px 3px 3px 3px;

                       background-color: #FFFFFF;

                       text-align: left;
                     }

                     div.table_of_contents_item {
                       clear: left;

                       width: 100%;

                       margin: 4px 0px 0px 0px;

                       background-color: #FFFFFF;

                       color: #000000;
                       text-align: left;
                     }

                     div.table_of_contents_item a {
                       margin: 6px 0px 0px 6px;
                     }

                     div.content_section {
                       margin: 3px 3px 3px 3px;

                       background-color: #FFFFFF;

                       text-align: left;
                     }

                     div.content_section_text {
                       padding: 4px 8px 4px 8px;

                       color: #000000;
                       font-size: 100%;
                     }

                     div.content_section_text pre {
                       margin: 8px 0px 8px 0px;
                       padding: 8px 8px 8px 8px;

                       border-width: 1px;
                       border-style: dotted;
                       border-color: #000000;

                       background-color: #F5F6F7;

                       font-style: italic;
                     }

                     div.content_section_text p {
                       margin-bottom: 6px;
                     }

                     div.content_section_text ul, div.content_section_text li {
                       padding: 4px 8px 4px 16px;
                     }

                     div.section_header {
                       padding: 3px 6px 3px 6px;

                       background-color: #8E9CB2;

                       color: #FFFFFF;
                       font-weight: bold;
                       font-size: 112%;
                       text-align: center;
                     }

                     div.section_header_red {
                       background-color: #CD214F;
                     }

                     div.section_header_grey {
                       background-color: #9F9386;
                     }

                     .floating_element {
                       position: relative;
                       float: left;
                     }

                     div.table_of_contents_item a,
                     div.content_section_text a {
                       text-decoration: none;
                       font-weight: bold;
                     }

                     div.table_of_contents_item a:link,
                     div.table_of_contents_item a:visited,
                     div.table_of_contents_item a:active {
                       color: #000000;
                     }

                     div.table_of_contents_item a:hover {
                       background-color: #000000;

                       color: #FFFFFF;
                     }

                     div.content_section_text a:link,
                     div.content_section_text a:visited,
                     div.content_section_text a:active {
                       background-color: #DCDFE6;

                       color: #000000;
                     }

                     div.content_section_text a:hover {
                       background-color: #000000;

                       color: #DCDFE6;
                     }

                     div.validator {
                     }
                       </style>
                     </head>
                     <body>
                       <div class="main_page">
                         <div class="page_header floating_element">
                           <img src="/icons/ubuntu-logo.png" alt="Ubuntu Logo" class="floating_element"/>
                           <span class="floating_element">
                             Apache2 Ubuntu Default Page
                           </span>
                         </div>
                   <!--      <div class="table_of_contents floating_element">
                           <div class="section_header section_header_grey">
                             TABLE OF CONTENTS
                           </div>
                           <div class="table_of_contents_item floating_element">
                             <a href="#about">About</a>
                           </div>
                           <div class="table_of_contents_item floating_element">
                             <a href="#changes">Changes</a>
                           </div>
                           <div class="table_of_contents_item floating_element">
                             <a href="#scope">Scope</a>
                           </div>
                           <div class="table_of_contents_item floating_element">
                             <a href="#files">Config files</a>
                           </div>
                         </div>
                   -->
                         <div class="content_section floating_element">

                           <div class="section_header section_header_red">
                             <div id="about"></div>
                             It works!
                           </div>
                           <div class="content_section_text">
                             <p>
                                   This is the default welcome page used to test the correct 
                                   operation of the Apache2 server after installation on Ubuntu systems.
                                   It is based on the equivalent page on Debian, from which the Ubuntu Apache
                                   packaging is derived.
                                   If you can read this page, it means that the Apache HTTP server installed at
                                   this site is working properly. You should <b>replace this file</b> (located at
                                   <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
                             </p>


                             <p>
                                   If you are a normal user of this web site and don't know what this page is
                                   about, this probably means that the site is currently unavailable due to
                                   maintenance.
                                   If the problem persists, please contact the site's administrator.
                             </p>

                           </div>
                           <div class="section_header">
                             <div id="changes"></div>
                                   Configuration Overview
                           </div>
                           <div class="content_section_text">
                             <p>
                                   Ubuntu's Apache2 default configuration is different from the
                                   upstream default configuration, and split into several files optimized for
                                   interaction with Ubuntu tools. The configuration system is
                                   <b>fully documented in
                                   /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                                   documentation. Documentation for the web server itself can be
                                   found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                                   package was installed on this server.

                             </p>
                             <p>
                                   The configuration layout for an Apache2 web server installation on Ubuntu systems is as follows:
                             </p>
                             <pre>
                   /etc/apache2/
                   |-- apache2.conf
                   |       `--  ports.conf
                   |-- mods-enabled
                   |       |-- *.load
                   |`-- *.conf
                   |-- conf-enabled
                   |       `-- *.conf
                   |-- sites-enabled
                   |`--*.conf
                             </pre>
                             <ul>
                                           <li>
                                             <tt>apache2.conf</tt> is the main configuration
                                             file. It puts the pieces together by including all remaining configuration
                                             files when starting up the web server.
                                           </li>

                                           <li>
                                             <tt>ports.conf</tt> is always included from the
                                             main configuration file. It is used to determine the listening ports for
                                             incoming connections, and this file can be customized anytime.
                                           </li>

                                           <li>
                                             Configuration files in the <tt>mods-enabled/</tt>,
                                             <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                                             particular configuration snippets which manage modules, global configuration
                                             fragments, or virtual host configurations, respectively.
                                           </li>

                                           <li>
                                             They are activated by symlinking available
                                             configuration files from their respective
                                             *-available/ counterparts. These should be managed
                                             by using our helpers
                                             <tt>
                                                   <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                                   <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                                             </tt>
                                             <tt>
                                                   <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                                   <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                                               </tt>
                                                   and
                                             <tt>
                                                   <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                                   <a href="http://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                                             </tt>. See their respective man pages for detailed information.
                                           </li>

                                           <li>
                                             The binary is called apache2. Due to the use of
                                             environment variables, in the default configuration, apache2 needs to be
                                             started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                                             <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                                             default configuration.
                                           </li>
                             </ul>
                           </div>

                           <div class="section_header">
                               <div id="docroot"></div>
                                   Document Roots
                           </div>

                           <div class="content_section_text">
                               <p>
                                   By default, Ubuntu does not allow access through the web browser to
                                   <em>any</em> file apart of those located in <tt>/var/www</tt>,
                                   <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                                   directories (when enabled) and <tt>/usr/share</tt> (for web
                                   applications). If your site is using a web document root
                                   located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                                   document root directory in <tt>/etc/apache2/apache2.conf</tt>.
                               </p>
                               <p>
                                   The default Ubuntu document root is <tt>/var/www/html</tt>. You
                                   can make your own virtual hosts under /var/www. This is different
                                   to previous releases which provides better security out of the box.
                               </p>
                           </div>

                           <div class="section_header">
                             <div id="bugs"></div>
                                   Reporting Problems
                           </div>
                           <div class="content_section_text">
                             <p>
                                   Please use the <tt>ubuntu-bug</tt> tool to report bugs in the
                                   Apache2 package with Ubuntu. However, check <a
                                   href="https://bugs.launchpad.net/ubuntu/+source/apache2">existing
                                   bug reports</a> before reporting a new bug.
                             </p>
                             <p>
                                   Please report bugs specific to modules (such as PHP and others)
                                   to respective packages, not to the web server itself.
                             </p>
                           </div>




                         </div>
                       </div>
                       <div class="validator">
                       </div>
                     </body>
                   </html>
                   ```

         1. Visualiser la page d’accueil depuis le navigateur de la machine physique est impossible. Pour-
           quoi ? (vous pouvez essayer pour vous en convaincre)

             On fait un `ping` sur l'adresse de la machine afin de voir si l'on peut
             y accéder:

             ```sh
             PING 10.0.2.15 (10.0.2.15) 56(84) bytes of data.
             --- 10.0.2.15 ping statistics ---
             4 packets transmitted, 0 received, 100% packet loss, time 3088ms
             ```

             > **Note:**  
             > L'adresse IP `10.0.2.15` est celle de la VM créée via Vagrant que l'on a
             > récupéré en faisant un simple `ip -br a`.

         1. La configuration réseau est bien compliquée.
             Analysez le fichier Vagrantfile et montrez qu’il y a 3 solutions
             (vous devez être capable de dire où elles se situent dans le fichier)
             pour permettre un accès simple au serveur Apache dans la VM.

             - Solution 1 : On configure un `forwarded_port` spécifique à la VM et au port

               ```sh
               config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
               ```

             - Solution 2: On configure le réseau en tant que `private_network` où l'on pourra donc accéder aux machines
               sur celui-ci

               ```sh
               config.vm.network "private_network", ip: "192.168.56.10"
               ```

             - Solution 3: On configure le réseau comme `public_network`, tout le monde pourra y accéder.

               ```sh
               config.vm.network "public_network"
               ```

         1. Implémentez les 3 options simultanément.
             Il faut redémarrer la VM une fois le fichier
             Vagrantfile modifié à l’aide de la commande:

             ```sh
             vagrant reload
             ```

             Nous avons donc le `Vagrantfile` suivant:

             ```Vagrantfile
             Vagrant.configure("2") do |config|
               config.vm.box = "ubuntu/xenial64"
               config.vm.provision "shell", inline: <<-SHELL
                 apt-get update
                 apt-get install -y apache2
               SHELL
               config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
               config.vm.network "private_network", ip: "192.168.56.10"
               config.vm.network "public_network"
             end
             ```

             Le reload nous donne:

             ```txt
             ==> default: Checking if box 'generic/ubuntu2204' version '4.3.6' is up to date...
             ==> default: Clearing any previously set network interfaces...
             ==> default: Preparing network interfaces based on configuration...
                 default: Adapter 1: nat
                 default: Adapter 2: hostonly
                 default: Adapter 3: bridged
             ==> default: Forwarding ports...
                 default: 80 (guest) => 8080 (host) (adapter 1)
                 default: 22 (guest) => 2222 (host) (adapter 1)
             ==> default: Running 'pre-boot' VM customizations...
             ==> default: Booting VM...
             ==> default: Waiting for machine to boot. This may take a few minutes...
                 default: SSH address: 127.0.0.1:2222
                 default: SSH username: vagrant
                 default: SSH auth method: private key

                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...

                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
                 default: Warning: Remote connection disconnect. Retrying...
                 default: Warning: Connection reset. Retrying...
             ==> default: Machine booted and ready!
             ==> default: Checking for guest additions in VM...
                 default: The guest additions on this VM do not match the installed version of
                 default: VirtualBox! In most cases this is fine, but in rare cases it can
                 default: prevent things such as shared folders from working properly. If you see
                 default: shared folder errors, please make sure the guest additions within the
                 default: virtual machine match the version of VirtualBox you have installed on
                 default: your host and reload your VM.
                 default:
                 default: Guest Additions Version: 6.1.38
                 default: VirtualBox Version: 7.0
             ==> default: Configuring and enabling network interfaces...
             ==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
             ==> default: flag to force provisioning. Provisioners marked to run always will still run.
             ```

         1. On essaie maintenant d'accéder à la VM et au serveur web:

             - Solution 1:

               Avec:

               ```sh
               curl 127.0.0.1:8080
               ```

               On obtient bien la page précédente.

             - Solution 2:

                Avec:

                ```sh
                ping 192.168.56.10
                ```

                On obtient:

                ```txt
                PING 192.168.56.10 (192.168.56.10) 56(84) bytes of data.
                64 bytes from 192.168.56.10: icmp_seq=1 ttl=64 time=0.250 ms
                64 bytes from 192.168.56.10: icmp_seq=2 ttl=64 time=0.245 ms
                64 bytes from 192.168.56.10: icmp_seq=3 ttl=64 time=0.270 ms
                64 bytes from 192.168.56.10: icmp_seq=4 ttl=64 time=0.639 ms
                --- 192.168.56.10 ping statistics ---
                4 packets transmitted, 4 received, 0% packet loss, time 3080ms
                rtt min/avg/max/mdev = 0.245/0.351/0.639/0.166 ms
                ```

             - Solution 3:

                  Avec

                  ```sh
                  ping 10.202.0.50
                  ```

                  On obtient:

                  ```txt
                  PING 10.202.0.50 (10.202.0.50) 56(84) bytes of data.
                  64 bytes from 10.202.0.50: icmp_seq=1 ttl=64 time=0.280 ms
                  64 bytes from 10.202.0.50: icmp_seq=2 ttl=64 time=0.346 ms
                  64 bytes from 10.202.0.50: icmp_seq=3 ttl=64 time=0.133 ms
                  64 bytes from 10.202.0.50: icmp_seq=4 ttl=64 time=0.189 ms
                  --- 10.202.0.50 ping statistics ---
                  4 packets transmitted, 4 received, 0% packet loss, time 3110ms
                  rtt min/avg/max/mdev = 0.133/0.237/0.346/0.081 ms
                  ```

                  > **Note:**  
                  > L'IP `10.202.0.50` a été récupérée en faisant un `ip -br a`.

         1. Quels sont (en quelques mots) les avantages/inconv ́enients des 3 options d’apr`es vous ?

        - Solution 1:
          - Avantages:
            - Simple à mettre en place
            - On peut choisir le port que l'on souhaite
          - Inconvénients:
            - On ne peut pas accéder à la VM depuis l'extérieur (Sauf mise en place de NAT sur l'hôte)
            - Obligation d'entrer pour chaque port une ligne de configuration

        - Solution 2:
          - Avantages:
            - On peut choisir l'IP que l'on souhaite
          - Inconvénients:
            - Non accessible depuis l'extérieur
            - Pas de filtrage des ports accessibles

        - Solution 3:
          - Avantages:
            - On peut accéder à la VM depuis l'extérieur
          - Inconvénients:
            - Nécéssite plus d'IP sur le réseau
            - Nécéssite la présence d'un DHCP sur le réseau

    2. ### 2.2 Customisation de l’instance - Partie 2

        1. Lors du reboot de la machine, Vagrant vous a demandé sur quelle interface physique de la machine doit être fait le pont (eth1 en l’occurence).  
            Pour ne pas avoir à faire cela à chaque reboot, on peut modifier le fichier Vagrantfile en compl ́etant la ligne sur l’interface r ́eseau par le nom exact de l’interface.  
            Cela donne (à adapter si besoin) :

            ```sh
            config.vm.network "public_network", bridge: "eth1"
            ```

        1. Vagrant utilise les possibilités de répertoire partagé fournies par Virtualbox. Nous allons l’illustrer ici pour permettre de modifier les fichiers du serveur Web de VM1.

            1. Dans le répertoire où se trouve le fichier Vagrantfile, créez un répertoire vagrantsite et placez dedans le fichier index.html suivant :

                ```html
                <html>
                  <body>
                    <div align="center">Vagrant Machine</div>
                  </body>
                </html>
                ```

                > **Attention:**  
                > Il faut faire reload pour redémarrer une VM et –provision pour que la partie provisioning se fasse.  
                > Pourquoi est-ce que la partie provisioning est-elle optionnelle et non exécutée à chaque boot ?

                La partie provisioning est optionnelle car elle peut être longue à s'exécuter et peut ne pas être nécessaire à chaque boot.
                Notament si nous ne modifions pas le VagrantFile

            1. Nous obtenons le `Vagrantfile` suivant:

                ```Vagrantfile
                # -*- mode: ruby -*-

                # vi: set ft=ruby

                # All Vagrant configuration is done below. The "2" in Vagrant.configure

                # configures the configuration version (we support older styles for

                # backwards compatibility). Please don't change it unless you know what

                # you're doing

                Vagrant.configure("2") do |config|

                  # The most common configuration options are documented and commented below

                  # For a complete reference, please see the online documentation at

                  # <https://docs.vagrantup.com>

                  config.vm.synced_folder "vagrantsite", "/opt/vagrantsite"

                  # Every Vagrant development environment requires a box. You can search for

                  # boxes at <https://vagrantcloud.com/search>

                  config.vm.box = "generic/ubuntu2204"
                  config.vm.network "public_network", bridge: "eth1"

                  # Disable automatic box update checking. If you disable this, then

                  # boxes will only be checked for updates when the user runs

                  # `vagrant box outdated`. This is not recommended

                  # config.vm.box_check_update = false

                  # Create a forwarded port mapping which allows access to a specific port

                  # within the machine from a port on the host machine. In the example below

                  # accessing "localhost:8080" will access port 80 on the guest machine

                  # NOTE: This will enable public access to the opened port

                  config.vm.network "forwarded_port", guest: 80, host: 8080

                  # Create a forwarded port mapping which allows access to a specific port

                  # within the machine from a port on the host machine and only allow access

                  # via 127.0.0.1 to disable public access

                  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

                  # Create a private network, which allows host-only access to the machine

                  # using a specific IP

                  config.vm.network "private_network", ip: "192.168.56.10"

                  # Create a public network, which generally matched to bridged network

                  # Bridged networks make the machine appear as another physical device on

                  # your network

                  config.vm.network "public_network"

                  # Share an additional folder to the guest VM. The first argument is

                  # the path on the host to the actual folder. The second argument is

                  # the path on the guest to mount the folder. And the optional third

                  # argument is a set of non-required options

                  # config.vm.synced_folder "../data", "/vagrant_data"

                  # Provider-specific configuration so you can fine-tune various

                  # backing providers for Vagrant. These expose provider-specific options

                  # Example for VirtualBox

                  #

                  # config.vm.provider "virtualbox" do |vb|

                  #   # Display the VirtualBox GUI when booting the machine

                  #   vb.gui = true

                  #

                  #   # Customize the amount of memory on the VM

                  #   vb.memory = "1024"

                  # end

                  #

                  # View the documentation for the provider you are using for more

                  # information on available options

                  # Enable provisioning with a shell script. Additional provisioners such as

                  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the

                  # documentation for more information about their specific syntax and use

                  config.vm.provision "shell", inline: <<-SHELL
                    apt-get update
                    apt-get install -y apache2
                    ln -s /opt/vagrantsite /var/www/html/vagrantsite
                  SHELL
                end
                ```

        1. Les modification escomptées ont bien été faites car:

            ```sh
            curl http://127.0.0.1:8080/vagrantsite/index.html
            ```

            donne

            ```html
            <html>
              <body>
                <div align="center">Vagrant Machine</div>
              </body>
            </html>
            ```

    3. ### 2.3 Préparation d’une image

        1. Faire un template va nous permettre de créer d’autres VMs suivant la même configuration. Cela pose un problème avec l’utilisation de la redirection de port que nous avons utilisée. Pourquoi ?

            Le problème que vas se poser est que nous allons rencontrer un conflit de port car nous allons avoir plusieurs VMs qui vont utiliser le port 8080 sur la loopback.

        2. Il faut modifier la directive ainsi :

            ```txt
            Vagrant.configure("2") do |config|
              config.vm.synced_folder "vagrantsite", "/opt/vagrantsite"
              config.vm.box = "generic/ubuntu2204"
              config.vm.network "public_network", bridge: "eth1"
              config.vm.network "forwarded_port", guest: 80, host: 8080,auto_correct: true
              config.vm.network "private_network", ip: "192.168.56.10"
              config.vm.network "public_network"
              config.vm.provision "shell", inline: <<-SHELL
                apt-get update
                apt-get install -y apache2
                ln -s /opt/vagrantsite /var/www/html/vagrantsite
              SHELL
            end
            ```

        3. Créer la box avec la commande :

            ```sh
              root at vmtp.ecadiere.fr in ~/Vagrant/VM1
              $ vagrant package
              ==> default: Attempting graceful shutdown of VM...
              ==> default: Clearing any previously set forwarded ports...
              ==> default: Exporting VM...
              ==> default: Compressing package to: /root/Vagrant/VM1/package.box
            ```

        4. Une fois la box faite, il faut l’ajouter à votre liste avec la commande:

            ```sh
            vagrant box add --name my-box ./package.box
            ```

            Ce qui nous donne:

            ```bash
            ==> box: Box file was not detected as metadata. Adding it directly...
            ==> box: Adding box 'my-box' (v0) for provider: 
              box: Unpacking necessary files from: file:///root/Vagrant/VM1/package.box
            ==> box: Successfully added box 'my-box' (v0) for 'virtualbox'!
            ```

        5. Listez vos boxes avec :

            ```sh
            vagrant box list
            ```

            Ce qui nous donne:

            ```txt
            generic/ubuntu2204 (virtualbox, 4.3.6)
            my-box             (virtualbox, 0)
            ubuntu/xenial64    (virtualbox, 20211001.0.0)
            ```

        6. Vagrant stocke les images (boxes) dans un répertoire particulier, ~/.vagrant.d/boxes. Faites un ls -R ~/.vagrant.d/boxes pour lister ce répertoire. Quelles sont les images ?

            On fait:

            ```sh
            ls -R ~/.vagrant.d/boxes
            ```

            ```txt
              /root/.vagrant.d/boxes:
              generic-VAGRANTSLASH-ubuntu2204  my-box  ubuntu-VAGRANTSLASH-xenial64

              /root/.vagrant.d/boxes/generic-VAGRANTSLASH-ubuntu2204:
              4.3.6  metadata_url

              /root/.vagrant.d/boxes/generic-VAGRANTSLASH-ubuntu2204/4.3.6:
              virtualbox

              /root/.vagrant.d/boxes/generic-VAGRANTSLASH-ubuntu2204/4.3.6/virtualbox:
              box.ovf		  generic-ubuntu2204-virtualbox-x64-disk001.vmdk  metadata.json
              box_update_check  info.json					  Vagrantfile

              /root/.vagrant.d/boxes/my-box:
              0

              /root/.vagrant.d/boxes/my-box/0:
              virtualbox

              /root/.vagrant.d/boxes/my-box/0/virtualbox:
              box-disk001.vmdk  box.ovf  metadata.json  Vagrantfile  vagrant_private_key

              /root/.vagrant.d/boxes/ubuntu-VAGRANTSLASH-xenial64:
              20211001.0.0  metadata_url

              /root/.vagrant.d/boxes/ubuntu-VAGRANTSLASH-xenial64/20211001.0.0:
              virtualbox

              /root/.vagrant.d/boxes/ubuntu-VAGRANTSLASH-xenial64/20211001.0.0/virtualbox:
              box.ovf		  ubuntu-xenial-16.04-cloudimg-configdrive.vmdk  Vagrantfile
              box_update_check  ubuntu-xenial-16.04-cloudimg.mf
              metadata.json	  ubuntu-xenial-16.04-cloudimg.vmdk
            ```

            Les box sont les fichier `.ovf` dans les répertoires `virtualbox` de chaque box.

        7. Est-ce que l’on peut effacer ~/Vagrant/VM1/package.box (avec une commande rm)? Dit autrement, est-ce que cela a une incidence sur l’image dans vagrant ?

           Non, cela n'a pas d'incidence sur l'image dans vagrant car elle est copiée dans le répertoire `~/.vagrant.d/boxes` lors de l'ajout de la box.

1. ## 3 - Vagrant *advanced version!*

    1. ### 3.1 - Vagrant Hub

        1. Les images sont associées à un compte utilisateur et ont un nom.
            Par exemple ubuntu/xenial64. Ubuntu est le nom du compte et xenial64 est le nom de l’image.

            1. Choisissez l’image ubuntu/xenial64 et cliquez dessus. Cliquez ensuite sur le nom du compte
              ubuntu pour avoir le profil de l’utilisateur. Est-ce une image en laquelle on peut avoir
              confiance ?

                  On va sur la page de `ubuntu/xenial64`:

                  [![vagrant-ubuntu-xenial64](./src/TP2/vagrant-ubuntu-xenial.png)](https://app.vagrantup.com/ubuntu/boxes/xenial64)

                  Puis sur la page `ubuntu`:

                  [![vagrant-ubuntu](./src/TP2/vagrant-ubuntu.png)](https://app.vagrantup.com/ubuntu)

                  Même si le profil n'a pas de preuve d'être le compte officiel du projet `Ubuntu`, il
                  donne plus confiance qu'autre chose.

            2. Même question pour `debian/jessie64`

                  On va sur la page de `debian/jessie64`:

                  [![vagrant-debian-jessie](./src/TP2/vagrant-debian-jessie.png)](https://app.vagrantup.com/debian/boxes/jessie64)

                  Puis sur la page `debian`:

                  [![vagrant-debian](./src/TP2/vagrant-debian.png)](https://app.vagrantup.com/debian)

                  Ce profil a l'air de bien être le compte officiel de `Debian`.

            3. Même question pour `centos/7`

                  On va sur la page de `centos/7`:

                  [![vagrant-centos-7](./src/TP2/vagrant-centos7.png)](https://app.vagrantup.com/centos/boxes/7)

                  Puis sur la page `centos`:

                  [![vagrant-centos](./src/TP2/vagrant-centos.png)](https://app.vagrantup.com/centos)

                  Vu que ce profil ne donne pas d'informations, on ne peux pas savoir s'il est le compte officiel de CentOS ou no

        2. Ajouter les images `debian/jessie64` et `centos/7` à votre bibliothèque locale.

            On fait:

              ```sh
              vagrant box add debian/jessie64
              vagrant box add centos/7
              ```

    2. ### 3.2 Autres commandes Vagrant et interaction avec Virtualbox

        1. Pour créer l’image à partir de VM1, Vagrant a stoppé VM1. Vous pouvez le vérifier avec :

            ```sh
            vagrant status
            ```

            Ce qui nous donne:

            ```txt
            Current machine states:

            default                   poweroff (virtualbox)

            The VM is powered off. To restart the VM, simply run `vagrant up`
            ```

            > **Note:**  
            > On peut aussi voir le statut de toutes les VM en faisant:
            >
            > ```sh
            > vagrant global-status
            > ```

        2. Redémarrez VM1. (avec quelle commande ?)

            Comme indiqué par la sortie de la commande `vagrant status`, on fait:

            ```sh
            vagrant up
            ```

        3. Vous pouvez faire des snapshots (instantanés) de la machine avec (le dernier paramètre est le nom utilisé par Vagrant) :

            On fait:

            ```sh
            vagrant snapshot save snap1
            ```

            Ce qui nous donne:

            ```txt
            ==> default: Snapshotting the machine as 'snap1'...
            ==> default: Snapshot saved! You can restore the snapshot at any time by
            ==> default: using `vagrant snapshot restore`. You can delete it using
            ==> default: `vagrant snapshot delete`.
            ```

            Quels nouveaux fichiers sont créés dans le répertoire de VM1 de Virtualbox (contentez vous de les lister) ?

            Les nouveau fichiers sont:

            ```txt
            2023-11-17T11-06-40-125440000Z.sav
            {812d3219-2870-42a7-a03a-8b4c14ee0fd5}.vmdk
            ```

            > **Note:**  
            > On peut restorer l'état de la VM via une snapshot en faisant:
            >
            > ```sh
            > vagrant snapshot save <save-name>
            > ```

        4. On peut mettre la VM en veille avec:

            ```sh
            vagrant suspend
            ```

            Ce qui nous donne :

            ```txt
            ==> default: Saving VM state and suspending execution...
            ```

        5. Mettre en veille ou faire un instantané sont des opérations quasiment similaires.
            Quels fichiers ont été créés par Virtualbox pour cette opération et quelle est la différence avec l'opération snaphsot ?

            Lorsque l'on met en veille avec `vagrant suspend`, nous avons les fichiers suivants ajoutés:

            ```txt
            2023-11-19T14-30-24-171358000Z.sav
            ```

            Lors de l'exicution de la commande suspend, on peut voir que la VM est sauvegardée dans un fichier `.sav` avec la date et l'heure de la sauvegarde.

            Au contraire de lorsque l'on fait un instantané (snapshot) avec `vagrant snapshot save <save-name>`:

            ```txt
            2023-11-17T11-06-40-125440000Z.sav
            {812d3219-2870-42a7-a03a-8b4c14ee0fd5}.vmdk
            ```

            On peut donc dire que la différence entre faire un `vagrant suspend` et une `vagrant snapshot save <save-name>` est
            que lorsque l'on fait une `snapshot` nous ne suspendons pas l'exécution et faisons un nouveau comprenant les différences
            au moment donné de la snapshot comparé à l'image de base, contrairement au `suspend` qui ne fait que arrêter l'exécution de la VM.

        6. Redémarrez la VM avec

            ```sh
            vagrant resume
            ```

            Ce qui nous donne:

            ```txt
            ==> default: Resuming suspended VM...
            ==> default: Booting VM...
            ==> default: Waiting for machine to boot. This may take a few minutes...
                default: SSH address: 127.0.0.1:2222
                default: SSH username: vagrant
                default: SSH auth method: private key
            ==> default: Machine booted and ready!
            ==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
            ==> default: flag to force provisioning. Provisioners marked to run always will still run.
            ```

            On voit les redirections de port avec:

            ```sh
            vagrant port
            ```

            ```txt
            The forwarded ports for the machine are listed below. Please note that
            these values may differ from values configured in the Vagrantfile if the
            provider supports automatic port collision detection and resolution.

                22 (guest) => 2222 (host)
                80 (guest) => 8080 (host)
            ``````

        7. Vagrant interagit avec l’hyperviseur qui gère les VMs, ici VirtualBox.  
           Souvent, il peut utiliser des fonctions avancées.  
           Dans le fichier Vagrantfile suivant, quelles fonctions avancées sont utilisées et quel est leur intérêt ?

            ```sh
              # -*- mode: ruby -*-
              # vi: set ft=ruby :
              VAGRANTFILE_API_VERSION = "2"
              Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
                config.vm.define "web" do |web|
                  web.vm.box ="ubuntu/xenial64"
                  web.vm.network "forwarded_port", guest:80, host:8888
                  web.vm.synced_folder "vagrantsite/", "/opt/vagrantsite", type:"rsync",
              rsync__args: ["--verbose", "--rsync-path='sudo rsync'", "--archive", "-- delete", "-z"]
              web.vm.provision "shell", inline: "apt-get install -y nginx;
              ln -s /opt/vagrantsite /var/www/html/vagrantsite"
              web.vm.provider "virtualbox" do |v|
                v.linked_clone = true
              v.memory = 1024
                  v.cpus = 2
                  v.gui = true
              end end
              end
            ```

            Les fonctionalités avancées utilisées sont :

             - `v.lined_clone` : Permet de faire une copie liée de la VM, c'est à dire que la VM créée sera liée à la VM de base et ne prendra pas plus de place sur le disque.
             - `v.memory` : Permet de définir la mémoire allouée à la VM
             - `v.cpus` : Permet de définir le nombre de coeurs alloués à la VM
             - `v.gui` : Permet de lancer la VM avec l'interface graphique
             - `rsync__args` : Permet de définir les arguments à passer à rsync lors de la synchronisation des fichiers

    3. ### 3.3 Vagrant Multi-machines

        1. Modifiez le script de manière à ce que ce soit l’image generic/ubuntu2204 qui soit utilisée.

            Après modification, le `Vagrantfile` ressemble à:

            ```sh
            # -*- mode: ruby -*-
            # vi: set ft=ruby :
            # Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
            VAGRANTFILE_API_VERSION = "2"
            Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
            # All Vagrant configuration is done here. The most common configuration
            # options are documented and commented below. For a complete reference,
            # please see the online documentation at vagrantup.com.
            # Every Vagrant virtual environment requires a box to build off of.

              config.vm.define "database" do |db|
                db.vm.box = "generic/ubuntu2204"
                db.vm.hostname = "db01"
                db.vm.network "private_network", ip: "192.168.56.100"
              end

              config.vm.define "web" do |web|
                web.vm.box = "generic/ubuntu2204"
                web.vm.hostname = "web01"
                web.vm.network "private_network", ip:"192.168.56.101"
                web.vm.provision "shell",
                inline: "echo '127.0.0.1 localhost web01\n192.168.56.100 db01' > /etc/hosts"
              end
            end
            ```

        2. Vous pouvez vous logez sur une machine ou sur l’autre avec la commande:

            ```sh
            vagrant ssh <VM-name>
            ```

            Dans notre cas, on fait:

            ```sh
            vagrant ssh web
            ```

            ou

            ```sh
            vagrant ssh db01
            ```

            Logez vous sur web et montrer que l’on peut pinger 192.168.56.100 :

            ```sh
            vagrant@web01:~$ ping 192.168.56.100
            PING db01 (192.168.56.100) 56(84) bytes of data.
            64 bytes from db01 (192.168.56.100): icmp_seq=1 ttl=255 time=3.60 ms
            64 bytes from db01 (192.168.56.100): icmp_seq=2 ttl=255 time=1.06 ms
            ```

        3. Pourquoi est-ce que `ping db01` fonctionne aussi ?

            `ping db01` fonctionne car nous avons ajouté la ligne suivante dans le `Vagrantfile`:

            ```sh
            inline: "echo '127.0.0.1 localhost web01\n192.168.56.100 db01' > /etc/hosts"
            ```

            Cette ligne permet de définir l'IP de la machine `db01` dans le fichier `/etc/hosts` de la machine `web01`.

        4. Peut-on pinger les 2 VMs depuis la machine physique ?

            Oui nous pouvons pinger les 2 VMs depuis la machine physique.

            ```txt
            PING 192.168.56.100 (192.168.56.100) 56(84) bytes of data.
            64 bytes from 192.168.56.100: icmp_seq=1 ttl=255 time=0.477 ms
            64 bytes from 192.168.56.100: icmp_seq=2 ttl=255 time=0.224 ms
            ^C
            --- 192.168.56.100 ping statistics ---
            2 packets transmitted, 2 received, 0% packet loss, time 1020ms
            rtt min/avg/max/mdev = 0.224/0.350/0.477/0.126 ms

            PING 192.168.56.101 (192.168.56.101) 56(84) bytes of data.
            64 bytes from 192.168.56.101: icmp_seq=1 ttl=64 time=2.27 ms
            64 bytes from 192.168.56.101: icmp_seq=2 ttl=64 time=1.68 ms
            ^C
            --- 192.168.56.101 ping statistics ---
            2 packets transmitted, 2 received, 0% packet loss, time 1001ms
            rtt min/avg/max/mdev = 1.682/1.977/2.273/0.295 ms
            ```

        5. Notez, en remarque finale, que l’on peut être plus générique en créant n machines où n est un nombre fixé par l’administrateur, comme on peut le voir dans le script ci-après. Quelle sera la contrainte physique du serveur à prendre en compte dans le choix de n ?

            ```sh
            VAGRANTFILE_API_VERSION = "2"
            # Define a variable - the number of web nodes.
            $cluster_nodes = 3
            $consul_server_ip = "192.168.30.130"
            Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
                # Define a global box file to be used by all machines.
                config.vm.box = "generic/ubuntu2204"
                # Create and provision a Consul server machine.
                config.vm.define "consul" do |consul|
                    consul.vm.hostname = "consul"
                    consul.vm.network "private_network", ip: $consul_server_ip
                    consul.vm.provision "shell", inline: "apt-get update && apt-get install
                    unzip"
                    consul.vm.provision "puppet" do |puppet|
                    puppet.manifests_path = "puppet/manifests"
                    puppet.module_path = "puppet/modules"
                    puppet.manifest_file = "site.pp"
                    end
                end
                # Create a number of cluster members.
                (1..$cluster_nodes).each do |i|
                    config.vm.define vm_name = "cluster%02d" % i do |cluster|
                        cluster.vm.hostname = vm_name
                        cluster.vm.provision "shell", inline: "apt-get update && apt-get
                        install -y unzip"
                        cluster.vm.provision "puppet" do |puppet|
                        puppet.manifests_path = "puppet/manifests"
                        puppet.module_path = "puppet/modules"
                        puppet.manifest_file = "site.pp"
                    end

                    cluster.vm.provision "shell", inline: "consul join #{$consul_server_ip}"
                    end
                end
            end
            ```

            La contrainte physique du serveur à prendre en compte dans le choix de n est son CPU ça RAM et son espace disque.

## Copyright &copy; 2023 Alexis Opolka & Enzo Cadière - All Rights Reserved
