%global pypi_name cooldict

Name:           python-%{pypi_name}
Version:        1.04
Release:        2%{?dist}
Summary:        Some useful dict-like structures

License:        BSD
URL:            https://github.com/zardus/cooldict
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Helper for handling dictonery-like structures.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Helper for handling dictonery-like structures.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.04-2
- Rebuilt for Python 3.9

* Tue Feb 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.04-1
- Initial package for Fedora

