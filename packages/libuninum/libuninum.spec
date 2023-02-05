Summary:       Library for converting unicode strings to numbers
Name:          libuninum
Version:       2.7
Release:       25%{?dist}
# numconv is GPLv2, lib is LGPLv2
License:       GPLv2 and LGPLv2
URL:           http://billposer.org/Software/libuninum.html
Source0:       http://billposer.org/Software/Downloads/libuninum-%{version}.tar.bz2
Patch0:        libuninum-2.7-64bit-clean.patch
BuildRequires:  gcc
BuildRequires: gmp-devel
%description
libuninum is a library for converting Unicode strings to
numbers. Internal computation is done using arbitrary precision
arithmetic, so there is no limit on the size of the integer that can
be converted. The value is returned as an ASCII decimal string, a GNU
MP object, or an unsigned long integer.  Auto-detection of the number
system is provided. The number systems supported include Arabic,
Armenian, Balinese, Bengali, Burmese, Chinese, Cyrillic, Devanagari,
Egyptian, Ethiopic, Glagolitic, Greek, Gujarati, Gurmukhi, Hebrew,
Kannada, Khmer, Klingon, Lao, Limbu, Malayalam, Mongolian, New Tai
Lue, Nko, Old Italic, Old Persian, Odia, Osmanya, Perso-Arabic,
Phoenician, Roman Numerals, Tamil, Telugu, Tengwar, Thai, and Tibetan.

%package       devel
Summary:       Header files, libraries and development documentation for %{name}
Requires:      %{name} = %{version}-%{release}
%description   devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

%prep
%setup -q
%patch0 -p1 -b .64bit-clean

%build
%configure --disable-static --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -D -m 0644 numconv.1 %{buildroot}/%{_mandir}/man1/numconv.1
rm -f %{buildroot}%{_bindir}/NumberConverter.tcl
rm -f %{buildroot}%{_libdir}/libuninum.la

%files
%license COPYING
%doc AUTHORS ChangeLog CREDITS NEWS README README_NUMBERCONVERTER TODO
%doc Examples
%{_bindir}/numconv
%{_libdir}/libuninum.so.*
%{_mandir}/man1/numconv.1*

%files devel
%license COPYING
%{_includedir}/uninum
%{_libdir}/libuninum.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.7-22
- Some clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-21.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-20.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-19.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-18.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-17.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-16.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-15.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-14.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.7-9.1
- rebuild with new gmp without compat lib

* Tue Oct 25 2011 Terje Rosten <terje.rosten@ntnu.no> - 2.7-9
- fix changelog

* Tue Oct 25 2011 Michael J Gruber <mjg@fedoraproject.org> - 2.7-8
- remove rpath for good
- remove unnecessary build link
- fix breakage on x86_64

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 2.7-7.1
- rebuild with new gmp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.7-6
- Use bzipped upstream tarball.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 22 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.7-3
- Rebuild, new tarball upstream
- Remove the tcl tool

* Tue May 20 2008 Terje Rosten <terje.rosten@ntnu.no> - 2.7-2
- Random cleanup

* Wed Dec 19 2007 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
