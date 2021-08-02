Title: Actions nexus avec curl
Date: 2021-08-02 17:00
Lang: fr
Tags: curl, nexus
Category: curl

# Upload

```
curl -v --user 'user:pass' --upload-file /path/to/file http://nexus/nexus/repository/component/subfolder/file
```
# Delete 

```
curl -X DELETE -v --user  'user:pass'  http://nexus/nexus/repository/component/subfolder/file
```
