# Pytest

[Pytest](https://docs.pytest.org/en/stable/) est un framework permettant de faciliter l'écriture de test unitaire en python. Il met a disposition des outils permettant de faciliter l'écriture de tests. Il permet également d'éxécuter des tests au format unit test.
Il permet également d'utiliser directement le mot clef `assert` ce qui permet d'écrire des tests beaucoups plus lisibles.

## Découverte et Structure

Pytest fait de la découverte pour les tests, par défaut il va scanner tout les fichiers du projet remonter les fichier `test_*.py` ou `*_test.py`.
À partir de ces fichiers, collectez les éléments de test :
 * Les fonctions ou méthodes de test préfixées par `test` en dehors de toute classe.
 * Les fonctions ou méthodes de test préfixées par `test` à l'intérieur de classes de test préfixées par `Test` (sans méthode `__init__`). Les méthodes décorées avec `@staticmethod` et `@classmethod` sont également considérées.

### Structure recommandée

```
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    conftest.py
    test_app.py
    test_view.py
    ...
```

[Documentation](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery)

## Fixtures

[Documentation](https://docs.pytest.org/en/stable/explanation/fixtures.html#)

Cet outil permet d'écrire des éléments réutilisables dans plusieurs tests, par défaut il existe déjà des fixtures utilisables permettant de :

 * capturer les logs, stdout et stderr
 * simuler des fichiers ou dossiers temporaires
 * du cache entre les sessions de tests

### Ecriture et usage

On peut créer une `fixture` en utilisant le décorateur `pytest.fixture` :

```python
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
```

### Accessibilité

Les fixtures seront acessibles dans le module dans lequel elles ont été écrite, pour les rendre accessible a l'ensemble des tests il faut les déclarer dans le fichier `conftest.py`.  
Vous pouvez vérifier l'ensemble des fixtures accessible avec la commande `pytest --fixtures`

## Tests paramétré

[Documentation](https://docs.pytest.org/en/stable/example/parametrize.html)

Les tests paramétré permettent d'optimiser l'écriture de tests en paramétrant un jeu de tests.

```python
import pytest

def add( a, b):
    return a + b

testdata = [ (1,1,2),
             (1,2,3),
             (-10,0,-10),
             (0.5,0.5,1),
             ("a","b","ab"),
             ([1],[0],[1,0]),
           ]

@pytest.mark.parametrize("a,b,expected", testdata )
def test_add( a, b, expected ):
    assert add(a,b) == expected 
```

L'avantage est que pytest va créer un test par tuple dans dans testdata et donc on saura précisément quelle valeur ne fonctionne pas si in test venait a échouer.  

## Attraper les erreurs

En utilisant `pytest.raise` vous pouvez attraper les erreurs de votre programme.  

```python
import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
``` 

