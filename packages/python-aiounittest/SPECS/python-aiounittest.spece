%global pypi_name aiounittest

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        3%{?dist}
Summary:        Test asyncio code more easily

License:        MIT
URL:            https://github.com/kwarunek/aiounittest
Source0:        https://github.com/kwarunek/aiounittest/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The aiounittest is a helper library to ease your pain (and boilerplate),
when writing tests of asynchronous code (:code:asyncio). You can test:

- synchronous code (same as the :code:unittest.TestCase)
- asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from (Python 3.4)

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-coverage
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The aiounittest is a helper library to ease your pain (and boilerplate),
when writing tests of asynchronous code (:code:asyncio). You can test:

- synchronous code (same as the :code:unittest.TestCase)
- asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from Python 3.4

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-2
- Fix description (rhbz#1786953)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Initial package for Fedora
