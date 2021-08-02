Title: Test StickySession avec curl
Date: 2021-08-02 13:15


Méthode pour tester une conf de loadbalancer avec curl avec du sticky session

En parallèle vérifier que la route est bien respectée en surveillant les logs des machine ciblées par les routes

Explication sur certaines options de curl

-H 'host:ServerName' pour cibler un vhost par son ServerName

--cookie-jar /tmp/cookie Sauver le cookie

* Récupérer le cookie 

```
curl --cookie-jar /tmp/cookie   -v -I -H 'host:ServerName' monserveur.cible-01

```

Dans la sortie console on aura l'ionformation de création du  

```
* Added cookie ROUTEID=".1" for domain ServerName, path /, expire 0
< Set-Cookie: ROUTEID=.1; path=/
Set-Cookie: ROUTEID=.1; path=/
```

* Utiliser le cookie sur une autre adresse partageant un Servername

--cookie /tmp/cookie Utilise le cookie créé

```
curl --cookie /tmp/cookie   -v -I -H 'host:ServerName' monserveur.cible-02
```

Le cookie est bien exploité

```
> HEAD / HTTP/1.1
> User-Agent: curl/7.29.0
> Accept: */*
> Cookie: ROUTEID=.1
> host:ServerName
```
