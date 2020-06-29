Name: python-mako
Version: 1.1.1
Release: 2%{?dist}
BuildArch: noarch

# Mostly MIT, but _ast_util.py is Python licensed.
# The documentation contains javascript for search licensed BSD or GPLv2
License: (MIT and Python) and (BSD or GPLv2)
Summary: Mako template library for Python
URL: http://www.makotemplates.org/
Source0: https://github.com/sqlalchemy/mako/archive/rel_%(echo %{version} | sed "s/\./_/g").tar.gz


BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-markupsafe
BuildRequires: python3-mock

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


%package -n python3-mako
Summary: %{summary}

# Beaker is the preferred caching backend, but is not strictly necessary
Recommends: python3-beaker

Obsoletes: python2-mako < 1.1.0-3

%{?python_provide:%python_provide python3-mako}

%description -n python3-mako %_description

This package contains the mako module built for use with python3.


%package doc
Summary: Documentation for the Mako template library for Python
Suggests: python3-mako = %{version}-%{release}

%description doc %_description

This package contains documentation in text and HTML formats.


%prep
%autosetup -n mako-rel_%(echo %{version} | sed "s/\./_/g")


%build
%py3_build


%install
%py3_install

mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/mako-render-%{python3_version}
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render-3
ln -s ./mako-render-%{python3_version} %{buildroot}/%{_bindir}/mako-render

# These are supporting files for building the docs.  No need to ship
rm -rf doc/build


%check
pytest-3


%files -n python3-mako
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render
%{_bindir}/mako-render-3
%{_bindir}/mako-render-%{python3_version}
%{python3_sitelib}/mako/
%{python3_sitelib}/Mako-*.egg-info/

%files doc
%doc doc


%changelog
* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#1787962) (#1793184)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-4
- Fix FTBFS with pytest-5 by dropping a BR on python-nose (mako does not use nose).

* Fri Nov 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Subpackage python2-mako has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Oct 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rename the Python-versioned executables not to start with "python"
- Make mako-render Python 3 on Fedora 32+

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (#1725969).
- https://docs.makotemplates.org/en/latest/changelog.html#change-1.1.0

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.12-3
- Rebuilt for Python 3.8

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
