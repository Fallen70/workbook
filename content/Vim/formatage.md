Title: Formatage contenu
Date: 2021-08-05 10:00
Lang: fr
Tags: html, json
Category: Vim

# Formater du contenu dans vim

## HTML

Installer l'utilitaire `tidy`

```
:!tidy -mi -html -wrap 0 %
```
## JSON 

Nécessite python sur la machine

```
:%!python -m json.tool
```
