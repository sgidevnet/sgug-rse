Name:           ascii
Version:        3.18
Release:        7%{?dist}
URL:            http://www.catb.org/~esr/ascii/
Source0:        http://www.catb.org/~esr/ascii/ascii-3.18.tar.gz
BuildRequires:  gcc

License:        GPLv2
Summary:        Interactive ascii name and synonym chart

%description
The ascii utility provides easy conversion between various byte representations
and the American Standard Code for Information Interchange (ASCII) character
table.  It knows about a wide variety of hex, binary, octal, Teletype mnemonic,
ISO/ECMA code point, slang names, XML entity names, and other representations.
Given any one on the command line, it will try to display all others.  Called
with no arguments it displays a handy small ASCII chart.

%prep
%setup -q

%build
make %{?_smp_mflags} ascii ascii.1 CFLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp ascii $RPM_BUILD_ROOT%{_bindir}
cp ascii.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_mandir}/man1/ascii.1*
%{_bindir}/ascii
%doc README COPYING

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 3.18-4
- Added gcc to build requirements

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 3.18-2
- Added xmlto to build requirements

* Wed Aug 02 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 3.18-1
- Update to 3.18 version

* Sat Jul 29 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 3.16-1
- Update to 3.16 version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Francisco Javier Tsao Santín <tsao@gpul.org> - 3.15-1
- Update to 3.15 version in order to fix bug 1266618

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 16 2009 Jochen Schmitt <Jochen herr-schmitt de> 3.8-1
- Initial package

