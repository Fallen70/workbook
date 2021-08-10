Title: Liste des services
Date: 2021-08-10 10:50
Category: Linux
Lang: fr
Tags: admin-sys, RedHat


Sources :

 * <https://linoxide.com/how-to-list-services-in-linux/>

Liste de tous les services

```bash
systemctl list-unit-files
```
Recherche d'un service 

```bash
systemctl | grep "apache2"
```

Liste des services avec netstat

```bash
netstat -pnltu 
```
