Title: Vérifier la date de fin d'un certificat SSL
Date: 2021-08-09 16:20
Category: Linux
Lang: fr
Tags: admin-sys, openssl

Le script a pour but d'être éxécuter sur la machine cible en local avec un outil type rundeck.

```bash
#!/bin/sh

HOSTNAME="localhost"
PORT="443"
ALERT_X_DAY_BEFORE=10

# Get current date as timestamp
CURR_DATE=$(date +%s)

# Get enddate from certificate of hostname:port identified
CERT_DATE_AS_STRING=$(echo | openssl s_client -connect ${HOSTNAME}:${PORT} 2>/dev/null | openssl x509 -enddate -noout | cut -d '=' -f 2)                                                                            

CERT_EXP_DATE=$(date --date="${CERT_DATE_AS_STRING}" +%s)

DAYS_REMAINING=$(( ( $CERT_EXP_DATE - $CURR_DATE ) / 86400 ))

if [ $DAYS_REMAINING -lt 0 ]; then
  echo "Certificat expiré  sur $(hostname -f)"
  exit 1;
fi

if [ $DAYS_REMAINING -lt $ALERT_X_DAY_BEFORE ]; then
  echo "$DAYS_REMAINING jours avant expiration sur $(hostname -f)"
  exit 1;
fi
```
