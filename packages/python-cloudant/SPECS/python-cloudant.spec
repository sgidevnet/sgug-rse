%global pypi_name cloudant

Name:           python-%{pypi_name}
Version:        2.13.0
Release:        2%{?dist}
Summary:        Cloudant/CouchDB Client Python library

License:        ASL 2.0
URL:            https://github.com/cloudant/python-cloudant
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Cloudant and CouchDB Client library for Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Cloudant and CouchDB Client library for Python.

%prep
%autosetup -n %{name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove shebang
sed -i -e '/^#!\//, 1d' src/cloudant/*.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.13.0-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.13.0-1
- Update to latest upstream release 2.13.0 (rhbz#1824898)

* Thu Mar 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.12.0-2
- Switch to upstream source
- Add LICENSE file (rhbz#1814686)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.12.0-1
- Initial package for Fedora
