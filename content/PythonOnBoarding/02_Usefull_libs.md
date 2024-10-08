Title: Librairies utiles
Date: 2024-10-08 14:00
Category: Python Onboarding
Lang: fr
Tags:python, training

# Built-in Functions

Python propose une série de fonction toutjours accessible sans nécessité d'import.

## Liste exhaustive

https://docs.python.org/3/library/functions.html

### zip

La méthode `zip` permet de prendre plusieurs `iterables` pour créer un tuple contenant un élement de chaque.  
Elle s'arrétera une fois que l'`iterable` le plus court est épuisé.


```python
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
```

    (1, 'sugar')
    (2, 'spice')
    (3, 'everything nice')



```python
for item in zip([1, 2], [3,4,5], [5,6,7] ):
    print(item)
```

    (1, 3, 5)
    (2, 4, 6)


### any / all
 * any renvoie `True` si un des éléments de l'iterable est vrai.
 * all renvoie `True` si tous les éléments de l'itérable sont vrai.


```python
any( [ False, False, True ] )

```




    True




```python
all( [ False, False, True ] )
```




    False



Il faut faire attention car Python ne va pas evaluer l'entiéreté de la condtion :
  * pour un `ET` il s'arrétera si il trouve un `False`
  * pour un `OU` il s'arrétera si il trouve un `True`
  
Dans l'exemple si dessous `not_defined_value` n'est pas évalué dans la condition.


```python
if True or not_defined_value:
    try:
        print( not_defined_value )
    except NameError as e:
        print( e )
```

    name 'not_defined_value' is not defined


### range / enumerate

Range permet de générer une série de nombre avec un début, une fin et un pas.   
Enuerate permet d'habiller un iterable pour attribuer un index a chaque élément


```python
list( range( 1,12,2 ))
```




    [1, 3, 5, 7, 9, 11]




```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
```




    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]




```python
list(enumerate(seasons, start=1))
```




    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]



### reversed / sorted

Permet de créer un iterator sur une `sequence` pour soit la lire a l'envers soit la trier



```python
seq_it = reversed( 'Hello' )
for letter in seq_it:
    print(letter)
```

    o
    l
    l
    e
    H


### abs / pow / min / max / sum

Pusieurs utilitaire pour des fonctions mathématiques

# Itertools libs

## Liste exhaustive

https://docs.python.org/3/library/itertools.html

# Collections libs

## liste exhaustive

https://docs.python.org/3/library/collections.html
