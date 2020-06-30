Summary:    MS Word to ASCII/Postscript converter
Name:       antiword
Version:    0.37
Release:    28%{?dist}
Source0:    http://www.winfield.demon.nl/linux/%{name}-%{version}.tar.gz
Source1:    antiword.sh
URL:        http://www.winfield.demon.nl/
Patch0:     antiword-0.32-fix-flags.patch
Patch1:     http://seclists.org/oss-sec/2014/q4/att-870/antiword-bGetPPS-Prevent-buffer-overflow-of-atPPSlist-_szName.diff
Patch2:     50_antiword-manpage-hyphen-to-minus.patch
Patch3:     docx.patch
Patch4:     remove-cjb.net-references.patch
License:    GPLv2+
BuildRequires: gcc

%description
Antiword is a free MS-Word reader for Linux, BeOS and RISC OS. It converts
the documents from Word 6, 7, 97 and 2000 to ASCII and Postscript. Antiword
tries to keep the layout of the document intact.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%{__chmod} a+r * Resources/* Docs/*

%build
OPT="$RPM_OPT_FLAGS" make all %{?_smp_mflags}

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 755 antiword $RPM_BUILD_ROOT%{_bindir}/antiword.bin
%{__install} -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/antiword
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -a Resources/* $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man1
%{__cp} Docs/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%{__chmod} 644 kantiword
iconv -f iso-8859-1 -t utf-8 Docs/antiword.php > Docs/antiword.php.utf8
iconv -f iso-8859-1 -t utf-8 Docs/Netscape > Docs/Netscape.utf8
%{__mv} Docs/antiword.php.utf8 Docs/antiword.php
%{__mv} Docs/Netscape.utf8 Docs/Netscape

%files
%license Docs/COPYING
%doc Docs/FAQ Docs/ReadMe Docs/Netscape Docs/ChangeLog
%doc Docs/Exmh Docs/Mozilla Docs/QandA Docs/Mutt Docs/antiword.php
%doc Docs/Emacs Docs/History kantiword
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Adrian Reber <adrian@lisas.de> - 0.37-25
- Added BR: gcc
- Added three patches from the debian package

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 02 2014 Adrian Reber <adrian@lisas.de> - 0.37-17
- added patch for "CVE-2014-8123 antiword: buffer overflow of atPPSlist[].szName[]" (#1169665)
- fixed dates in changelog

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Apr 06 2008 Adrian Reber <adrian@lisas.de> - 0.37-7
- added wrapper script from Michal Jaegermann to better
  handle UTF input files (#191060)

* Tue Feb 12 2008 Adrian Reber <adrian@lisas.de> - 0.37-6
- rebuilt for gcc43

* Wed Dec 12 2007 Adrian Reber <adrian@lisas.de> - 0.37-5
- rebuilt for EL-5 branch
- added dist tag
- fixed a few rpmlint warnings

* Fri Aug 24 2007 Adrian Reber <adrian@lisas.de> - 0.37-4
- rebuilt

* Mon Sep 11 2006 Adrian Reber <adrian@lisas.de> - 0.37-3
- rebuilt

* Mon Feb 13 2006 Adrian Reber <adrian@lisas.de> - 0.37-2
- rebuilt

* Wed Dec 07 2005 Adrian Reber <adrian@lisas.de> - 0.37-1
- updated to 0.37

* Tue May 10 2005 Adrian Reber <adrian@lisas.de> - 0.36.1-2
- updated to 0.36.1

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb 03 2005 Adrian Reber <adrian@lisas.de> - 0:0.36-1
- updated to 0.36

* Wed Jul 14 2004 Adrian Reber <adrian@lisas.de> - 0:0.35-0.fdr.1
- updated to 0.35
- better spec file

* Wed Apr 23 2003 Adrian Reber <adrian@lisas.de> - 0.33-0.fdr.2
- s/$RPM_BUILD_ROOT/%%{buildroot}/
- Epoch:0 added
- make %%{?_smp_mflags}
- removed unnecessary Prefix: %%{_prefix}
- fixed group
- applied more of the fedora spec template

* Tue Feb 25 2003 Adrian Reber <adrian@lisas.de> - 0.33-0.fdr.1
- applied fedora naming conventions

* Sun Dec 22 2002 Adrian Reber <adrian@lisas.de>
- updated to 0.33
- demandrakefied

* Fri Feb 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.32-2mdk
- rebuild to fix invalid-packager

* Mon Oct 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.32-1mdk
- new version
- fix obsolete-tag Copyright

* Sat Jun 23 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.31-2mdk
- have the resources files findable by default by the binary
- use our flags
- install man page

* Thu Jan 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.31-1mdk
- updated to 0.31

* Thu Jul 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.30-2mdk
- BM
- macros

* Thu Jul 13 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com> 0.30-1mdk
  - v0.30 (initial packaging from freshmeat)
