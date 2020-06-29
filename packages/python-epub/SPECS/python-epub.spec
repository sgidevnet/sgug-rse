
%global srcname epub
%global commit d6db4535273d3ad2193dcb6fe090f90a1d3a3b78
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:           python-%{srcname}
Version:        0.5.2
Release:        21%{?dist}
Summary:        Python library for reading EPUB files

License:        LGPLv3+
URL:            http://epub.exirel.me
Source0:        https://bitbucket.org/exirel/%{srcname}/get/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# This patch adds a test suite to the setup() call
Patch0:         %{name}-test-suite.patch
# Skip python 3.8 incompatible tests
Patch1:         python-38-test-suite.patch

BuildArch:      noarch
# Temporary fix to handle the python2 issue and still support epel7
%if 0%{?fedora}
BuildRequires:  python3-sphinx
%else
BuildRequires:  python3-sphinx
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Epub is a Python library for reading e-book files in the EPUB (version 2)
format.

%package -n python3-%{srcname}
Summary:        Python library for reading EPUB files
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Epub is a Python library for reading e-book files in the EPUB (version 2)
format.

%package doc
Summary:        Documentation for %{name}

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n exirel-%{srcname}-%{shortcommit}
touch test/__init__.py

%build
%py3_build

%make_build -C docs html
rm -f docs/_build/html/.buildinfo

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/*

%files doc
%license LICENSE.txt
%doc docs/_build/html/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.2-19
- Skip python 3.8 incompatible tests

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.2-15
- Subpackage python2-epub has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.2-10
- Add conditionals for python2-* BRs to support epel7

* Thu Jul 06 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.2-9
- Use python2-* Requires and BR instead of python-*

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 0.5.2-7
- Remove %%{hgtag} macro
- Add missing license file to -doc subpackage

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Feb 27 2016 Filip Szymański <fszymanski@fedoraproject.org> - 0.5.2-4
- Add EPEL7 compatibility
- Rename macros

* Tue Feb 23 2016 Filip Szymański <fszymanski@fedoraproject.org> - 0.5.2-3
- Change source code URL
- Add setup.py patch
- Add %%check section
- Move HTML documentation to -doc subpackage

* Mon Feb 22 2016 Filip Szymański <fszymanski@fedoraproject.org> - 0.5.2-2
- Create python2- subpackage
- Add HTML documentation

* Sat Jan 16 2016 Filip Szymański <fszymanski@fedoraproject.org> - 0.5.2-1
- Initial RPM release
