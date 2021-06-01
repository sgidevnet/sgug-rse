%global tilp_version 1.18

Name:           libtifiles2
Version:        1.1.7
Release:        8%{?dist}
Summary:        Texas Instruments calculator files library

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        http://sourceforge.net/projects/tilp/files/tilp2-linux/tilp2-%{tilp_version}/%{name}-%{version}.tar.bz2

BuildRequires:  glib2-devel, zlib-devel, pkgconfig, libticonv-devel, tfdocgen, libarchive-devel, gettext
BuildRequires:  autoconf, automake, libtool, gettext-devel

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc

Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description
The tifiles library is a library capable of reading, modifying,
and writing TI formatted files. It can also group/ungroup files.
This library is able to manipulate files in a fairly transparent
fashion. With this library, the developer does not have to worry
about the different file formats.

%description devel
Include files and libraries for developing applications that
make use of libtifiles.

%description doc
HTML documentation for linking and developing applications
using libtifiles2.

%prep
%setup -q
sed -i 's/\r$//' docs/html/style.css
sed -i 's/\r$//' docs/html/clean.bat
rm po/fr.gmo

# Invoke autoconf.
autoreconf --force --install

%build
%configure --disable-static
make %{?_smp_mflags}
make -C po fr.gmo

%check
make check

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libtifiles2.la
make -C docs install DESTDIR=%{buildroot}
# The docs install makefile does this, but we want it to go into
# licenses.
rm %{buildroot}/%{_pkgdocdir}/COPYING
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%{_libdir}/libtifiles2.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%license COPYING

%files doc
%doc %{_pkgdocdir}/html/
%license COPYING

%files devel
%{_libdir}/libtifiles2.so
%{_libdir}/pkgconfig/tifiles2.pc
%{_includedir}/tilp2/export2.h
%{_includedir}/tilp2/files8x.h
%{_includedir}/tilp2/files9x.h
%{_includedir}/tilp2/stdints2.h
%{_includedir}/tilp2/tifiles.h
%{_includedir}/tilp2/types73.h
%{_includedir}/tilp2/types82.h
%{_includedir}/tilp2/types83.h
%{_includedir}/tilp2/types83p.h
%{_includedir}/tilp2/types84p.h
%{_includedir}/tilp2/types85.h
%{_includedir}/tilp2/types86.h
%{_includedir}/tilp2/types89.h
%{_includedir}/tilp2/types89t.h
%{_includedir}/tilp2/types92.h
%{_includedir}/tilp2/types92p.h
%{_includedir}/tilp2/typesnsp.h
%{_includedir}/tilp2/typesv2.h
%{_includedir}/tilp2/typesxx.h

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Ben ROsser <rosser.bjr@gmail.com> - 1.1.7-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 4 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.6-4
- Switched to using global instead of define.
- Package now correctly owns the package documentation directory.
- Test suite is now ran.

* Fri Feb 27 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.6-3
- Fixed a problem where documentation files would be duplicated.
- Made the -doc subpackage noarch and removed dependency on libtifiles2.
- Changed spec to remove prebuild *.gmo file and rebuild it.

* Tue Feb 24 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.6-2
- Fixed localization to use lang_find macro.
- Fixed wrong end of file encodings on some documentation files.

* Mon Feb 23 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.6-1
- Bumped release number.
- Added license tag and missing documentation files.
- Added doc subpackage for the HTML documentation.

* Sat Apr 20 2013 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.6-0
- Updated to latest upstream tilp version

* Wed Jul 11 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.5-3
- Added full documentation, built by tfdocgen

* Wed Jun 20 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.5-2
- Added devel subpackage dependency on parent package

* Wed Jun 20 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.5-1
- Removed libtool archive from package

* Tue Jun 19 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.5-0
- Upgraded to version 1.1.5
- Added a -devel subpackage for the library files
- Vastly improved spec file

* Sat Jul 30 2011 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.4-0
- Initial version of the package

