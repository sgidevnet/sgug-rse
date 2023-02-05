Name:           chntpw
# Version is taken from HISTORY.txt
Version:        1.00
Release:        5.140201%{?dist}
Summary:        Change passwords in Windows SAM files
License:        GPLv2
URL:            http://pogostick.net/~pnh/ntpasswd/
Source0:        http://pogostick.net/~pnh/ntpasswd/chntpw-source-140201.zip
Source2:        chntpw-README.Dist
# The man pages are borrowed from Debian
Source10:       chntpw.8
Source11:       reged.8
Source12:       sampasswd.8
Source13:       samusrgrp.8

BuildRequires:  gcc
BuildRequires:  libgcrypt-devel

# Patches sent upstream on 2009-06-08.
Patch1:         chntpw-140201-get_abs_path.patch

# Patch from Debian (RHBZ#504595).
Patch3:         chntpw-140201-port-to-gcrypt-debian.patch

# Patches from Jim Meyering to improve robustness of the code.
Patch4:         chntpw-110511-robustness.patch
Patch5:         chntpw-080526-correct-test-for-failing-open-syscall.patch
Patch6:         chntpw-110511-detect-failure-to-write-key.patch
Patch7:         chntpw-110511-reged-no-deref-null.patch

# Patch derived from Oleg Samarin (RHBZ#1645886)
Patch8:		chntpw-140201-fix-bogus-errno-use.patch


%description
This is a utility to (re)set the password of any user that has a valid
(local) account on your Windows NT/2k/XP/Vista etc system. You do not
need to know the old password to set a new one. It works offline, that
is, you have to shutdown your computer and boot off a floppy disk or CD
or another system. Will detect and offer to unlock locked or disabled
out user accounts! There is also a registry editor and other registry
utilities that works under Linux/Unix, and can be used for other things
than password editing.


%prep
%setup -q -n %{name}-140201
cp -p %{SOURCE2} README.Dist
sed -e 's/\r$//' WinReg.txt > WinReg.txt.eol
touch -c -r WinReg.txt WinReg.txt.eol
mv WinReg.txt.eol WinReg.txt

%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1


%build
make CC="%__cc" EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
    chntpw cpnt reged sampasswd samusrgrp


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp chntpw cpnt reged sampasswd samusrgrp $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8/
cp -p %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
    $RPM_BUILD_ROOT%{_mandir}/man8/



%files
%doc GPL.txt LGPL.txt README.txt regedit.txt WinReg.txt HISTORY.txt
%doc README.Dist
%{_bindir}/chntpw
%{_bindir}/cpnt
%{_bindir}/reged
%{_bindir}/sampasswd
%{_bindir}/samusrgrp
%{_mandir}/man8/*.8*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-5.140201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Conrad Meyer <cemeyer@uw.edu> - 1.00-4.140201
- Add fix for rhbz# 1645886.  Thanks Oleg Samarin.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-3.140201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Conrad Meyer <cemeyer@uw.edu> - 1.00-2.140201
- Add missing GCC BR after removal from buildroot
- Unfuck version number bumped incorrectly by RE

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-1.140201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Conrad Meyer <cemeyer@uw.edu> - 1.00-0.140201
- Update to latest upstream, 1.00 / 140201
- Rebase patches as needed
- Import additional and enhanced manual pages from Debian
- Adds two new binaries: sampasswd and samusrgrp
- Clean up rpmlint warnings (tabs, spelling, log date)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.6-30.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.6-29.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.6-28.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.6-27.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.6-26.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-25.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-24.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-23.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 0.99.6-22.110511
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-21.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-20.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-19.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-18.110511
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Conrad Meyer <konrad@tylerc.org> - 0.99.6-17.110511
- Fix 'robustness' patch (#755622)

* Tue Nov 1 2011 Conrad Meyer <konrad@tylerc.org> - 0.99.6-16.110511
- Update to latest upstream (110511) (#750005).
- Update fedora patches to apply cleanly, dropping useless hunks
  as needed.
- Add upstream version to "Release" tag, so that people can
  actually tell which version of upstream we're shipping from the
  rpm version.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 7 2010 Conrad Meyer <konrad@tylerc.org> - 0.99.6-14
- Upstream changed hosts; fixed URL and Source0.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Richard W.M. Jones <rjones@redhat.com> - 0.99.6-12
- Two^W Three more patches from Jim Meyering to improve general code quality.

* Mon Jul 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.99.6-10
- Three patches from Jim Meyering aiming to improve the general
  robustness of the code.

* Mon Jun  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.99.6-9
- Compile against libgcrypt instead of OpenSSL (RHBZ#504595).
- Compile as a 64 bit native binary on 64 bit platforms.

* Mon Jun  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.99.6-8
- Fix three crashing bugs in 'reged -x' command.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.99.6-6
- rebuild with new openssl

* Sun Oct 12 2008 Conrad Meyer <konrad@tylerc.org> - 0.99.6-5
- Bump because force-tag was removed. Please add it back.

* Sat Oct 11 2008 Conrad Meyer <konrad@tylerc.org> - 0.99.6-4
- Fix EOL encodings in WinReg.txt.

* Sat Oct 11 2008 Conrad Meyer <konrad@tylerc.org> - 0.99.6-3
- More miscellaneous small changes.

* Fri Oct 10 2008 Conrad Meyer <konrad@tylerc.org> - 0.99.6-2
- Revert to original Makefile.
- Miscellaneous small changes.

* Wed Oct 1 2008 Conrad Meyer <konrad@tylerc.org> - 0.99.6-1
- Initial package.
