%global tilp_version 1.18

Name:           libticonv
Version:        1.1.5
Release:        8%{?dist}
Summary:        Texas Instruments calculators charsets library

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        http://sourceforge.net/projects/tilp/files/tilp2-linux/tilp2-%{tilp_version}/%{name}-%{version}.tar.bz2

BuildRequires:  glib2-devel, pkgconfig, tfdocgen
BuildRequires:  autoconf, automake, libtool

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc

Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description
The ticonv library is a library capable of conversions between
Texas Instruments character sets and UTF-8/UTF-16 character sets.

%description devel
Include files and libraries for linking and developing
applications using libticonv.

%description doc
HTML documentation for linking and developing applications
using libticonv.

%prep
%setup -q
# Fix wrong EOF encodings.
sed -i 's/\r$//' README
sed -i 's/\r$//' ChangeLog
sed -i 's/\r$//' AUTHORS
sed -i 's/\r$//' docs/html/clean.bat
sed -i 's/\r$//' docs/html/style.css

# Invoke autoconf.
libtoolize
aclocal
autoheader
automake --add-missing
autoconf

%build
%configure --disable-static --enable-iconv
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libticonv.la
make -C docs install DESTDIR=%{buildroot}
rm %{buildroot}/%{_pkgdocdir}/COPYING

%ldconfig_scriptlets

%files
%{_libdir}/libticonv.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%license COPYING

%files doc
%doc %{_pkgdocdir}/html/
%doc %{_pkgdocdir}/charsets/

%files devel
%{_libdir}/libticonv.so
%{_libdir}/pkgconfig/ticonv.pc
%{_includedir}/tilp2/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.1.5-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 4 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.4-5
- Switched to using global instead of define for macros.
- Package now owns its documentation directory.
- Tests are now ran in the check section of the specfile.

* Fri Feb 27 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.4-4
- Fixed doc subpackage to be noarch and not contain duplicate files.

* Mon Feb 16 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.4-3
- Added a doc subpackage for the HTML documentation.

* Tue Feb 10 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.4-2
- Added license tag for COPYING license text.

* Mon Feb 2 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.4-1
- Updated to latest upstream tilp version

* Wed Jul 11 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.3-5
- Added full documentation, built by tfdocgen

* Wed Jun 20 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.3-4
- Removed libtool archives from compilation
- Added versioned Require for libticonv-devel

* Tue Jun 19 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.3-3
- devel subpackage now requires the parent package, as is proper

* Tue Jun 19 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.3-2
- Added libticonv-devel subpackage
- Fixed description line's length

* Tue Jun 19 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.3-1
- libticonv will take ownership of /usr/include/tilp2

* Tue Jun 19 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.3-0
- Updated to 1.1.3, vastly improved specfile

* Sat Jul 30 2011 'Ben Rosser' <rosser.bjr@gmail.com> 1.1.2-0
- Initial version of the package
