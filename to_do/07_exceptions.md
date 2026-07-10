# Exceptions

Il y a des Classes dédiées à la gestion des exceptions en Python, lorsque le progrmme tente une action impossible il lancera une exception.  
Comme par exemple accéder à un index inéxistant, faire une addition sur une `string`.

```python
import sys

def count_to(number):
    for n in range(1, number+1):
        print(n)

def main():
    stop = sys.argv[1]
    count_to(stop)

if __name__ == "__main__":
    main()
```
si on l'execute on obtiendra le le resultat suivant :
```
$ python count.py 5
Traceback (most recent call last):
  File "/opt/git/python_onboarding/count.py", line 12, in <module>
    main()
  File "/opt/git/python_onboarding/count.py", line 9, in main
    count_to(stop)
  File "/opt/git/python_onboarding/count.py", line 4, in count_to
    for n in range(1, number+1):
TypeError: can only concatenate str (not "int") to str
```

## Traceback 

Lors d'une erreur python affichera la pile d'erreur, les `Traceback` python sont conçu pour être lu en commançant par la fin. Dans notre exemple ce qui nous intéresse c'est la trace suivante :
```
  File "/opt/git/python_onboarding/count.py", line 4, in count_to
    for n in range(1, number+1):
TypeError: can only concatenate str (not "int") to str
```
On tente de faire une concatenation `+` entre un `str` et un `int`, ce qui provoque une exception de type `TypeError`.  

Si nous souhaitons corriger l'erreur il faudrait écrire :
```python
import sys

def count_to(number):
    for n in range(1, int(number)+1):
        print(n)

def main():
    stop = sys.argv[1]
    count_to(stop)

if __name__ == "__main__":
    main()
```
```
$ python count.py 5
1
2
3
4
5
````

## Traiter une exception

Pour traiter les exceptions, vous pouvez utiliser les mots clefs `try`, `except` et `finally`. 

```python
try:
    2 / 0
except ZeroDivisionError as e:
    print( f"An error '{e}' occured")
```

Vous pouvez soit traiter l'erreur soit la propager en utilisant `raise`

Tout ce qui se trouve en dessous du mot clef `finally` sera toujours éxécuté exception ou pas.

```python
def divide( a, x ):
    try:
        r = a / x
    except ZeroDivisionError as e:
        print( "Zero Division Error")
    finally:
        r = 1
    return r
```

Cette methode renverra tourjours `1`.
           
```python
def divide( a, x ):
    try:
        return = a / x
    except ZeroDivisionError as e:
        print( "Zero Division Error")
    finally:
        return 1
```


## Les types courant d'exceptions

* TypeError : Se produit lorsqu'une opération ou une fonction est appliquée à un objet d'un type inapproprié. Cela peut arriver, par exemple, si vous essayez d'effectuer une opération entre deux types incompatibles.
* ValueError : Se produit lorsqu'une fonction reçoit un argument de type correct, mais dont la valeur est inappropriée. Cela arrive souvent lors de conversions de types.
* KeyError : Se produit lorsqu'une clé demandée dans un dictionnaire n'existe pas. Cela signifie que vous essayez d'accéder à une clé qui n'est pas présente.
* IndexError : Se produit lorsque vous essayez d'accéder à un index d'une liste qui est hors de sa portée. Cela se produit généralement lorsque l'index est supérieur à la longueur de la liste moins un.


## Lancer ou propager une exception:

Pour lancer ou propager une exception il suffit d'utiliser le mot clef raise. N'héstez pas a utiliser les types courant lorsque cela correspond a l'erreur rencontrée.

```python

def divide( a, x ):
    try:
        a = int(a)
        x = int(x)
    except ValueError as e:
        raise TypeError( "Unable to cast int" ) from e 
    if x == 0:
        raise ValueError( "Cannot divide by Zero" )
    return a / x
```

## Créer une exception

Il suffit de créer une classe qui hérite d'une Exception, vous pouvez bien sûr hériter des classes que vous avez créé.

```python
class MainCustomException(Exception):
  pass

class SubCustomException1(MainCustomException):
  pass

class SubCustomException2(MainCustomException):
  pass
```

## Pour aller plus loin

### Attention a ne pas être trops haut dans l'except

Si vous attrapez une erreur de haut niveau vous attrapez toutes celles en dessous ( voir la hiérrarchie plus bas ).  

Cela peut poser des problème car vous pouvez attraper la `KeyboardInterrupt` exception et empécher le `Ctrl C` de fonctionner.

[example](../../example/exceptions/keyboard_interruption_catch.py)

### GroupedException

Introduit en 3.11, cette classe permet de regrouper des exceptions de différents type pour les traiter ultérieurment.

https://docs.python.org/3/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions

### Hiérarchie des excpetions

Vous pouvez afficher la hiérarchie des `Exceptiions` en affichant l'aide du module `builtins`.

```python
import builtins
help(builtins)
Help on built-in module builtins:

NAME
    builtins - Built-in functions, exceptions, and other objects.

DESCRIPTION
    Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.

CLASSES
    object
        BaseException
            Exception
                ArithmeticError
                    FloatingPointError
                    OverflowError
                    ZeroDivisionError
                AssertionError
                AttributeError
                BufferError
                EOFError
                ImportError
                    ModuleNotFoundError
                LookupError
                    IndexError
                    KeyError
                MemoryError
                NameError
                    UnboundLocalError
                OSError
                    BlockingIOError
                    ChildProcessError
                    ConnectionError
                        BrokenPipeError
                        ConnectionAbortedError
                        ConnectionRefusedError
                        ConnectionResetError
                    FileExistsError
                    FileNotFoundError
                    InterruptedError
                    IsADirectoryError
                    NotADirectoryError
                    PermissionError
                    ProcessLookupError
                    TimeoutError
                ReferenceError
                RuntimeError
                    NotImplementedError
                    RecursionError
                StopAsyncIteration
                StopIteration
                SyntaxError
                    IndentationError
                        TabError
                SystemError
                TypeError
                ValueError
                    UnicodeError
                        UnicodeDecodeError
                        UnicodeEncodeError
                        UnicodeTranslateError
                Warning
                    BytesWarning
                    DeprecationWarning
                    EncodingWarning
                    FutureWarning
                    ImportWarning
                    PendingDeprecationWarning
                    ResourceWarning
                    RuntimeWarning
                    SyntaxWarning
                    UnicodeWarning
                    UserWarning
            GeneratorExit
            KeyboardInterrupt
            SystemExit
```
