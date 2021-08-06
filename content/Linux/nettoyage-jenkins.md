Title: Nettoyage Jenkins
Date: 2021-08-05 13:30
Category: Linux
Lang: fr
Tags: Jenkins, admin-sys

Actions en s'appuyant sur les fichiers .pom:
 
 *  Nettoyage des logs catalina
 *  Suppression du cache Jenkins

```bash
#!/bin/bash

export TOMCAT_DIR='/path/to/jenkins/tomcat'
export CACHES_DIR='/path/to/jenkins/jenkins_data/caches'

# Clean catalina.out without restart
echo 'Cleaning catalina.out'
echo $(date)' Cleaned by XXXXX' > ${TOMCAT_DIR}/logs/catalina.out

# Cleaning caches dir
echo 'Cleaning caches dir'
rm -rvf ${CACHES_DIR}/*
```
