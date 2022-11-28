Name:		wavpack
Summary:	A completely open audiocodec
Version:	5.1.0
Release:	16%{?dist}
License:	BSD
Url:		http://www.wavpack.com/
Source:		http://www.wavpack.com/%{name}-%{version}.tar.bz2
Patch1:		wavpack-0001-issue-27-do-not-overwrite-stack-on-corrupt-RF64-file.patch
Patch2:		wavpack-0002-issue-28-do-not-overwrite-heap-on-corrupt-DSDIFF-fil.patch
Patch3:		wavpack-0003-issue-28-fix-buffer-overflows-and-bad-allocs-on-corr.patch
Patch4:		wavpack-0004-issue-33-sanitize-size-of-unknown-chunks-before-mall.patch
Patch5:		wavpack-0005-issue-30-issue-31-issue-32-no-multiple-format-chunks.patch
Patch6:		wavpack-0006-issue-53-error-out-on-zero-sample-rate.patch
Patch7:		wavpack-0007-issue-54-fix-potential-out-of-bounds-heap-read.patch
Patch8:		wavpack-0008-issue-41-make-sure-DFF-chunk-does-not-have-negative-.patch
Patch9:		wavpack-0009-issue-43-catch-zero-channel-count-in-DSF-and-DSDIFF-.patch
Patch10:	wavpack-0010-issue-65-make-sure-DSDIFF-files-have-a-valid-channel.patch
Patch11:	wavpack-0011-issue-67-make-sure-sample-rate-is-specified-and-non-.patch
Patch12:	wavpack-0012-issue-68-clear-WaveHeader-at-start-to-prevent-uninit.patch
Patch13:	wavpack-0013-issue-66-make-sure-CAF-files-have-a-desc-chunk.patch
# For autoreconf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

%package devel
Summary:	WavPack - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Files needed for developing apps using wavpack

%prep
%autosetup -p1

%build
autoreconf -ivf
# Debian and Buildroot recomendation:
# WavPack "autodetects" CPU type to enable ASM code. However, the assembly code
# for ARM is written for ARMv7 only and building WavPack for an ARM-non-v7
# architecture will fail.
# http://lists.busybox.net/pipermail/buildroot/2015-October/142117.html
%configure --disable-static \
%ifarch armv3l armv4b armv4l armv4tl armv5tel armv5tejl armv6l armv6hl
    --disable-asm \
%endif

make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

#%%ldconfig_scriptlets

%files
%{_bindir}/*
%{_libdir}/libwavpack.so.*
%{_mandir}/man1/wavpack.1*
%{_mandir}/man1/wvgain.1*
%{_mandir}/man1/wvunpack.1*
%{_mandir}/man1/wvtag.1*
%doc AUTHORS
%license COPYING

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libwavpack.so
%doc ChangeLog README

%changelog
* Thu Jul 09 2020  HAL <notes2@gmx.de> - 5.1.0-16
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Mon Aug 19 2019 Tomas Korbar <tkorbar@redhat.com> - 5.1.0-16
- Fix for CVE-2019-1010317

* Mon Aug 19 2019 Tomas Korbar <tkorbar@redhat.com> - 5.1.0-15
- Fix for CVE-2019-1010319

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Peter Lemenkov <lemenkov@gmail.com> - 5.1.0-13
- Fix for CVE-2019-11498

* Wed Apr 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 5.1.0-12
- Fix for CVE-2018-19840, CVE-2018-19841

* Thu Feb 28 2019 Sérgio Basto <sergio@serjux.com> - 5.1.0-11
- Make the manual pages decompression format agnostic

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Miroslav Lichvar <mlichvar@redhat.com> - 5.1.0-8
- Fix for CVE-2018-10536, CVE-2018-10537, CVE-2018-10538, CVE-2018-10539,
  CVE-2018-10540

* Tue Feb 20 2018 Peter Lemenkov <lemenkov@gmail.com> - 5.1.0-7
- Fix for CVE-2018-6767, CVE-2018-7253, and two more GH issues

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.0-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sérgio Basto <sergio@serjux.com> - 5.1.0-1
- Update wavpack to 5.1.0

* Thu Apr 21 2016 Sérgio Basto <sergio@serjux.com> - 4.80.0-1
- Update wavpack to 4.80.0

* Mon Mar 28 2016 Sérgio Basto <sergio@serjux.com> - 4.75.2-1
- Update to 4.75.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.70.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.70.0-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.70.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Peter Lemenkov <lemenkov@gmail.com> - 4.70.0-1
- Ver. 4.70.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.60.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 4.60.1-7
- Reconfigure to allow building on AArch64
- Cleanup spec-file

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.60.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan  3 2013 Miroslav Lichvar <mlichvar@redhat.com> 4.60.1-5
- Fix -Wstrict-aliasing compiler warnings

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.60.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.60.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.60.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan  9 2011 Peter Lemenkov <lemenkov@gmail.com> 4.60.1-1
- Version 4.60.1 (bugfix release)
- Added man-pages
- The only patch was rebased
- Small cosmetic spec-file cleanups

* Mon Sep 28 2009 Peter Lemenkov <lemenkov@gmail.com> 4.60-1
- Version 4.60

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.50.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.50.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Peter Lemenkov <lemenkov@gmail.com> 4.50.1-2
- Fixes to meet the Fedora Packaging Guidelines

* Sun Aug 24 2008 Peter Lemenkov <lemenkov@gmail.com> 4.50.1-1
- Version 4.50.1

* Wed Jun 18 2008 Peter Lemenkov <lemenkov@gmail.com> 4.50-1
- Version 4.50

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.41-2
- Autorebuild for GCC 4.3

* Sat May 12 2007 Peter Lemenkov <lemenkov@gmail.com> 4.41-1
- Version 4.41
- Removed unnecessary --with-pic

* Fri Dec 15 2006 Peter Lemenkov <lemenkov@gmail.com> 4.40-1.1
- Rebuild

* Fri Dec 15 2006 Peter Lemenkov <lemenkov@gmail.com> 4.40-1
- Version 4.40

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 4.32-3%{?dist}
- Rebuild for FC6

* Sat Jul 01 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.32-2%{?dist}
- force PIC-only code

* Wed Jun 28 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.32-1%{?dist}
- Version 4.32

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.31-2%{?dist}
- rebuild

* Sat Jan 07 2006 Peter Lemenkov <lemenkov@newmail.ru> 4.31-1
- Fixed several issues with wavpack.pc.in
- Cosmetic fixes.
- Version 4.31

* Sun Nov 13 2005 Peter Lemenkov <lemenkov@newmail.ru> 4.3-1
- Initial build for FC-Extras
- Version 4.3

