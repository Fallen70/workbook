Title: Nettoyage d'un repository M2
Date: 2021-08-05 13:20
Category: Linux
Lang: fr
Tags: Maven, admin-sys

Actions en s'appuyant sur les fichiers .pom:
 
 *  Suppression des snapshots avec un ctime >14j
 *  Suppression des autres avec un atime > 60j

ctime -> date de création

atime -> date de derniner accés

```bash
#!/bin/bash

export MVN_REPO_DIR='/path/to/m2'

# Cleaning mvn SNAPSHOT repository
echo 'Cleaning SNAPSHOT repository'
for snapshot_dir in $(find ${MVN_REPO_DIR} -ctime +14 -type d -name '*-SNAPSHOT' );
  do rm -rvf $snapshot_dir;
done;

# Cleaning all mvn repository
echo 'Cleaning all with atime > 60 days'
for file in $(find ${MVN_REPO_DIR} -atime +60 -type f -name '*.pom'); 
  do rm -rvf $( dirname $file ); 
done;
```
