%bcond_with tests

Name:           adb-enhanced
Version:        2.5.4
Release:        2%{?dist}
Summary:        Swiss-army knife for Android testing and development

License:        ASL 2.0
URL:            https://github.com/ashishb/adb-enhanced
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
%autosetup
# Remove standard lib
sed -i -e '39d' setup.py

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests/adbe_tests.py
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/adbe
%{python3_sitelib}/adbe/
%{python3_sitelib}/adb_enhanced*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.4-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.4-1
- Update prep section
- Update to latest upstream release (rhbz#1819115)

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.2-1
- Initial package for Fedora
