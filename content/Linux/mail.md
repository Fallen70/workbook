Title: Debug envoi de mail
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: admin-sys, sendmail, exchange


# sendmail

## Test simple

Ecrire le contenu a envoyer dans /tmp/test.mail

```bash
sendmail -v recipient@domain < /tmp/test.mail
```

## Queue

```bash
mailq
sendmail -bp
```

## Aggregation des erreurs des mails dans la queue
```bash
mailq | grep smtpmailer.domain | sort  | uniq -c | sort
```

## Forcer l'envoi des mails en attente

```bash
sendmail -q -v
```

# Debug exchange avec  telnet

Source :

 * <https://docs.microsoft.com/en-us/exchange/mail-flow/test-smtp-with-telnet?view=exchserver-2019>

```bash
telnet smtpmailer.domain 25
```
Il faut ensuite taper chaque ligne suivante, valider avec la touche `entrée`.

`EHLO domain`

`MAIL FROM: <sender@domain>`

`RCPT TO: <recipient@domain> NOTIFY=success,failure`

`DATA`

`Subject: Telnet`

`Envoyé avec telnet.`

`.`

`QUIT`
