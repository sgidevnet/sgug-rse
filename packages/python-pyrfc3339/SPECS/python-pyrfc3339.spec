%global srcname pyRFC3339
%if 0%{?rhel} && (0%{?rhel} <= 7)
%bcond_without python2
%else
%bcond_with python2
%endif

%global py3_prefix python%{python3_pkgversion}

Name:           python-pyrfc3339
Version:        1.1
Release:        5%{?dist}
Summary:        Generate and parse RFC 3339 timestamps

License:        MIT
URL:            https://pypi.python.org/pypi/pyRFC3339
Source0:        %{pypi_source}
# release tarballs do not contain unit tests (pyrfc3339/tests/tests.py)
# https://raw.githubusercontent.com/kurtraschke/pyRFC3339/master/pyrfc3339/tests/tests.py
# v1.1: git commit e30cc155
Source1:        https://raw.githubusercontent.com/kurtraschke/pyRFC3339/e30cc1555adce0ecc7bd65509a2249d47e5a41b4/pyrfc3339/tests/tests.py

BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# --- unit tests ---
BuildRequires:  python-nose
BuildRequires:  pytz
%endif

BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-setuptools
# --- unit tests ---
BuildRequires:  %{py3_prefix}-nose
BuildRequires:  %{py3_prefix}-pytz

%description
This package contains a python library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%if %{with python2}
%package -n python2-pyrfc3339
Summary:        %{summary}
%{?python_provide:%python_provide python2-pyrfc3339}

%description -n python2-pyrfc3339
This package contains a Python 2 library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.
%endif

%package     -n %{py3_prefix}-pyrfc3339
Summary:        Generate and parse RFC 3339 timestamps
%{?python_provide:%python_provide python3-pyrfc3339}

%description -n %{py3_prefix}-pyrfc3339
This package contains a Python 3 library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.



%prep
%autosetup -n %{srcname}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with python2}
%py2_install
%endif
%py3_install

%check
cp -a %{SOURCE1} .
%if %{with python2}
nosetests-2.7 tests.py
%endif
nosetests-%{python3_version} tests.py

%if %{with python2}
%files -n python2-pyrfc3339
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/pyrfc3339
%{python2_sitelib}/%{srcname}-%{version}-*.egg-info
%endif

%files -n %{py3_prefix}-pyrfc3339
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/pyrfc3339
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info


%changelog
* Thu Jun 25 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1-5
- add python-setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1-3
- also package+run unit tests
- build Python 3 subpackage also in EPEL 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Eli Young <elyscape@gmail.com> - 1.1-1
- Update to 1.1 (#1697425)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-12
- Subpackage python2-pyrfc3339 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 1.0-2
- epel7: Only build python2 package

* Tue Nov 10 2015 James Hogarth <james.hogarth@gmail.com>    - 1.0-1
- Add installed tests back as per review
- Update to new 1.0 PyPi release
- Add external license file
* Sun Nov 08 2015 James Hogarth <james.hogarth@gmail.com>    - 0.2-2
- Update to follow the python guidelines
* Wed Oct 28 2015 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2-1
- initial packaging
