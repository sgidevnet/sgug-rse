%global srcname pybtex-docutils

Name:           python-%{srcname}
Version:        0.2.2
Release:        4%{?dist}
Summary:        Docutils backend for pybtex

License:        MIT
URL:            https://github.com/mcmtroffaes/%{srcname}
Source0:        %pypi_source
BuildArch:      noarch

# Switch from nose to pytest
# https://github.com/mcmtroffaes/pybtex-docutils/commit/27f909de995d3a5f785fbb132666416a0d31789e
Patch0:         0001-Switch-to-pytest.patch
# Use a pytest fixture instead of unittest
# https://github.com/mcmtroffaes/pybtex-docutils/commit/03db06860010ceba5f0113bfb67d6721c4c4caa0
Patch1:         0002-Use-pytest-fixture-instead-of-TestCase.patch
# Use em instead of the deprecated emph in the tests
# https://github.com/mcmtroffaes/pybtex-docutils/commit/6f3b8d5e0a003107072aa020d8b802cfec42fceb
Patch2:         0003-Update-deprecated-tag.patch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-docs
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%global common_desc %{expand:
This package contains a docutils backend for pybtex, a BibTeX-compatible
bibliography processor written in Python.  Bibliographic references in
BibTeX format (or any other format supported by pybtex) can be inserted
into python documentation to be rendered by docutils.}

%description
%common_desc

%package -n python3-%{srcname}
Summary:        Docutils backend for pybtex
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)

%description -n python3-%{srcname}
%common_desc

%prep
%autosetup -n %{srcname}-%{version} -p1

# Update the sphinx theme name
sed -i "s/'default'/'classic'/" doc/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('http://docs\.python\.org/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" doc/conf.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
PYTHONPATH=$PWD make -C doc html
rst2html --no-datestamp LICENSE.rst LICENSE.html

%install
%pyproject_install

%check
PYTHONPATH=$PWD pytest test

%files -n python3-%{srcname}
%doc doc/_build/html/*
%license LICENSE.html
%{python3_sitelib}/pybtex_docutils*
%{python3_sitelib}/__pycache__/pybtex_docutils*

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-4
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Jerry James <loganjerry@gmail.com> - 0.2.2-3
- Add upstream patches to switch from nose to pytest

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Jerry James <loganjerry@gmail.com> - 0.2.2-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-11
- Subpackage python2-pybtex-docutils has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-9
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar  2 2016 Jerry James <loganjerry@gmail.com> - 0.2.1-2
- Expand package description
- Fix sphinx and noseutils invocations for python 3
- Do not convert license file to HTML

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 0.2.1-1
- Initial RPM
