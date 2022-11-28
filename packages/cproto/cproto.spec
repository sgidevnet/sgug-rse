Summary: Generates function prototypes and variable declarations from C code
Name: cproto
Version: 4.7o
Release: 3%{?dist}
License: Public Domain
Source: ftp://invisible-island.net/cproto/cproto-%{version}.tgz
URL: http://invisible-island.net/
BuildRequires:  gcc-c++
BuildRequires: byacc, flex

%description
Cproto generates function prototypes and variable declarations from C
source code. Cproto can also convert function definitions between the
old style and the ANSI C style. This conversion will overwrite the
original files, however, so be sure to make a backup copy of your
original files in case something goes wrong. Cproto uses a Yacc
generated parser, so it should not be confused by complex function
definitions as much as other prototype generators.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%doc AUTHORS CHANGES MANIFEST README
%{_bindir}/cproto
%{_mandir}/man1/cproto.1*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7o-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7o-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.7o-1
- new upstream release fixes rhbz #1655648

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 4.7m-8
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7m-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7m-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7m-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7m-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7m-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7m-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Filipe Rosset <rosset.filipe@gmail.com> - 4.7m-1
- Rebuilt for new upstream release 4.7m, fixes rhbz #1240269

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7l-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7l-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7l-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Filipe Rosset <rosset.filipe@gmail.com> - 4.7l-1
- Rebuilt for new upstream release 4.7l
- spec cleanup, added checks to package, fixes rhbz #1023694

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7j-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7j-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7j-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7j-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7j-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Jindrich Novy <jnovy@redhat.com> 4.7j-1
- update to 4.7j

* Thu Jul 15 2010 Jindrich Novy <jnovy@redhat.com> 4.7i-1
- update to 4.7i

* Fri Sep  4 2009 Jindrich Novy <jnovy@redhat.com> 4.7h-1
- update to 4.7h

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7g-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Jindrich Novy <jnovy@redhat.com> 4.7g-1
- update to 4.7g

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 4.7f-3
- manual rebuild because of gcc-4.3 (#434184)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.7f-2
- Autorebuild for GCC 4.3

* Thu Jan  3 2008 Jindrich Novy <jnovy@redhat.com> 4.7f-1
- update to 4.7f
- drop patch0, fixed upstream

* Fri Oct 19 2007 Jindrich Novy <jnovy@redhat.com> 4.7e-5
- fix segfault while parsing #include directive (#315061)

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 4.7e-4
- rebuild for BuildID

* Mon May  7 2007 Jindrich Novy <jnovy@redhat.com> 4.7e-3
- %%makeinstall -> make install
- spec cleanup

* Mon Sep 11 2006 Jindrich Novy <jnovy@redhat.com> 4.7e-2
- rebuild

* Sun Mar  5 2006 Jindrich Novy <jnovy@redhat.com> 4.7e-1
- update to 4.7e

* Tue Nov 29 2005 Jindrich Novy <jnovy@redhat.com> 4.7d-2
- fix source, rebuild

* Mon Nov 28 2005 Jindrich Novy <jnovy@redhat.com> 4.7d-1
- update to 4.7d

* Sat Aug 13 2005 Jindrich Novy <jnovy@redhat.com> 4.7c-7
- prepare for Fedora Extras inclusion (#165811)

* Fri Mar  4 2005 Jindrich Novy <jnovy@redhat.com> 4.7c-6
- rebuilt with gcc4

* Thu Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 4.7c-5
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 4.7c-4
- add RPM_OPT_FLAGS to CFLAGS
- convert Copyright to License
- rebuild with -D_FORTIFY_SOURCE=2

* Thu Oct 14 2004 Jindrich Novy <jnovy@redhat.com> 4.7c-3
- define OPT_LINTLIBRARY to enable type definitions output
  and other cproto features disabled otherwise

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May  4 2004 Bill Nottingham <notting@redhat.com> 4.7c-1
- update to 4.7c (#54814)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Bill Nottingham <notting@redhat.com> 4.6-16
- fix build with new bison

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 4.6-14
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Bill Nottingham <notting@redhat.com> 4.6-12
- don't strip it

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Aug 13 2001 Bill Nottingham <notting@redhat.com>
- predefine __builtin_va_list (#46246, original patch from <urban@teststation.com>)

* Tue Jun 12 2001 Bill Nottingham <notting@redhat.com>
- actually *apply* the 4.6.1 patch. Fixes #35654, at least.

* Fri Dec 01 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Fri Oct 13 2000 Bill Nottingham <notting@redhat.com>
- use /lib/cpp, not gcc -E, again (#20535)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Bill Nottingham <notting@redhat.com>
- rebuild against glibc-2.2, FHS stuff

* Tue Feb  1 2000 Bill Nottingham <notting@redhat.com>
- use /lib/cpp, not gcc -E (#8612)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- update to 4.6.1 (#1516).
- use %%configure

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
