Summary: Shamir's secret sharing scheme
Name: ssss
Version: 0.5
Release: 22%{?dist}.2
License: GPLv2
Url:  http://point-at-infinity.org/%{name}
Source: http://point-at-infinity.org/%{name}/%{name}-%{version}.tar.gz
Source1: ssss.1.gz
BuildRequires:  gcc
BuildRequires: gmp-devel, xmlto

%description
ssss is an implementation of Shamir's secret sharing scheme.  ssss does
both: the generation of shares for a known secret and the reconstruction
of a secret using user provided shares.

%prep
%setup -q 
# fix transposed arguments in memset call
sed -i 's/memset(buf, degree \/ 8 + 1, 0);/memset(buf, 0, degree \/ 8 + 1);/' ssss.c
%build
# Makefile target strips binary
gcc $RPM_OPT_FLAGS -lgmp -o ssss-split ssss.c

%install
rm -rf ${RPM_BUILD_ROOT}
install -d 0755 ${RPM_BUILD_ROOT}%{_bindir} 
install -d 0755 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 0755 ssss-split ${RPM_BUILD_ROOT}%{_bindir}
ln  ${RPM_BUILD_ROOT}%{_bindir}/ssss-split ${RPM_BUILD_ROOT}%{_bindir}/ssss-combine 
install -m 0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1/
ln  ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss-split.1.gz
ln  ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss-combine.1.gz

%files 
%doc doc.html HISTORY LICENSE THANKS ssss.manpage.xml
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-22.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5-7.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 0.5-7.1
- rebuild with new gmp

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-4
- Autorebuild for GCC 4.3

* Wed Aug  8 2007 Paul Wouters <paul@xelerance.com> - 0.5-3
- Fixed a memset swapped argument found by davej
- Updated license field to reflect GPLv2

* Thu Sep 14 2006 Paul Wouters <paul@xelerance.com> - 0.5-2
- Fixed optflags macro call

* Thu Sep 14 2006 Paul Wouters <paul@xelerance.com> - 0.5-1
- Initial package
- Avoid make target because it includes stripping binary
- Include man page as seperate source to avoid needing xmltoman, which
  is a non-existing package in Fedora.
- Create proper links for man pages
