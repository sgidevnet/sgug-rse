Name:		nawk
Version:	20180827
Release:	2%{?dist}
Summary:	"The one true awk" descended from UNIX V7
License:	MIT
URL:		https://github.com/onetrueawk/awk
Source0:	https://github.com/onetrueawk/awk/archive/%{version}.tar.gz

# remove obsolete macros and change name from awk to nawk 
Patch0:		nawk-manpage.patch
BuildRequires:  gcc
BuildRequires:	bison

%description
This is the version of awk described in "The AWK Programming Language", by Al 
Aho, Brian Kernighan, and Peter Weinberger. (Addison-Wesley, 1988, ISBN 
0-201-07981-X).

%prep
%autosetup -n awk-%{version}

%build
make CFLAGS="%{optflags}" YACC='bison -y -d' CC="%{__cc}"

%install
rm -rf %{buildroot}

# the nawk binary is saved as a.out so we need to make our directory
# and give the binary a good name
mkdir -p %{buildroot}%{_bindir}
cp a.out %{buildroot}%{_bindir}/nawk

mkdir -p %{buildroot}%{_mandir}/man1/
cp awk.1 %{buildroot}%{_mandir}/man1/nawk.1

%files
%doc FIXES README ChangeLog
%{_bindir}/nawk
%{_mandir}/man1/nawk.1.*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180827-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May  5 2019 Mark McKinstry <mmckinst@fedoraproject.org> - 20180827-1
- update to 20180827 (RHBZ#1625789)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20121220-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121220-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121220-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121220-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Mark Mckinstry <mmckinst@nexcess.net> - 20121220-1
- upgrade to 20121220
- fix YACC variable to match update makefile

* Tue Nov 15 2011 Mark McKinstry <mmckinst@nexcess.net> 20110810-2
- take out smp in make

* Sun Aug 14 2011 Mark McKinstry <mmckinst@nexcess.net> 20110810-1
- upgrade to 20110810 version

* Wed May 11 2011 Mark McKinstry <mmckinst@nexcess.net> 20110506-1
- upgrade to 20110506 version

* Thu Oct 7 2010 Mark McKinstry <mmckinst@nexcess.net> 20100523-3
- define CC in the make

* Tue Oct 5 2010 Mark McKinstry <mmckinst@nexcess.net> 20100523-2
- don't compress the man page
- remove un-needed optimization from the makefile
- add comments explaining the patches

* Tue Sep 28 2010 Mark McKinstry <mmckinst@nexcess.net> 20100523-1
- initial build 
