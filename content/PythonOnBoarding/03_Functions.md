Title: Ecriture Fonctions
Date: 2024-10-08 14:00
Category: Python Onboarding
Lang: fr
Tags:python, training

# Fonctions

on utilise le mot réservé `def` pour définir les fonction


```python
def greet(name):
    print("Hello", name )

greet("World")
```

    Hello World


Si aucun `return` dans la fonction elle renvoie `None`.


```python
a = greet( "Toto" )

print( a )
```

    Hello Toto
    None


## arguments

Il ya deux types d'arguments qui peuvent être utilisé pour lors de l'appel d'une fonction: 
 * les `positional` arguments
 * les `named` ou `keyword` arguments
 
###  positional argument

Par example print peux prendre plusieurs `proistional argument`


```python
print( 1,2,3,4 )
```

    1 2 3 4


### named argument

La fonction print accepte aussi des `named` argument


```python
print(help(print))
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    
    None



```python
print(2, 1, 3, 4, sep=' ')
print(2, 1, 3, 4)
print(2, 1, 3, 4, sep='-')
print(2, 1, 3, 4, sep=', ')
```

    2 1 3 4
    2 1 3 4
    2-1-3-4
    2, 1, 3, 4



```python
print(2, 1, 3, 4, sep=', ', end='!!')

```

    2, 1, 3, 4!!

### Accepter un nombre inconnu d'argument

Il est donc possible d'écrire une fonction qui prendra un nombre inconnu d'arguments.  
Si on reprend la fonction greet écrit plus on peut l'appeler avec un `positional` argument
```python
def greet(name):
    print("Hello", name )
```


```python
greet("Toto")
```

    Hello Toto


Avec un `named` argument


```python
greet( name="Toto" )
```

    Hello Toto


Mais pas avec plusieurs arguments


```python
try:
    greet( "Tata", "Titi" )
except TypeError as e:
    print(e)
```

    greet() takes 1 positional argument but 2 were given


Il faut redéfinir la fonction en utilisant une étoile sur l'argument, de cette maniére nous allons capturer tout les `positional` arguments sou la forme d'un tuple.  
Vous trouverez ceci souvent sous cette forme `def ma_fonction( *args ):`.


```python
def greet( *names ):
    for name in names:
        print( "Hello", name )
        
greet( "Tata", "Titi" )
```

    Hello Tata
    Hello Titi


On peut même l'appeler sans argument, ça n'est pas considéré comme une erreur le tuple `names` sera vide


```python
greet()
```

On peut ajouter un ou plusieur `positional` argument avant les * dans la signature


```python
def greet( greeting, *names ):
    for name in names:
        print( greeting, name )
        
greet( "Hi", "Tata", "Titi" )
```

    Hi Tata
    Hi Titi


Si on veut utiliser un `named` argument pour lui donner une valeur par défaut on devra positioner la variable greeting aprés les *.


```python
def greet( greeting="Hello", *names ):
    for name in names:
        print( greeting, name )
        
greet( "Tata", "Titi" )
```

    Tata Titi



```python
def greet(*names, greeting="Hello" ):
    for name in names:
        print( greeting, name )
        
greet( "Tata", "Titi", greeting="Hi" )
```

    Hi Tata
    Hi Titi


### Accepter un nombre inconnu de `named`/ `keyword` argument

De la même maniérer il est possible d'écrire une fonction qui accepte un nombre inconnu de `named` argument.  
Il faut dans ce cas utilser ** avant le nom de la variable qui va capturer ces éléments sous la forme d'un `dict`.  
Couramment la fonction sera écrite de cette maniére `def ma_fonction( **kwargs )`


```python
def say_things(name, **things):
    for thing, c in things.items():
        print(f"{name} has {c} {thing}")
    print("That's all!")

say_things("Toto", ducks=2, pig=1)
```

    Toto has 2 ducks
    Toto has 1 pig
    That's all!


## Point d'attention concernant les valeurs par default

Lors de l'éxecution le code de la fonction n'est évalué qu'une seul fois, ceci peut provoquer des bugs.

### Pas de mutable

Il ne faut pas utiliser de `mutable` comme valeur par défaut


```python
def init_list( *args, default=[] ):
    for value in args:
        default.append( value )
    return default

l1 = init_list( 1 )
l2 = init_list( 2,3 )

print( l1, l2 )
```

    [1, 2, 3] [1, 2, 3]


### Pas de valeur aléatoire

Pour la même raison utiliser une valeur alétoire n'aura aucun effet.


```python
import random
colors = [ "blue", "pink", "green" ]
def pick_color( color=random.choice( colors ) ):
    return color
```


```python
for _ in range(50):
    print( pick_color() )
```

    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green
    green

