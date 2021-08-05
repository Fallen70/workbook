Title: Création d'utilisateur
Date: 2021-08-05 13:40
Category: bash
Lang: fr
Tags: bash

Sources :
 
 *  <https://www.starmate.fr/creer-un-utilisateur-et-son-passwd-en-une-commande/>
 *  <https://stackoverflow.com/questions/14810684/check-whether-a-user-exists>

```bash
# Check if user exists
if ! id -u $FS_USER > /dev/null 2>&1; then
    echo "The user does not exist; execute below commands to create and try again:"
    echo "  root@sh1:~# adduser --home /usr/local/freeswitch/ --shell /bin/false --no-create-home --ingroup daemon --disabled-password --disabled-login $FS_USER"
    echo "  ..."
    echo "  root@sh1:~# chown freeswitch:daemon /usr/local/freeswitch/ -R"
    exit 1
fi
```
