# sgug-rse - Troubleshooting Guide for SGUG-RSE

The definitive guide to help with questions and tips for installing and using your new RSE installation.

## Contributing

Want to help? Please see our [contribution guide](contributing.md).


## How to get this working

### Sudo
You may have hit an issue if you are installing RSE from scrach on a IRIX system. Your user is not in the sudoers file and you've seen an response like this:

```
[your username] is not in the sudoers file.  This incident will be reported.
```

Don't worry, we can set your use up in the sudoers file quickly and easily with a few simple commands.

Why sudo? Many things in UNIX require you to do things as your user, not root. Sudo is a program that allows you to more easily execute commands as the root user without having to invoke a root shell via `su`.

You already have sudo installed, we just need to authorize your username on IRIX to use it.

If you are comfortable editing files with vi and you know what to do then go a head and become root (using su) and edit a new file called `/usr/sgug/etc/sudoers.d/USER` where USER is the username that should have access to sudo.

```
$ su -
[root password]
# vi /usr/sgug/etc/sudoers.d/USER
```

Add the following in the file, but replace USER by the actual username:

```
# Don't ask a password for USER for 10 minutes once one is entered
Defaults:USER timestamp_timeout=600
USER    ALL=(ALL)       ALL
```

And save the file.

If you don't know how to use vi, you can type the following instead as root, replacing USER by your username:

```
NAME=USER
cat << EOF > /usr/sgug/etc/sudoers.d/$NAME
# Don't ask a password for $NAME for 10 minutes once one is entered
Defaults:$NAME timestamp_timeout=600
$NAME    ALL=(ALL)       ALL
EOF
```


#### invoke a bash shell
These commands require bash. Luckily, you just installed it when you untarred the RSE selfhoster tarball...
```
octane 104# /usr/sgug/bin/bash
bash-5.0# 
```

#### set an env variable in your bash shell that is your current username
Here I'm assuming that the _last_ entry in the /etc/passwd file is your newly created username. If it's not then please set the env variable manually with this command:

```
bash-5.0# sudo_user=dillera
```
Substitute your actuall username there.

To do this the easy way:
```
bash-5.0# sudo_user=`awk -F: 'END {print $1 } ' /etc/passwd` && echo $sudo_user
```

#### set and env variable in your bash shell that is the new updated `sys` group

```
$ fixed_line=`awk -v name="$sudo_user" '/sys::/{print $0 "," name } ' /etc/group`
```

#### update your /etc/group file with the new updated `sys` groups, also make a backup first
The backup will be named `/etc/group.bak` if you need it...

```
sed -i.bak "/^sys::/c ${fixed_line}" /etc/group
```

#### Exit and re-login to your SGI
We have fixed the group file now so that you are part of the `sys` group, and you can use sudo. However, the fact that you are in the `sys` group is not known to IRIX until you logout and then back in. So you need to exit all the way out of the SGI and back to your host system (or logout if you are using the window manager). Then just log back in.

When you log back in use the `groups` command to verify you are part of the `sys` group:

```
octane ~ $ groups
user sys
```

You should see `sys` - if you do not something didn't go right. Check the `/etc/group` file and fix it.

Now you should be set to continue on and use `rpm` and `tdnf` as sudo on your IRIX system!




#end


