# Module et Package

## Module

Un fichier Python (.py) destiné à être importé par d'autres fichiers .py. L'importation d'un module exécute le code contenu dans ce module et donne accès à un objet de module qui stocke les fonctions, classes et autres données de ce module.

Les variables définies dans un module qui ne se trouvent pas à l'intérieur d'une fonction ou d'une classe sont appelées variables globales. Les variables globales de chaque module sont accessibles en tant qu'attributs de l'objet module.

Python met en cache les modules après leur importation, donc l'importation du même module deux fois renverra le même objet module.

## Package

Un module Python créé à partir d'un répertoire (au lieu d'un seul fichier .py). Les packages Python sont créés en faisant un répertoire contenant un fichier `__init__.py`. Les packages Python peuvent contenir des sous-modules et des sous-packages.

## Comment vider le cache d'un module

Le cache des modules que Python utilise est une fonctionnalité, pas un bug : Python le fait pour des raisons de performance. Cependant, cette fonctionnalité peut commencer à ressembler à un bug lorsque nous testons notre code depuis le REPL Python tout en effectuant des modifications.

La manière la plus simple de résoudre ce problème est de quitter le REPL et de démarrer un nouveau REPL, ce qui lance un tout nouveau processus Python (avec un tout nouveau dictionnaire sys.modules). Mais il existe d'autres moyens de le faire.

Vous pouvez également essayer de modifier sys.modules, en supprimant des éléments pour vider le cache de ce module :
```python
del sys.modules['points']
```
Ou vous pourriez utiliser la fonction reload du module importlib de Python, qui recharge un objet de module :
```python
from importlib import reload
```
Dans les deux cas, vous pourriez ne pas résoudre complètement votre problème. En effet, recharger un module ne supprime pas les références aux anciennes versions des classes ainsi que les instances des anciennes versions des classes. Donc, la manière la plus simple de vraiment résoudre ce problème est de quitter le REPL et de le redémarrer.

### régle d'import

Ne pas faire d'import complet d'un moduile `import *`, cela rend le code difficle a débugger et a maintenir.  

Dans certain cas il est possible de rencontrer un cas ou un module à le même nom dans deux packages différents.  
Il est possible de renommer le module importé dynamiquement en utilisant le mot clef `as`

```python
from math import sqrt as msqrt
from cmath import sqrt as csqrt
msqrt(4)
csqrt(4)
```

# Structure d'un projet

Exemple d'un package app avec un sous package :

```
app/
├── app_module.py
├── __init__.py
└── sub_package1
    ├── __init__.py
    └── package.py
```

## Python path

Pour être en mesure d'importer quelquechose du package app il faut que le PYTHONPATH soit correct:

 * Soit python est exécuté dans le dossier qui contien le dossier app
 * Soit la variable PYTHONPATH doit contenir le chemin vers le dossier contenant app

**exemple:** si mon chemin est `/path/to/my/app`

### via le contexte

```bash
cd /path/to/my
python 
```

### via le PYTHONPATH

```bash
export PYTHONPATH=/path/to/my/
python
```

## import d'un module

```python
from app import app_module
```

# venv

Python permet de créer un environnement virtuel pour l'installation des packages. Cela ne permet que de cloisonner l'installation des packages mais pas le socle python qui reste commun.

Cela permet également de sélectionner une versions spécifique de python pour ce venv.

## Création du venv 

```shell
python -m venv venv
```

## activation

Activer le venv permet de surcharger les variables d'environnement pour que les binaires du venv prennent le dessus sur les variables par défaut du systéme.

### Linux
```shell
source venv/bin/activate
```
### Windows
#### bat
```shell
venv\Script\activate.bat
```
#### powershell
```shell
.\venv\Script\Activate.ps1
```


## desactivation

Il est possible de désactiver le venv pour remettre les variables d'environnement dans leur état initial.

### Linux
```shell
deactivate
```
### Windows
```shell
deactivate
```

## Ajouter des variable au venv

Le script `activate` peut être modifié pour ajouter des varaibles d'environnement accéssibles dans le contexte du venv.

Pour ajouter une variable il suffit de la mettre à la fin de ce fichier.

### Linux
fin du script `venv/bin/activate`
```shell
export VARIABLE='TEST'
```
### Windows
#### bat
fin du script `venv\Script\activate.bat`
```shell
SET VARIABLE='TEST'
```
#### powershell
fin du script `venv\Script\Activate.ps1`
```shell
$env:VARIABLE='TEST'
```
Pour s'assurer que la variable n'est plus utilisable une fois sorti du contexte du venv il faut ajouter sa suppression dans la méthode `deactivate` du script `activate`  en général au début du fichier.

### Linux
deactivate du script `venv/bin/activate`
```shell
unset VARIABLE
```
### Windows
#### bat
deactivate du script `venv\Script\activate.bat`
```shell
SET VARIABLE=
```
#### powershell
deactivate du script `venv\Script\Activate.ps1`
```shell
Remove-Item env:VARIABLE
```

# Windows

## Configurer dynamiquement le PYTHONPATH venv 

https://medium.com/@HojjatA/how-to-set-the-pythonpath-for-your-virualenv-in-windows-2ab5bf596e15
