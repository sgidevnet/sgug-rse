%global srcname toolz
%global desc Toolz provides a set of utility functions for iterators, functions, and\
dictionaries. These functions interoperate well and form the building blocks\
of common data analytic operations. They extend the standard libraries\
itertools and functools and borrow heavily from the standard libraries of\
contemporary functional languages.\
\
Toolz provides a suite of functions which have the following functional\
virtues:\
\
    Composable: They interoperate due to their use of core data structures.\
    Pure: They don’t change their inputs or rely on external state.\
    Lazy: They don’t run until absolutely necessary, allowing them to support\
          large streaming data sets.\
\
Toolz functions are pragmatic. They understand that most programmers have\
deadlines.\
\
    Low Tech: They’re just functions, no syntax or magic tricks to learn\
    Tuned: They’re profiled and optimized\
    Serializable: They support common solutions for parallel computing\
\
This gives developers the power to write powerful programs to solve complex\
problems with relatively simple code. This code can be easy to understand\
without sacrificing performance. Toolz enables this approach, commonly\
associated with functional programming, within a natural Pythonic style\
suitable for most developers.

%if (%{defined fedora} && 0%{?fedora} < 30) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without python2
%endif

Name:           python-%{srcname}
Version:        0.10.0
Release:        5%{?dist}
Summary:        A functional standard library for Python

License:        BSD
URL:            http://github.com/pytoolz/%{srcname}/
Source0:        https://github.com/pytoolz/toolz/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%if %{with python2}
%package -n python2-%{srcname}
Summary:        A functional standard library for Python 2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%endif


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A functional standard library for Python %{python3_version}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{desc}


%prep
%setup -q -n %{srcname}-%{version}


%build
%if %{with python2}
%py2_build
%endif
%py3_build


%install
%py3_install
%if %{with python2}
%py2_install
%endif


%check
%if %{with python2}
nosetests-%{python2_version}
%endif
nosetests-%{python3_version}


%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE.txt
%{python2_sitelib}/%{srcname}*
%{python2_sitelib}/tlz/
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/tlz/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.8

* Tue Jul 30 2019 Orion Poplawski <orion@nwra.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Carl George <carl@george.computer> - 0.9.0-8
- EPEL compatibility

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Orion Poplawski <orion@nwra.com> - 0.9.0-6
- Drop python 2 for Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Orion Poplawski <orion@nwra.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Orion Poplawski <orion@cora.nwra.com> - 0.8.0-1
- Update to 0.8.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.7.4-1
- Initial package
