Summary: Produces a document with syntax highlighting
Name: source-highlight
Version: 3.1.8
Release: 25%{?dist}
License: GPLv3+
Source0: ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
Source1: ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz.sig
# Fix for https://savannah.gnu.org/bugs/index.php?55967
Patch: source-highlight-3.1.8-no-black.patch
URL: http://www.gnu.org/software/src-highlite/
BuildRequires: bison, flex, boost-devel
BuildRequires: help2man, ctags, chrpath, pkgconfig(bash-completion)
BuildRequires: gcc, gcc-c++
Requires: ctags

%description
This program, given a source file, produces a document with syntax
highlighting. At the moment this package can handle:
Java, Javascript, C/C++, Prolog, Perl, Php3, Python, Flex, ChangeLog, Ruby,
Lua, Caml, Sml and Log as source languages, and HTML, XHTML and ANSI color
escape sequences as output format.


%package devel
Summary: Development files for source-highlight
Requires: %{name}%{?_isa} = %{version}-%{release}
# For linking against source-higlight using pkgconfig
Requires: boost-devel

%description devel
Development files for source-highlight

%prep
%autosetup -p1

%build
%configure --disable-static \
           --with-boost-regex=boost_regex
%make_build

%install
%make_install

mv $RPM_BUILD_ROOT%{_datadir}/doc/ docs
%{__sed} -i 's/\r//' docs/source-highlight/*.css

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/source-highlight
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/source-highlight-settings

echo -e "\ncxx = cpp.lang" >> $RPM_BUILD_ROOT%{_datadir}/source-highlight/lang.map

bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p $RPM_BUILD_ROOT$bashcompdir
mv $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/source-highlight \
    $RPM_BUILD_ROOT$bashcompdir/
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%files
%doc docs/source-highlight/*
%{_bindir}/cpp2html
%{_bindir}/java2html
%{_bindir}/source-highlight
%{_bindir}/source-highlight-esc.sh
%{_bindir}/check-regexp
%{_bindir}/source-highlight-settings
%{_bindir}/src-hilite-lesspipe.sh
%{_datadir}/bash-completion/
%{_libdir}/libsource-highlight.so.*
%dir %{_datadir}/source-highlight
%{_datadir}/source-highlight/*
%{_mandir}/man1/*
%{_infodir}/source-highlight*.info*

%files devel
%dir %{_includedir}/srchilite
%{_libdir}/libsource-highlight.so
%{_libdir}/pkgconfig/source-highlight.pc
%{_includedir}/srchilite/*.h

%changelog
* Thu Jun 25 2020  HAL <notes2@gmx.de> - 3.1.8-25
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 fedora-toolbox <otaylor@redhat.com> - 3.1.8-24
- Patch esc.style to avoid using the black color (#1688372)

* Mon Feb 18 2019 Adrian Reber <adrian@lisas.de> - 3.1.8-23
- Require boost-devel in the source-highlight-devel package (#1638029)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-21
- Rebuilt for Boost 1.69

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.1.8-20
- Rebuild with fixed binutils

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.8-19
- Replace obsolete scriptlets

* Mon Jul 16 2018 Adrian Reber <adrian@lisas.de> - 3.1.8-18
- Added BR gcc, gcc-c++
- Small SPEC file cleanups

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-15
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-12
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-11
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-9
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-8
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.1.8-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Fri Jul 24 2015 Adrian Reber <adrian@lisas.de> - 3.1.8-3
- another rebuild for Boost 1.58

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.1.8-2
- rebuild for Boost 1.58

* Wed Jul 22 2015 Adrian Reber <adrian@lisas.de> - 3.1.8-1
- updated to 3.1.8

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.7-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Rex Dieter <rdieter@fedoraproject.org> 3.1.7-7
- rebuild (gcc5)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.1.7-6
- Rebuild for boost 1.57.0

* Sat Jan 24 2015 Ville Skyttä <ville.skytta@iki.fi> - 3.1.7-5
- Install bash completion to %%{_datadir}/bash-completion

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 3.1.7-2
- Rebuild for boost 1.55.0

* Fri Aug 23 2013 Adrian Reber <adrian@lisas.de> - 3.1.7-1
- updated to 3.1.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 3.1.6-5
- Rebuild for boost 1.54.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.1.6-4
- Rebuild for Boost-1.53.0

* Wed Aug  8 2012 Bill Nottingham <notting@redhat.com> - 3.1.6-3
- rebuild against new boost

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Adrian Reber <adrian@lisas.de> - 3.1.6-1
- updated to 3.1.6
- removed buildroot and clean section
- fixed "missing c++ source language detection for .cxx extension" (#728311)
- fixed "source-highlight : Conflicts with autoconf-archive" (#797794)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-10
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011  <dodji@redhat.com> - 3.1.4-8
- Rebuild against boost 1.48

* Thu Jul 21 2011 Adrian Reber <adrian@lisas.de> - 3.1.4-7
- and again a rebuilt for boost.

* Fri Apr 01 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.4-6
- Another rebuild, libboost SONAME has changed again

* Wed Mar 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.4-5
- Rebuild for correct libboost SONAME

* Sun Mar 13 2011 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.4-4
- Rebuild for boost 1.46.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Bastien Nocera <bnocera@redhat.com> 3.1.4-2
- Rebuild against newer boost

* Mon Aug 16 2010 Leigh Scott <leigh123linux@googlemail.com> - 3.1.4-1
- updated to 3.1.4

* Thu Aug  5 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1.3-3
- rebuild for new boost (again)

* Tue Jul 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.3-2
- Rebuild for new boost
- Fix Requires for %%post and %%preun

* Fri Jun 04 2010 Leigh Scott <leigh123linux@googlemail.com> - 3.1.3-1
- updated to 3.1.3
- change configure command so it finds boost_regex
- fix source url's
- add devel package
- fix directory ownership
- fix rpath on binary

* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> - 2.10-5
- rebuilt for new boost.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> - 2.10-2
- Rebuild for boost-1.37.0.

* Sat Aug 16 2008 Adrian Reber <adrian@lisas.de> - 2.10-1
- updated to 2.10

* Fri Jun 13 2008 Adrian Reber <adrian@lisas.de> - 2.9-1
- updated to 2.9
- removed upstreamed gcc43 patch

* Tue Feb 12 2008 Adrian Reber <adrian@lisas.de> - 2.8-2
- added gcc43 patch

* Fri Dec 14 2007 Adrian Reber <adrian@lisas.de> - 2.8-1
- updated to 2.8
- license changed to GPLv3+

* Sun Sep 16 2007 Adrian Reber <adrian@lisas.de> - 2.7-1
- updated to 2.7
- updated files section
- updated license

* Mon Aug 20 2007 Caolan McNamara <caolanm@redhat.com> - 2.4-2
- rebuild for boost rebuild

* Fri Sep 15 2006 Adrian Reber <adrian@lisas.de> - 2.4-1
- updated to 2.4

* Tue Mar 21 2006 Adrian Reber <adrian@lisas.de> - 2.3-2
- using a new url.lang to fix #195720
  (https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=131352)

* Sun Mar 12 2006 Adrian Reber <adrian@lisas.de> - 2.3-1
- updated to 2.3

* Mon Oct 17 2005 Adrian Reber <adrian@lisas.de> - 2.2-1
- updated to 2.2
- added ctags BuildRequires and Requires

* Wed Aug 31 2005 Adrian Reber <adrian@lisas.de> - 2.1.2-1
- updated to 2.1.2
- removed boost-compile-fix patch

* Thu Aug 25 2005 Adrian Reber <adrian@lisas.de> - 2.1.1-2
- rebuilt due to boost's SONAME change (boost 1.33.0)
- added patch to compile with boost 1.33.0

* Wed Aug 03 2005 Adrian Reber <adrian@lisas.de> - 2.1.1-1
- updated to 2.1.1 (fixes #164861)

* Mon Aug 01 2005 Adrian Reber <adrian@lisas.de> - 2.1-1
- updated to 2.1

* Sun Jun 19 2005 Adrian Reber <adrian@lisas.de> - 2.0-1
- updated to 2.0
- added boost-devel, help2man to BR
- included info file

* Wed May 11 2005 Adrian Reber <adrian@lisas.de> - 1.11-1
- updated to 1.11
- included the documentation
- optimised the %%descritpion

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jun 22 2004 Adrian Reber <adrian@lisas.de> - 0:1.9-0.fdr.2
- added the Epoch: 0

* Tue Jun 22 2004 Adrian Reber <adrian@lisas.de> - 1.9-0.fdr.1
- removed mandrake specific macros

* Thu Jun 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.9-1mdk
- 1.9

* Wed Jan 07 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8-1mdk
- 1.8
- drop Prefix tag
- clean out redundant buildrequires
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install, not %%prep
- use %%makeinstall_std macro
- cosmetics

* Wed Mar 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.7-1mdk
- 1.7

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.6.3-1mdk
- 1.6.3

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.6.2-1mdk
- 1.6.2

* Sat Nov 23 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.6.1-1mdk
- 1.6.1
- fix unpackaged files

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5-2mdk
- rebuild

* Thu Jul 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5-1mdk
- 1.5

* Wed Jun 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- obsoletes java2html & cpp2html
