Name:           bodr
Version:        10
Release:        12%{?dist}
Summary:        Blue Obelisk Data Repository

License:        MIT
URL:            http://www.blueobelisk.org
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  perl(diagnostics)
Requires:       pkgconfig

%description
The Blue Obelisk Data Repository lists many important chemoinformatics data
such as element and isotope properties, atomic radii, etc. including
references to original literature. Developers can use this repository to make
their software interoperable.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

#make docs nicer
mv $RPM_BUILD_ROOT%{_docdir}/bodr DOC


%files
%doc DOC/* NEWS TODO
%{_datadir}/bodr
%{_datadir}/pkgconfig/bodr.pc


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Julian Sikorski <belegdol@fedoraproject.org> - 10-9
- Dropped needless defattr

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Julian Sikorski <belegdol@fedoraproject.org> - 10-6
- Added perl(diagnostics) to BuildRequires

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 25 2013 Julian Sikorski <belegdol@fedoraproject.org> - 10-1
- Updated to version 10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 9-3
- Rebuilt for gcc-4.7
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 27 2010 Julian Sikorski <belegdol@fedoraproject.org> - 9-1
- Updated to version 9

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  2 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 8-1
- Updated to version 8

* Sun Aug 26 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 6-2
- Rebuild

* Sat Apr 21 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 6-1
- Initial RPM release
