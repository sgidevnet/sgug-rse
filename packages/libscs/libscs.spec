Name:           libscs
Version:        1.4.1
Release:        19%{?dist}.2
Summary:        Software Carry-Save Multiple-Precision Library

License:        LGPLv2+
URL:            http://www.ens-lyon.fr/LIP/Arenaire/Ware/SCSLib/
Source0:        http://www.ens-lyon.fr/LIP/Arenaire/Ware/SCSLib/scslib-%{version}.tar.gz
Patch0:         scslib-1.4.1-shared.patch

BuildRequires:  autoconf, automake, libtool
%if 0%{?fedora} > 0 || 0%{?rhel} > 5
BuildRequires:  mpfr-devel, gmp-devel
%endif

%description
The Software Carry-Save (SCS) Library is a fast and lightweight
multiple-precision library.

SCSLib has the following features:

- Multiple-precision
SCSLib is a fixed-precision library, where precision is selected at
compile-time. Out-of-the-box, the library ensures 210 bits of precision
(quad-double).

- Floating-point format
The SCS format is a floating-point format where exponents are machine integers
(usually 32-bit numbers), which ensures a huge exponent range.

- Supported operations
SCSLib currently offers addition/subtraction, multiplication, and an
experimental division, plus all the useful conversion functions.

- IEEE-754 compatibility
The range of SCS numbers includes the range of IEEE double-precision numbers,
including denormals and exceptional cases. Conversions between SCS format and 
IEEE-754 doubles, as well as arithmetic operations, follow the IEEE rules
concerning the exceptional cases. SCS doesn't ensure correct rounding, but
provides conversions to doubles in the four IEEE-754 rounding modes.

- Performance
SCSLib is designed to be fast. With 210 bits, it outperforms MPF for most
operations on most architectures.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%if 0%{?fedora} > 0 || 0%{?rhel} > 5
Requires:       mpfr-devel, gmp-devel
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n scslib-%{version}
%patch0 -p1 -b .shared


%build
# autoreconf required because the patch modifies autoconf files
autoreconf --install --force
%configure --disable-static \
%if 0%{?fedora} > 0 || 0%{?rhel} > 5
	--enable-mpfr --enable-gmp
%endif

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%doc DocsDev/html/*
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-19.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-18.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-17.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-16.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-11.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.1-4.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.4.1-4.1
- rebuild with new gmp

* Mon Feb 21 2011 Tim Niemueller <tim@niemueller.de> - 1.4.1-4
- Do not require mpfr on el5

* Sun Feb 20 2011 Tim Niemueller <tim@niemueller.de> - 1.4.1-3
- Make -devel subpackage depend on mpfr-devel and gmp-devel

* Sat Feb 19 2011 Tim Niemueller <tim@niemueller.de> - 1.4.1-2
- Fix typo in configure flags (mpfs -> mpfr)

* Sat Feb 19 2011 Tim Niemueller <tim@niemueller.de> - 1.4.1-1
- Initial package

