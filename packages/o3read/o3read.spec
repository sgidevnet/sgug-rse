Summary:	Standalone converter for OpenOffice.org documents
Name:		o3read
Version:	0.0.4
Release:	20%{?dist}
License:	GPLv2+
URL:		http://siag.nu/o3read/
Source0:	http://siag.nu/pub/o3read/%{name}-%{version}.tar.gz
Patch0:		o3read-makefile.patch
Conflicts:	tracker < 0.6.4-4

BuildRequires:  gcc
%description
o3read is a standalone converter for the OpenOffice.org writer and calc
documents to text, html, and a dump of the parse tree.
It doesn't depend on Open Office or any other external tools or libraries.

%prep
%setup -q
%patch0 -p0 -b .mak

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" 

%install
rm -rf %buildroot
make install DESTDIR=%buildroot PREFIX=%{_prefix} MANNDIR=%{_mandir}

%files
%doc ChangeLog COPYING README TODO
%{_bindir}/o3*
%{_bindir}/utf*
%{_mandir}/man1/*.*

%Changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.0.4-2
- Rebuild for gcc43

* Sun Jan 20 2008 Deji Akingunola <dakingun@gmail.com> - 0.0.4-1
- Initial build for Fedora
