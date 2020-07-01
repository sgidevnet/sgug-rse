%global srcname munkres

Name:           python-%{srcname}
Version:        1.1.2
Release:        5%{?dist}
Summary:        A Munkres algorithm for Python

License:        BSD
URL:            http://software.clapper.org/munkres/
Source0:        https://github.com/bmc/munkres/archive/release-%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Buildarch:      noarch

%description
The Munkres module provides an implementation of the Munkres algorithm (also
called the Hungarian algorithm or the Kuhn-Munkres algorithm). The algorithm
models an assignment problem as an NxM cost matrix, where each element
represents the cost of assigning the ith worker to the jth job, and it figures
out the least-cost solution, choosing a single item from each row and column in
the matrix, such that no row and no column are used more than once.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The Munkres module provides an implementation of the Munkres algorithm (also
called the Hungarian algorithm or the Kuhn-Munkres algorithm). The algorithm
models an assignment problem as an NxM cost matrix, where each element
represents the cost of assigning the ith worker to the jth job, and it figures
out the least-cost solution, choosing a single item from each row and column in
the matrix, such that no row and no column are used more than once.

%prep
%autosetup -n %{srcname}-release-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/__pycache__/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-5
- Rebuilt for Python 3.9

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.2-1
- Update to latest upstream release 1.1.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.12-8
- Subpackage python2-munkres has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-6
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.12-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.12-1
- Update to latest upstream release 1.0.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-2
- Rebuild for Python 3.6

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.8-1
- Update to latest upstream release 1.0.8

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.7-1
- Update spec file
- Update to latest upstream release 1.0.7

* Fri Sep 13 2013 Ian Weller <iweller@redhat.com> - 1.0.5.4-1
- Initial package build
