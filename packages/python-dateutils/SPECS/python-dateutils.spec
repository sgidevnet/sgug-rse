%global pypi_name dateutils

Name:           python-%{pypi_name}
Version:        0.6.8
Release:        2%{?dist}
Summary:        Various utilities for working with date and datetime objects

License:        Public Domain
URL:            https://github.com/jmcantrell/python-dateutils
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This package is providing more complex arithmetic operations on dates/times.
Heavy use is made of the relativedelta type from the dateutil library. Much
of this package is just a light wrapper on top of this with some added
features such as range generation and business day calculation.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package is providing more complex arithmetic operations on dates/times.
Heavy use is made of the relativedelta type from the dateutil library. Much
of this package is just a light wrapper on top of this with some added
features such as range generation and business day calculation.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Not shipping dateadd and datediff as they are not ported to Python 3
# https://github.com/jmcantrell/python-dateutils/issues/2 
rm -rf dateutils/{dateadd.py,datediff.py}
sed -i -e '33,39d' setup.py
# Remove standard lib
sed -i -e '28d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.mkd
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.8-1
- Add README file
- Update to latest upstream release 0.6.8

* Tue Mar 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.7-1
- Initial package for Fedora

