%global srcname cftime

Name:           python-%{srcname}
Version:        1.1.3
Release:        2%{?dist}
Summary:        Time-handling functionality from netcdf4-python

# calendar calculation routines in _cftime.pyx derived from calcalcs.c by David
# W. Pierce with GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
License:        MIT and GPLv3
URL:            https://pypi.python.org/pypi/cftime
Source0:        %{pypi_source}

BuildRequires:  gcc
%{?python_enable_dependency_generator}

%description
Time-handling functionality from netcdf4-python.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  %{py3_dist coverage}
BuildRequires:  python%{python3_pkgversion}-coveralls
BuildRequires:  python%{python3_pkgversion}-pytest-cov
BuildRequires:  python%{python3_pkgversion}-numpy
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Time-handling functionality from netcdf4-python.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-%{python3_version} -v

%files -n python%{python3_pkgversion}-%{srcname}
%license COPYING
%doc README.md
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Orion Poplawski <orion@nwra.com> - 1.1.3-1
- Update to 1.1.3

* Fri May 08 2020 Orion Poplawski <orion@nwra.com> - 1.1.2-1
- Update to 1.1.2

* Thu Mar 26 2020 Orion Poplawski <orion@nwra.com> - 1.1.1.2-1
- Update to 1.1.1.2

* Wed Mar 18 2020 Orion Poplawski <orion@nwra.com> - 1.1.1-1
- Update to 1.1.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Orion Poplawski <orion@nwra.com> - 1.0.4.2-1
- Update to 1.0.4.2

* Mon Oct 21 2019 Orion Poplawski <orion@nwra.com> - 1.0.4-1
- Update to 1.0.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Sep 11 2019 Orion Poplawski <orion@nwra.com> - 1.0.3.4-5
- Enable python automatic dependency generator (for EPEL8)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Orion Poplawski <orion@nwra.com> - 1.0.3.4-2
- Fix license

* Tue Feb 26 2019 Orion Poplawski <orion@nwra.com> - 1.0.3.4-1
- Initial Fedora package
