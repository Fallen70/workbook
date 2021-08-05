Title: TIME_WAIT
Date: 2021-08-05 13:50
Category: linux
Lang: fr
Tags: netstat, linux

Sources :
 
 *  <https://vincent.bernat.ch/fr/blog/2014-tcp-time-wait-state-linux>
 *  <https://www.skyminds.net/serveur-dedie-reduire-les-connexions-time_wait-des-sockets-et-optimiser-tcp/>

```bash
netstat -nat | awk '{print $6}' | sort | uniq -c | sort -n
```
