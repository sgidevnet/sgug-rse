Name:           lz4
Version:        1.9.1
Release:        1%{?dist}
Summary:        Extremely fast compression algorithm

License:        GPLv2+ and BSD
URL:            https://lz4.github.io/lz4/
Source0:        https://github.com/lz4/lz4/archive/v%{version}/%{name}-%{version}.tar.gz

Patch100:       lz4.sgifixes.patch

Obsoletes:      %{name} < 1.7.5-3

BuildRequires:  gcc

%description
LZ4 is an extremely fast loss-less compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-core CPU. It also features
an extremely fast decoder, with speed in multiple GB/s per core, typically
reaching RAM speed limits on multi-core systems.

%package        libs
Summary:        Libaries for lz4
Obsoletes:      %{name} < 1.7.5-3

%description    libs
This package contains the libaries for lz4.

%package        devel
Summary:        Development files for lz4
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header(.h) and library(.so) files required to build
applications using liblz4 library.

%package        static
Summary:        Static library for lz4

%description    static
LZ4 is an extremely fast loss-less compression algorithm. This package
contains static libraries for static linking of applications.

%prep
%autosetup

#exit 1
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
%configure
%make_build

%install
%configure
# Someone thinks that plain Makefiles are good for bigger projects than hello world..
%make_install LIBDIR=%{_libdir} PREFIX=%{_prefix}

#%%ldconfig_scriptlets libs

%files
%license programs/COPYING
%doc NEWS
%{_bindir}/lz4
%{_bindir}/lz4c
%{_bindir}/lz4cat
%{_bindir}/unlz4
%{_mandir}/man1/lz4.1*
%{_mandir}/man1/lz4c.1*
%{_mandir}/man1/lz4cat.1*
%{_mandir}/man1/unlz4.1*

%files libs
%doc lib/LICENSE
%{_libdir}/liblz4.so.*

%files devel
%{_includedir}/lz4*.h
%{_libdir}/liblz4.so
%{_libdir}/pkgconfig/liblz4.pc

%files static
%doc lib/LICENSE
%{_libdir}/liblz4.a

%changelog
* Wed Aug 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.1-1
- Update to 1.9.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.3-1
- Update to latest version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1.2-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1.2-2
- Switch to %%ldconfig_scriptlets

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1.2-1
- Update to 1.8.1.2

* Sat Aug 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.5-4
- Split libs properly for multilib

* Sat Mar  4 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.5-3
- Split libs out to a sub package

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.7.5-1
- Update to 1.7.5

* Fri Nov 25 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.7.4.2-1
- Update to 1.7.4.2 (RHBZ #1397373)

* Sat Nov 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.7.3-1
- Update to 1.7.3 (RHBZ #1395458)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - r131-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 pjp <pjp@fedoraproject.org> - r131-1
- New: Dos/DJGPP target #114.
- Added: Example using lz4frame library #118.
- Changed: liblz4.a no longer compiled with -fPIC by default.

* Thu Jun 18 2015 pjp <pjp@fedoraproject.org> - r130-1
- Fixed: incompatibility sparse mode vs console.
- Fixed: LZ4IO exits too early when frame crc not present.
- Fixed: incompatibility sparse mode vs append mode.
- Performance fix: big compression speed boost for clang(+30%%).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - r129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 pjp <pjp@fedoraproject.org> - r129-1
- New LZ4_compress_fast() API.
- New LZ4 CLI improved performance with multiple files.
- Other bug fix and documentation updates.

* Mon Apr 06 2015 pjp <pjp@fedoraproject.org> - r128-2
- Update files section to install unlz4 & its manual

* Wed Apr 01 2015 pjp <pjp@fedoraproject.org> - r128-1
- lz4cli sparse file support
- Restored lz4hc compression ratio
- lz4 cli supports long commands
- Introduced lz4-static sub package BZ#1208203

* Thu Jan 08 2015 pjp <pjp@fedoraproject.org> - r127-2
- Bump dist to override an earlier build.

* Wed Jan 07 2015 pjp <pjp@fedoraproject.org> - r127-1
- Fixed a bug in LZ4 HC streaming mode
- New lz4frame API integrated into liblz4
- Fixed a GCC 4.9 bug on highest performance settings

* Thu Nov 13 2014 pjp <pjp@fedoraproject.org> - r124-1
- New LZ4 HC Streaming mode

* Tue Sep 30 2014 pjp <pjp@fedoraproject.org> - r123-1
- Added experimental lz4frame API.
- Fix s390x support.

* Sat Aug 30 2014 pjp <pjp@fedoraproject.org> - r122-1
- new release
- Fixed AIX & AIX64 support (SamG)
- Fixed mips 64-bits support (lew van)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - r121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - r121-2
- fix destdir

* Fri Aug 08 2014 pjp <pjp@fedoraproject.org> - r121-1
- new release
- Added a pkg-config file.
- Fixed a LZ4 streaming crash bug.

* Thu Jul 03 2014 pjp <pjp@fedoraproject.org> - r119-1
- new release
- Fixed a high Address allocation issue in 32-bits mode.

* Sat Jun 28 2014 pjp <pjp@fedoraproject.org> - r118-1
- new release
- install libraries under appropriate _libdir directories.

* Sat Jun 14 2014 pjp <pjp@fedoraproject.org> - r117-3
- Move shared library object to -devel package.

* Sat Jun 07 2014 pjp <pjp@fedoraproject.org> - r117-2
- Skip static library from installation.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - r117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jun 06 2014 pjp <pjp@fedoraproject.org> - r117-1
- new release
- added lz4c & lz4cat manual pages.

* Sun Apr 13 2014 pjp <pjp@fedoraproject.org> - r116-1
- new release 116
- added lz4cat utility for posix systems

* Sat Mar 15 2014 pjp <pjp@fedoraproject.org> - r114-1
- new release r114
- added RPM_OPT_FLAGS to CFLAGS
- introduced a devel package to build liblz4

* Thu Jan 02 2014 pjp <pjp@fedoraproject.org> - r110-1
- new release r110

* Sun Nov 10 2013 pjp <pjp@fedoraproject.org> - r108-1
- new release r108

* Wed Oct 23 2013 pjp <pjp@fedoraproject.org> - r107-1
- new release r107

* Mon Oct 07 2013 pjp <pjp@fedoraproject.org> - r106-3
- fixed install section to replace /usr/ with a macro.
  -> https://bugzilla.redhat.com/show_bug.cgi?id=1015263#c5

* Sat Oct 05 2013 pjp <pjp@fedoraproject.org> - r106-2
- fixed install section above as suggested in the review.
  -> https://bugzilla.redhat.com/show_bug.cgi?id=1015263#c1

* Sun Sep 22 2013 pjp <pjp@fedoraproject.org> - r106-1
- Initial RPM release of lz4-r106
