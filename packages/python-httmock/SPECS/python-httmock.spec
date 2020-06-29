%{?python_enable_dependency_generator}
# Created by pyp2rpm-3.3.0
%global pypi_name httmock

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        3%{?dist}
Summary:        A mocking library for requests

License:        ASL 2.0
URL:            https://github.com/patrys/httmock
Source0:        https://files.pythonhosted.org/packages/source/h/httmock/httmock-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/patrys/httmock/%{version}/tests.py
BuildArch:      noarch
 
%description
A mocking library for requests for Python.
You can use it to mock third-party APIs and test libraries 
that use requests internally. 

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(requests) >= 1
 
%description -n python3-%{pypi_name}
A mocking library for requests for Python.
You can use it to mock third-party APIs and test libraries 
that use requests internally. 

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-1
- Update to 1.3.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.6-5
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-4
- Subpackage python2-httmock has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-2
- Rebuilt for Python 3.7

* Fri May 11 2018 Steve Traylen <steve.traylen@cern.ch> - 1.2.6-1
- Initial package.
