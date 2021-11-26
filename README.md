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

**NOTE**: While we are not yet out of beta, it is recommended to remove any previous sgug-rse installation before extracting this new one. We don't yet support in-place upgrades using RPMs:

```shell
# As root
rm -rf /usr/sgug/*
```

**(1)** Add your user account to the irix `sys` group - this will allow you to use the sgug `sudo` out of the box with your user password - then you can follow the steps below without additional hoop jumping.

Need help with setting up sudo? Please see our [troubleshooting guide](troubleshooting.md).



**(2)** Ensure your system can cope with long command line buffers:

```shell
# As root
su -
# Show existing value
systune ncargs
# Tweak if < 262144
systune ncargs 262144
```

**(3)** Download the artifacts for the latest version from the github releases tab (assuming they aren't too big).

You'll find three main archives:

```shell
sgug-rse-selfhoster-0.0.7beta.tar.gz
sgug-rse-localrepo-0.0.7beta.tar.gz
```

**(4)** Extract the selfhoster and local repo archives under `/usr` as root (important, sgug-rse _installation_ files are root owned and managed):

```shell
su -  #(enter root password)
cd /usr
gunzip -dc /path/to/sgug-rse-selfhoster-0.0.7beta.tar.gz | tar xf -
gunzip -dc /path/to/sgug-rse-localrepo-0.0.7beta.tar.gz | tar xf -
(log out of root)
```

**(5)** Setup SGUG environment.

```shell
TODO
```

**(6)** Now you can search for and install sgug RPM packages. Note that you have to be root in order for the `tdnf` tool to work:

```shell
sudo tdnf install mpg123
```
```
Installing:
mpg123-libs                    mips            1.25.10-2.sgug       sgugrselocal    425.17k 435369
mpg123                         mips            1.25.10-2.sgug       sgugrselocal    249.11k 255085

Total installed size: 674.27k 690454
Is this ok [y/N]:

Downloading:
mpg123-libs                             225085   100%
mpg123                                  129151   100%
Testing transaction
Running transaction
Installing/Updating: mpg123-libs-1.25.10-2.sgug.mips
Installing/Updating: mpg123-1.25.10-2.sgug.mips

Complete!
```

You can search for packages with:

```shell
sudo tdnf search mpg123
```
```
mpg123 : Real time MPEG 1.0/2.0/2.5 audio player/decoder for layers 1, 2 and 3
mpg123-devel : Real time MPEG 1.0/2.0/2.5 audio player/decoder for layers 1, 2 and 3
mpg123-libs : Real time MPEG 1.0/2.0/2.5 audio player/decoder for layers 1, 2 and 3
```

## (Re-)build RPMs from Source

You can rebuild any of the existing package from source, for example if you want to try out different build options. For that you need to install the source RPM archive (`sgug-rse-srpms`) in addition to the `sgug-rse-selfhoster` and `sgug-rse-localrepo`.

You want to contribute a new package to the sgug-rse repository? That's great! Please check out the [contribution guidelines](./contributing.md) for more details.

**(1)** Before you start, make sure you are in sgugshell:

```shell
/usr/sgug/bin/sgugshell
```

**(2)** Install common build tools:

```shell
sudo tdnf install wget rpm-build autoconf automake libtool gcc gcc-c++
```

**(3)** Create build directories in your user's home:

```shell
mkdir -p ~/rpmbuild/SPECS
mkdir -p ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SRPMS
mkdir -p ~/rpmbuild/RPMS
```

**(4)** Download the source RPM archive for the latest version
(`sgug-rse-srpms-x.y.z.tar.gz`) from the [Github releases tab](https://github.com/sgidevnet/sgug-rse/releases) and extract it into the build directory: 

```shell
cd /tmp
wget https://github.com/sgidevnet/sgug-rse/releases/download/v0.0.7beta/sgug-rse-srpms-0.0.7beta.tar.gz

cd ~/rpmbuild
gunzip -dc /tmp/sgug-rse-srpms-0.0.7beta.tar.gz | tar xf -
```

**(5)** To rebuild an RPM package you first have to install the SRPM of the package (in this example we will rebuild mpg123):

```shell
cd ~/rpmbuild/
rpm -ivh ~/rpmbuild/SRPMS/mpg123-1.25.10-2.sgug.src.rpm
```

You can modify the specfile locally in the `~/rpmbuild/SPECS/` directory if you want to try out different build options.
Now you can run `rpmbuild` on the package's specfile:

```shell
cd ~/rpmbuild/
rpmbuild -ba ~/rpmbuild/SPECS/mpg123.spec --nocheck
```

**(6)** After building, install of fresh RPMs must be done as root (add `--reinstall` to refresh an already installed package):

```shell
sudo rpm -ivh ~/rpmbuild/RPMS/mips/m4*.rpm
```

## Bugs

There will be bugs, I'm afraid. This platform is relatively new, much as the GCC underpinning it is. Please do file an issue for things you find - it helps a lot to double check there isn't already one for the problem you have.

Feel free to contact us on the forums or in discord and we may be able to help.
