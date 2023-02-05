Summary: Rename multiple files
Name: ren
Version: 1.0
Release: 30%{?dist}.2.1
License: Public Domain
Source: ftp://sunsite.unc.edu/pub/Linux/utils/file/ren-1.0.tar.gz
Patch0: ren-1.0.Wall.patch
URL: http://linux.maruhn.com/sec/ren.html

BuildRequires:  gcc
%description
Whereas mv can rename (as opposed to move) only one file at a time,
ren can rename many files according to search and replacement
patterns, ala VMS and MS-DOS (but better). ren checks for replacement name
collisions and handles rename chains (1 goes to 2 goes to 3 etc.)
gracefully.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
#there is no install script included in the upstream Makefile
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1/
install -m 755 ren %{buildroot}/%{_bindir}
install -m 644 -p ren.1 %{buildroot}/%{_mandir}/man1/


%files
%doc README
%{_mandir}/man1/ren.1*
%{_bindir}/ren

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-22.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-21.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-19.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-18.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-17.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Sat Feb 09 2008 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.0-12.2.1
- wrong date for previous changelog entry 

* Wed Aug 22 2007 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.0-12.2
- rebuilt for gcc4.3.0

* Wed Aug 22 2007 lonely wolf <wolfy@fedoraproject.org> - 1.0-12.1
- rebuilt

* Sat Jun 30 2007 lonely wolf <wolfy@fedoraproject.org> - 1.0-12
- fix preserving of man timestamp. Thanks Patrice Dumas for reporting it.

* Fri Sep 22 2006 lonely wolf <wolfy@pcnet.ro> - 1.0-11
- "freshly" included source did not have correct timestamps. Fixed.

* Fri Sep 22 2006 lonely wolf <wolfy@pcnet.ro> - 1.0-10
- the included tar.gz file did not match the md5sum from upstrean. recreated the src.rpm with a freshly downloaded one

* Fri Sep 22 2006 lonely wolf <wolfy@pcnet.ro> - 1.0-9
- cosmetic fixes

* Thu Jul 27 2006 lonely wolf <wolfy@pcnet.ro> - 1.0-8
- fix generation of debuginfo package

* Wed Jun 28 2006 lonely wolf <wolfy@pcnet.ro> - 1.0-7
- cleanup (%%defattr, %%make)

* Thu Jun 23 2006 lonely wolf <wolfy@pcnet.ro> - 1.0-6
- minor spec cleaning

* Fri Jun 23 2006 Alan Iwi <A.M.Iwi@rl.ac.uk>
- buildroot
- man file is gzipped and is in %%{_mandir}/man1
- patch0: changes to ensure a clean build with gcc -Wall

* Sun Aug 30 1998 W. L. Estes <wlestes@uncg.edu>
- fix docdir permissions

* Sat Aug 01 1998 W. L. Estes <wlestes@hamlet.uncg.edu>
- buildroot
- drop patch to Makefile
- relocateable
- defattr in filelist
