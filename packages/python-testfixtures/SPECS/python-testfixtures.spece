%global pypi_name testfixtures

Name:           python-%{pypi_name}
Version:        6.14.1
Release:        3%{?dist}
Summary:        Collection of helpers and mock objects for unit tests

License:        MIT
URL:            https://github.com/Simplistix/testfixtures
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-django
BuildRequires:  python3-twisted
BuildRequires:  python3-zope-component
BuildRequires:  python3-sybil
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v testfixtures/tests/*.py \
  -k "not test_log_then_patch and not test_our_wrap_dealing_with_mock_patch and not test_patch_with_dict"

%files -n python3-%{pypi_name}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.egg-info/

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> -6.14.1-3
- Add python3-setuptools as BR

* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.1-2
- Remove *.egg in prep section

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.1-1
- Exclude the failing tests for now
- Update to latest upstream release 6.14.1

* Sat Apr 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.14.0-1
- Update to latest upstream release 6.14.0

* Wed Feb 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.13.0-1
- Update to latest upstream release 6.13.0

* Mon Feb 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.12.0-1
- Update to latest upstream release 6.12.0

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.10.3-1
- Update to latest upstream release 6.10.3

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.8.2-2
- Fix license, URL and naming (rhbz#1708161)

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.8.2-1
- New spec file for re-review

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.3-5
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Miro Hrončok <mhroncok@redhat.com> - 4.14.3-4
- Fix pytohn2-django requires https://fedoraproject.org/wiki/Changes/Django20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Björn Esser <besser82@fedoraproject.org> - 4.14.3-1
- New upstream release (rhbz#1450930)

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.5-1
- Initial import (rhbz#1445824)

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.5-0.2
- Fix E: python-bytecode-wrong-magic-value

* Wed Apr 26 2017 Björn Esser <besser82@fedoraproject.org> - 4.13.5-0.1
- Initial rpm-release (rhbz#1445824)
