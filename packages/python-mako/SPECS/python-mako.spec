#%%if 0%%{?fedora} || 0%%{?rhel} >= 8
%bcond_without python3
#%%else
#%%bcond_with python3
#%%endif

#%%if 0%{?rhel} > 7
%bcond_with python2
#%%else
#%%bcond_without python2
#%%endif

%global upname Mako

Name: python-mako
Version: 1.1.0
Release: 1%{?dist}
BuildArch: noarch

# Mostly MIT, but _ast_util.py is Python licensed.
# The documentation contains javascript for search licensed BSD or GPLv2
License: (MIT and Python) and (BSD or GPLv2)
Summary: Mako template library for Python
URL: http://www.makotemplates.org/
Source0: https://github.com/sqlalchemy/mako/archive/rel_%(echo %{version} | sed "s/\./_/g").tar.gz

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-pytest
BuildRequires: python2-setuptools
BuildRequires: python2-markupsafe
#BuildRequires: python2-beaker
BuildRequires: python2-nose
BuildRequires: python2-mock
%endif #{with python2}

%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-markupsafe
#BuildRequires: python3-beaker
BuildRequires: python3-mock
BuildRequires: python3-nose
%endif #{with python3}

%global _description\
Mako is a template library written in Python. It provides a familiar, non-XML\
syntax which compiles into Python modules for maximum performance. Mako's\
syntax and API borrows from the best ideas of many others, including Django\
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded\
Python (i.e. Python Server Page) language, which refines the familiar ideas of\
componentized layout and inheritance to produce one of the most straightforward\
and flexible models available, while also maintaining close ties to Python\
calling and scoping semantics.

%description %_description

%if %{with python2}
%package -n python2-mako
Summary: %summary
Requires: python2-markupsafe

# Beaker is the preferred caching backend, but is not strictly necessary
Recommends: python2-beaker

%{?python_provide:%python_provide python2-mako}

%description -n python2-mako %_description
%endif #{with python2}

%package doc
Summary: Documentation for the Mako template library for Python
License: (MIT and Python) and (BSD or GPLv2)
%if %{with python3}
Requires:   python3-mako = %{version}-%{release}
%else
Requires:   python2-mako = %{version}-%{release}
%endif #{with python3}

%description doc
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

This package contains documentation in text and HTML formats.


%if %{with python3}
%package -n python3-mako
Summary: Mako template library for Python 3
Requires: python3-markupsafe

# Beaker is the preferred caching backend, but is not strictly necessary
Recommends: python3-beaker

%{?python_provide:%python_provide python3-mako}

%if %{without python2}
Obsoletes: python2-mako < %{version}-%{release}
%endif #{without python2}

%description -n python3-mako
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

This package contains the mako module built for use with python3.
%endif #{with python3}

%prep
%autosetup -n mako-rel_%(echo %{version} | sed "s/\./_/g")


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python3:%py3_install}

%if %{with python2}
mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/python3-mako-render
%endif

%{?with_python2:%py2_install}

# These are supporting files for building the docs.  No need to ship
rm -rf doc/build

%check
%if %{with python2}
py.test-2
%endif #{with python2}

%if %{with python3}
py.test-3
%endif

%if %{with python2}
%files -n python2-mako
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render
%{python2_sitelib}/*
%endif %{with python2}

%if %{with python3}
%files -n python3-mako
%license LICENSE
%doc CHANGES README.rst examples
%if %{with python2}
%{_bindir}/python3-mako-render
%else
%{_bindir}/mako-render
%endif
%{python3_sitelib}/*
%endif

%files doc
%doc doc


%changelog
* Sat Jun 20 2020 Daniel Hams <daniel.hams@gmail.com>
- Updated to install without pip install shortcut

* Mon Jun 08 2020  HAL <notes2@gmx.de> - 1.1.0-2
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (#1725969).
- https://docs.makotemplates.org/en/latest/changelog.html#change-1.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12 (#1708706).
- https://docs.makotemplates.org/en/latest/changelog.html#change-1.0.12

* Wed Apr 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-1
- Update to 1.0.9 (#1698191, #1700055)

* Wed Mar 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-1
- Update to 1.0.8 (#1470902, #1690902)

* Wed Mar 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-1
- Update to 1.0.7 (#1470902)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-10
- Rebuilt for Python 3.7

* Wed Mar 28 2018 Petr Viktorin <pviktori@redhat.com> - 1.0.6-9
- Make python-beaker an optional dependency
- Add missing python_provide for python3-mako
- Conditionalize the Python 2 subpackage
- Modernize the specfile

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
