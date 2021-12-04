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

Now you should be set to continue on and use `rpm` and `tdnf` as sudo on your IRIX system!

#end


