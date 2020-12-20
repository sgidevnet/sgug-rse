# sgug-rse

Silicon Graphics User Group RPM Software Environment

## Licensing

It is intended that any fedora `.spec` files listed here are under the "Fedora Project Contributor Agreement": https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement.

Notably - fedora specifically mentions spec file licensing here: https://fedoraproject.org/wiki/Licensing:Main#License_of_Fedora_SPEC_Files

Unless otherwise stated, those `.spec` files remain under their original license as per their contribution to Fedora. This project does not attempt to supplant nor change the license of these works.

The modifications from the original fedora `.spec` files fall under the license of the sgug-rse project, namely GPL3.

## Contributing

Want to help? Please see our [contribution guide](contributing.md).

## How to get this working

NOTE: While we are not yet out of beta, it is recommended to remove any previous sgug-rse installation before extracting this new one. We don't yet support in-place upgrades using RPMs.

(1) Add your user account to the irix `sys` group - this will allow you to use the sgug `sudo` out of the box with your user password - then you can follow the steps below without additional hoop jumping.

(2) Ensure your system can cope with long command line buffers:

```
# As root
su -
# Show existing value
systune ncargs
# Tweak if < 262144
systune ncargs 262144
```

(3) Optional - remove any previous sgug-rse installation:

```
# As your user
rm -rf ~/rpmbuild/SRPMS/*
rm -rf ~/rpmbuild/RPMS/*
# As root
rm -rf /usr/sgug/*
```

(4) Download the artifacts for the latest version from the github releases tab (assuming they aren't too big).

You'll find three main archives - and there might be "update" archives too that need to be extracted:

```
sgug-rse-selfhoster-0.0.7beta.tar.gz
sgug-rse-srpms-0.0.7beta.tar.gz
sgug-rse-rpms-0.0.7beta.tar.gz

sgug-rse-rpms-0.0.7betaupdateNUM.tar.gz
```

(5) Extract the selfhoster archive under /usr as root (important, sgug-rse _installation_ files are root owned and managed):

```
su - (enter root password)
cd /usr
gunzip -dc /path/to/sgug-rse-selfhoster-0.0.7beta.tar.gz |tar xf -
(log out of root)
```

(6) You'll need to setup some new directories for your user:

```
mkdir -p ~/rpmbuild/SPECS
mkdir -p ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SRPMS
mkdir -p ~/rpmbuild/RPMS
```

(7) As your user extract the SRPMs and RPMs in an appropriate place.

```
cd ~/rpmbuild
gunzip -dc /path/to/sgug-rse-srpms-0.0.7beta.tar.gz | tar xf -
gunzip -dc /path/to/sgug-rse-rpms-0.0.7beta.tar.gz | tar xf -
# Optional
mkdir ~/rpmupdates
cd ~/rpmupdates
gunzip -dc /path/to/sgug-rse-rpms-0.0.7betaupdateNUM.tar.gz | tar xf -
```

(8) You'll need to clone this repo (sgug-rse) -

```
cd ~
/usr/sgug/bin/git clone https://github.com/sgidevnet/sgug-rse.git sgug-rse.git
```
Adjust that path as appropriate for where you wish the repo to live.

(Of course you can fork the repo and clone from your own copy!)

(9) Now you can install all packages (you can pick and choose if that's your thing):

```
/usr/sgug/bin/sgugshell
cd ~/rpmbuild/RPMS
sudo rpm --reinstall -ivh noarch/*.rpm mips/*.rpm
```

and for any upgrades/updates:

* CARE: You must use the "upgrade" flag for any upgraded packages to avoid double-installs

```
/usr/sgug/bin/sgugshell
cd ~/rpmupdates/RPMS
sudo rpm -Uvh noarch/*.rpm mips/*.rpm
```

(10) Now you can rebuild one of the out-of-the-box packages with:

```
/usr/sgug/bin/sgugshell
cd ~/rpmbuild/SPECS
rpm -ivh ../SRPMS/m4-1.4.18-11.sgugbeta.src.rpm
cp -r ~/sgug-rse.git/packages/m4/* ~/rpmbuild/
rpmbuild -ba m4.spec --nocheck
```

(11) Installing RPMs must be done as root (add `--reinstall` to refresh an already installed package):

```
/usr/sgug/bin/sgugshell
sudo rpm -ivh ~/rpmbuild/RPMS/mips/m4*.rpm
```

## Bugs

There will be bugs, I'm afraid. This platform is relatively new, much as the GCC underpinning it is. Please do file an issue for things you find - it helps a lot to double check there isn't already one for the problem you have.

Feel free to contact us on the forums or in discord and we may be able to help.
