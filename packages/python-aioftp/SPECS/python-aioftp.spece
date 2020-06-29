%global pypi_name aioftp

Name:           python-%{pypi_name}
Version:        0.16.0
Release:        2%{?dist}
Summary:        FTP client/server for asyncio

License:        ASL 2.0
URL:            https://github.com/aio-libs/aioftp
Source0:        %{pypi_source}
BuildArch:      noarch

%description
FTP client/server for asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-async-timeout
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-siosocks
BuildRequires:  python3-trustme
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
FTP client/server for asyncio.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license license.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-2
- Rebuilt for Python 3.9

* Fri Apr 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to latest upstream release 0.16.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-2
- Better use of wildcards (rhbz#1787314)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.0-1
- Initial package for Fedora
