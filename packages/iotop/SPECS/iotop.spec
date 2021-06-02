Name: iotop
Version: 0.6
Release: 20%{?dist}
Summary: Top like utility for I/O       
License: GPLv2+
URL: http://guichaz.free.fr/iotop/            
Source0: http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2

# rhbz#1035503
Patch0: iotop-0.6-noendcurses.patch
Patch1: iotop-0.6-python3.patch

# Fix build error with Python 3 caused by itervalues() in setup.py
# http://repo.or.cz/iotop.git/commit/99c8d7cedce81f17b851954d94bfa73787300599
Patch2:	iotop-python3build.patch

# sent upstream, iotop <= 0.6, rhbz#1285088
Patch3: iotop-0.3.2-batchprintutf8.patch

BuildArch: noarch
BuildRequires:	python3-devel

%description
Linux has always been able to show how much I/O was going on
(the bi and bo columns of the vmstat 1 command).
iotop is a Python program with a top like UI used to
show of behalf of which process is the I/O going on.

%prep
%setup -n %{name}-%{version}
%patch0 -p1 -b .noendcurses
%patch1 -p1 -b .python3
%patch2	-p1
%patch3 -p1 -b .batchprintutf8

%build
%py3_build

%install
%py3_install

%files -n %{name}
%doc NEWS THANKS README ChangeLog
%license COPYING
%{python3_sitelib}/*
%{_sbindir}/iotop
%{_mandir}/man8/iotop.*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-17
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6-13
- Rebuild for Python 3.6

* Mon Nov 14 2016 Michal Hlavinka <mhlavink@redhat.com> - 0.6-12
- fix printing unicode strings in batch mode (#1285088)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 29 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.6-10
- SPEC file cleanup
- Added licence tag
- Removal of old and unneeded macros
- Use of newest python macros
- Removed Python 2 dependency
- Added patch for Python 3 build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Adel Gadllah <adel.gadllah@gmail.com> - 0.6-8
- Fix python3 patch

* Sun Nov 15 2015 Adel Gadllah <adel.gadllah@gmail.com> - 0.6-7
- Rebuilt with python3 - RH#1282262

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Michal Hlavinka <mhlavink@redhat.com> - 0.6-5
- always ignore nocbreak errors, there is way too many false positives (#1035503)

* Wed Dec 03 2014 Michal Hlavinka <mhlavink@redhat.com> - 0.6-4
- ignore curses failures during termination (#1035503)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Michal Hlavinka <mhlavink@redhat.com> - 0.6-1
- iotop updated to 0.6

* Tue Feb 05 2013 Michal Hlavinka <mhlavink@redhat.com> - 0.5-1
- iotop updated to 0.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Michal Hlavinka <mhlavink@redhat.com> - 0.4.4-1
- iotop updated to 0.4.4

* Fri Oct 14 2011 Michal Hlavinka <mhlavink@redhat.com> 0.4.3-3
- fix typo in last patch

* Thu Oct 13 2011 Michal Hlavinka <mhlavink@redhat.com> 0.4.3-2
- after CVE-2011-2494 fix, iotop needs root privileges

* Sun Sep 18 2011 Adel Gadllah <adel.gadllah@gmail.com> 0.4.3-1
- New upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jan 12 2010 Adel Gadllah <adel.gadllah@gmail.com> 0.4-1
- New upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.3-1
- New upstream version
- fixes RH #475917

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.1-2
- Rebuild for Python 2.6

* Wed Jul 09 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2.1-1
- Update to 0.2.1

* Mon Jul 07 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2-2
- New upstream tarball..

* Mon May 26 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2-1
- Update to new upstream version

* Fri Dec 28 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-3
- Fix build issue

* Fri Dec 28 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-2
- Fix traceback on xterm-color RH #400071

* Sat Nov 3 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-1
- Fix version

* Sat Nov 3 2007 Adel Gadllah <adel.gadllah@gmail.com> 20070930-1
- Initial Build
