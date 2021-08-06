Title: Ulimit
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: admin-sys

Liste par process

```bash
lsof | cut -d\  -f1 | sort | uniq -c | sort -nr | less   
```
