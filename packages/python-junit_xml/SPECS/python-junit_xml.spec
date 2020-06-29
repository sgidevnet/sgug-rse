%global srcname junit_xml
%global sum python library for creating junit xml files
%global gh_owner kyrus
%global pypi_name junit-xml

%if 0%{?fedora}
# escaping for EPEL.
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%endif

Name:           python-%{srcname}
Version:        1.8
Release:        11%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# Fix for python 3.8 test failures
# Based on https://github.com/kyrus/python-junit-xml/commit/63db26da353790500642fd02cae1543eb41aab8b.patch
Patch0:         python-3.8-test-failures-fixes.patch

BuildRequires:  python3-devel

# For tests
%if 0%{?fedora}
%else
BuildRequires: pytest
%endif

BuildRequires: python3-six
BuildRequires: python3-pytest

%description
This has the python libraries for creating junit XML from python

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This has the python libraries for creating junit XML from python


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
mkdir results
%{__python3} -m pytest --junitxml=./results/junit-py3.xml

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Adrian Reber <adrian@lisas.de> - 1.8-9
- Apply adapted upstream fix for test failures

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8-5
- Subpackage python2-junit_xml has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 James Hogarth <james.hogarth@gmail.com> - 1.8-1
- update to 1.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 James Hogarth <james.hogarth@gmail.com> - 1.7-1
- Initial package
