Title: Cacher information Serveur
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: admin-sys, apache, php

Source :

 * <https://www.if-not-true-then-false.com/2009/howto-hide-and-modify-apache-server-information-serversignature-and-servertokens-and-hide-php-version-x-powered-by/>

Pour tester :

```
$ lynx -head -mime_header http://www.ubuntu.com
HTTP/1.0 200 OK
Date: Fri, 20 Nov 2009 09:25:46 GMT
Server: Apache/2.2.8 (Ubuntu) mod_python/3.3.1 Python/2.5.2 PHP/5.2.4-2ubuntu5.7 with Suhosin-Patch mod_ssl/2.2.8 OpenSSL/0.9.8g
X-Powered-By: PHP/5.2.4-2ubuntu5.7
Content-Type: text/html; charset=utf-8
Age: 13
Content-Length: 0
X-Cache: HIT from avocado.canonical.com
X-Cache-Lookup: HIT from avocado.canonical.com:80
Via: 1.0 avocado.canonical.com:80 (squid/2.6.STABLE18)
Connection: close
```
# Summary

Safest basic setup is following:
httpd.conf or apache.conf rows:

```
ServerSignature Off
ServerTokens Prod
```

php.ini row:

```
expose_php = Off
```

After all changes remember reload server and check results. The results should look like this:

Before:

```
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2009 12:20:30 GMT
Server: Apache/2.2.4 (Ubuntu) PHP/5.2.3-1ubuntu6.4
X-Powered-By: PHP/5.2.3-1ubuntu6.4
Connection: close
Content-Type: text/html; charset=UTF-8
```

After:

```
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2009 13:06:21 GMT
Server: Apache
Connection: close
Content-Type: text/html; charset=UTF-8
```
