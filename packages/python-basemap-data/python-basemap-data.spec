Name:           python-basemap-data
Version:        1.2.0
Release:        2%{?dist}
Summary:        Data for python-basemap
License:        GPLv2 and Public Domain
URL:            http://matplotlib.sourceforge.net/matplotlib.toolkits.basemap.basemap.html
Source0:        http://downloads.sourceforge.net/matplotlib/basemap-%{version}.tar.gz
Obsoletes:	python-basemap-data-hires < %{version}-%{release}
Provides:	python-basemap-data-hires = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  python2-devel

%description
Data for python-basemap


%prep
%setup -q -n basemap-%{version}rel


%build


%install
# Install the data
install -d $RPM_BUILD_ROOT%{_datadir}
cp -a lib/mpl_toolkits/basemap/data/ $RPM_BUILD_ROOT%{_datadir}/basemap



%files
%license LICENSE_data
%doc README.md
%{_datadir}/basemap/


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.0.7-6
- Undo hires package split, BZ 1203048.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Jon Ciesla <limburgher@gmail.com> - 1.0.7-1
- 1.0.7.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 04 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.6-1
- 1.0.6, BZ 870640.

* Wed Jan 30 2013 Jon Ciesla <limburgher@gmail.com> - 0.99.4-6
- Corrected Source0, BZ 905962.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 28 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.99.4-2
- Move python-basemap-examples subpackage to python-basemap srpm 
- Make it possible to install python-basemap-data without python-basemap

* Fri Dec 11 2009 Jon Ciesla <limb@jcomserv.net> - 0.99.4-1
- Update to latest upstream.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.99.2-1
- Update to latest release

* Thu Dec 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.99.1-1
- Update to match matplotlib release

* Thu Aug 23 2007 Orion Poplawski <orion@cora.nwra.com> 0.9.5-3
- Update license tags

* Thu Mar 29 2007 Orion Poplawski <orion@cora.nwra.com> 0.9.5-2
- Change Requires from /usr/share/basemap to python-basemap

* Wed Mar 28 2007 Orion Poplawski <orion@cora.nwra.com> 0.9.5-1
- Split into regular and -hires packages
- Ship the basemap examples in python-basemap-examples

* Mon Feb 19 2007 Orion Poplawski <orion@cora.nwra.com> 0.9-2
- Add BR: python-devel

* Mon Jul  3 2006 Orion Poplawski <orion@cora.nwra.com> 0.9-1
- Update to 0.9

* Fri Feb 24 2006 Orion Poplawski <orion@cora.nwra.com> 0.8-1
- Update to 0.8

* Sun Nov 20 2005 Orion Poplawski <orion@cora.nwra.com> 0.7-1
- Initial package for Fedora Extras
