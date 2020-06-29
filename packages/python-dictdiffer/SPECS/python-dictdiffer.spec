%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%global library dictdiffer

Name:       python-%{library}
Version:    0.8.1
Release:    4%{?dist}
Summary:    Dictdiffer is a module that helps you to diff and patch dictionaries
License:    MIT
URL:        https://github.com/inveniosoftware/dictdiffer
Source0:    https://github.com/inveniosoftware/dictdiffer/archive/v%{version}.tar.gz
BuildArch:  noarch

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    Dictdiffer is a module that helps you to diff and patch dictionaries
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
BuildRequires: python-pytest-runner
BuildRequires: python-setuptools
BuildRequires: python-setuptools_scm
BuildRequires: git

%if 0%{?fedora}
BuildRequires: python2-pytest
BuildRequires: python2-pytest-pep8
BuildRequires: python2-pytest-cov
BuildRequires: python2-pydocstyle
BuildRequires: python2-isort
BuildRequires: python2-coverage
BuildRequires: python2-mock
BuildRequires: python2-tox
%endif

%description -n python2-%{library}
Dictdiffer is a module that helps you to diff and patch dictionaries
%endif

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: Dictdiffer is a module that helps you to diff and patch dictionaries
%if 0%{?rhel} < 8
%{?python_provide:%python_provide python%{python3_pkgversion}-%{library}}
%else
%{?python_provide:%python_provide python3-%{library}}
%endif

%if 0%{?rhel} < 8
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pytest-runner
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-setuptools_scm
%else
BuildRequires: python3-devel
BuildRequires: python3-pytest-runner
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
%endif
%if 0%{?fedora}
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-pytest-cache
%if 0%{?fedora} < 32
BuildRequires: python3-pytest-pep8
%endif
BuildRequires: python3-pydocstyle
BuildRequires: python3-isort
BuildRequires: python3-coverage
BuildRequires: python3-mock
BuildRequires: python3-tox
%endif

BuildRequires: git
%description -n python3-%{library}
Dictdiffer is a module that helps you to diff and patch dictionaries
%endif

#recommonmark not available for docs in EPEL
%if 0%{?fedora}
%package doc
Summary: Documentation for %{name}.
%if 0%{?with_python3}
BuildRequires: python3-sphinx
BuildRequires: python3-recommonmark
%else
BuildRequires: python2-sphinx
BuildRequires: python2-recommonmark
%endif
%description doc
%{summary}
%endif

%description
Dictdiffer is a module that helps you to diff and patch dictionaries

%prep
%autosetup -n %{library}-%{version} -S git
# EL7 lacks python2-pytest-runner
%if 0%{?rhel} < 8
sed -i -e /pytest-runner/d setup.py
%endif

%if 0%{?rhel}
sed -i 's/setuptools_scm>=3.1.0/setuptools_scm>=1.15.7/' setup.py
%endif

sed -i 's/tox>=3.7.0/tox>=3.4.0/' setup.py

# python-check-manifest package does not exist
sed -i -e /check-manifest/d setup.py


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%if 0%{?fedora}
PYTHONPATH=%{buildroot}/%{python3_sitelib} sphinx-build docs/ html
%{__rm} -rf html/.buildinfo
%{__rm} -rf html/.doctrees
%endif

%check
#epel is missing deps for checks
%if 0%{?fedora}
#python3-pytest-pep8 seems to be missing in F32 at the moment
%if 0%{?fedora} >= 29 && 0%{?fedora} < 32

%if 0%{?with_python2}
%{__python2} setup.py test
%endif

%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%endif
%endif

%if 0%{?with_python2}
%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{library}/*
%{python2_sitelib}/%{library}-*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{library}/*
%{python3_sitelib}/%{library}-*.egg-info
%endif

%if 0%{?fedora}
%files doc
%license LICENSE
%doc html
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 28 2019 Jaosn Montleon <jmontleo@redhat.com> 0.8.1-2
- Bump release due to infra problem

* Fri Dec 13 2019 Jaosn Montleon <jmontleo@redhat.com> 0.8.1-1
- Update to upstream 0.8.1

* Tue Nov 19 2019 Jason Montleon <jmontleo@redhat.com> 0.8.0-1
- Update to upstream 0.8.0

* Fri Oct 18 2019 Jason Montleon <jmontleo@redhat.com> 0.7.1-8
- Fix build failures, epel 8 macros

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 8 2019 Orion Poplawski <orion@nwra.com> - 0.7.1-4
- Drop BR on pytest-cache

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Dniel Mellado <dmellado@redhat.com> 0.7.1-2
- Remove inconsistency in build requirements
- Align spec in SRPM

* Tue Dec 4 2018 John Kim <jkim@redhat.com> 0.7.1-1
- Bump Versio to 0.7.1-1
- Fixed URL, Source0
- Enable disable python3 for rhel
- Add docs for fedora
- Enable tests for fedora

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.1-1
- Initial Build
