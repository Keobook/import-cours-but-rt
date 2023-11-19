#!/bin/bash

server_image="fedora-39"
client_image="centos-8.0"

server_name="nfs-server"

root_pwd="root"

date
echo Copyright \(c\) 2023 Alexis Opolka, All Rights Reserved - The Unlicense License

echo Here's a little recap of information while you're waiting:
echo    - Number of VMs: 3
echo    - Types:
echo      - Server: Fedora 39
echo      - Client: CentOS-8

if ( ! test -d "./temp/" ); then
  ### We create a temp folder for the images
  mkdir -p ./temp/
fi;

if (! test -f "./temp/nfs-server.qcow2" ); then

  echo Building the server via virt-builder...
  virt-builder $server_image --output ./temp/$server_name.qcow2 --format qcow2 --root-password password:$root_pwd --size 6G

else

  echo We have one image already, we\'re going to use it without building it...

fi;


echo Now we\'re installing the server as $server_name

if ( virsh list | grep $server_name ); then

  virsh destroy nfs-server
  virsh undefine nfs-server
fi;

virt-install --name $server_name \
  --memory 2048 --vcpus 4 \
  --disk path=./temp/$server_name.qcow2,format=qcow2,bus=virtio,size=5 \
  --import --os-variant fedora-unknown \
  --network default \
  --firstboot-command 'localectl set-keymap azerty' \
  --firstboot-command 'suder useradd -m -G wheel -p "test" test; chage -d 0 test' \
  --firstboot-install nfs-utils \ 
  --firstboot-command 'sudo systemctl enable --now nfs-server' \
  --firstboot-command 'sudo cat /proc/fs/nfsd/versions; sudo mkdir -p /srv/nfs4/{backups,www} /opt/backups/ /var/www/' \
  --firstboot-command 'sudo mount --bind /opt/backups /srv/nfs4/backups; sudo mount --bind /var/www /srv/nfs4/www; sudo exportfs -ra' \
  --firstboot-command  'sudo firewall-cmd --new-zone=nfs --permanent' \
  --firstboot-command  'sudo firewall-cmd --zone=nfs --add-service=nfs --permanent' \
  --firstboot-command  'sudo firewall-cmd --zone=nfs --add-source=10.202.0.0/16 --permanent' \
  --firstboot-command  'sudo firewall-cmd --reload'