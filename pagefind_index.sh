mkdir index
cp -r output/*.html index/
rm index/categories.html index/index.html index/archives.html index/tags.html index/authors.html 
./pagefind --source "index" --glob *.html
cp -r index/_pagefind/ output/
rm -rf index
