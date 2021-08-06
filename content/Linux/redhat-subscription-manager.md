Title: Subcription manager
Date: 2021-08-06 13:50
Category: Linux
Lang: fr
Tags: RedHat, admin-sys, ansible

# Prérequis 

Les commandes sont lancées en utilisant ansible et un inventory pour pouvoir propoager la configuration.

Il faut évidemment disposer de licences redhat et d'un compte associé ( `<login>` et '<password>' ).

# Register

Source : 

 * <https://access.redhat.com/solutions/253273>

```bash
ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m redhat_subscription -a "state=present username=<login> password=<password> auto_attach=true"
```

# Lock version

Source :

 * <https://access.redhat.com/solutions/238533>

```bash
ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m "command /usr/sbin/subscription-manager release --list"

ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m "command /usr/sbin/subscription-manager release --set=<version>"

ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m "command /usr/sbin/subscription-manager release --show"

ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m "command yum clean all"
```

# Unsubscribe

Source :

 * <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/installation_guide/ch-deregister_rhn_entitlement>

```bash
ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m "command /usr/sbin/subscription-manager unregister --username=<login>"
```

## Redhat 7:
```bash
ansible all -i inventory -u ansible  -b --become-user=root --become-method=sudo -m "command /usr/sbin/subscription-manager unregister"
```

