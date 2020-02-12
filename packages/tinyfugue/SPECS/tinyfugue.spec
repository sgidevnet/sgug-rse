%global packageversion 50b8

Name:    tinyfugue
Version: 5.0
Release: 0.32.b8%{?dist}
Summary: A MU* client
License: GPLv2+
URL:     http://tinyfugue.sourceforge.net/
Source:  http://downloads.sourceforge.net/tinyfugue/tf-%{packageversion}.tar.gz
Patch0:  tf-50b7.build.patch
Patch1:  tf-50b8.x86_64.patch
Patch100: tinyfugue508.irix.patch
# https://sourceforge.net/tracker/?func=detail&aid=3486514&group_id=186112&atid=915972
Patch2:  tf-50b8.pcre.patch
BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: sed

%description
TinyFugue is the ubiquitous MUD/MOO/MUSH/MUCK/etc client for UNIX. This client
allows you to interact with multiple worlds simultaneously, create command
macros, and create hooks and triggers for automated responses to game messages.

%prep
%setup -q -n tf-%{packageversion}
# TinyFugue's build system is abysmal. Kluge it to honor $DESTDIR
%patch0 -p1
# x86_64 fix (#743468)
%patch1 -p1
# Unbundle the old PCRE and update to 8.30
%patch2 -p1
%patch100 -p1
rm -rf src/pcre-2.08

%build
%configure --enable-core
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}
install -D -p -m 644 src/tf.1.nroffman %{buildroot}%{_mandir}/man1/tf.1

%files
%doc CHANGES COPYING CREDITS README
%{_bindir}/tf
%{_datadir}/tf-lib/
%{_mandir}/man1/tf.1*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.32.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.31.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.30.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Petr Šabata <contyk@redhat.com> - 5.0-0.29.b8
- Adding missing build dependencies (coreutils and sed used in configure, gcc
  needed for build)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.28.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.27.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.26.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.25.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-0.24.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.23.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.22.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.21.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.20.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.19.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.18.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Šabata <contyk@redhat.com> - 5.0-0.17.b8
- Unbundle pcre-2.08 (duh) and patch for 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.16.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Petr Sabata <contyk@redhat.com> - 5.0-0.15.b8
- Don't crash on /ps @ x86_64 (#743468)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.14.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 5.0-0.13.b8
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.12.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-0.11.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 5.0-0.10.b8
- rebuild with new openssl

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0-0.9.b8
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0-0.8.b8
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 5.0-7
 - Rebuild for deps

* Thu Feb 15 2007 Callum Lerwick <seg@haxxed.com> - 5.0-0.6.b8
- New upstream version.

* Tue Jan 09 2007 Callum Lerwick <seg@haxxed.com> - 5.0-0.6.b7
- Add ncurses-devel BR, fixes #221762.

* Tue Sep 05 2006 Callum Lerwick <seg@haxxed.com> - 5.0-0.5.b7
- Bump for FC6 mass rebuild.

* Wed Apr 05 2006 Callum Lerwick <seg@haxxed.com> - 5.0-0.4.b7
- Pass --enable-core to configure so we get a useful debuginfo package.

* Sun Mar 05 2006 Callum Lerwick <seg@haxxed.com> - 5.0-0.3.b7
- Added {?dist} to Release.

* Wed Feb 22 2006 Callum Lerwick <seg@haxxed.com> - 5.0-0.2.b7
- Removed Epoch.

* Sun Jan 29 2006 Callum Lerwick <seg@haxxed.com> - 0:5.0-0.1.b7
- Initial packaging.
