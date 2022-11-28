Summary:	Open audio/video container format library
Name:		libmatroska
Version:	1.5.2
Release:	1%{?dist}
License:	LGPLv2+
URL:		https://www.matroska.org/
Source0:	https://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	cmake3
BuildRequires:	gcc-c++
BuildRequires:	libebml-devel >= 1.3.8
Requires:	libebml%{_isa} >= 1.3.8

%description
Matroska is an extensible open standard Audio/Video container.  It
aims to become THE standard of multimedia container formats.  Matroska
is usually found as .mkv files (matroska video) and .mka files
(matroska audio).


%package	devel
Summary:	Matroska container format library development files
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	%{_libdir}/cmake
Requires:	libebml-devel >= 1.3.8
Requires:	pkgconfig

%description	devel
Matroska is an extensible open standard Audio/Video container.  It
aims to become THE standard of multimedia container formats.  Matroska
is usually found as .mkv files (matroska video) and .mka files
(matroska audio).

This package contains the files required to rebuild applications which
will use the Matroska container format.


%prep
%setup -q


%build
%cmake3 .
%make_build


%install
%make_install


%ldconfig_scriptlets


%files
%license LICENSE.LGPL
%doc ChangeLog
%{_libdir}/%{name}.so.6*

%files devel
%{_includedir}/matroska/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/Matroska
%{_libdir}/cmake/Matroska/MatroskaConfig.cmake
%{_libdir}/cmake/Matroska/MatroskaConfigVersion.cmake
%{_libdir}/cmake/Matroska/MatroskaTargets-noconfig.cmake
%{_libdir}/cmake/Matroska/MatroskaTargets.cmake


%changelog
* Tue Sep 10 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.5.2-1
- update to 1.5.2 (#1688000)
- drop obsolete patch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.5.0-1
- update to 1.5.0
- backport fixes for invalid memory access and null pointer dereference
- fix unowned %{_libdir}/cmake/ebml directory

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.4.9-2
- Append curdir to CMake invokation. (#1668512)

* Tue Jul 24 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.4.9-1
- update to 1.4.9 (#1570226)
- switch build system to cmake, add missing dependencies
- use ldconfig_scriptlets macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.4.8-1
- Update to 1.4.8 (#1495383)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.4.7-1
- Update to 1.4.7 (#1431305)
- Use license and make build macros
- Make -devel require the same arch of main package
- Sync libebml version requirement between main and -devel

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.4.5-1
- Update to 1.4.5 (#1352477)
- Bump min required libebml version to 1.3.4
- use https for URLs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.4.4-1
- Update to 1.4.4 (required by mkvtoolnix 8.5.x)
- Bump min required libebml version to 1.3.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.4.2-3
- rebuilt for gcc-5.0.0-0.22.fc23

* Thu Mar 05 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.4.2-2
- rebuilt for gcc-5.0

* Wed Jan 14 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.4.2-1
- Update to 1.4.2
- Bump min required libebml version to 1.3.1
- Adapt specfile to the new autotools-based build system

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4.0-1
- Update to 1.4.0
- Spec file clean-up

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Thu Jul 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Mon Feb 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- New release 1.1.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Martin Sourada <mso@fedoraproject.org> - 1.0.0-1
- New release
- Fixes issues with elements with an unknown size that have come up with the 
  recent popularity of WebM files
- Bumps version of libmatroska.so
  
* Mon May 24 2010 Martin Sourada <mso@fedoraproject.org> - 0.9.0-1
- New release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.1-3
- Autorebuild for GCC 4.3

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.1-2
- Update License tag for new Licensing Guidelines compliance

* Mon Feb 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.1-1
- New upstream release 0.8.1

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-4
- Drop static lib from -devel package
- FE6 Rebuild

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.0-3
- Taking over as maintainer since Anvil has other priorities
- Long long due rebuild with new gcc for FC-5, it seems this may have already
  been done, since the last rebuild was of March 16 and the Rebuild Request
  bug of March 19? Rebuilding anyway to be sure (bug 185875)

* Thu Mar 16 2006 Dams <anvil[AT]livna.org> - 0.8.0-2.fc5
- Rebuild

* Tue Nov 29 2005 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0.
- Add a full description for the devel package.
- Some other minor spec file changes.

* Sun Jun  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.7.7-2
- Split development files into a devel subpackage.
- Run ldconfig at post (un)install time.
- Fix shared library file modes.
- Improve description.

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 0.7.7-1
- update to 0.7.7 (fixes x86_64 build)
- include shared libs

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.7.5-3
- rebuild on all arches

* Sun Feb 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.7.5-2
- 0.7.5.

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 0.7.4-2
- Update to 0.7.4.
- Bump release to provide Extras upgrade path.
- Fix spaces/tabs uglyness.

* Sun Aug 29 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.3-0.fdr.1
- Update to 0.7.3.
- Honor $RPM_OPT_FLAGS.

* Mon Jul 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.7.0-0.fdr.1
- Update to 0.7.0.
- Improved 64-bit arch build fix.

* Wed May  19 2004 Justin M. Forbes <64bit_fedora@comcast.net> 0:0.6.3-0.fdr.4
- Change linux makefile to use lib64 ifarch x86_64 for sane build

* Sat Apr  3 2004 Dams <anvil[AT]livna.org> 0:0.6.3-0.fdr.3
- Typo in description

* Sun Feb 29 2004 Dams <anvil[AT]livna.org> 0:0.6.3-0.fdr.2
- Added license files as doc
- Requires libebml-devel (headers needed)

* Sat Feb 28 2004 Dams <anvil[AT]livna.org>
- Initial build.

