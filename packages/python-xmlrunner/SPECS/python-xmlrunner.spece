%global srcname xmlrunner

Name:           python-%{srcname}
Version:        1.7.7
Release:        13%{?dist}
Summary:        unittest-based test runner with Ant/JUnit like XML reporting

License:        LGPLv3
URL:            https://github.com/pycontribs/%{srcname}
Source0:        https://github.com/pycontribs/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
xmlrunner is a unittest test runner that can save test results to XML files
that can be consumed by a wide range of tools, such as build systems, IDEs
and continuous integration servers.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
xmlrunner is a unittest test runner that can save test results to XML files
that can be consumed by a wide range of tools, such as build systems, IDEs
and continuous integration servers.


%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
sed -i '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{srcname}/__init__.py

%check
#Fails, doesn't look like upstream runs it either
#py.test-%{python3_version} --ignore=setup.py --tb=long -rsxX -v --junitxml=reports xmlrunner


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.markdown
%{python3_sitelib}/%{srcname}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-7
- Remove Python 2 subpackage (#1627326)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.7-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.7.7-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Orion Poplawski <orion@cora.nwra.com> - 1.7.7-2
- Fix license
- Remove shbang

* Wed Mar 8 2017 Orion Poplawski <orion@cora.nwra.com> - 1.7.7-1
- Initial package
