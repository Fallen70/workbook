Title: Télecharger certificats
Date: 2021-08-09 17:00
Category: Linux
Lang: fr
Tags: admin-sys, openssl

Récupére tous les certificats affiché par `$HOST:$PORT`.

```bash
rm -rf /tmp/certs/
mkdir -p /tmp/certs/
openssl s_client -showcerts -connect $HOST:$PORT </dev/null 2>/dev/null | sed -n "/BEGIN CERTIFICATE/,/END CERTIFICATE/p" | awk 'BEGIN {c=0;} /BEGIN CERT/{c++} { print > "/tmp/certs/cert." c ".pem"}'
```
