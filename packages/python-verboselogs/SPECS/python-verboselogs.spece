%global srcname verboselogs

Name:           python-%{srcname}
Version:        1.7
Release:        10%{?dist}
Summary:        Verbose logging level for Python's logging module

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Compatibility with astroid 2.0 - not submitted upstream
Patch0:         %{name}-1.7-astroid2.patch
# Use a more available sphinx theme - not submitted upstream
Patch1:         %{name}-1.7-sphinx-theme.patch

BuildArch:      noarch

%description
The verboselogs package extends Python's logging module to add the log levels
NOTICE, SPAM, SUCCESS and VERBOSE:

- The NOTICE level sits between the predefined WARNING and INFO levels.
- The SPAM level sits between the predefined DEBUG and NOTSET levels.
- The SUCCESS level sits between the predefined WARNING and ERROR levels.
- The VERBOSE level sits between the predefined INFO and DEBUG levels.

The code to do this is simple and short, but I still don't want to copy/paste it
to every project I'm working on, hence this package.


%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-astroid
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pylint
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
The verboselogs package extends Python's logging module to add the log levels
NOTICE, SPAM, SUCCESS and VERBOSE:

- The NOTICE level sits between the predefined WARNING and INFO levels.
- The SPAM level sits between the predefined DEBUG and NOTSET levels.
- The SUCCESS level sits between the predefined WARNING and ERROR levels.
- The VERBOSE level sits between the predefined INFO and DEBUG levels.

The code to do this is simple and short, but I still don't want to copy/paste it
to every project I'm working on, hence this package.


%prep
%autosetup -p1


%build
%py3_build

# Don't install pylint.py or tests.py
rm build/lib/%{srcname}/{pylint,tests}.py

sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo


%install
%py3_install


%check
PYTHONUNBUFFERED=1 py.test-%{python3_version} %{srcname}/tests.py


%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7-10
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Scott K Logan <logans@cottsay.net> - 1.7.8-9
- Drop unsupported comments from spec file
- Add weak dependency for EPEL 8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Scott K Logan <logans@cottsay.net> - 1.7-4
- Drop python2 and python3_other
- Add patches for astroid and sphinx compatibility

* Fri Oct 26 2018 Scott K Logan <logans@cottsay.net> - 1.7-3
- Pattern conformance

* Fri Sep 28 2018 Scott K Logan <logans@cottsay.net> - 1.7-2
- Add setuptools dependency for EPEL

* Fri Sep 28 2018 Scott K Logan <logans@cottsay.net> - 1.7-1
- Initial package
