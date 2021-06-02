Name:		distribution-gpg-keys
Version:	1.44
Release:	1%{?dist}
Summary:	GPG keys of various Linux distributions

License:	CC0
URL:		https://github.com/xsuchy/distribution-gpg-keys
# Sources can be obtained by
# git clone git://github.com/xsuchy/distribution-gpg-keys.git
# cd distribution-gpg-keys
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%if 0%{?fedora} > 0
Suggests:	ubu-keyring
Suggests:	debian-keyring
Suggests:	archlinux-keyrings
Suggests:   %{name}-copr
%endif

%description
GPG keys used by various Linux distributions to sign packages.

%package copr
Summary: GPG keys for Copr projects
BuildArch: noarch

%description copr
GPG keys used by Copr projects.

%prep
%setup -q


%build
#nothing to do here


%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/


%files
%license LICENSE
%doc README.md SOURCES.md
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/copr

%files copr
%license LICENSE
%{_datadir}/%{name}/copr

%changelog
* Mon Oct 19 2020 Miroslav Suchý <msuchy@redhat.com> 1.44-1
- update copr keys
- update link to fedora rawhide
- add Fedora ELN keys
- add Zoom gpg key
- Add Oracle Linux GPG keys

* Wed Oct 07 2020 Miroslav Suchý <msuchy@redhat.com> 1.43-1
- now really add f33
- add f33 releasers

* Mon Oct 05 2020 Miroslav Suchý <msuchy@redhat.com> 1.42-1
- update copr keys
- add rpmfusion 33 and update latest links

* Thu Aug 06 2020 Miroslav Suchý <msuchy@redhat.com> 1.41-1
- add Fedora 34 key
- update copr keys
- add Qubes signing keys

* Mon Jul 13 2020 Miroslav Suchý <msuchy@redhat.com> 1.40-1
- update copr keys
- Add Datto's third party repository GPG keys
- Add EuroLinux keys

* Thu May 28 2020 Miroslav Suchý <msuchy@redhat.com> 1.39-1
- update copr keys
- add intel gpg key
- add RosaLinux GPG keyring

* Tue Apr 21 2020 Miroslav Suchý <miroslav@suchy.cz> 1.38-1
- update copr keys
- add mysql gpg key
- add BlueJeans key
- Add symlink from CentOS 8 to CentOS Official key
- add remi 2020 key and update for f32 branch

* Tue Feb 18 2020 Miroslav Suchý <msuchy@redhat.com> 1.37-1
- update copr keys
- f29 is eoled
- Symlink Rawhide to Fedora 33 key
- Add remi 2020 key

* Wed Jan 29 2020 Miroslav Suchý <msuchy@redhat.com> 1.36-1
- update copr keys
- add Fedora 33 gpg key
- Add keys for IUS repository (https://ius.io)

* Thu Sep 26 2019 Miroslav Suchý <msuchy@redhat.com> 1.35-1
- update copr keys
- Add key for Amazon Linux 2

* Tue Aug 20 2019 Miroslav Suchý <msuchy@redhat.com> 1.34-1
- update copr keys
- fix whitespace error in fedora-32 key (rhbz#1743422)
- Add RPM Fusion keys for fedora 32

* Fri Aug 16 2019 Miroslav Suchý <msuchy@redhat.com> 1.33-1
- add EPEL-8
- add CentOS 8 keys
- add Fedora 32 key

* Mon Jul 08 2019 Miroslav Suchý <msuchy@redhat.com> 1.32-1
- Update Copr keys
- Add OpenMandriva package signing key
- add Zimbra key

* Thu May 16 2019 Miroslav Suchý <msuchy@redhat.com> 1.31-1
- update Copr keys

* Thu Apr 11 2019 Miroslav Suchý <msuchy@redhat.com> 1.30-1
- Deleted old Copr keys and added new Copr keys
- readme: add note about Debian, Ubuntu and Arch
- update list of keys in README
- add brave key
- Add remi 2019 key

* Tue Feb 19 2019 Miroslav Suchý <msuchy@redhat.com> 1.29-1
- update Copr keys
- add F31 key and point rawhide to F31
- add Fedora iot keys

* Thu Jan 31 2019 Miroslav Suchý <msuchy@redhat.com> 1.28-1
- update copr keys
- Add cuda 2019 - el8 - fedora 31 keys (rpmfusion)

* Wed Jan 02 2019 Miroslav Suchý <msuchy@redhat.com> 1.27-1
- update copr keys

* Fri Nov 16 2018 Miroslav Suchý <msuchy@redhat.com> 1.26-1
- add RPM-GPG-KEY-redhat8-release

* Thu Nov 15 2018 Miroslav Suchý <msuchy@redhat.com> 1.25-1
- update copr keys
- add RPM-GPG-KEY-redhat8-beta key
- add RPM-GPG-KEY-redhat-auxiliary2

* Thu Nov 08 2018 Miroslav Suchý <msuchy@redhat.com> 1.24-1
- update Copr keys
- add Microsoft key

* Fri Sep 14 2018 Miroslav Suchý <msuchy@redhat.com> 1.23-1
- update copr keys
- add rawhide as symlink to F30

* Sun Aug 12 2018 Miroslav Suchý <msuchy@redhat.com> 1.22-1
- update copr keys
- add fedora 30

* Tue Apr 24 2018 Miroslav Suchý <msuchy@redhat.com> 1.21-1
- Add openSUSE Package Signing Key

* Mon Apr 16 2018 Miroslav Suchý <msuchy@redhat.com> 1.20-1
- add scientific linux key
- update copr keys
- add Fedora 29 key
- Update keys for rpmfusion
- Add rpmfusion f29 f30 keys for free nonfree

* Wed Feb 21 2018 Miroslav Suchý <msuchy@redhat.com> 1.19-1
- update copr keys

* Sun Jan 21 2018 Miroslav Suchý <msuchy@redhat.com> 1.18-1
- add UnitedRPMs
- Add remi 2018 key
- update Copr keys

* Thu Dec 21 2017 Miroslav Suchý <msuchy@redhat.com> 1.17-1
- update Copr keys

* Mon Nov 20 2017 Miroslav Suchý <msuchy@redhat.com> 1.16-1
- update Copr keys

* Tue Sep 19 2017 Miroslav Suchý <msuchy@redhat.com> 1.15-1
- update Copr keys
- add new remi key

* Mon Aug 21 2017 Miroslav Suchý <msuchy@redhat.com> 1.14-1
- update Copr keys
- add remi's repository gpg key
- add jpackage gpg key
- add CalcForge gpg key
- add virtualbox gpg key
- add PostgreSQL RPM Building Project gpg keys
- add Skype gpg key
- add Google gpg key
- add dell public key
- add RPM-GPG-KEY-adobe-linux
- add Dropbox gpg key
- add RPM-GPG-KEY-fedora-28-primary
- add rpmfusion 28

* Mon Jul 31 2017 Miroslav Suchý <msuchy@redhat.com> 1.13-1
- update Copr keys
- add fedora modularity gpg key
- add SCL SIG key

* Thu Jul 13 2017 Miroslav Suchý <msuchy@redhat.com> 1.12-1
- update Copr keys
- Update Red Hat Keys

* Mon Apr 03 2017 Miroslav Suchý <msuchy@redhat.com> 1.11-1
- update Copr keys
- update source for rpmfusion
- Update symlinks for rpmfusion lastest/rawhide
- Add rpmfusion free/nonfree 27 keys
- Add rpmfusion free/nonfree 26 keys

* Thu Mar 16 2017 Miroslav Suchý <msuchy@redhat.com> 1.10-1
- update COPR keys
- add F27 key

* Thu Dec 01 2016 Miroslav Suchý <msuchy@redhat.com> 1.9-1
- add new copr keys
- add Fedora 26 keys
- add more CentOS 7 keys (aarch64, debug, SIGs, testing)

* Mon Oct 24 2016 Miroslav Suchý <miroslav@suchy.cz> 1.8-1
- update copr gpg keys
- README.md: Indicate what keys are actually included
- add rpmfusion F19 keys
- add note how to verify gpg key using fingerprint
- RPMFusion add fedora-20 and fedora-21 keys
- RPMFusion add rpmfusion el-7 keys
- RPMFusion add fedora-25 keys
- use symbol links .
- Add a crucial information to README.md

* Mon Sep 12 2016 Miroslav Suchý <msuchy@redhat.com> 1.7-1
- do not use weak deps on rhel

* Mon Sep 12 2016 Miroslav Suchý <msuchy@redhat.com> 1.6-1
- Rename mageia pubkey to RPM-GPG-KEY-Mageia

* Mon Aug 08 2016 Miroslav Suchý <msuchy@redhat.com> 1.5-1
- move copr keys to subpackage
- update copr gpg keys
- add RPM-GPG-KEY-CentOS-SIG-AltArch-7-ppc64le
- add F25 keys

* Mon Mar 14 2016 Miroslav Suchý <msuchy@redhat.com> 1.4-1
- update SOURCES
- update copr gpg keys
- add mageia gpg keys

* Tue Feb 02 2016 Miroslav Suchý <msuchy@redhat.com> 1.3-1
- add copr keys
- added obsolete gpg keys
- document from where those keys can be originally obtained
- suggest installations of other keyrings
- do not include email in changelog items

* Fri Oct 16 2015 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- document how to do release
- change license to CC-0

* Thu Oct 15 2015 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- initial package



