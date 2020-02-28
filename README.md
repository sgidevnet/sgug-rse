# sgug-rse

Silicon Graphics User Group RPM Software Environment

## Licensing

It is intended that any fedora `.spec` files listed here are under the "Fedora Project Contributor Agreement": https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement.

Notably - fedora specifically mentions spec file licensing here: https://fedoraproject.org/wiki/Licensing:Main#License_of_Fedora_SPEC_Files

Unless otherwise stated, those `.spec` files remain under their original license as per their contribution to Fedora. This project does not attempt to supplant nor change the license of these works.

The modifications from the original fedora `.spec` files fall under the license of the sgug-rse project, namely GPL3.

## How to get this working

NOTE: While we are not yet out of beta, it is recommended to remove any previous sgug-rse installation before extracting this new one. We don't yet support in-place upgrades using RPMs.

(1) Download the artifacts for the latest version from the github releases tab (assuming they aren't too big).

You'll find three main archives - and there might be "update" archives too that need to be extracted:

```
sgug-rse-selfhoster-0.0.4beta.tar.gz
sgug-rse-srpms-0.0.4beta.tar.gz
sgug-rse-rpms-0.0.4beta.tar.gz

sgug-rse-rpms-0.0.4betaupdateNUM.tar.gz
```

(2) Extract the selfhoster archive under /usr as root (important, sgug-rse _installation_ files are root owned and managed):

```
su - (enter root password)
cd /usr
gunzip -dc /path/to/sgug-rse-selfhoster-0.0.4beta.tar.gz |tar xf -
(log out of root)
```

(3) You'll need to setup some new directories for your user:

```
mkdir -p ~/rpmbuild/SPECS
mkdir -p ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SRPMS
mkdir -p ~/rpmbuild/RPMS
```

(4) As your user extract the SRPMs and RPMs in an appropriate place.

```
cd ~/rpmbuild
gunzip -dc /path/to/sgug-rse-srpms-0.0.4beta.tar.gz | tar xf -
gunzip -dc /path/to/sgug-rse-rpms-0.0.4beta.tar.gz | tar xf -
# Optional
mkdir ~/rpmupdates
cd ~/rpmupdates
gunzip -dc /path/to/sgug-rse-rpms-0.0.4betaupdateNUM.tar.gz | tar xf -
```

(5) You'll need to clone this repo (sgug-rse) -

```
cd ~
git clone https://github.com/sgidevnet/sgug-rse.git sgug-rse.git
```
Adjust that path as appropriate for where you wish the repo to live.

(Of course you can fork the repo and clone from your own copy!)

(6) Now you can install all packages (you can pick and choose if that's your thing):

```
cd ~/sgug-rse.git
./sgugshell.sh
cd ~/rpmbuild/RPMS
sudo rpm --reinstall -ivh noarch/*.rpm mips/*.rpm
```

and for any upgrades/updates:

```
cd ~/sgug-rse.git
./sgugshell.sh
cd ~/rpmupdates/RPMS
sudo rpm -Uvh noarch/*.rpm mips/*.rpm
```

(7) Now you can build a package with:

```
cd ~/sgug-rse.git
./sgugshell.sh
cd ~/rpmbuild/SPECS
rpm -ivh ../SRPMS/m4-1.4.18-11.sgugbeta.src.rpm
cp -r ~/sgug-rse.git/packages/m4/* ~/rpmbuild/
rpmbuild -ba m4.spec --nocheck
```

(8) Installing RPMs must be done as root (add `--reinstall` to refresh a package):

```
su -
cd ~user/sgug-rse.git
./sgugshell.sh
rpm -ivh ~/rpmbuild/RPMS/mips/m4*.rpm
```

## Bugs

There will be bugs, I'm afraid. This platform is relatively new, much as the GCC underpinning it is. Please do file an issue for things you find - it helps a lot to double check there isn't already one for the problem you have.

Feel free to contact us on the forums or in discord and we may be able to help.
