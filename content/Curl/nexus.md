Title: Actions nexus avec curl
Date: 2021-08-02 17:00
Category: Curl
Lang: fr
Tags: nexus, admin-sys

# Upload

```bash
curl -v --user 'user:pass' --upload-file /path/to/file http://nexus/nexus/repository/component/subfolder/file
```
# Delete 

```bash
curl -X DELETE -v --user  'user:pass'  http://nexus/nexus/repository/component/subfolder/file
```
