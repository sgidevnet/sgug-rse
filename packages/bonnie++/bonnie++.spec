Name:           bonnie++
Version:        1.98
Release:        1%{?dist}
Summary:        Filesystem and disk benchmark & burn-in suite
License:        GPLv2
URL:            http://www.coker.com.au/bonnie++/
Source0:        http://www.coker.com.au/bonnie++/experimental/bonnie++-%{version}.tgz
Patch0:         %{name}-makefile.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
bonnie++ filesystem and disk benchmark suite aggressively reads & writes
in various ways on your filesystem then outputs useful benchmark performance
data.  bonnie++ is also useful as a hardware, disk, and filesystem stability
test, exposing some types of hardware or kernel failures that would otherwise
be difficult to detect.

Do not leave bonnie++ installed on a production system.  Use only while you
test servers.

%prep
%autosetup

%build
%configure --disable-stripping
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install

%files
%doc readme.html copyright.txt credits.txt debian/changelog
%{_mandir}/man1/bon_csv2html.1*
%{_mandir}/man1/bon_csv2txt.1*
%{_mandir}/man1/generate_randfile.1*
%{_mandir}/man8/bonnie++.8*
%{_mandir}/man8/getc_putc.8.*
%{_mandir}/man8/zcav.8*
%{_sbindir}/bonnie++
%{_sbindir}/getc_putc
%{_sbindir}/getc_putc_helper
%{_sbindir}/zcav
%{_bindir}/bon_csv2html
%{_bindir}/bon_csv2txt
%{_bindir}/generate_randfile


%changelog
* Wed Jul 03 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.98-1
- new upstream release 1.98, fixes rhbz #1668945

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.97.3-1
- Rebuilt for new upstream release 1.97.3, fixes rhbz #1114277

* Mon Dec 19 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.96-13
- Spec clean up, silent rpmlint

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 1.96-11
- Patched to build with GCC 6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.96-9
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  9 2009 Rob Myers <rmyers@fedoraproject.org> - 1.96
- Update to experimental version (#490895)
- Merge patch from David Fetter

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03e-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.03e-2
- Don't strip binaries before -debuginfo is generated (#505570).

* Wed May 13 2009 Steven Pritchard <steve@kspei.com> 1.03e-1
- Update to 1.03e
- Drop gcc43 patch (upstream has a fix)
- Use configure and patch Makefile to install correctly

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.03c-1
- update to 1.03c
- fix license tag

* Fri Feb 08 2008 Warren Togami <wtogami@redhat.com> 1.03a-9
- rebuild for gcc-4.3

* Tue Aug 21 2007 Warren Togami <wtogami@redhat.com> 1.03a-7
- rebuild for F8

* Thu Sep 14 2006 Warren Togami <wtogami@redhat.com> 0:1.03a-6
- rebuild for FC6

* Thu Mar 16 2006 Warren Togami <wtogami@redhat.com> 0:1.03a-5
- rebuild for FC5

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Dec 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.03a-3
- Let rpmbuild take care of stripping binaries.

* Sun May 18 2003 Warren Togami <warren@togami.com> - 0:1.03-0.fdr.2.a
- #267 Ville's docs, optflags and mandir patch

* Tue May 06 2003 Warren Togami <warren@togami.com> - 0:1.03-0.fdr.1.a
- Initial RPM release
