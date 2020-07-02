%global pypi_name QtPy
%global simple_name qtpy

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        4%{?dist}
Summary:        Provides an abstraction layer on top of the various Qt bindings

License:        MIT and BSD
URL:            https://github.com/spyder-ide/%{simple_name}
Source0:        https://github.com/spyder-ide/%{simple_name}/archive/v%{version}/%{simple_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description

QtPy (pronounced ‘cutie pie’) is a small abstraction layer that lets you 
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout 
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import qt from 
qtpy instead of PyQt5.

%package -n     python3-%{pypi_name}
Summary:        Provides an abstraction layer on top of the various Qt bindings
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}

QtPy (pronounced ‘cutie pie’) is a small abstraction layer that lets you 
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout 
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import qt from 
qtpy instead of PyQt5.

%prep
%autosetup -n %{simple_name}-%{version}

rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name} 
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python3_sitelib}/qtpy
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun May 05 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sat Mar 23 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2
- Drop py2 sub-packages

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.7

* Tue May 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sat May 05 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Sat Mar 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 23 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-6
- Rebuild for Python 3.6

* Fri Sep 30 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.1.2-5
- Add BSD in license

* Fri Sep 30 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.1.2-4
- Add doc files

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.1.2-3
- Fix source URL

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.1.2-2
- Fix license installation

* Thu Aug 11 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.1.2-1
- Initial package.
