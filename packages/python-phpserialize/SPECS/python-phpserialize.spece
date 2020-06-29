%global pypi_name phpserialize

Name:           python-%{pypi_name}
Version:        1.3
Release:        7%{?dist}
Summary:        A port of the serialize and unserialize functions of php to python

License:        BSD
URL:            http://github.com/mitsuhiko/phpserialize
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
phpserialize a port of the serialize and unserialize functions of php to
python. This module implements the python serialization interface (eg: provides
dumps, loads and similar functions).


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
phpserialize a port of the serialize and unserialize functions of php to
python. This module implements the python serialization interface (eg: provides
dumps, loads and similar functions).


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# tests fail with "ModuleNotFoundError: No module named 'tests'"
# disabling for now
# %{__python3} setup.py test


%files -n python3-%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 José Matos <jamatos@fedoraproject.org> - 1.3-2
- fix source url, summary and description.

* Sat Sep  1 2018 José Matos <jamatos@fedoraproject.org> - 1.3-1
- initial package.
