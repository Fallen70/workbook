Title: Package installé par taille
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: RedHat, admin-sys


```bash
rpm -qa --queryformat '%10{size} - %-25{name} \t %{version}\n' | sort -n
```
