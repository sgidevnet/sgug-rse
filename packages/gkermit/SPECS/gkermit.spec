Name:           gkermit
Version:        1.00
Release:        25%{?dist}
Summary:        A utility for transferring files using the Kermit protocol
License:        GPLv2+
URL:            http://www.kermitproject.org/gkermit.html
Source0:        ftp://kermit.columbia.edu/kermit/archives/gku100.tar.gz

# Fedora-specific patches:
# Patch makefile to handle of CC, CFLAGS, install directory variables per
# Fedora packaging spec, and to not install gkermit.txt as that will be
# handled as a doc file.
# and 
Patch0:         gkermit-1.00-makefile.patch

# Patch to use stdlib.h, string.h, and unistd.h headers, rather than
# assuming the argument profiles of various standard library functions.
Patch1:         gkermit-1.00-std_headers.patch

# NOT patching incorrect FSF address as reported by rpmlint.  As of
# 14-JUL-2012, policy states that only upstream notification is required.
# Upstream was notified by email on 14-JUL-2012, and a reply was received
# the same day stating that the address will not be changed.

BuildRequires:  gcc
%description
G-Kermit is a utility for file transfer using the Kermit protocol,
supporting text and binary transfers on 7-bit and 8-bit connections.
It is most useful as a remote endpoint; for a more fully-featured Kermit
program, use the ckermit package.

%prep
%setup -q -c
%patch0 -p1 -b .makefile
%patch1 -p1 -b .std_headers

%build
# Unfortunately we cannot use smp_mflags because Makefile isn't SMP-safe.
# With smp_mflags, make will attempt to run generated programs such as
# ./gwart before they have been compiled.
make RPM_CFLAGS="%{optflags} -DERRNO_H"

%install
install -d -m0755 %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc ANNOUNCE COPYING README
%{_bindir}/gkermit
%{_mandir}/man1/gkermit.1*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 30 2014 Eric Smith <brouhaha@fedoraproject.org>  1.00-16
- Updated URL.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Eric Smith <brouhaha@fedoraproject.org>  1.00-11
- Added description of patches per package review comments.

* Fri Jul 13 2012 Eric Smith <brouhaha@fedoraproject.org>  1.00-10
- Updated to current Fedora packaging standards.

* Mon Jul  9 2001 Tim Powers <timp@redhat.com>
- when you rebuild, add a changelog entry and bump the release #

* Tue Dec 19 2000 Philipp Knirsch <pknirsch@redhat.de>
- rebuild

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 26 2000 Nalin Dahyabhai <nalin@redhat.com>
- Remove the setgid bit. (#11870)

* Mon Jun  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- FHS fixes.

* Wed May 10 2000 Tim Powers <timp@redhat.com>
- quiet setup
- rebuilt for 7.0

* Sun Feb 27 2000 Cristian Gafton <gafton@redhat.com>
- make gkermit setgid uucp

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Thu Jan 13 2000 Cristian Gafton <gafton@redhat.com>
- create first version of the package
