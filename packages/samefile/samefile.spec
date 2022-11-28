Name:		samefile
Version:	2.14
Release:	13%{?dist}
Summary:	Command-line utility to find identical files on the file system

License:	BSD
URL:		http://www.schweikhardt.net/samefile/
Source0:	http://www.schweikhardt.net/%{name}-%{version}.tar.gz

BuildRequires:  gcc


%description
The samefile utility finds files with identical contents, independent of file 
name. This program is for you if you are notoriously low on disk space, keep 
exceeding your disk quota, pay for your storage by the megabyte, run any kind 
of file server, need to reduce the size of your backups, or just want to get 
a feeling for how much redundant files are there on your system.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%check
make test


%files
%doc README ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.14-10
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.14-1
- Update to 2.14 (which automates the LFS compilation)

* Fri Feb 22 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.13-5
- Fix a couple of long-casts and %%ld usage for off_t, so file sizes
  are printed correctly, for example.

* Wed Feb 20 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.13-4
- Build with -D_FILE_OFFSET_BITS=64 for LFS as well as stat64 usage.
- Minor spec cleanup for modern guidelines.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 15 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.13-1
- Update to 2.13 (man page fix and cosmetic fixes only, however).

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 5 2008 Vivek Shah <boni.vivek at gmail.com> 2.12-3
- Fixed SOURCE0 URL

* Mon Aug 25 2008 Vivek Shah <boni.vivek at gmail.com> 2.12-2
- Added self check and ChangeLog file

* Thu Aug 21 2008 Vivek Shah <boni.vivek at gmail.com> 2.12-1
- Initial Package
