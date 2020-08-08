%global make_check 1

Summary: Library for accessing various audio file formats
Name: audiofile
Version: 0.3.6
Release: 23%{?dist}
Epoch: 1
# library is LGPL / the two programs GPL / see README
License: LGPLv2+ and GPLv2+
Source: http://audiofile.68k.org/%{name}-%{version}.tar.gz
URL: http://audiofile.68k.org/
BuildRequires:  gcc-c++
BuildRequires: libtool
#BuildRequires: alsa-lib-devel
BuildRequires: flac-devel
# optional for rebuilding manual pages from .txt
#BuildRequires: asciidoc

Patch0: audiofile-0.3.6-CVE-2015-7747.patch
# fixes to make build with GCC 6
Patch1: audiofile-0.3.6-left-shift-neg.patch
Patch2: audiofile-0.3.6-narrowing.patch
# pull requests #42,#43,#44
Patch3: audiofile-0.3.6-pull42.patch
Patch4: audiofile-0.3.6-pull43.patch
Patch5: audiofile-0.3.6-pull44.patch
Patch6: 822b732fd31ffcb78f6920001e9b1fbd815fa712.patch
Patch7: 941774c8c0e79007196d7f1e7afdc97689f869b3.patch
Patch8: fde6d79fb8363c4a329a184ef0b107156602b225.patch

Patch100: audiofile.sgifixes.patch

%description
The Audio File library is an implementation of the Audio File Library
from SGI, which provides an API for accessing audio file formats like
AIFF/AIFF-C, WAVE, and NeXT/Sun .snd/.au files. This library is used
by the EsounD daemon.

Install audiofile if you are installing EsounD or you need an API for
any of the sound file formats it can handle.

%package devel
Summary: Development files for Audio File applications
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The audiofile-devel package contains libraries, include files, and
other resources you can use to develop Audio File applications.

%prep
%setup -q
%patch0 -p1 -b .CVE-2015-7747
%patch1 -p1 -b .left-shift-neg
%patch2 -p1 -b .narrowing-conversion
%patch3 -p1 -b .pull42
%patch4 -p1 -b .pull43
%patch5 -p1 -b .pull44
%patch6 -p1 -b .CVE-2018-17095
%patch7 -p1 -b .CVE-2018-13440
%patch8 -p1 -b .CVE-2018-13440

%patch100 -p1

# A place to generate the SGUG patch
#exit 1

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1 -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
autoreconf -f -i
%configure
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a


%check
%if %{make_check}
make check
%endif


#%%ldconfig_scriptlets


%files
%license COPYING COPYING.GPL
%doc ACKNOWLEDGEMENTS AUTHORS NEWS NOTES README TODO
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_libdir}/lib*.so.1*
%{_mandir}/man1/*

%files devel
%doc ChangeLog docs/*.3.txt
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2020 Daniel Hams <daniel.hams@gmail.com> - 1:0.3.6-23
- Upgrade to version in fc31, all tests passing.

* Thu Jul 09 2020  HAL <notes2@gmx.de> - 1:0.2.7-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:0.3.6-21
- Fixes for CVE-2018-13440.

* Tue Oct 09 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:0.3.6-20
- Fix for CVE-2018-17095.

* Mon Aug 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:0.3.6-19
- Fix build

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.3.6-17
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 12 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 1:0.3.6-13
- Merge upstream pull requests #42,#43,#44 from Agostino Sarubbo to fix
  security issues.  CVE-2017-6827, CVE-2017-6828,
  CVE-2017-6829, CVE-2017-6830, CVE-2017-6831,
  CVE-2017-6832, CVE-2017-6833, CVE-2017-6834, CVE-2017-6835,
  CVE-2017-6836, CVE-2017-6837, CVE-2017-6838, CVE-2017-6839

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  3 2016 Michael Schwendt <mschwendt@fedoraproject.org> - 1:0.3.6-11
- patch to compile with GCC 6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  8 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1:0.3.6-9
- Merge fix from upstream pull request #25 for CVE-2015-7747.
  Test conversion from e.g. 16-bit LE stereo to 8-bit LE mono
  no longer causes corruption.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:0.3.6-7
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 11 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1:0.3.6-6
- BR flac-devel for FLAC support introduced in 0.3.6.
