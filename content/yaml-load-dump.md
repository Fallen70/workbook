Title: Load et Dump yaml
Date: 2023-06-29 11:44
Category: Python
Lang: fr
Tags: yaml

# Prérequis
```python
# import pyyaml module
import yaml
from yaml.loader import SafeLoader
```

# Chargement depuis un fichier

```python
# Open the file and load the file
with open('fichier.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
```
	
# Dump dans un fichier

```python	
# Dump data
with open('fichier.yml', 'w') as f:
    yaml.dump(data,f )
```