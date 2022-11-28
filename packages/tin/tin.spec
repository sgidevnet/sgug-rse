Name: tin
Version: 2.4.2
Release: 5%{?dist}
Summary: Basic Internet news reader
License: BSD
URL: http://www.tin.org/
Source0: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz
Source1: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz.sign
BuildRequires:  gcc-c++
BuildRequires: ncurses-devel, byacc, pcre-devel, gnupg2
BuildRequires: perl-generators

%description
Tin is a basic, easy to use Internet news reader.  Tin can read news
locally or remotely via an NNTP (Network News Transport Protocol)
server.

Install tin if you need a basic news reader.

%prep
%setup -q

%build
%configure \
	--with-libdir=/usr/sgug/var/lib/news \
	--with-spooldir=/var/spool/news/articles \
	--enable-nntp \
	--enable-prototypes \
	--disable-echo \
	--disable-mime-strict-charset \
	--enable-color \
	--enable-ncurses \
	--with-screen=ncursesw \
	--enable-locale \
	--with-pcre

%{__sed} -i -e 's/@\$(INSTALL) -s/@\$(INSTALL)/g' src/Makefile

%{__make} clean %{?_smp_mflags}
%{__make} build %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/pcre"

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

# url_handler.sh conflicts with mutt
%{__rm} -f $RPM_BUILD_ROOT/%{_bindir}/url_handler.pl
# INSTALL file is not needed in the final RPM
%{__rm} -f doc/INSTALL

%find_lang %{name}

%files -f %name.lang
%doc README doc/*
%{_bindir}/tin
%{_bindir}/rtin
%{_bindir}/metamutt
%{_bindir}/opt-case.pl
%{_bindir}/w2r.pl
%{_bindir}/tinews.pl
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Wed Apr 21 2021  HAL <notes2@gmx.de> - 2.4.2-5
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Adrian Reber <adrian@lisas.de> - 2.4.2-1
- updated to 2.4.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Adrian Reber <adrian@lisas.de> - 2.4.1-1
- updated to 2.4.1

* Tue Aug 30 2016 Adrian Reber <adrian@lisas.de> - 2.4.0-1
- updated to 2.4.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Adrian Reber <adrian@lisas.de> - 2.2.1-1
- updated to 2.2.1

* Fri Dec 27 2013 Adrian Reber <adrian@lisas.de> - 2.2.0-1
- updated to 2.2.0
- spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0.1-5
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Adrian Reber <adrian@lisas.de> - 2.0.1-3
- Add configure option '--with-screen=ncursesw' (fixes #890764)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Adrian Reber <adrian@lisas.de> - 2.0.1-1
- updated to 2.0.1

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.0.0-4
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for glibc bug#747377

* Wed Sep 14 2011 Adrian Reber <adrian@lisas.de> - 2.0.0-1
- updated to 2.0.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 13 2010 Adrian Reber <adrian@lisas.de> - 1.8.3-7
- added BR on gnupg2 (bz #574976)
- use the %%find_lang macro
- remove binary stripping from Makefile with sed instead of perl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.3-4
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Adrian Reber <adrian@lisas.de> - 1.8.3-3
- license updated

* Fri Aug 24 2007 Adrian Reber <adrian@lisas.de> - 1.8.3-2
- rebuilt

* Wed Jun 20 2007 Adrian Reber <adrian@lisas.de> - 1.8.3-1
- updated to 1.8.3
- removed desktop file (bz #241463)

* Fri Sep 15 2006 Adrian Reber <adrian@lisas.de> - 1.8.2-1
- updated to 1.8.2

* Mon Mar 13 2006 Adrian Reber <adrian@lisas.de> - 1.8.1-1
- updated to 1.8.1

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.6.2-4
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jun 24 2004 Adrian Reber <adrian@lisas.de> - 0:1.6.2-0.fdr.2
- changed BuildRequires from bison to byacc
- added pcre-devel as BuildRequires
- replaced all commands with rpmmacros
- made make use RPM_OPT_FLAGS

* Sun Nov 23 2003 Adrian Reber <adrian@lisas.de> - 0:1.6.2-0.fdr.1
- updated to 1.6.2

* Fri Jun 06 2003 Adrian Reber <adrian@lisas.de> - 0:1.4.7-0.fdr.2
- remove stripping from Makefile; let rpm strip the binaries
- moved the documentation from docdir/doc to docdir

* Sat May 31 2003 Adrian Reber <adrian@lisas.de> - 0:1.4.7-0.fdr.1
- updated to 1.4.7
- Source now macroless
- BuildRoot changed to the format from the fedora spec template
- added smp_mflags to the makes
- more fedorafication

* Thu May 01 2003 Adrian Reber <adrian@lisas.de> - 0:1.4.6-0.fdr.3
- Added BuildRequires: bison, desktop-files-utils
- removed --verbose and --mandir from configure
- s/X-Red-Hat-Extra/X-Fedora/ in desktop-file-install
- added release macro to BuildRoot

* Tue Feb 25 2003 Adrian Reber <adrian@lisas.de> - 1.4.6-1.fedora.1
- applied fedora naming conventions

* Tue Aug 22 2000 Than Ngo <than@redhat.com>
- add applink file (Bug #16568)

* Mon Aug 07 2000 Preston Brown <pbrown@redhat.com>
- 1.4.4 fixes buffer overflow, memory leaks.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 02 2000 Preston Brown <pbrown@redhat.com>
- fix spooldir to be /var/spool/news/articles not /var/spool/news

* Fri Mar 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with current ncurses

* Thu Feb 17 2000 Preston Brown <pbrown@redhat.com>
- rebuild with new vi in the buildroots so it finds the right default editor

* Thu Feb 10 2000 Preston Brown <pbrown@redhat.com>
- bump epoch

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- upgrade to 1.4.2 (stable)

* Mon May 31 1999 Jeff Johnson <jbj@redhat.com>
- update to tinpre-1.4-19990517.
- fix libdir=/var/lib/news (#7).
- fix spooldir=/var/spool/news.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- upgraded to latest dev version snapshot.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Dec 22 1998 Preston Brown <pbrown@redhat.com>
- upgraded again to latest snapshot.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- Alan is right; 1.22 is full of bugs and ANCIENT. Moved to latest tin.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- turned on DONT_LOG_USER - get rid of the silly file in /tmp. We probably
  ought to move to a newer tin soon.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov 3 1997 Erik Troan <ewt@redhat.com>
- hacked to use just termios, not a motley mix of termios and termio

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
