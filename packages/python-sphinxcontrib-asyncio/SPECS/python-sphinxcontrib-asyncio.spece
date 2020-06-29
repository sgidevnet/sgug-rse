%global pypi_name sphinxcontrib-asyncio

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        4%{?dist}
Summary:        Sphinx extension to support coroutines in markup

License:        ASL 2.0
URL:            https://github.com/aio-libs/sphinxcontrib-asyncio
Source0:        https://github.com/aio-libs/sphinxcontrib-asyncio/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/aio-libs/sphinxcontrib-asyncio/master/LICENSE
BuildArch:      noarch

%description
Sphinx extension for adding asyncio-specific markups.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Sphinx extension for adding asyncio-specific markups.

%package -n python-%{pypi_name}-doc
Summary:        sphinxcontrib-asyncio documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -p %{SOURCE1} .

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_asyncio-%{version}-py*.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-2
- Better use of wildcards (rhbz#1787226)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
