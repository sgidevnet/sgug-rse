Name: swarp
Version: 2.38.0
Release: 13%{?dist}
Summary: Tool that resamples and co-adds together FITS images

License: GPLv3+
URL: http://www.astromatic.net/software/%{name}
Source0: http://www.astromatic.net/download/swarp/swarp-%{version}.tar.gz

BuildRequires:	gcc

%description
SWarp is a program that resamples and co-adds together FITS images 
using any arbitrary astrometric projection defined in the WCS standard. 

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q

%build
%configure --enable-threads
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS BUGS COPYRIGHT HISTORY README THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/manx/*
%{_datadir}/%{name}/

%files doc
%doc COPYRIGHT doc/swarp.pdf 

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.38.0-11
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.38.0-1
- Correct source url
- License is GPLv3+
- New upstream source (2.38)

* Thu Dec 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 2.19.1-8
- Fix format security error (bz #1037344)
- Spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 2.19.1-2
- EVR bump to rebuild

* Mon Dec 13 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.19.1-1
- New upstream version
- Removed patch, it's in upstream now

* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.17.6-2
- License in -doc subpackage

* Tue Mar 30 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.17.6-1
- New version from astromatic.iap.fr. 
- License is Cecill know
- Documentation in -doc subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> 2.17.1-3
- Include unowned /usr/share/swarp directory

* Sat Jun 21 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.17.1-2
- Spec cleanup

* Thu Jun 19 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.17.1-1
- Initial spec file.
