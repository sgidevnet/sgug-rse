# Created by pyp2rpm-3.3.2
%global pypi_name hyperframe

%global common_description %{expand:
Pure-Python HTTP/2 framing This library contains the HTTP/2
framing code used in the hyper project. It provides a pure-Python codebase
that is capable of decoding a binary stream into HTTP/2 frames. This library is
used directly by hyper and a number of other projects to provide HTTP/2 frame
decoding logic.}

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        6%{?dist}
Summary:        HTTP/2 framing layer for Python

License:        MIT
URL:            http://hyper.rtfd.org
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

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
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.2.0-4
- Drop Python 2 subpackage (#1750718)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 5.2.0-1
- Release 5.2.0
- Add actual tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 5.1.0-1
- Initial package.
