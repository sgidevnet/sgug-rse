%bcond_with tests

%global srcname humanfriendly

Name:           python-%{srcname}
Version:        4.18
Release:        2%{?dist}
Summary:        Human friendly output for text interfaces using Python

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
The functions and classes in the humanfriendly package can be used to make text
interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
  simple, human friendly formats.
- Easy to use timers for long running operations, with human friendly
  formatting of the resulting timespans.
- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.
- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its size.


%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-capturer
BuildRequires:  python%{python3_pkgversion}-coloredlogs
BuildRequires:  python%{python3_pkgversion}-pytest
%endif # with_tests

%if 0%{?fedora}
Suggests:       %{name}-doc = %{version}-%{release}
%endif # fedora

%description -n python%{python3_pkgversion}-%{srcname}
The functions and classes in the humanfriendly package can be used to make text
interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
  simple, human friendly formats.
- Easy to use timers for long running operations, with human friendly
  formatting of the resulting timespans.
- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.
- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its size.


%prep
%autosetup


%build
%py3_build

# Don't install the tests.py
rm build/lib/%{srcname}/tests.py

sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo


%install
%py3_install


%if 0%{?with_tests}
%check
PYTHONUNBUFFERED=1 py.test-%{python3_version} %{srcname}/tests.py
%endif # with_tests


%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{srcname}


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Scott K Logan <logans@cottsay.net> - 4.18-1
- Update to 4.18
- Drop python2 and python3_other

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 4.17-1
- Update to 4.17

* Fri Sep 28 2018 Scott K Logan <logans@cottsay.net> - 4.16.1-6
- Fix monotonic dependency for EPEL

* Mon Sep 24 2018 Scott K Logan <logans@cottsay.net> - 4.16.1-5
- Disable python2 for Fedora 30+
- Better conditionals in spec

* Fri Sep 21 2018 Scott K Logan <logans@cottsay.net> - 4.16.1-4
- Enable both python34 and python36 for EPEL

* Fri Sep 21 2018 Scott K Logan <logans@cottsay.net> - 4.16.1-3
- Switch EPEL to python36

* Fri Sep 21 2018 Scott K Logan <logans@cottsay.net> - 4.16.1-2
- Enable python34 builds for EPEL

* Thu Sep 20 2018 Scott K Logan <logans@cottsay.net> - 4.16.1-1
- Initial package
