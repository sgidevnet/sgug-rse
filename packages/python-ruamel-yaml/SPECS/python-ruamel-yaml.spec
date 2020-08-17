%global pypi_name ruamel.yaml
%global pname ruamel-yaml
%global commit ff02b83b8f91
%global debug_package %{nil}

Name:           python-%{pname}
Version:        0.16.5
Release:        2%{?dist}
Summary:        YAML 1.2 loader/dumper package for Python

License:        MIT
URL:            https://bitbucket.org/ruamel/yaml
# Use bitbucket sources so we can run the tests
Source0:        https://bitbucket.org/ruamel/yaml/get/%{version}.tar.gz#/%{pname}-%{version}.tar.gz
# Works with pytest 2.7
Patch0:         python-ruamel-yaml-pytest27.patch

# Don't require ruamel.std.pathlib, but use stdlib's pathlib on py3, pathlib2 on py2
Patch1:         python-ruamel-yaml-pathlib.patch


%description
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11

%package -n     python%{python3_pkgversion}-%{pname}
Summary:        YAML 1.2 loader/dumper package for Python
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:       python%{python3_pkgversion}-ruamel-yaml-clib
# typing was added in Python 3.5
%if %{python3_pkgversion} == 34
BuildRequires:  python%{python3_pkgversion}-typing
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-ruamel-yaml-clib
Requires:       python%{python3_pkgversion}-setuptools
%if %{python3_pkgversion} == 34
Requires:       python%{python3_pkgversion}-typing
%endif

%description -n python%{python3_pkgversion}-%{pname}
ruamel.yaml is a YAML 1.2 loader/dumper package for Python.
It is a derivative of Kirill Simonov’s PyYAML 3.11

%prep
%autosetup -n %{pname}-%{commit} -p1
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%{__python3} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT

%check
PYTHONPATH=$(echo build/lib) py.test-%{python3_version} _test/test_*.py

%files -n python%{python3_pkgversion}-%{pname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/ruamel
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Aug 30 2019 Chandan Kumar <raukadah@gmail.com> - 0.16.5-2
- Added ruamel-yaml-clib as Requires and BuildRequires

* Tue Aug 27 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.16.5-1
- Update to 0.16.5

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.41-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.41-3
- Subpackage python2-ruamel-yaml has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 0.15.41-1
- Update to 0.15.41
- Add patch not to require ruamel.std.pathlib

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.14-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.13.14-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 9 2017 Orion Poplawski <orion@nwra.com> - 0.13.14-1
- Update to 0.13.14

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.13.13-3
- The ruamel.yaml needs at least typing >= 3.5.2.2
  related: #1386563

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Orion Poplawski <orion@cora.nwra.com> - 0.13.13-1
- Update to 0.13.13

* Tue Jan 31 2017 Orion Poplawski <orion@cora.nwra.com> - 0.12.14-7
- Add patch to support pytest 2.7 in EPEL7

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.14-6
- Rebuild for Python 3.6

* Wed Oct 26 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.14-5
- Require python34-typing on EPEL
- Ignore python2 test failure due to old pytest on EPEL7

* Wed Oct 26 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12.14-4
- Build python3 package
- Run tests

* Tue Oct 25 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-3
- Disabling python3 as python3-ruamel-ordereddict not available

* Mon Oct 24 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-2
- Fixed python2-typing runtime dependency issue

* Fri Oct 14 2016 Chandan Kumar <chkumar@redhat.com> - 0.12.14-1
- Initial package.
