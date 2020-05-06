Name:           ncdu
Version:        1.14.2
Release:        1%{?dist}
Summary:        Text-based disk usage viewer

License:        MIT
URL:            http://dev.yorhel.nl/ncdu/
Source0:        http://dev.yorhel.nl/download/ncdu-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel

Patch100:       ncdu.sgigetcwdfix.patch

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%setup -q
%patch100 -p1 -b .sgigetcwdfix

%build
export CPPFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export DEFAULT_SHELL="%{_bindir}/sh"
%configure --with-ncurses --with-shell=$DEFAULT_SHELL
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_mandir}/man1/ncdu.1*
%doc ChangeLog COPYING
%{_bindir}/ncdu

%changelog
* Tue Apr 21 2020 Daniel Hams <daniel.hams@gmail.com> - 1.14.2-1
- Import into wip

* Tue Feb 11 2020 Richard Fearn <richardfearn@gmail.com> - 1.14.2-1
- Update to new upstream version 1.14.2

* Sun Aug 11 2019 Richard Fearn <richardfearn@gmail.com> - 1.14.1-1
- Update to new upstream version 1.14.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Richard Fearn <richardfearn@gmail.com> - 1.14-1
- Update to new upstream version 1.14 (#1672365)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Richard Fearn <richardfearn@gmail.com> - 1.13-3
- Add BuildRequires: gcc
  (see https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Richard Fearn <richardfearn@gmail.com> - 1.13-1
- Update to new upstream version 1.13 (#1539676)
- Use %%{version} macro in source URL

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 1.12-6
- Remove unnecessary Group: tag

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Richard Fearn <richardfearn@gmail.com> - 1.12-2
- Don't assume man page compression method will be gzip

* Sat Aug 27 2016 Richard Fearn <richardfearn@gmail.com> - 1.12-1
- Update to new upstream version 1.12 (#1370824)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Richard Fearn <richardfearn@gmail.com> - 1.11-1
- Update to new upstream version 1.11 (#1209036)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Richard Fearn <richardfearn@gmail.com> - 1.10-1
- update to new upstream version 1.10 (#962116)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Richard Fearn <richardfearn@gmail.com> - 1.9-1
- update to new upstream version 1.9

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Richard Fearn <richardfearn@gmail.com> - 1.8-1
- update to new upstream version 1.8

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Richard Fearn <richardfearn@gmail.com> - 1.7-1
- update to new upstream version 1.7
- remove unnecessary bits from spec

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 28 2009 Richard Fearn <richardfearn@gmail.com> - 1.6-1
- update to new upstream version 1.6

* Sun Jul 26 2009 Richard Fearn <richardfearn@gmail.com> - 1.5-1
- update to new upstream version 1.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.4-1
- new upstream version

* Fri Apr 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-2
- remove unnecessary Requires:
- use %%configure macro instead of ./configure
- don't need to mark man page as %%doc
- make package summary more descriptive

* Sat Mar  1 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-1
- initial package for Fedora
