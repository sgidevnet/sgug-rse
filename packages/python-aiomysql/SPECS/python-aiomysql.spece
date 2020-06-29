%global pypi_name aiomysql

Name:           python-%{pypi_name}
Version:        0.0.20
Release:        4%{?dist}
Summary:        MySQL driver for asyncio

License:        MIT
URL:            https://github.com/aio-libs/aiomysql
Source0:        https://github.com/aio-libs/aiomysql/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiomysql is a "driver" for accessing a MySQL database from the asyncio 
(PEP-3156/tulip) framework. It depends on and reuses most parts of PyMySQL.
aiomysql tries to be like awesome aiopg library and preserve same api, look
and feel.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiomysql is a "driver" for accessing a MySQL database from the asyncio 
(PEP-3156/tulip) framework. It depends on and reuses most parts of PyMySQL.
aiomysql tries to be like awesome aiopg library and preserve same api, look
and feel.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Testing is done with a Docker container
#%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.20-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20-2
- Better use of wildcards (rhbz#1787216)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.20-1
- Initial package for Fedora
