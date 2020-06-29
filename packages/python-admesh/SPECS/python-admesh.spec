%global pypi_name admesh

Name:           python-%{pypi_name}
Version:        0.98.9
Release:        7%{?dist}
Summary:        Python bindings for ADMesh, STL manipulation library

License:        GPLv2+
URL:            https://github.com/admesh/python-admesh
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# https://github.com/admesh/python-admesh/issues/15
Source1:        %{url}/raw/v%{version}/test/utils.py

BuildRequires:  gcc

BuildRequires:  admesh-devel >= 0.98

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest-runner

%description
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.

%package -n     python3-%{pypi_name}
Summary:        Python 3 bindings for ADMesh, STL manipulation library
%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes:      python2-%{pypi_name} < 0.98.8-2
Obsoletes:      python-%{pypi_name} < 0.98.8-2

%description -n python3-%{pypi_name}
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.


%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} test/

%build
%py3_build


%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-3 -v \
%ifarch ppc64
  -k "not test_saved_equals_original_binary" # likely a bug in admesh itself
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%attr(0755,root,root) %{python3_sitearch}/%{pypi_name}.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.98.9-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.98.9-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Miro Hrončok <mhroncok@redhat.com> - 0.98.9-1
- Update to 0.98.9
- Temporarily skip a test on ppc64

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.98.8-3
- Rebuilt for Python 3.7

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.98.8-2
- Remove legacy Python subpackage

* Wed Feb 14 2018 Miro Hrončok <mhroncok@redhat.com> - 0.98.8-1
- Updated to new version 0.98.8 to fix FTBFS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Miro Hrončok <mhroncok@redhat.com> - 0.98.7-1
- Updated to new version 0.98.7
- Updated to the new naming scheme

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.98.5-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Miro Hrončok <mhroncok@redhat.com> - 0.98.5-1
- New version 0.98.5, fix FTBFS

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Miro Hrončok <mhroncok@redhat.com> - 0.98.3-1
- New version 0.98.3

* Wed Sep 03 2014 Miro Hrončok <mhroncok@redhat.com> - 0.98.1-1
- New version
- Run tests, add BR pytest

* Wed Sep 03 2014 Miro Hrončok <mhroncok@redhat.com> - 0.98-3
- Set correct executable permissions
- Typo in summary

* Thu Jul 31 2014 Miro Hrončok <mhroncok@redhat.com> - 0.98-2
- Require setuptools.

* Tue Jul 29 2014 Miro Hrončok <mhroncok@redhat.com> - 0.98-1
- Initial package.
