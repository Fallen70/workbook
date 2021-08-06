Title: Find et lien symbolique
Date: 2021-08-02 16:20
Category: Linux
Lang: fr
Tags: find, sym-links

Tiré de <https://stackoverflow.com/questions/8513133/how-do-i-find-all-of-the-symlinks-in-a-directory-tree/21438684>

# Find symbolic links
```bash
find . -type l -ls
```

# Find symbolic links to a specific target
```bash
find . -lname link_target
```

Note that link_target may contain wildcard characters.

# Find broken symbolic links
```bash
find -L . -type l -ls
```

The -L option instructs find to follow symbolic links, unless when broken.

# Find & replace broken symbolic links
```bash
find -L . -type l -delete -exec ln -s new_target {} \;
```

More find examples can be found here: <https://hamwaves.com/find/>
