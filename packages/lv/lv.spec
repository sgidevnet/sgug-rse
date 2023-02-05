%global vver	451

Name:		lv
Version:	4.51
Release:	36%{?dist}
License:	GPLv2+
URL:		http://www.ff.iij4u.or.jp/~nrt/lv/
BuildRequires:	ncurses-devel autoconf
BuildRequires:	gcc

Source:		http://www.ff.iij4u.or.jp/~nrt/freeware/%{name}%{vver}.tar.gz
Patch1:		lv-4.49.4-nonstrip.patch
Patch2:		lv-4.51-162372.patch
Patch3:		lv-+num-option.patch
Patch4:		lv-fastio.patch
Patch5:		lv-lfs.patch
Patch6:		%{name}-aarch64.patch
Patch7:		%{name}-no-sigvec.patch

Summary:	A Powerful Multilingual File Viewer
%description
lv is a powerful file viewer like less.
lv can decode and encode multilingual streams through
many coding systems: ISO-8859, ISO-2022, EUC, SJIS, Big5,
HZ, Unicode.
It recognizes multi-bytes patterns as regular
expressions, lv also provides multilingual grep.
In addition, lv can recognize ANSI escape sequences
for text decoration.

%prep
%setup -q -n %{name}%{vver}
%patch1 -p1 -b .nonstrip
%patch2 -p1 -b .162372
%patch3 -p1 -b .num
%patch4 -p1 -b .fastio
%patch5 -p1 -b .lfs
%patch6 -p1 -b .6-aarch64
%patch7 -p1 -b .7-sigvec

%build
cd src
autoconf
%configure --enable-fastio
make %{?_smp_mflags}

%install
cd src
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make install bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} mandir=$RPM_BUILD_ROOT%{_mandir} INSTALL="install -p"

%files
%license GPL.txt
%doc README build hello.sample hello.sample.gif index.html
%doc relnote.html
%{_bindir}/lv
%{_bindir}/lgrep
%{_mandir}/man1/lv.1.gz
%{_libdir}/lv


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com> - 4.51-33
- Add BR: gcc

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.51-32
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.51-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Akira TAGOH <tagoh@redhat.com> - 4.51-25
- Drop obsolete sigvec support (#1151982)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Akira TAGOH <tagoh@redhat.com> - 4.51-22
- Fix a typo in %%description. (#1053146)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Akira TAGOH <tagoh@redhat.com> - 4.51-20
- Rebuilt for aarch64 support (#926100)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.51-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Akira TAGOH <tagoh@redhat.com> - 4.51-13
- Rebuild for gcc-4.3.

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 4.51-12
- Rebuild

* Thu Aug  9 2007 Akira TAGOH <tagoh@redhat.com> - 4.51-11
- Update License tag.

* Mon Feb  5 2007 Akira TAGOH <tagoh@redhat.com> - 4.51-10
- updated License tag.
- clean up spec file for mass package review. (#226112)

* Tue Jan 16 2007 Miroslav Lichvar <mlichvar@redhat.com> - 4.51-9
- link with ncurses
- add dist tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.51-8.1
- rebuild

* Mon Jun 12 2006 Akira TAGOH <tagoh@redhat.com> - 4.51-8
- clean up the spec file.
- add autoconf to BuildReq. (#194753)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.51-7.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.51-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 31 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-7
- lv-+num-option.patch: applied a patch to allow +num option to jump to the specific line.
- lv-fastio.patch: applied a patch to improve the performance to read the files.
- lv-lfs.patch: applied a patch for Lerge File Summit support.

* Mon Jul 11 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-6
- lv-4.51-162372.patch: silence gcc warning. (#162372)

* Thu Mar 17 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-5
- rebuilt

* Thu Feb 10 2005 Akira TAGOH <tagoh@redhat.com> - 4.51-4
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Akira TAGOH <tagoh@redhat.com> 4.51-1
- New upstream release.
- lv-fix-install-opts.patch: removed because it's unnecessary anymore.

* Tue Nov 25 2003 Akira TAGOH <tagoh@redhat.com> 4.50-1
- New upstream release.
  here is this release of note.
  - [4.49.5.a]
  - Added ISO-8859-10,11,13,14,15,16.
  - Changed coding system names for '=' key.
  - [4.49.5.b]
  - Updated KSX1001 <-> Unicode mapping table.
  - [4.49.5.c]
  - Input coding detection improved.
  - -D option now specifies default (fall-back) coding system, not default EUC coding system.
  - Output coding detection based on LC_CTYPE locale.
  - [4.49.5.d]
  - Checks $EDITOR and $VISUAL variables when invoking an editor.
  - [4.49.5.f]
  - Initialize file->used[] in FileAttach() in file.c to avoid segfault in lgrep.
  - [4.5.0]
  - added polling function for regular files with slightly modified patch from Pawel S. Veselov <vps@manticore.2y.net>.
  - enabled itable cache.
  - Big5 to Unicode mapping didn't work at all (fixed offset of coding system table)
    (See http://lists.debian.or.jp/debian-devel/200311/msg00006.html)
  - fixed editor call not to return by SIGINT unexpectedly.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 12 2003 Akira TAGOH <tagoh@redhat.com> 4.49.5-1
- New upstream release.
- lv-4.49.4-dont-read-dotlv-on-cwd.patch: removed.
- lv-4.49.4-fix-manpage.patch: removed.

* Mon Apr 28 2003 Akira TAGOH <tagoh@redhat.com> 4.49.4-11
- lv-4.49.4-fix-manpage.patch: fix the man pages to reflect previous changes.

* Mon Apr 28 2003 Akira TAGOH <tagoh@redhat.com> 4.49.4-10
- lv-4.49.4-dont-read-dotlv-on-cwd.patch: don't read .lv file from current
  directory to prevent the possibility of local root exploit.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Akira TAGOH <tagoh@redhat.com> 4.49.4-6
- lv-4.49.4-nonstrip.patch: applied to fix the stripped binary.
- s/Copyright/License/

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jul 24 2001 SATO Satoru <ssato@redhat.com>
- BuildPrereq: libtermcap-devel (close #49517)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Dec 20 2000 SATO Satoru <ssato@redhat.com>
- clean up spec

* Tue Dec 19 2000 SATO Satoru <ssato@redhat.com>
- new upstream
- use system-defined macros

* Thu Aug 24 2000 SATO Satoru <ssato@redhat.com>
- fix spec (remove japanese description)

* Mon Aug 07 2000 SATO Satoru <ssato@redhat.com>
- fix spec (make prefix... replaced with %%makeinstall)

* Tue Jul 04 2000 SATO Satoru <ssato@redhat.com>
- initial release.

