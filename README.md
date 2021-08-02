# Prérequis

python 3

```
pip install pelican  markdown ghp-import 
```

# Deploiement

Tiré de https://github.com/getpelican/pelican/blob/master/docs/tips.rst#publishing-to-github

```
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ git push origin gh-pages
```


