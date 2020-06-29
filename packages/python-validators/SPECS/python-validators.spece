%global pypi_name validators

Name:           python-%{pypi_name}
Version:        0.14.2
Release:        4%{?dist}
Summary:        Data validation in Python for humans

License:        BSD
URL:            https://github.com/kvesteri/validators
Source0:        %pypi_source
#Source0:        https://github.com/kvesteri/validators/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or
a schema.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-decorator
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or
a schema.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
pytest-%{python3_version}

%files -n python3-%{pypi_name}
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.2-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.2-2
- Fix wildcard

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.14.2-1
- Update to latest upstream release 0.14.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.13.0-1
- Update to latest upstream release 0.13.0
- Update source
- Update variable name

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.12.0-2
- Initial import

* Mon Dec 25 2017 William Moreno Reyes <williamjmorenor@gmail.com> - 0.12.0-1
- Initial packaging
  Skip docs build with sphinx because a lot of extensions
