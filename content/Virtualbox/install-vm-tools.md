Title: Installation VM Tools
Date: 2021-08-05 08:40
Category: Virtualbox
Lang: fr


A faire aprés modification du Kernel

Aprés  lancement de la VM depuis le menu Périphérique choisir `Insérer l'image CD des Additions invité`

![Menu Virtualbox]({static}/images/virtualbox/vm-tools.png)


# Montage et éxecution du CD:

```bash
sudo mount /dev/cdrom /mnt/cdrom
cd /mnt/cdrom/
sudo ./VBoxLinuxAdditions.run
```
