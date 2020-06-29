%global modname pytest-catchlog
%global altname pytest_catchlog

Name:               python-%{modname}
Version:            1.2.2
Release:            17%{?dist}
Summary:            py.test plugin to catch log messages (fork of pytest-capturelog)
License:            MIT

Source0:            https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.zip
URL:                https://github.com/eisensheng/pytest-catchlog
BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-py
BuildRequires:      python%{python3_pkgversion}-pytest

%description
py.test plugin to catch log messages. This is a fork of pytest-capturelog.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

%description -n python%{python3_pkgversion}-%{modname}
py.test plugin to catch log messages. This is a fork of pytest-capturelog.
Python %{python3_version} version.

%prep
%autosetup -n %{modname}-%{version}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

# Tests don't work due a missing dependency in pytest
#%check
#export PYTHONPATH=$(pwd)
#
#py.test-%{python3_version} -v test_pytest_catchlog.py


%files -n python%{python3_pkgversion}-%{modname}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/__pycache__/%{altname}.*
%{python3_sitelib}/%{altname}.py
%{python3_sitelib}/%{altname}-*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-12
- Subpackage python2-pytest-catchlog has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-9
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Denis Fateyev <denis@fateyev.com> - 1.2.2-8
- Disabled test suite due pytest broken deps

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.2-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-3
- Rebuild for Python 3.6

* Thu Aug 04 2016 Denis Fateyev <denis@fateyev.com> - 1.2.2-2
- Added test suite

* Fri Jul 08 2016 Denis Fateyev <denis@fateyev.com> - 1.2.2-1
- Initial Fedora release
