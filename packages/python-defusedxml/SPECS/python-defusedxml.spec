%global pypi_name    defusedxml
%global base_version 0.7.0
%global prerel       rc1
%global upstream_version %{base_version}%{?prerel}
Name:           python-%{pypi_name}
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        2%{?dist}
Summary:        XML bomb protection for Python stdlib modules
License:        Python
URL:            https://github.com/tiran/defusedxml
Source0:        %{pypi_source %{pypi_name} %{upstream_version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module.


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
The defusedxml package contains several Python-only workarounds and fixes for
denial of service and other vulnerabilities in Python's XML libraries. In order
to benefit from the protection you just have to import and use the listed
functions / classes from the right defusedxml module instead of the original
module. This is the python%{python3_pkgversion} build.


%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

%build
%py3_build

%install
%py3_install

%check
%{python3} tests.py


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.txt README.html CHANGES.txt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{upstream_version}-py%{python3_version}.egg-info/


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0~rc1-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0~rc1-1
- Update to 0.7.0rc1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-1
- Update to 0.6.0 (#1699639)
- Remove Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Adam Williamson <awilliam@redhat.com> - 0.5.0-1
- Update to 0.5.0, drop merged/superseded patches
- Enable Python 3 build for EPEL 7, per https://fedoraproject.org/wiki/PackagingDrafts:Python3EPEL
- Drop format-string patch as Python 2.6 is no longer supported anyway
- Update URL to github
- Update source URL for pypi changes

* Thu Dec 22 2016 Adam Williamson <awilliam@redhat.com> - 0.4.1-9
- Fix incompatibility with Python 3.6 (gh#3 / gh#4)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Ralph Bean <rbean@redhat.com> - 0.4.1-6
- Added explicit python2 subpackage with modern provides statement.
- Only apply the entity_loop patch on enterprisey builds.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 05 2015 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Add patches by Avram Lubkin
- https://bugzilla.redhat.com/show_bug.cgi?id=927883#c14

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-1
- Updated to 0.4.1 (#1100730)

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Miro Hrončok <mhroncok@redhat.com> - 0.4-1
- Initial package.
