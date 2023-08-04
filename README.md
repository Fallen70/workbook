# Prérequis

python 3

```
pip install pelican  markdown ghp-import 
```

# Deploiement

Tiré de https://github.com/getpelican/pelican/blob/master/docs/tips.rst#publishing-to-github

```
$ pelican content -o output -s publishconf.py
$ ghp-import output -b gh-pages
$ git push origin gh-pages
```

# Test avec la recherche pagefind

https://pagefind.app/

```
$ pelican content/  --relative-urls
$ mkdir index
$ cp -r output/*.html index/
$ rm index/categories.html index/index.html index/archives.html index/tags.html index/authors.html 
$ pagefind --source "index" --glob *.html
$ cp -r index/_pagefind output/pagefind
$ rm -rf index
$ python -m http.server 9000
```
