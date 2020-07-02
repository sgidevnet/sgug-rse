%global pypi_name nanoid

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Unique string ID generator for Python

License:        MIT
URL:            https://github.com/puyuan/py-nanoid
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/puyuan/py-nanoid/master/LICENSE
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Nano ID is a tiny, secure, URL-friendly, unique string ID generator for
Python. It uses cryptographically strong random APIs and tests distribution
of symbols and a larger alphabet than UUID (A-Za-z0-9_-).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Nano ID is a tiny, secure, URL-friendly, unique string ID generator for
Python. It uses cryptographically strong random APIs and tests distribution
of symbols and a larger alphabet than UUID (A-Za-z0-9_-).

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE 

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# License file missing: https://github.com/puyuan/py-nanoid/pull/19
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-2
- Add license (rhbz#1830267)

* Fri May 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Initial package for Fedora
