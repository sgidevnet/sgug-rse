%global pypi_name pyftdi

Name:           python-%{pypi_name}
Version:        0.51.2
Release:        2%{?dist}
Summary:        Python support for FTDI devices

License:        BSD
URL:            https://github.com/eblot/pyftdi
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyFtdi aims at providing a user-space driver for modern FTDI devices.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyFtdi aims at providing a user-space driver for modern FTDI devices.

%package -n %{name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster
BuildRequires:  python3-sphinx-autodoc-typehints

%description -n %{name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
#PYTHONPATH=${PWD} sphinx-build-3 pyftdi/doc html
#rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Not running tests for now as it's not clear how they will play with then
# build system
#%check
#PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} %{pypi_name}/tests/*.py

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/*.py
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info/

#%files -n %{name}-doc
#%doc html
#%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.51.2-2
- Rebuilt for Python 3.9

* Fri May 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.51.2-1
- Update to latest upstream release 0.51.2 (rhbz#)

* Wed Apr 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.50.2-1
- Update to latest upstream release 0.50.1 (rhbz#1826260)

* Fri Apr 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.50.1-1
- Update to latest upstream release 0.50.1 (rhbz#1821032)

* Sun Apr 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.50.0-1
- Update to latest upstream release 0.50.0 (rhbz#1821032)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.48.3-1
- Update to latest upstream release 0.48.3 (rhbz#1816213)

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.48.2-1
- Update to latest upstream release 0.48.2 (rhbz#1816213)

* Tue Mar 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.47.2-1
- Update to latest upstream release 0.47.2 (rhbz#1815122)

* Tue Mar 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.46-1
- Update to latest upstream release 0.46

* Sat Feb 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.44.2-1
- Move docs to subpackage
- Update to latest upstream release 0.44.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.42.2-1
- Update to latest upstream release 0.42.2

* Wed Sep 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.30.3-1
- Update to latest upstream release 0.30.3

* Sat Sep 07 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.30.0-1
- Update to latest upstream release 0.30.0

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.29.6-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.29.6-1
- Update to latest upstream release 0.29.6
- Fix license tag (rhbz#1732803)

* Wed Jul 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.29.2-1
- Initial package for Fedora
