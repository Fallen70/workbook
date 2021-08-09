Title: Génération de certificat
Date: 2021-08-09 16:50
Category: Linux
Lang: fr
Tags: admin-sys, openssl

```bash
#!/bin/bash

# Nettoyage du dossier temporaire cible
rm -rf /tmp/@option.host@
mkdir -p /tmp/@option.host@

# Définition des fichiers cible
export host="server.name"
export key='/tmp/'$host'/'$host'.key'
export csr='/tmp/'$host'/'$host'.csr'
export srl='/tmp/'$host'/'$host'.srl'
export crt='/tmp/'$host'/'$host'.crt'

#-- generate key
openssl genrsa -out ${key}  $RD_OPTION_KEY_SIZE

#-- generate csr
openssl req -new -key ${key} -out ${csr} -subj "/CN=@option.host@"

#-- generate self siging key
openssl x509 -req -days $RD_OPTION_KEY_DURATION -in ${csr} -signkey ${key} -out ${crt}

#-- cleanup
rm -f ${srl}
```
