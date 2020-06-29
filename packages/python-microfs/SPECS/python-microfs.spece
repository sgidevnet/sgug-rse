%global pypi_name microfs

Name:           python-%{pypi_name}
Version:        1.3.1

# no tests in sdist, no tags on github
%global commit 2fdfb2525889bf19f1f2d49c546f525855654fbc
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Release:        7%{?dist}
Summary:        CLI and Python module to work with BBC micro:bit filesystem

License:        MIT
URL:            https://github.com/ntoll/microfs
Source0:        %{url}/archive/%{commit}/%{pypi_name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pyserial
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%?python_enable_dependency_generator

%description
A simple command line tool and module for interacting with the limited file
system provided by MicroPython on the BBC micro:bit.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Provides:       %{pypi_name} == %{version}-%{release}
Provides:       ufs == %{version}-%{release}

%description -n python3-%{pypi_name}
A simple command line tool and module for interacting with the limited file
system provided by MicroPython on the BBC micro:bit.

%prep
%autosetup -n %{pypi_name}-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -vv tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/ufs
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-1
- Initial package
