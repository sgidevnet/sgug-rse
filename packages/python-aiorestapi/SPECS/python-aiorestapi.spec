%global pypi_name aiorestapi

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Rapid rest resources for aiohttp

License:        ASL 2.0
URL:            https://github.com/aiselis/aiorestapi
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiorestapi allows you to quickly create a rest resource in a few steps. It
automatically creates the resource routes on the collections or individual
items; it's simply to specify the suffix '_collection' or '_item' on the
methods. The serialization/deserialization of results/requests occurs
transparently using python dictionaries.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiorestapi allows you to quickly create a rest resource in a few steps. It
automatically creates the resource routes on the collections or individual
items; it's simply to specify the suffix '_collection' or '_item' on the
methods. The serialization/deserialization of results/requests occurs
transparently using python dictionaries.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
