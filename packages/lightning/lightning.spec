Name:           lightning
Version:        2.1.2
Release:        8%{?dist}
Summary:        Library for generating assembly code on run time

License:        LGPLv2+
URL:            http://www.gnu.org/software/lightning/lightning.html
Source0:        ftp://ftp.gnu.org/gnu/lightning/lightning-%{version}.tar.gz

BuildRequires:  texinfo, gcc
BuildRequires:  binutils-devel

%description
GNU lightning is a library to aid in making portable programs
that compiles assembly code at run time.

%package devel
Summary:        Header for the lightning package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains development header and libraries of the
ligthing package

%prep
%setup -q 

%build
%configure --enable-static=no --enable-shared=yes --with-gnu-ld --with-pic
%make_build V=1 CFLAGS="%{optflags} -fno-strict-aliasing"

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir
mv $RPM_BUILD_ROOT%{_includedir}/lightning.h $RPM_BUILD_ROOT%{_includedir}/lightning

%check
#See http://lists.gnu.org/archive/html/lightning/2017-09/msg00022.html
#make check V=1 CFLAGS="-g -fno-strict-aliasing -fPIC"

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING COPYING.DOC COPYING.LESSER
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/lightning/
%{_infodir}/lightning.info.*
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.1.2-7
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Antonio Trande <sagitterATfedoraproject.org> - 2.1.2-4
- Add gcc BR

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.1.2-3
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Antonio Trande <sagitter@fedoraproject.org> 2.1.2-1
- Update to 2.1.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Antonio Trande <sagitter@fedoraproject.org> 2.1.0-5
- Rebuild for new branches
- Use %%license tag

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.1.0-2
- Remove %%ExclusiveArch statement

* Sun Feb  8 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.1.0-1
- New upstream release
- Remove backported patch
- Add pkgconfig support

* Sat Oct 04 2014 Dan Horák <dan[at]danny.cz> - 2.0.4-5
- set ExclusiveArch to arches lightning has been ported to

* Fri Aug 29 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.4-4
- Fix misplaced texinfo-install scriptlets (#1135042)
- Add Patch to fix broken texinfo file from upstream
- Add missing BR to texinfo

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.4-2
- No prelink on aarch64/ppc64le

* Tue Apr 15 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.4-1
- New upstream release

* Thu Jan  9 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.3-1
- New upstream release

* Mon Nov  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.2-1
- New upstream release

* Fri Sep 27 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.1-2
- Fix build issues on armv7hl

* Fri Sep 27 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.1-1
- New upstream release

* Fri Aug 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.0-2
- Fir FTBFS on the armv7hl plattform

* Sat Aug 24 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.0-1
- New upstream release
- Support for more architectures
- Clen up SPEC file
- Create devel subpackage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar  3 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.2-16
- Failback to release 1.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 28 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.2c-1
- New upstream release

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-14
- fix license tag

* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.2-13
- Rebuild for gcc-4.3

* Wed Jan 23 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.2-12
- Rebuild

* Sun Aug 12 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2-11
- Changing license tag

* Thu Jul  5 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2-9
- Add prelink as a BR

* Wed Jul  4 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2-8
- Fix ppc execstack issue (#246732)

* Wed Jul  4 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2-7
- Exclude ppc architecture (#246732)

* Tue Jun 26 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2-6
- Downgrade because compiling issues
 
* Thu Jun 21 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2a-4
- Increase release number

* Mon May 21 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.2a-3
- Changing summary of the Package (#240230)

* Wed Nov 29 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2a-2
- New upstream version

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2-4
- Rebuild for FC-6

* Mon Feb 20 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2-3
- Remove %%{_infodir}/dir

* Sun Feb 19 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2-2
- Fix buildRequires
- rmove %%{_infodir}/dir file

* Sun Dec  4 2005 Jochen Schmitt <Jochen herr-schmitt de> 1.2-1
- Initial RPM
