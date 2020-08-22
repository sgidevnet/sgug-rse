Summary:        Sgugrse package repositories
Name:           sgugrse-repos
Version:        0.0.6beta
Release:        1%{?_module_build:%{?dist}}
License:        MIT
URL:            https://sgugrseproject.org/

Provides:       sgugrse-repos(%{version})
Requires:       system-release(%{version})
Requires:       sgugrse-gpg-keys >= %{version}-%{release}
Provides:       sgugrse-repos-modular = %{version}-%{release}
BuildArch:      noarch

#Source1:        archmap
Source2:        sgugrse.repo
Source3:        sgugrse-updates.repo
Source4:        sgugrse-updates-testing.repo
#Source5:        sgugrse-rawhide.repo
#Source6:        sgugrse-cisco-openh264.repo

# Source10:       RPM-GPG-KEY-sgugrse-7-primary
# ...
# Source54:       RPM-GPG-KEY-sgugrse-34-primary

Source100:      sgugrse-modular.repo
Source101:      sgugrse-updates-modular.repo
Source102:      sgugrse-updates-testing-modular.repo
#Source103:      sgugrse-rawhide-modular.repo
#Source104:      RPM-GPG-KEY-sgugrse-modularity

#Source150:      RPM-GPG-KEY-sgugrse-iot-2019
Source151:      sgugrse.conf

%description
Sgugrse package repository files for yum and dnf along with gpg public keys

# %package rawhide
# Summary:        Rawhide repo definitions
# Requires:       sgugrse-repos = %{version}-%{release}
# Obsoletes:      sgugrse-release-rawhide <= 22-0.3
# Obsoletes:      sgugrse-repos-rawhide-modular < 29-0.6
# Provides:       sgugrse-repos-rawhide-modular = %{version}-%{release}

# %description rawhide
# This package provides the rawhide repo definitions.


%package -n sgugrse-gpg-keys
Summary:        Sgugrse RPM keys
Obsoletes:      sgugrse-release-rawhide <= 22-0.3

%description -n sgugrse-gpg-keys
This package provides the RPM signature keys.


%package ostree
Summary:        OSTree specific files

%description ostree
This package provides ostree specfic files like remote config from
where client''s system will pull OSTree updates.



%prep
echo "This package is super not finished"
exit 1

%build

%install
rm -rf $RPM_BUILD_ROOT
# Install the keys
install -d -m 755 $RPM_BUILD_ROOT/usr/sgug/etc/pki/rpm-gpg
install -m 644 %{_sourcedir}/RPM-GPG-KEY* $RPM_BUILD_ROOT/usr/sgug/etc/pki/rpm-gpg/

# Link the primary/secondary keys to arch files, according to archmap.
# Ex: if there's a key named RPM-GPG-KEY-sgugrse-19-primary, and archmap
#     says "sgugrse-19-primary: i386 x86_64",
#     RPM-GPG-KEY-sgugrse-19-{i386,x86_64} will be symlinked to that key.
export PREV_WD=`pwd`
cd $RPM_BUILD_ROOT/usr/sgug/etc/pki/rpm-gpg/
# Don't need this for sgugrse - we're mips only
# for keyfile in RPM-GPG-KEY*; do
#     key=${keyfile#RPM-GPG-KEY-} # e.g. 'sgugrse-20-primary'
#     arches=$(sed -ne "s/^${key}://p" %{_sourcedir}/archmap) \
#         || echo "WARNING: no archmap entry for $key"
#     for arch in $arches; do
#         # replace last part with $arch (sgugrse-20-primary -> sgugrse-20-$arch)
#         ln -s $keyfile ${keyfile%%-*}-$arch # NOTE: RPM replaces %% with %
#     done
# done
# and add symlink for compat generic location
ln -s RPM-GPG-KEY-sgugrse-%{version}-primary RPM-GPG-KEY-%{version}-sgugrse
cd $PREV_WD

install -d -m 755 $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d
for file in %{_sourcedir}/sgugrse*repo ; do
  install -m 644 $file $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d
done

# Install ostree remote config
install -d -m 755 $RPM_BUILD_ROOT/usr/sgug/etc/ostree/remotes.d/
install -m 644 %{_sourcedir}/sgugrse.conf $RPM_BUILD_ROOT/usr/sgug/etc/ostree/remotes.d/

%files
%dir /usr/sgug/etc/yum.repos.d
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-modular.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-updates.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-updates-testing.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-modular.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-updates-modular.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-updates-testing-modular.repo

#%%files rawhide
#%%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-rawhide.repo
#%%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-rawhide-modular.repo


%files -n sgugrse-gpg-keys
%dir /usr/sgug/etc/pki/rpm-gpg
/usr/sgug/etc/pki/rpm-gpg/RPM-GPG-KEY-*


%files ostree
%dir /usr/sgug/etc/ostree/remotes.d/
/usr/sgug/etc/ostree/remotes.d/sgugrse.conf

%changelog
* Sat Aug 22 2020 Daniel Hams <daniel.hams@gmail.com> - 1-1
- Initial setup

