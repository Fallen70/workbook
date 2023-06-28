Title: Archivage depuis un disque plein
Date: 2023-06-28 08:49
Category: Linux
Lang: fr
Tags: admin-sys, tar, find

# Méthode pour archiver des fichiers sur une période de temps

## Création d'un tar vide

```shell
cd /tmp
mkdir 2020
tar cvf 2020.tar 2020/
rm -rf 2020
```

## Copie des fichiers par année

```shell
cd /files/to/archive
for file in $(find . -newermt 20200101 -not -newermt 20210101); do tar -rvf /tmp/2020.tar $file; done
```

## Compression de l'archive

```shell
gzip /tmp/2020.tar
```
