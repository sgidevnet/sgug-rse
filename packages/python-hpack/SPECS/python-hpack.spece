# Created by pyp2rpm-3.3.2
%global pypi_name hpack

%global common_description %{expand:
HTTP/2 Header Encoding for Python This module contains a pure-Python
HTTP/2 header encoding (HPACK) logic for use in Python programs that implement
HTTP/2. It also contains a compatibility layer that automatically enables the
use of nghttp2 if it's available.}

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        10%{?dist}
Summary:        Pure-Python HPACK header compression

License:        MIT
URL:            http://hyper.rtfd.org
Source0:        https://github.com/python-hyper/hpack/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -rf bench

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-8
- Drop Python 2 subpackage (#1750717)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-5
- Add actual tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Initial package.
