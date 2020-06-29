%global        with_python2 0

Summary:       Generate tables in terminals from list of strings
Name:          python-terminaltables
Version:       3.1.0
Release:       18%{?dist}
License:       MIT
URL:           https://github.com/Robpol86/terminaltables
Source0:       https://github.com/Robpol86/terminaltables/archive/v%{version}.tar.gz
BuildArch:     noarch
%if %{with_python2}
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pylint
BuildRequires: python2-colorama
BuildRequires: python2-colorclass
BuildRequires: python2-flake8
BuildRequires: python2-pep8
BuildRequires: python2-pytest-cov
BuildRequires: python2-termcolor
%endif
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# Testing:
BuildRequires: python3-pytest
BuildRequires: python3-colorama
BuildRequires: python3-colorclass
BuildRequires: python3-termcolor
%global _description \
Easily draw tables in terminal/console applications (written in\
Python) from a list of lists of strings. Supports multi-line rows.
%description %_description

%if %{with_python2}
%package     -n python2-terminaltables
Summary:        %summary
%{?python_provide:%python_provide python2-terminaltables}
%description -n python2-terminaltables %_description
%endif

%package     -n python3-terminaltables
Summary:        %summary
%{?python_provide:%python_provide python3-terminaltables}
%description -n python3-terminaltables %_description

%prep
%setup -q -n terminaltables-%{version}
rm -rf terminaltables.egg-info

%build
%if %{with_python2}
%{py2_build}
%endif
%{py3_build}

%install
%if %{with_python2}
%{py2_install}
%endif
%{py3_install}

%check
%if %{with_python2}
py.test --cov-report term-missing --cov-report xml --cov terminaltables --cov-config tox.ini tests
%endif
py.test-3 tests || :

%if %{with_python2}
%files -n python2-terminaltables
%doc README.rst
%license LICENSE
%{python2_sitelib}/terminaltables
%{python2_sitelib}/terminaltables-%{version}-py?.?.egg-info/
%endif

%files -n python3-terminaltables
%doc README.rst
%license LICENSE
%{python3_sitelib}/terminaltables
%{python3_sitelib}/terminaltables-%{version}-py?.?.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-15
- Fix test stuff (rhbz#1716534)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-11
- Remove Python 2 subpackage in rawhide

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-9
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-8
- Remove unused build dependency on tox

* Mon Feb 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-7
- Clean up

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-3
- Add trailing /
- Testing enabled

* Mon May 15 2017 Terje Rosten <terje.rosten@ntnu.no> - 3.1.0-2
- Minor tweaks

* Sun Apr 23 2017 Dick Marinus <dick@mrns.nl> - 3.1.0-1
- Initial package
