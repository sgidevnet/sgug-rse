Name:           libzeitgeist
Version:        0.3.18
Release:        18%{?dist}
Summary:        Client library for applications that want to interact with the Zeitgeist daemon

License:        LGPLv3 and GPLv3
URL:            https://launchpad.net/libzeitgeist
Source0:        http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:         %{name}-disable-log-test.patch

# fixes env problem (mtasaka)
# https://bugzilla.gnome.org/show_bug.cgi?id=704593
Patch1:         %{name}-tests-glib-2.40-envnull.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= 2.26
BuildRequires:  gtk-doc

%description
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package        devel
Summary:        Development files for %{name}%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%configure --disable-static
make V=1 %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -d -p -m 755 %{buildroot}%{_datadir}/vala/vapi
install -D -p -m 644 bindings/zeitgeist-1.0.{vapi,deps} %{buildroot}%{_datadir}/vala/vapi
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove duplicate documentation
rm -fr %{buildroot}%{_defaultdocdir}/%{name}


%ldconfig_scriptlets


%files

# documentation
%doc COPYING COPYING.GPL README

# essential
%{_libdir}/*.so.*


%files devel

# Documentation
%doc AUTHORS ChangeLog COPYING COPYING.GPL MAINTAINERS NEWS 
%doc examples/*.vala examples/*.c
%{_datadir}/gtk-doc/html/zeitgeist-1.0/

# essential
%{_includedir}/zeitgeist-1.0/
%{_libdir}/pkgconfig/zeitgeist-1.0.pc
%{_libdir}/*.so

# extra
%{_datadir}/vala/vapi/


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.18-16
- Remove arch-dependent BuildRequires (#1545196)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Renich Bon Ciric <renich@woralelandia.com> - 0.3.18-7
- Fix test by mtasaka; because of https://bugzilla.gnome.org/show_bug.cgi?id=704593.
- Fixes bug 1106094
- Using autosetup instead of setup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Renich Bon Ciric <renich@woralelandia.com> - 0.3.18-3
- removed require on Zeitgeist

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 5 2012 Renich Bon Ciric <renich@woralelandia.com> - 0.3.18-1
- Updated to version 0.3.18.
- Disabled a log test since it's failing because no libzeitgeist daemon is present at build time.
- Added missing Result Type constant (*CurrentUri and *EventOrigin).
- Now async functions fail instead of lingering indefinitely if Zeitgeist isn't available.

* Mon Mar 19 2012 Renich Bon Ciric <renich@woralelandia.com> - 0.3.14-1
- Updated to version 0.3.14
- Update to shared-desktop-ontologies-0.8
- Return relevancies of events when searching index
- Update the ZeitgeistEvent and ZeitgeistSubject with event origin and subject current uri
- Zeitgeist isn't autostarted after it disappears
- Removed log-fix patch

* Wed Apr 06 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.10-1
- Updated to version 0.3.10
- Fixed bugs:
    https://bugs.launchpad.net/ubuntu/+source/libzeitgeist/+bug/742438
- Renamed log fix patch to something more appropriate

* Sat Apr 02 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-4
- Added -p to install statements (forgot some)
- Moved README to the main package from devel

* Fri Mar 25 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-3
- Removed Rubys geo2 dependency since is not needed; it's provided by glibc-devel

* Thu Mar 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-2
- Log test failure repaired by patch from Mamoru Tasaka

* Mon Mar 21 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-1
- Updated to 0.3.6
- Implemented the isa macro for the devel subpackage.
- Eliminated the doc macro from gtk-doc since it gets marked automatically

* Sat Mar 12 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-3
- Removed mistaken isa macro from zeitgeist require

* Thu Mar 10 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-2
- Cleaned up old stuff (BuildRoot, Clean and stuff of sorts)
    https://fedoraproject.org/wiki/Packaging/Guidelines#BuildRoot_tag
    https://fedoraproject.org/wiki/Packaging/Guidelines#.25clean
- Added glib2-devel and gtk-doc as a BuildRequires
- Added GPLv3 since it covers the documentation examples
- Updated Requires to use the new arch specification macro when accordingly
    https://fedoraproject.org/wiki/Packaging/Guidelines#Requires
- Configured install to preserve timestamps
- Added V=1 to the make flags for more verbosity on build
- Added a check section
- Removed disable-module from configure statement since it's not needed anymore: 
    https://bugs.launchpad.net/libzeitgeist/+bug/683805

* Thu Feb 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-1
- updated to latest version

* Sun Feb 06 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-3
- got rid of INSTALL from docs
- got rid ot dorcdir and used doc to include html docs

* Sat Feb 05 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-2
- removed duplicate documentation
- added the use of macros for everything; including source and build dir.
- revised path syntax

* Thu Jan 27 2011 - Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-1
- First buildName:           libzeitgeist
