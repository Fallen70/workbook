Title: RAM/SWAP
Date: 2021-08-05 13:50
Category: linux
Lang: fr
Tags: linux

# Swappiness

 * <https://geekeries.de-labrusse.fr/?p=1806>

```bash
sudo sysctl -w vm.swappiness=30
```
# RAM & SWAP

Sources :
 
 *  <https://www.vincentliefooghe.net/content/linux-gestion-la-ram-et-du-swap>
 *  <https://linuxpedia.fr/doku.php/expert/analyser_usage_memoire_vive>
 *  <https://www.selenic.com/smem/>

```bash
for proc in /proc/[0-9]*; do   awk '/VmSwap/ { print $2 "\t'`readlink $proc/exe | awk '{ print $1 }'`'" }' $proc/status; done | sort -n | awk '{ total += $1 ; print $0 } END { print total "\tTotal"}'

for file in /proc/*/status ; do awk '/Tgid|VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | grep kB  | sort -k 3 -n
```
