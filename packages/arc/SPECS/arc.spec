Name:      arc
Version:   5.21p
Release:   16%{?dist}
Summary:   Arc archiver
License:   GPL+
URL:       http://arc.sourceforge.net/
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# 2 small polish patches courtesy of Debian
Patch0:    arc-5.21p-spelling.patch
Patch1:    arc-5.21p-manpage-section-fix.patch
# Arc was once shareware, but has been relicensed to the GPL with permission
# of its original author. But there still is some confusing license text in the
# docs this clarifies those parts of the text (rhbz#947786)
Patch2:    arc-5.21p-clarify-license.patch
# Fix reading v1 headers
Patch3:    arc-5.21p-hdrv1-read-fix.patch
# Fix arcdie crash
Patch4:    arc-5.21p-fix-arcdie.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1179143
Patch5:    arc-5.21p-directory-traversel.patch
Patch6:    arc-5.21p-compiler-warn.patch
Patch7:    arc-5.21p-fcommon-fix.patch

BuildRequires:  gcc

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.


%prep
%autosetup -p1
sed -i -e 's,^OPT =.*$,OPT = ${RPM_OPT_FLAGS},' Makefile


%build
make %{?_smp_mflags}


%install
install -m 0755 -d %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 0755 arc marc %{buildroot}%{_bindir}
install -m 0644 arc.1 marc.1 %{buildroot}%{_mandir}/man1/


%files
%doc LICENSE COPYING PATCHLEVEL Readme Arc521.doc
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Feb 15 2020 Hans de Goede <hdegoede@redhat.com> - 5.21p-16
- Fix FTBFS (rhbz#1799162)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.21p-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21p-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Hans de Goede <hdegoede@redhat.com> - 5.21p-5
- Fix directory traversal security issue (rhbz#1179143)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21p-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21p-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21p-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 Hans de Goede <hdegoede@redhat.com> 5.21p-1
- Update to latest upstream release: 5.21p
- arc was once shareware relicensed to the GPL with permission of its original
  author, update the docs to reflect this (rhbz#947786)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-9
- Rebuilt for glibc bug#747377

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21o-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.21o-5
- Autorebuild for GCC 4.3

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.21o-4
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 5.21o-3
- FE6 Rebuild

* Sun May  7 2006 <j.w.r.degoede@hhs.nl> 5.21o-2
- Unorphan, build for FC-5, devel

* Thu Oct 13 2005 <Nicolas.Mailhot at laPoste.net> 5.21o-1
- 5.21o
- more upstream gcc warning cleanups

* Sat Oct 9 2005 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 5.21n-1
- 5.21n
- upstream gcc warning cleanups

* Sat Oct 8 2005 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 5.21m-1
- update to 5.21m (CAN-2005-2945, CAN-2005-2992, #168945)
- last maintained package for now (-> orphan)

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 5.21j-4
- fix build with gcc4, patch from Nicolas Mailhot (#156225)

* Sun May 22 2005 Ralf Corsepius <ralf[AT]links2linux.de>
- Use RPM_OPT_CFLAGS inside of Makefile.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 5.21j-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 0:5.21j-0.fdr.1
- Fedorization

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 5.21j-0.num.1
- Update to 5.21j

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
