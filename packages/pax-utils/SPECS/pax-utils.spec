# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

%bcond_without check

Summary: ELF utils that can check files for security relevant properties
Name: pax-utils
Version: 1.2.4
Release: 7%{?dist}
# http://packages.gentoo.org/package/app-misc/pax-utils
URL: https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities
Source0: https://distfiles.gentoo.org/distfiles/%{name}-%{version}.tar.xz
Patch0: paxutils.sgifixups.patch
License: GPLv2
BuildRequires:  gcc
#BuildRequires: libcap-devel
#if %{with check}
#BuildRequires: python3-pyelftools
#endif

%description
pax-utils is a small set of utilities for peforming Q/A (mostly security)
checks on systems (most notably, `scanelf`).  It is focused on the ELF
format, but does include a Mach-O helper too for OS X systems.

While heavily integrated into Gentoo's build system, it can be used on any
distro as it is a generic toolset.

Originally focused only on [PaX](https://pax.grsecurity.net/), it has been
expanded to be generally security focused.  It still has a good number of
PaX helpers for people interested in that.

# Here's a terminator

%prep
%setup -q
%patch0 -p1 -b .sgifixups
sed -i -e 's|#!/usr/bin/python.*|#!%{_bindir}/python3|' lddtree.py

%build
export gl_cv_func_getopt_posix=no
%configure --without-python --with-gnu-ld
make %{?_smp_mflags} V=1

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_bindir}/dumpelf
rm -f $RPM_BUILD_ROOT%{_bindir}/pspax
rm -f $RPM_BUILD_ROOT%{_bindir}/scanmacho
rm -f $RPM_BUILD_ROOT%{_bindir}/symtree

rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/dumpelf*
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/pspax*
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/scanmacho*


%if %{with check}
%check
make check
%endif

%files
%license COPYING
%doc BUGS README.md TODO
#%{_bindir}/dumpelf
%{_bindir}/lddtree
#%{_bindir}/pspax
%{_bindir}/scanelf
#%{_bindir}/scanmacho
#%{_bindir}/symtree
#%{_mandir}/man1/dumpelf.1*
#%{_mandir}/man1/pspax.1*
%{_mandir}/man1/scanelf.1*
#%{_mandir}/man1/scanmacho.1*

%changelog
* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 1.2.4-7
- Remove hard coded shell paths

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.2.3-4
- switch to python3 for tests
- use make_install macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Mar 06 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.2.3-1
- update to 1.2.3 (#1548693)
- switch to HTTPS URLs
- drop some obsolete workarounds

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.2.2-3
- add EPEL support
- update URL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.2.2-1
- update to 1.2.2

* Sun Nov 13 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.1.7-1
- update to 1.1.7 (#1394478)
- use license macro
- drop redundant defattr
- update summary and description

* Sun Mar 06 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.1.6-1
- update to 1.1.6 (#1314760)

* Mon Feb 15 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.1.5-1
- update to 1.1.5 (#1306483)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.1.4-1
- update to 1.1.4 (#1286232)
- drop no longer needed patch

* Fri Jul 31 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.0.5-1
- update to 1.0.5 (#1242478)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.0.3-1
- update to 1.0.3 (#1206988)

* Mon Mar 16 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.0.2-1
- update to 1.0.2
- rebase ld.so-path patch (.py script fixed upstream)

* Fri Mar 06 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.0.1-1
- update to 1.0.1
- manpages are back upstream, so drop the patch
- make builds verbose

* Wed Mar 04 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.0-1
- update to 1.0
- re-enable building manpages

* Tue Dec 02 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.9.2-1
- update to 0.9.2
- fix lddtree to search for ld.so in more locations (patch by Jakub Čajka)

* Tue Oct 28 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.9.1-1
- update to 0.9.1
- adapt specfile to upstream introduction of autotools
- drop obsolete specfile parts

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.8.1-1
- update to 0.8.1

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.7-2
- Fix build with unversioned %%{_docdir_fmt}.

* Fri Apr 12 2013 Dominik Mierzejewski <rpm@greysector.net> 0.7-1
- updated to 0.7

* Mon Mar 25 2013 Dominik Mierzejewski <rpm@greysector.net> 0.6-1
- updated to 0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 15 2012 Dominik Mierzejewski <rpm@greysector.net> 0.5-1
- updated to 0.5
- added testsuite call

* Tue Sep 04 2012 Dominik Mierzejewski <rpm@greysector.net> 0.4-1
- updated to 0.4
- enabled libcap support

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 07 2010 Dominik Mierzejewski <rpm@greysector.net> 0.2.1-1
- updated to 0.2.1, upstream changelog:
  Fix garbage in symbol matching output.

* Tue Feb 09 2010 Dominik Mierzejewski <rpm@greysector.net> 0.2-1
- updated to 0.2
- updated file list

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Dominik Mierzejewski <rpm@greysector.net> 0.1.19-1
- updated to 0.1.19
- fix installed binaries permissions

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Dominik Mierzejewski <rpm@greysector.net> 0.1.17-1
- initial build
