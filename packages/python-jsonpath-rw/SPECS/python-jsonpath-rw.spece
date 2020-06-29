%global pypi_name jsonpath-rw

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        2%{?dist}
Summary:        Extended implementation of JSONPath for Python

License:        ASL 2.0
URL:            https://github.com/kennknowles/python-jsonpath-rw
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%package -n python3-%{pypi_name}
Summary:        %{sumary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-ply
BuildRequires:  python3-decorator
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/jsonpath.py
%{python3_sitelib}/jsonpath_rw/
%{python3_sitelib}/jsonpath_rw-%{version}*-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Add CLI tool, enable tests and use dependency generator
- Update to latest upstream release 1.4.0 (rhbz#1818602)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-19
- Subpackage python2-jsonpath-rw has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-17
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-15
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.3-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-12
- Python 2 binary package renamed to python2-jsonpath-rw
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 06 2014 Steve Linabery <slinaber@redhat.com> - 1.2.3-2
- Add python3 specific logic around files section for python3 pkg

* Thu Jan 02 2014 Steve Linabery <slinaber@redhat.com> - 1.2.3-1
- Initial packaging for Fedora
