Summary:        Sgugrse package repositories
Name:           sgugrse-repos
Version:        0.0.7beta
Release:        3%{?_module_build:%{?dist}}
License:        MIT
URL:            https://sgugrseproject.org/

Provides:       sgugrse-repos(%{version})
Requires:       system-release(%{version})
Requires:       sgugrse-gpg-keys >= %{version}-%{release}
BuildArch:      noarch

#Source1:        archmap
Source2:        sgugrselocal.repo
Source3:        sgugrse.repo
Source4:        sgugrse-updates.repo
Source5:        sgugrse-updates-testing.repo

Source10:       RPM-GPG-KEY-sgugrse-primary

Source151:      sgugrse.conf

%description
Sgugrse package repository files for yum and dnf along with gpg public keys

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

# and add symlink for compat generic location
ln -s RPM-GPG-KEY-sgugrse-primary RPM-GPG-KEY-sgugrse-%{version}-primary
# and symlinks for various repo needs
ln -s RPM-GPG-KEY-sgugrse-primary RPM-GPG-KEY-sgugrse-%{version}-mips

cd $PREV_WD

install -d -m 755 $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d
install -m 644 %{_sourcedir}/sgugrselocal.repo $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d
install -m 644 %{_sourcedir}/sgugrse.repo $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d
install -m 644 %{_sourcedir}/sgugrse-updates.repo $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d
install -m 644 %{_sourcedir}/sgugrse-updates-testing.repo $RPM_BUILD_ROOT/usr/sgug/etc/yum.repos.d

# Install ostree remote config
install -d -m 755 $RPM_BUILD_ROOT/usr/sgug/etc/ostree/remotes.d/
install -m 644 %{_sourcedir}/sgugrse.conf $RPM_BUILD_ROOT/usr/sgug/etc/ostree/remotes.d/

%files
%dir /usr/sgug/etc/yum.repos.d
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrselocal.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-updates.repo
%config(noreplace) /usr/sgug/etc/yum.repos.d/sgugrse-updates-testing.repo

%files -n sgugrse-gpg-keys
%dir /usr/sgug/etc/pki/rpm-gpg
/usr/sgug/etc/pki/rpm-gpg/RPM-GPG-KEY-*


%files ostree
%dir /usr/sgug/etc/ostree/remotes.d/
/usr/sgug/etc/ostree/remotes.d/sgugrse.conf

%changelog
* Fri Dec 18 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7beta-3
- Update with real test amazon aws repo but leave disabled

* Thu Dec 17 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7beta-2
- Disable test repos, enable local repo for microdnf installs

* Wed Dec 16 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7beta-1
- Enable update and test update repos

* Mon Dec 14 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7alpha-2
- Enable a single repository while we are testing, disable gpg checking for now.

* Tue Nov 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.0.7alpha-1
- Use a temporary key while in testing phase

* Sat Aug 22 2020 Daniel Hams <daniel.hams@gmail.com> - 1-1
- Initial setup

