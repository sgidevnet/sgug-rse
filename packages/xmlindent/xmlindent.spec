Name: xmlindent
Version: 0.2.17
Release: 30%{?dist}
Summary: XML stream reformatter
License: GPLv2+
URL: http://xmlindent.sf.net/
Source0: http://downloads.sourceforge.net/xmlindent/xmlindent-%{version}.tar.gz
BuildRequires: flex flex-static
BuildRequires: gcc

%description
XML Indent is a XML stream reformatter written in ANSI C.
It is analogous to GNU indent.

%prep
%setup -q

sed -i -e "s,-Wall,-Wall \$(CFLAGS),g" -e "s,555,755," -e "s,444,644," Makefile

%build
CFLAGS=$RPM_OPT_FLAGS make %{?_smp_mflags}

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

%files
%license LICENSE
%doc ChangeLog BUGS README
%{_bindir}/xmlindent
%{_mandir}/man1/xmlindent.1*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Adrian Reber <adrian@lisas.de> - 0.2.17-28
- Added BR: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Adrian Reber <adrian@lisas.de> - 0.2.17-21
- Clean up spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Adrian Reber <adrian@lisas.de> - 0.2.17-12
- BR flex-static for "FTBFS xmlindent-0.2.17-11.fc12" (#660866)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 16 2008 Adrian Reber <adrian@lisas.de> - 0.2.17-9
- rebuilt for gcc43

* Thu Oct 11 2007 Adrian Reber <adrian@lisas.de> - 0.2.17-8
- rebuilt for BuildID
- updated license tag
- fixed sourceforge URL

* Tue Sep 12 2006 Adrian Reber <adrian@lisas.de> - 0.2.17-7
- rebuilt

* Tue Feb 21 2006 Adrian Reber <adrian@lisas.de> - 0.2.17-6
- rebuilt

* Wed Jun 08 2005 Adrian Reber <adrian@lisas.de> - 0.2.17-5
- rebuilt

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.2.17-4
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Dec 07 2004 Adrian Reber <adrian@lisas.de> - 0:0.2.17-2
- applied patch from Ville Skyttä (bug #2078)

* Fri Sep 17 2004 Adrian Reber <adrian@lisas.de> - 0:0.2.17-0.fdr.1
- Initial RPM release.
