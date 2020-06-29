%global pypi_name confuse

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        6%{?dist}
Summary:        A Python module for handling YAML configuration files

License:        MIT
URL:            https://github.com/beetbox/confuse
Source0:        https://github.com/beetbox/confuse/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch  

%description
Confuse is a configuration library for Python that uses YAML. It takes
care of defaults, overrides, type checking, command-line integration, human-
readable errors, and standard OS-specific locations.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#BuildRequires:  python3-PyYAML
#BuildRequires:  python3-tox
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Confuse is a configuration library for Python that uses YAML. It takes
care of defaults, overrides, type checking, command-line integration, human-
readable errors, and standard OS-specific locations.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Python 3.7 is not yet support by upstream
#%check
#tox -e py%{python3_version_nodots} 

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora
