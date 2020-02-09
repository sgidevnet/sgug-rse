Summary: File system tree viewer
Name: tree
Version: 1.8.0
Release: 3%{?dist}
License: GPLv2+
URL: http://mama.indstate.edu/users/ice/tree/
Source: ftp://mama.indstate.edu/linux/tree/tree-%{version}.tgz

BuildRequires: gcc

# Preserve timestamp on man page.
Patch2: tree-preserve-timestamps.patch

# Document --du and --prune options in help output (bug #948991).
Patch4: tree-args.patch

# Use correct default for dircolors "ec" field (bug #812934).
Patch6: tree-dircolors-ec.patch

# Keep file size field length constant regardless of whether SI units
# are used (bug #997937).
Patch7: tree-size-field-len.patch

# fix programming mistakes detected by static analysis
Patch8: tree-static-analysis.patch

# irix patch
Patch100: tree-1.8.0.patch

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the DOS tree
utility.

%prep
#%patch100 -p1 -b .tree-1.8.0.patch
%autosetup -p1

# do not escape UTF-8 chars in file names by default in UTF-8 locale (#1480778)
sed -e 's/LINUX/__linux__/' -i tree.c

%build
make CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS)" \
  LDFLAGS="$RPM_LD_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}

make	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/tree.1

%files
%{_bindir}/tree
%{_mandir}/man1/tree.1*
%doc README LICENSE

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Kamil Dudka <kdudka@redhat.com> - 1.8.0-1
- update to the latest upstream release

* Wed Nov 07 2018 Kamil Dudka <kdudka@redhat.com> - 1.7.0-16
- fix programming mistakes detected by static analysis

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 1.7.0-14
- Use LDFLAGS from redhat-rpm-config

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> - 1.7.0-13
- add explicit BR for the gcc compiler

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Kamil Dudka <kdudka@redhat.com> - 1.7.0-11
- do not escape UTF-8 chars in file names by default in UTF-8 locale (#1480778)
- modernize spec file (Group, BuildRoot, autosetup, clean, defattr)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Kamil Dudka <kdudka@redhat.com> - 1.7.0-7
- drop a non-upstream patch that disabled color output by default (#1284657)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.7.0-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Tim Waugh <twaugh@redhat.com> - 1.7.0-1
- 1.7.0 (bug #1090962).

* Fri Aug 16 2013 Tim Waugh <twaugh@redhat.com> - 1.6.0-11
- Keep file size field length constant regardless of whether SI units
  are used (bug #997937).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  9 2013 Tim Waugh <twaugh@redhat.com> - 1.6.0-9
- Use correct default for dircolors "ec" field (bug #812934).

* Thu Jul  4 2013 Tim Waugh <twaugh@redhat.com> - 1.6.0-8
- Handle large UID/GID values (bug #980945).

* Thu Apr 11 2013 Tim Waugh <twaugh@redhat.com> - 1.6.0-7
- Document --du and --prune options in help output (bug #948991).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Tim Waugh <twaugh@redhat.com> 1.6.0-3
- Put LFS_CFLAGS in CFLAGS not CPPFLAGS so they actually get used
  (bug #769655).

* Mon Jul  4 2011 Tim Waugh <twaugh@redhat.com> 1.6.0-2
- Don't strip the binary too early (bug #718456).

* Mon Jun 27 2011 Tim Waugh <twaugh@redhat.com> 1.6.0-1
- 1.6.0 (bug #716879).

* Fri May 20 2011 Tim Waugh <twaugh@redhat.com> 1.5.3-4
- Fixed memory leak spotted by coverity (bug #704570).

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar  3 2010 Tim Waugh <twaugh@redhat.com> 1.5.3-2
- Added comments to all patches.

* Fri Nov 27 2009 Tim Waugh <twaugh@redhat.com> 1.5.3-1
- 1.5.3 (bug #517342, bug #541255).

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Tim Waugh <twaugh@redhat.com> 1.5.2.2-3
- Reinstate no-color-by-default patch (bug #504245).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Tim Waugh <twaugh@redhat.com> 1.5.2.2-1
- 1.5.2.2.

* Mon Nov 24 2008 Tim Waugh <twaugh@redhat.com> 1.5.2.1-2
- Better summary.

* Tue Sep  2 2008 Tim Waugh <twaugh@redhat.com> 1.5.2.1-1
- Removed patch fuzz.
- 1.5.2.1.

* Mon Jun 16 2008 Tim Waugh <twaugh@redhat.com> 1.5.2-1
- 1.5.2.
- Dropped no-colour patch.

* Thu Jun  5 2008 Tim Waugh <twaugh@redhat.com> 1.5.1.2-1
- 1.5.1.2.

* Fri Apr 25 2008 Tim Waugh <twaugh@redhat.com> 1.5.1.1-1
- 1.5.1.1.

* Mon Feb 11 2008 Tim Waugh <twaugh@redhat.com> 1.5.0-9
- Rebuild for GCC 4.3.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 1.5.0-8
- More specific license tag.

* Wed Feb  7 2007 Tim Waugh <twaugh@redhat.com> 1.5.0-7
- Current version no longer ships binary, so don't try removing
  it (bug #226503).

* Tue Feb  6 2007 Tim Waugh <twaugh@redhat.com> 1.5.0-6
- Preserve timestamps on install (bug #226503).
- Added SMP flags (bug #226503).
- Removed Prefix: tag (bug #226503).
- Removed bogus mkdir call (bug #226503).
- Ship the LICENSE file (bug #226503).
- Fixed summary (bug #226503).

* Fri Dec 15 2006 Tim Waugh <twaugh@redhat.com> 1.5.0-5
- Fixed '--charset' option (bug #188884).

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 1.5.0-4
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.5.0-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.5.0-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 1.5.0-3
- Rebuild for new GCC.

* Sun Dec 05 2004 Florian La Roche <laroche@redhat.com>
- add quotes around CPPFLAGS

* Mon Sep 13 2004 Tim Waugh <twaugh@redhat.com> 1.5.0-1
- 1.5.0 (bug #131854).
- No longer need utf8 or gcc34 patches.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb  5 2004 Tim Waugh <twaugh@redhat.com> 1.4b3-2
- Fixed compilation with GCC 3.4.

* Wed Aug 13 2003 Tim Waugh <twaugh@redhat.com> 1.4b3-1
- Upgraded (bug #88525).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov  8 2002 Tim Waugh <twaugh@redhat.com> 1.2-21
- Assume -N except if -q is given (bug #77517).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 23 2002 Tim Waugh <twaugh@redhat.com> 1.2-18
- Don't explicitly strip binaries (bug #62569).
- Fix malloc/realloc problems (bug #56858).

* Fri Mar 22 2002 Tim Waugh <twaugh@redhat.com> 1.2-17
- Large file support (bug #61456).

* Wed Feb 27 2002 Tim Waugh <twaugh@redhat.com> 1.2-16
- Rebuild in new environment.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Oct  5 2001 Tim Waugh <twaugh@redhat.com> 1.2-14
- Fix size format (bug #54298).
- Don't use colours by default (bug #25389).

* Mon Jul 30 2001 Tim Waugh <twaugh@redhat.com> 1.2-13
- Change Copyright: to License:.
- Don't dump core if LS_COLORS is too big (bug #50016).

* Wed May 30 2001 Tim Waugh <twaugh@redhat.com> 1.2-12
- Sync description with specspo.

* Tue Oct 10 2000 Tim Waugh <twaugh@redhat.com> 1.2-11
- Don't blabber about carrots in the man page (bug #18823)
- Use RPM_OPT_FLAGS while building

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild, FHS stuff

* Thu Feb  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- remove executable bit from man page (Bug #9035)
- deal with rpm compressing man pages

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- installing in /usr/bin

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed src url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
