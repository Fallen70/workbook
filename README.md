# Prérequis

python 3

```
pip install pelican  markdown ghp-import 
```

# Deploiement

```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ git push origin gh-pages
```


