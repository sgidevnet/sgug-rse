%global desc This module provides function decorators which can be used to wrap \
a function such that it will be retried until some condition is met. \
It is meant to be of use when accessing unreliable resources with the \
potential for intermittent failures i.e. network resources and external \
APIs. Somewhat more generally, it may also be of use for dynamically \
polling resources for externally generated content.
%global srcname backoff


Name:      python-%{srcname}
Version:   1.6.0
Release:   7%{?dist}
BuildArch: noarch

License: MIT
Summary: Python library providing function decorators for configurable backoff and retry
URL:     https://github.com/litl/%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/litl/backoff/issues/56
# Patch from https://github.com/litl/backoff/pull/55
Patch0:  0000-Drop-support-for-Python-3.4-to-support-aiohttp-3.3.patch

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio


%description
%{desc}


%package -n python3-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
py.test-3 tests


%files -n python3-%{srcname}
%license LICENSE
%doc CHANGELOG.md
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1566766).
- https://github.com/litl/backoff/blob/v1.6.0/CHANGELOG.md
- Import a patch from an upstream pull request to solve a Python 3.7 compatibility issue (#1605610).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-2
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.4.3-1
- Initial release (#1553447).
