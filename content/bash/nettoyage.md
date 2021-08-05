Title: Nettoyage de fichier/dossier en fonction de la taille
Date: 2021-08-05 12:50
Category: bash
Lang: fr
Tags: awk, bash, du

# Liste de fichier qui dépassent une taille en byte

```bash
du -s * | sort -n | awk  '{  if ( $1 > 400000 ) print $2; }'
```
## Suppression du contenu trop volumineux

```bash
for dir in $( du -s * | sort -n | awk  '{  if ( $1 > 400000 ) print $2; }' );
  do rm -rvf $dir;
done;
```
