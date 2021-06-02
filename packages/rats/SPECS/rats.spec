Name:           rats
Version:        2.4
Release:        14%{?dist}
Summary:        Rough Auditing Tool for Security
License:        GPLv2
URL:            https://code.google.com/p/rough-auditing-tool-for-security/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/rough-auditing-tool-for-security/rats-%{version}.tgz
Patch1:         0002-Fix-engine-output-and-php-extension.patch
Patch2:         0003-Fix-report-layout.patch
Patch3:         rats-2.4-gtk-vuln.patch
Patch4:         rats-2.4-hash.patch
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  gcc

%description
RATS(Rough Auditing Tool for Security) scans through code, finding potentially
dangerous function calls. The goal of this tool is not to definitively find 
bugs (yet). The current goal is to provide a reasonable starting point for 
performing manual security audits.

The initial vulnerability database is taken directly from things that could be 
easily found when starting with the forthcoming book, "Building Secure 
Software" by Viega and McGraw.  

%prep
%autosetup -p1

# $(DESTDIR) hack.
sed -e 's/$(BINDIR)/$(DESTDIR)$(BINDIR)/g' \
    -e 's/ $(LIBDIR)/ $(DESTDIR)$(LIBDIR)/g' \
    -e 's/$(MANDIR)/$(DESTDIR)$(MANDIR)/g' \
    -e 's/ $(SHAREDIR)/ $(DESTDIR)$(SHAREDIR)/g' -i Makefile.in

%build
%configure --datadir=%{_datadir}/%{name}
%make_build lex && %make_build

%install
%make_install

%files
%doc COPYING README
%{_bindir}/rats
%{_datadir}/rats
%{_mandir}/man1/rats.1*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.4-11
- Update Source0 URL
- Remove patch for conflicting types (it was triggering compilation errors)
- Use autosetup for cleaner spec file
- Fix changelog bogus dates

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.4-10
- BR gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-5
- Fix bug in patch 0002 (bug 1129580)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Christopher Meng <rpm@cicku.me> - 2.4-1
- Update to 2.4
- Many thanks to Slawomir Czarko <slawomir@ezono.com>

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Tue Oct 9 2007 Scott Henson <shenson@redhat.com> - 2.1-5
 - Change the Makefile.in so we can use the configure macro
 - Rename all patches to .patch to be more standard

* Tue Oct 9 2007 Scott Henson <shenson@redhat.com> - 2.1-4
 - Do configure ourselves because datadir gets set wrong otherwise.

* Tue Oct 9 2007 Scott Henson <shenson@redhat.com> - 2.1-3
 - Break the monolithic patch into pieces
 - Build Clean, contains build cleanups and spelling corrections
 - Php, adds support for php3 and php4 files
 - Report, adds some html output cleanup
 - Lex, some lex bug fixes
 - GTK-Vuln, adds some gtk vulnerabilities
 - Also generate lex output files on each build.

* Mon Oct 8 2007 Scott Henson <shenson@redhat.com> - 2.1-2
 - Move configure to the build stage and simplify it to just use the configure macro
 - Comment as to why we don't use make install
 - Remove the GPL comment from the Description
 - Update upstream to Fortify Software
 - Other misc cleanups.  

* Wed Sep 26 2007 Scott Henson <shenson@redhat.com> - 2.1-1
 - Initial packaged version
