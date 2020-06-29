%if 0%{?rhel} == 7
%bcond_with    python3
%bcond_without python2
%else
%bcond_with    python2
%bcond_without python3
%endif

%global library string_utils

Name:       python-%{library}
Version:    1.0.0
Release:    2%{?dist}
Summary:    A python module containing utility functions for strings
License:    MIT
URL:        https://github.com/daveoncode/python-string-utils
Source0:    https://github.com/daveoncode/python-string-utils/archive/v%{version}.tar.gz
BuildArch:  noarch

%if 0%{?with_python2}
%package -n python2-%{library}
Summary:    A python module containing utility functions for strings
%{?python_provide:%python_provide python2-%{library}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: git

Requires: python2

%description -n python2-%{library}
A python module containing utility functions for strings
%endif

%if 0%{?with_python3}
%package -n python3-%{library}
Summary: A python module containing utility functions for strings
%if 0%{?rhel} < 8
%{?python_provide:%python_provide python%{python3_pkgversion}-%{library}}
%else
%{?python_provide:%python_provide python3-%{library}}
%endif

%if 0%{?rhel}
%if 0%{?rhel} < 8
BuildRequires: python%{python3_pkgversion}-coverage
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-wheel
%else
BuildRequires: python3-coverage
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
%endif
%else
BuildRequires: python3-coverage
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-wheel
%endif
BuildRequires: git

%description -n python3-%{library}
A python module containing utility functions for strings
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
A python module containing utility functions for strings

%prep
%autosetup -n python-string-utils-%{version} -S git

# Let's handle dependencies ourseleves

%build
%if 0%{?with_python2}
%if 0%{?rhel} < 8
%py_build
%else
%py2_build
%endif
%endif

%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?fedora}
sphinx-build docs/ html
%{__rm} -rf html/.buildinfo
%{__rm} -rf html/.doctrees
%endif

%install
%if 0%{?with_python2}

%if 0%{?rhel} < 8
%py_install
%else
%py2_install
%endif

mkdir -p %buildroot/%_defaultdocdir/python2-string_utils
install -p -m 644 %buildroot/usr/README/README.md %buildroot/%_defaultdocdir/python2-%{library}
%{__rm} -f %buildroot/usr/README/README.md
%endif

%if 0%{?with_python3}
%py3_install
mkdir -p %buildroot/%_defaultdocdir/python3-string_utils
install -p -m 644 %buildroot/usr/README/README.md %buildroot/%_defaultdocdir/python3-%{library}
%{__rm} -f %buildroot/usr/README/README.md
%endif

%check

%if 0%{?with_python2}
coverage run -m unittest
%endif
%if 0%{?with_python3}
coverage run -m unittest
%endif

%if 0%{?with_python2}
%files -n python2-%{library}
%license %attr(644,-,-) LICENSE

%if 0%{?rhel} < 8
%doc %{_defaultdocdir}/python2-%{library}/README.md
%else
%doc README.md
%endif

%{python2_sitelib}/%{library}/
%{python2_sitelib}/python_%{library}-*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{library}
%license %attr(644,-,-) LICENSE

%if 0%{?rhel} < 8
%doc %{_defaultdocdir}/python3-%{library}/README.md
%else
%doc README.md
%endif

%{python3_sitelib}/%{library}/
%{python3_sitelib}/python_%{library}-*.egg-info
%endif

%if 0%{?fedora}
%files doc
%license %attr(644,-,-) LICENSE
%doc html
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Jason Montleon <jmontleo@redhat.com> - 1.0.0-1
- Update to 1.0.0. Drops Python 2 support.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Yatin Karel <ykarel@redhat.com> - 0.6.0-10
- Fix condition for El8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Daniel Mellado <dmellado@redhat.com> 0.6.0-4
- Fix rpmlint permissions issues
- Fix docs
- Fix doctree removal
- Fix version mismatch in spec

* Tue Dec 4 2018 John Kim <jkim@redhat.com> 0.6.0-3
- Fixed URL, Source0
- Enable disable python3 for rhel
- Enable test
- Add doc

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.0-2
- Fix python_provide for EL7 python3

* Wed May 10 2017 Jason Montleon <jmontleo@redhat.com> 0.6.0-1
- Initial Build
