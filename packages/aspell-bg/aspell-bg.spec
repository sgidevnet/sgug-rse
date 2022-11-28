%define lang bg
%define langrelease 0
Summary: Bulgarian dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 4.1
Release: 20%{?dist}
License: GPLv2
URL: http://aspell.net/
Source:   http://prdownloads.sourceforge.net/bgoffice/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2
Buildrequires: aspell >= 12:0.60
Requires: aspell >= 12:0.60

%define debug_package %{nil}

%description
Provides the word list/dictionaries for the following: Bulgarian

%prep

%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}

%build
./configure 
make %{?_smp_mflags}
iconv -f windows-1251 -t utf-8 <bg_phonet.dat >bg_phonet.dat.tmp
mv bg_phonet.dat.tmp bg_phonet.dat


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%files
%doc COPYING Copyright
%{_libdir}/aspell-0.60/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 50:4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 50:4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 50:4.1-2
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Ivana Varekova <varekova@redhat.com> - 50:4.1-1
- update to 4.1

* Wed Jun 27 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50-16
- Resolves: #245257
  aspell-bg 50:0.50-15 kills bulgarian.kbd

* Wed May  2 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50-15
- Resolves: 238426
  convert bulgarian.kbd file

* Wed Mar 28 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50-14
- variable DESTDIR is set in make command

* Tue Mar 27 2007 Ivana Varekova <varekova@redhat.com> - 50:0.50-13
- use configure script to generate makefile

* Thu Feb 22 2007 Ivana Varekova <varekova redhat com> - 50:0.50-12
- spec file cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50-11.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50-11.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 50:0.50-11.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Jul 15 2005 Ivana Varekova <varekova@redhat.com> 50:0.50-11
- fix aspell dependence

* Fri Jul 15 2005 Ivana Varekova <varekova@redhat.com> 50:0.50-10
- build with aspell-0.60.3
- convert bulgarian.kdb to utf-8

* Thu Feb 24 2005 Ivana Varekova <varekova@redhat.com> 50:0.50-8
- build new version (tarball 0.50-2), bug #142238

* Tue Oct 26 2004 Adrian Havill <havill@redhat.com> 50:0.50-4
- aspell already owns cp1251.dat (#137022)

* Tue Oct 19 2004 Adrian Havill <havill@redhat.com> 50:0.50-3
- fix version in changelog; incorrect
- fix corrupted word list; incorrect, wrong codeset (#128137)

* Wed Oct 14 2004 Adrian Havill <havill@redhat.com> 50:0.50-2
- Remove debuginfo

* Wed Aug 11 2004 Adrian Havill <havill@redhat.com> 50:0.50-1
- initial release
