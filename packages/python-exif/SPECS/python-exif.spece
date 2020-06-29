%global oname   exif-py

%if 0%{?fedora} < 32
%global         py2 1
%endif

Summary:        Python module to extract EXIF information
Name:           python-exif
Version:        2.2.0
Release:        6%{?dist}
License:        BSD
URL:            https://github.com/ianare/exif-py
Source0:        https://github.com/ianare/%{oname}/archive/%{version}/%{oname}-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?py2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%global _description\
Python Library to extract EXIF information in digital camera image files.

%description %_description

%if 0%{?py2}
%package -n python2-exif
Summary: %summary
%{?python_provide:%python_provide python2-exif}

%description -n python2-exif %_description
%endif

%package -n    python3-exif
Summary:       Python 3 module to extract EXIF information
%description -n python3-exif %_description

%prep
%setup -q -n %{oname}-%{version}

%build
%{?py2:%py2_build}
%py3_build

%install
%if 0%{?py2}
%py2_install
mv %{buildroot}%{_bindir}/EXIF.py %{buildroot}%{_bindir}/python2-EXIF.py
ln -s python2-EXIF.py %{buildroot}%{_bindir}/python2-EXIF
%endif
%py3_install
ln -s EXIF.py %{buildroot}%{_bindir}/EXIF

%if 0%{?py2}
%files -n python2-exif
%license LICENSE.txt
%doc ChangeLog.rst README.rst
%{_bindir}/python2-EXIF
%{_bindir}/python2-EXIF.py
%{python2_sitelib}/ExifRead-*-*.egg-info
%{python2_sitelib}/exifread
%endif

%files -n python3-exif
%license LICENSE.txt
%doc ChangeLog.rst README.rst
%{_bindir}/EXIF
%{_bindir}/EXIF.py
%{python3_sitelib}/exifread
%{python3_sitelib}/ExifRead-*-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-3
- Drop Python 2 support in newer Fedoras

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-1
- 2.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-10
- Make Python 3 default

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-8
- Python 2 binary package renamed to python2-exif
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 20 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-1
- 2.1.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.1.1-1
- 2.1.1

* Mon Apr 13 2015 Terje Rosten <terje.rosten@ntnu.no> - 2.0.2-1
- 2.0.2
- Add python3 sub package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.4.2-1
- 1.4.2
- Fix github source url

* Tue Oct 22 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.4.1-1
- 1.4.1

* Tue Aug 13 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.3.3-1
- 1.3.3, (fixing bz #996583)
- Project has moved to github

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Terje Rosten <terjeros@phys.ntnu.no> - 1.1.0-1
- 1.1.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.8-2
- Rebuild for Python 2.6

* Fri Aug 15 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.8-1
- 1.0.8

* Mon Mar  3 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-4
- Fix script (bz #435758)

* Mon Feb 11 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-3
- Add script and changes.txt

* Sat Jan 19 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-2
- Improve setup.py

* Thu Jan  3 2008 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-1
- 1.0.7
- Include egg info

* Mon Nov 19 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.5-1
- 1.0.5

* Mon Aug 06 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-3
- Tagging...

* Mon Aug 06 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-2
- Fix typo in url
- Add python-devel to buildreq
- Add license to setup.py
- Strip code from %%doc file
- Fix typo in sitelib macro

* Sat Aug 04 2007 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-1
- Initial build

