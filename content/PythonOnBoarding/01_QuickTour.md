Title: Tour d'horizon Python
Date: 2024-10-08 14:00
Category: Python Onboarding
Lang: fr
Tags:python, training

# Mutability

Les listes, dictionnaires et ensembles sont considéré comme `mutable`, les Strings, tuples, entiers, et floats sont `immutable`

Un objet `mutable` est un objet qui peut être modifié.
On peut changer les propriétés d'un objet mutable une fois qu’il a été défini.
Une erreur courante est de confondre modification et réassignation.

## id
La méthode `id` permet de connaitre la référence assignée par Python


```python
print("Example d'un objet immutable" )
a = 1000
print("a = 1000" )
print( f"ref a:{id(a)}" )
a = a + 1
print("a = a + 1" )
print( f"ref a:{id(a)}" )
```

    Example d'un objet immutable
    a = 1000
    ref a:139996751941264
    a = a + 1
    ref a:139996751941232



```python
print("Example d'un objet mutable" )
l0 = [ 1,2,3 ]
print( "l0 = [ 1,2,3 ]" )
print( f"ref l0:{id(l0)}" )
l1 = l0
print( "l1 = l0" )
print( f"ref l1:{id(l1)}" )
l1.append(4)
print( "l1.append(4)" )
print( f"l0:{l0}" )
print( f"l1:{l1}" )
```

    Example d'un objet mutable
    l0 = [ 1,2,3 ]
    ref l0:139996743323464
    l1 = l0
    ref l1:139996743323464
    l1.append(4)
    l0:[1, 2, 3, 4]
    l1:[1, 2, 3, 4]


# Iterables

Il y a plusieurs type d'`iterable` en Python :
  * Les `list`
  * Les `tuples`
  * Les `string`
  * les `set`
  * les `dict`

Tous les `iterable` peuvent être utilisés comme support pour une boucle `for`


```python
fruits= ['apple', 'lemon', 'pear', 'watermelon']
coordinates = (1, 8, 2)
greeting = "Hi y'all!"
colors = {'red', 'blue', 'yellow'}
item_counts = {'computers': 1, 'headphones': 2, 'ducks': 3}

print("List")
for fruit in fruits:
    print( fruit )
print("Dict")
for key in item_counts:
    print( f"{key}:{item_counts[key]}" )
```

    List
    apple
    lemon
    pear
    watermelon
    Dict
    computers:1
    headphones:2
    ducks:3


## Sequences

Les sequences sont un type d'`iterable` qui conserve les données de maniére ordonnée et permet un accés par `index`.
Sont concernés les `list`, `tuples` et `string`. La valeur de l'`index` va de 0 a len(seq) - 1.

On peux utiliser des valeurs négatives pour parcourir la séquence à l'envers.


```python
# Premier élément
fruits[0]
```




    'apple'




```python
# Dernier élément
coordinates[-1]
```




    2



### Slices
On peut utiliser des `slices` sur une `sequence` pour récupérer une portion de la `sequence` il faut délimiter la portion entre crochet `[start:stop]`
 * start index est inclusif ( par défaut 0 )
 * stop index est exclusif, Python s'arrétera juste avant ( par défaut `len(list)` )


```python
# Les deux premiers
fruits[:2]
```




    ['apple', 'lemon']




```python
fruits[0:2]
```




    ['apple', 'lemon']




```python
# Tout sauf le dernier
greeting[:-1]
```




    "Hi y'all"




```python
greeting[0:-1]
```




    "Hi y'all"




```python
greeting[3:-1]
```




    "y'all"



Si on utilise des index negatif sur le start index on part de la fin.


```python
coordinates[-2:]
```




    (8, 2)



Si le stop index dépasse ça ne pose pas de problème


```python
coordinates[:5]
```




    (1, 8, 2)



### Reverse
On peut inverser une séquence avec cette formultation `[::-1]`


```python
fruits
```




    ['apple', 'lemon', 'pear', 'watermelon']




```python
fruits[::-1]
```




    ['watermelon', 'pear', 'lemon', 'apple']



## Comprehension

Il existe une forme compacté pour construire un `iterable` avec une boucle for.


```python
# Liste des nombre pair < 10:
res = []
for i in range(10):
    if i % 2 == 0:
        res.append(i)
res
```




    [0, 2, 4, 6, 8]




```python
# La même chose sous forme de list comprehension
[ i for i in range(10) if i %2 == 0 ]
```




    [0, 2, 4, 6, 8]


