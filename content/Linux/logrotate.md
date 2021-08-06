Title: Logrotate
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: admin-sys, logrotate

Source :

 * <https://www.croc-informatique.fr/2009/06/rotation-des-logs-avec-logrotate/>
 * <http://www.delafond.org/traducmanfr/man/man8/logrotate.8.html>

Créer un fichier du nom de votre service (pour mémo) dans le répertoire /etc/logrotate.d. Nous allons prendre pour exemple le service postfix :

```bash
  vi /etc/logrotate.d/postfix
```
Saisissez ces quelques lignes :

```
  /var/log/maillog {
  daily
  missingok
  rotate 52
  compress
  delaycompress
  notifempty
  create 640 root
  sharedscripts
  postrotate
  if [ -f /var/run/postfix.pid ]; then
  /etc/init.d/postfix reload > /dev/null
  fi
  endscript
  }
```
**/var/log/maillog** : Correspond au fichier log à utiliser

**daily** : La rotation s’effectuera tous les jours. Nous pouvons aussi mettre weekly pour toutes les semaines , monthly pour tous les mois.

**missingok** : signifie que l’absence du/des fichier(s) log(s) n’est pas anormale. Si cette option n’est pas active alors l’administrateur recevra un mail si le/les log(s) est/sont manquant(s).

**rotate 52**: Nous garderons 52 fichiers. Soit pour mon cas, 52 jours de logs

**compress** : Les fichiers logs secondaire c’est à dire tout ce qui n’est pas le fichier de log principal seront compréssés.

**delaycompress** : Reporte la compression du journal précédent au prochain cycle de permutation. Ceci n’a un effet qu’utilisé en combinaison avec l’option compress. Elle peut être utilisée quand il n’est pas possible de demander à un programme de fermer son journal et qu’il puisse par conséquent continuer à écrire pour un moment dans le journal précédent.

**notifempty** : permet de ne pas permuter le journal lorsqu’il est vide

**create 640 root** : Les fichiers secondaire créés auront pour créateur root et auront les droits 640

**postrotate/endscript** : Les lignes entre prerotate et endscript (chacun devant apparaître sur une ligne isolée) sont exécutées avant permutation du journal. Ces directives doivent apparaîtrent dans la définition d’un journal

**sharedscripts** : permet d’executer qu’ une fois le script postrotate par rotation

# Execution 

Une fois que vous avez fini de configurer votre logrotate, vous pouvez forcer sont éxecution de cette manière :
```bash
logrotate -f  /etc/logrotate.conf
```
Pour débugger :
```bash
logrotate -d /etc/logrotate.conf
```
