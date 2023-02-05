Name:		fedorainfinity-backgrounds
Version:	0.0.5    
Release:	19%{?dist}
Summary:	Fedora Infinity desktop backgrounds
URL:		http://fedoraproject.org/wiki/Artwork/F8Themes/Infinity

License:	LGPLv2
Source0:	desktop-backgrounds-infinity-%{version}.tar.bz2
BuildArch:	noarch

%description
This package contains desktop backgrounds for the Fedora Infinity theme, 
which was the default theme for Fedora 8.

%prep
%setup -q -n desktop-backgrounds-infinity-%{version}


%install
# copy image files
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/backgrounds/infinity
cp -a $RPM_BUILD_DIR/desktop-backgrounds-infinity-%{version}/*.png \
	$RPM_BUILD_ROOT/%{_prefix}/share/backgrounds/infinity
# copy slideshow xml file
cp -a $RPM_BUILD_DIR/desktop-backgrounds-infinity-%{version}/infinity.xml \
	$RPM_BUILD_ROOT/%{_prefix}/share/backgrounds/infinity
# copy metadata xml file for GNOME
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/gnome-background-properties
cp -a $RPM_BUILD_DIR/desktop-backgrounds-infinity-%{version}/desktop-backgrounds-infinity.xml \
	$RPM_BUILD_ROOT/%{_prefix}/share/gnome-background-properties
# copy metadata xml file for MATE
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/mate-background-properties
ln -s ../gnome-background-properties/desktop-backgrounds-infinity.xml \
	$RPM_BUILD_ROOT/%{_prefix}/share/mate-background-properties


%files
%license COPYING
%{_datadir}/backgrounds/infinity
%{_datadir}/gnome-background-properties
%{_datadir}/mate-background-properties


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Mathieu Bridon <bochecha@daitauha.fr> - 0.0.5-11
- Add the XML metadata for MATE. (RHBZ#1226604)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 05 2010 Mathieu Bridon <bochecha@fedoraproject.org> - 0.0.5-4
- Fix folder ownership (RHBZ#569417)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr  8 2008 Matthias Clasen <mclasen@redhat.com> - 0.0.5-1
- Incorporate package review feedback

* Sun Apr  6 2008 Matthias Clasen <mclasen@redhat.com> - 0.0.4-1
- Initial package split off from desktop-backgrounds-basic
