%global srcname sseclient
%bcond_with network

Name:           python-%{srcname}
Version:        0.0.26
Release:        2%{?dist}
Summary:        Python library for iterating over HTTP Server Sent Events (SSE)

License:        MIT
URL:            https://github.com/btubbs/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a Python client library for iterating over http Server Sent Event
(SSE) streams (also known as EventSource, after the name of the Javascript
interface inside browsers). The SSEClient class accepts an URL on init, and
is then an iterator over messages coming from the server.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-mock
BuildRequires:  python3-pkginfo
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a Python client library for iterating over http Server Sent Event
(SSE) streams (also known as EventSource, after the name of the Javascript
interface inside browsers). The SSEClient class accepts an URL on init, and
is then an iterator over messages coming from the server.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with network}
%check
pytest-%{python3_version} -v
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info
%{python3_sitelib}/sseclient.py*
%{python3_sitelib}/__pycache__/sseclient*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.26-2
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.26-1
- Update to latest upstream release 0.0.26
- Fix description and Source0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.18-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.18-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jeremy Cline <jeremy@jcline.org> - 0.0.18-1
- Initial package
