%global pypi_name aiosqlite

Name:           python-%{pypi_name}
Version:        0.12.0
Release:        2%{?dist}
Summary:        Asyncio bridge to the standard SQLite3 module

License:        MIT
URL:            https://github.com/jreese/aiosqlite
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aiosqlite AsyncIO bridge to the standard SQLite3 module for Python 3.5+.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-aiounittest
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiosqlite AsyncIO bridge to the standard SQLite3 module for Python 3.5+.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to latest upstream release 0.12.0

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-4
- Fix ownership

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-2
- Use var for souce URL
- Better use of wildcards (rhbz#1786955)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Initial package for Fedora
