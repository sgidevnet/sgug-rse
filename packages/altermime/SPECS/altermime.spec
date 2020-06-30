Name:           altermime
Version:        0.3.10
Release:        22%{?dist}
Summary:        Alter MIME-encoded mailpacks

License:        BSD
URL:            http://www.pldaniels.com/altermime/
Source0:        http://www.pldaniels.com/altermime/altermime-%{version}.tar.gz
Patch0:         altermime-0.3.10-fprintf-compiler-error.patch
Patch1:         altermime-0.3.10-cflags.patch

BuildRequires:  gcc

%description
alterMIME is a small program which is used to alter MIME-encoded mailpacks.

alterMIME can:

 * Insert disclaimers
 * Insert arbitary X-headers
 * Modify existing headers
 * Remove attachments based on filename or content-type
 * Replace attachments based on filename 

%prep
%setup -q
%patch0 -p0
%patch1 -p0


%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
# Makefile has hardcoded paths
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 altermime %{buildroot}%{_bindir}/


%files
%{_bindir}/*

%doc CHANGELOG LICENCE README


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Tim Jackson <rpm@timj.co.uk> - 0.3.10-18
- Add missing BuildRequires on gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Tim Jackson <rpm@timj.co.uk> 0.3.10-5
- Ensure distribution-supplied CFLAGS are used during compile
- Fix build on F15

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Tim Jackson <rpm@timj.co.uk> 0.3.10-1
- Update to version 0.3.10

* Sat Jul 19 2008 Tim Jackson <rpm@timj.co.uk> 0.3.8-1
- Update to version 0.3.8

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.7-3
- Autorebuild for GCC 4.3

* Sat Sep 09 2006 Tim Jackson <rpm@timj.co.uk> 0.3.7-2
- Rebuild for FE6

* Fri Mar 31 2006 Tim Jackson <rpm@timj.co.uk> 0.3.7-1
- Update to 0.3.7

* Fri Feb 17 2006 Tim Jackson <rpm@timj.co.uk> 0.3.6-2
- Rebuild for FC5

* Wed Jan 11 2006 Tim Jackson <rpm@timj.co.uk> 0.3.6-1
- Intial build for FE
