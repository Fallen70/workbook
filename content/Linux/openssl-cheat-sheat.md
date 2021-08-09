Title: OpenSSL CheatSheat
Date: 2021-08-09 16:00
Category: Linux
Lang: fr
Tags: admin-sys, openssl

Sources :

 *  <https://www.kinamo.fr/fr/support/faq/commandes-openssl-utiles>
 *  <https://www.system-linux.eu/index.php?post/2017/03/03/Convertir-un-fichier-pfx-en-crt-et-key>

# OpenSSL - commandes utiles

## Comment se servir d'OpenSSL?
OpenSSL est véritablement le couteau suisse de la gestion de certificats, mais à l'instar du canif suisse, on passe un temps fou à essayer de distinguer la lime à ongles du tire-bouchon. Vous trouverez ci-dessous une liste des commandes les plus fréquemment utilisées.

## Demandes de certificats et gestion de clés
Si vous avez commandé un certificat, il faut générer une demande de certificat pour finaliser la commande. Vous pouvez le faire comme suivant, avec une nouvelle private key:

```bash
openssl req -sha256 -nodes -newkey rsa:2048 -keyout www.server.com.key -out www.server.com.csr
```

Vous pouvez également employer le Générateur de CSR Kinamo pour créer votre CSR.
Générer une nouvelle demande de certificat à base d'une clé existante:

```bash
openssl req -new -sha256 -key www.server.com.key -out www.server.com.csr
```

Générer une demande de certificat à base d'un certificat existant:

```bash
openssl x509 -x509toreq -in www.server.com.crt -out www.server.com.csr -signkey www.server.com.key
```

Générer une nouvelle clé RSA:

```bash
openssl genrsa -out www.server.com.key 2048
```

Générer une nouvelle clé ECC:

```bash
openssl ecparam -out server.key -name prime256v1 -genkey
```

Générer un certificat auto-signé (self-signed) pour des tests:

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout www.server.com.key -out www.server.com.crt -days 365
```

## Afficher et contrôler les certificats

Contrôler et afficher une demande de certificat:

```bash
openssl req -noout -text -verify -in www.server.com.csr
```

Contrôler et afficher une clé privée et publique:

```bash
openssl rsa -noout -text -check -in www.server.com.key
```

Afficher le contenu décodé d'un certificat en format PEM:

```bash
openssl x509 -noout -text -in www.server.com.crt
```

Afficher le contenu d'un certificat en format PKCS#7:

```bash
openssl pkcs7 -print_certs -in www.server.com.p7b
```

Afficher le contenu d'un certificat et d'une clé en format PKCS#12:

```bash
openssl pkcs12 -info -in www.server.com.pfx
```

Contrôler une connection SSL et afficher tous les certificats intermédiaires:

```bash
openssl s_client -connect www.server.com:443
```

Contrôler si un certificat, une demande de certificat et une clé ont la même clé publique:

```bash
openssl x509 -noout -modulus www.server.com.crt | openssl sha256
openssl req -noout -modulus www.server.com.csr | openssl sha256
openssl rsa -noout -modulus www.server.com.key | openssl sha256
```

## Convertir des certificats

Conversion d'un fichier PKCS#12 ( .pfx .p12, typiquement utulisé sur Microsoft Windows) contenant clé privée et certificat vers le format PEM (utilisé sur Linux):

```bash
openssl pkcs12 -nodes -in www.server.com.pfx -out www.server.com.crt
```

Conversion du format PEM vers le format PKCS#12:

```bash
openssl pkcs12 -export -in www.server.com.crt -inkey www.server.com.key -out www.server.com.pfx
```

Conversion du format PKCS#7 ( .p7b .p7c ) vers le format PEM:

```bash
openssl pkcs7 -print_certs -in www.server.com.p7b -out www.server.com.crt  
```

Conversion du format PEM vers le format PKCS#7:

```bash
openssl crl2pkcs7 -nocrl -certfile www.server.com.crt -out www.server.com.p7b
```

Conversion du format DER (.crt .cer ou .der) vers le format PEM:

```bash
openssl x509 -inform der -in certificate.cer -out certificate.pem
```

## Extraire la clef :
```bash
openssl pkcs12 -in votre.pfx -nocerts -out votre.key -nodes
```

## Extraire le certificat :
```bash
openssl pkcs12 -in votre.pfx -clcerts -nokeys -out votre.crt
```

## Créer le fullchain.pem
```bash
openssl pkcs12 -in votre.pfx -out fullchain.pem -nodes
```

## Générer une demande de certificat à base d'un certificat existant:
```bash
openssl x509 -x509toreq -in www.server.com.crt -out www.server.com.csr -signkey ww.server.com.key
```

