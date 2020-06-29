%bcond_without python2

Name:           python-markupsafe
Version:        1.1.1
Release:        6%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD
URL:            https://pypi.org/project/MarkupSafe/
Source0:        %pypi_source MarkupSafe

BuildRequires:  gcc

%description
A library for safe markup escaping.


%if %{with python2}
%package -n python2-markupsafe
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python 2
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
%{?python_provide:%python_provide python2-markupsafe}

%description -n python2-markupsafe
A library for safe markup escaping. Python 2 version.
%endif


%package -n python3-markupsafe
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python 3
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-markupsafe}

%description -n python3-markupsafe
A library for safe markup escaping. Python 3 version.


%prep
%autosetup -n MarkupSafe-%{version}


%build
%if %{with python2}
%py2_build
%endif

%py3_build


%install
%if %{with python2}
%py2_install
# C code errantly gets installed
rm %{buildroot}%{python2_sitearch}/markupsafe/*.c
%endif

%py3_install
# C code errantly gets installed
rm %{buildroot}%{python3_sitearch}/markupsafe/*.c


%check
%if %{with python2}
%{__python2} setup.py test
%endif
%{__python3} setup.py test


%if %{with python2}
%files -n python2-markupsafe
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python2_sitearch}/MarkupSafe-%{version}-py%{python2_version}.egg-info/
%{python2_sitearch}/markupsafe/
%endif


%files -n python3-markupsafe
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitearch}/MarkupSafe-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/markupsafe/


%changelog
* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#1680333)

* Mon Feb 18 2019 Yatin Karel <ykarel@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-1
- Update to 1.0 (#1430160)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.23-18
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Troy Dawson <tdawson@redhat.com> - 0.23-15
- Clean up spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.23-12
- Rebuild for Python 3.6

* Thu Sep 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.23-11
- Ship python2-markupsafe
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Robert Kuska <rkuska@redhat.com> - 0.23-8
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.23-5
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.23-3
- Really rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.23-2
- Rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.23-1
- Update to 0.23

* Fri Oct 11 2013 Luke Macken <lmacken@redhat.com> - 0.18-1
- Update to 0.18 (#678537)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-6
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 0.11-2
- rebuild for newer python3

* Thu Sep 30 2010 Luke Macken <lmacken@redhat.com> - 0.11-1
- Update to 0.11

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9.2-5
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Fri Jul 23 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-3
- Fix missing setuptools BuildRequires.

* Thu Jun 24 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-2
- Fixed sitearch and python3 definitions to work better with older Fedora/RHEL.

* Wed Jun 23 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-1
- Initial version.
