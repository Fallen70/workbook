Title: Copie clef publique ssh
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: ssh, ansible


# bash

Liste les cibles dans hosts.txt

```bash
#!/bin/bash
 
for host in $(cat ./hosts.txt); do
echo $host;
cat ~/.ssh/id_rsa.pub | ssh root@${host} 'cat >> ~/.ssh/authorized_keys'
done 

for host in $(cat ./hosts.txt) ; do echo $host; sshpass -p '<password>' ssh-copy-id root@${host}; done; 
```

# ansible


```yaml
- hosts: servers_to_update 
  remote_user: root
  become: yes
  become_method: sudo
  tasks:
    - name: "Copie de la clef publique" 
      authorized_key:
        user: "{{ authorised_username }}"
        state: present
        key: "{{ lookup('file', 'files/ssh_pub/id_rsa.pub') }}"
  tags: always
```
