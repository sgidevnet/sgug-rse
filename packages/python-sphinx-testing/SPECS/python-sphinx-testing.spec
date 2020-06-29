%global srcname sphinx-testing

Name:           python-%{srcname}
Version:        1.0.1
Release:        8%{?dist}
Summary:        Testing utility classes and functions for Sphinx extensions

License:        BSD
URL:            https://github.com/sphinx-doc/sphinx-testing
Source0:        %pypi_source
# See https://bugzilla.redhat.com/show_bug.cgi?id=1789151
Patch0:         %{name}-open-mode.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)

%global common_desc %{expand:
This package provides a few utility classes and functions to help
authors of Sphinx extensions write tests for those extensions.}

%description
%common_desc

%package -n python3-%{srcname}
Summary:        Testing utility classes and functions for Sphinx extensions
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%common_desc

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove useless shebang
sed -i '\@/usr/bin/env python@d' src/sphinx_testing/path.py

%build
%py3_build
rst2html --no-datestamp CHANGES.rst CHANGES.html
rst2html --no-datestamp README.rst README.html

%install
%py3_install

%check
# upstream project uses nose which is no longer maintained, along with nose-cov
# which isn't packaged.
# Using py.test just works: https://github.com/sphinx-doc/sphinx-testing/issues/15
PYTHONPATH=$PWD/src pytest-%{python3_version} -v tests

%files -n python3-%{srcname}
%doc AUTHORS Sphinx-AUTHORS *.html
%license LICENSE
%{python3_sitelib}/sphinx_testing*

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan  8 2020 Jerry James <loganjerry@gmail.com> - 1.0.1-6
- Add -open-mode patch to fix FTBFS with python 3.9

* Thu Jan  2 2020 Jerry James <loganjerry@gmail.com> - 1.0.1-5
- Switch from nose to pytest (thanks to Alfredo Deza)
- Drop redundant Requires

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream version (bz 1700035)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- New upstream version (bz 1669778)

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- New upstream version
- Drop all patches; all upstreamed

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 0.7.2-6
- Drop python2 subpackage (bz 1645075)
- Use upstream's version of the -test patch
- Add -badge, -sphinx8, -desc, and -py33 patches from upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Jerry James <loganjerry@gmail.com> - 0.7.2-1
- New upstream version (bz 1447818)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuild for Python 3.6

* Tue Mar  1 2016 Jerry James <loganjerry@gmail.com> - 0.7.1-2
- Clarify the description
- Fix nosetests invocation
- Don't preserve timestamp of altered file

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 0.7.1-1
- Initial RPM
