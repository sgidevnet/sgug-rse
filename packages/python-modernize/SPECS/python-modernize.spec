%global srcname modernize

Name:           python-modernize
Version:        0.7
Release:        6%{?dist}
Summary:        Modernizes Python code for eventual Python 3 migration

License:        BSD
URL:            https://pypi.python.org/pypi/modernize
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It attempts, but does not guarantee, to generate a Python 2/3 compatible
codebase.  The code that it generates needs python2.6+ and has a runtime
dependency on python-six.

%package -n python3-modernize
Summary:            Fancy python dictionary types
%{?python_provide:%python_provide python3-modernize}
Provides: python-modernize = %{version}-%{release}
Obsoletes: python-modernize < 0.4-3

%description -n python3-modernize
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It attempts, but does not guarantee, to generate a Python 2/3 compatible
codebase.  The code that it generates needs python2.6+ and has a runtime
dependency on python-six.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-modernize
%doc README.rst
%{python3_sitelib}/modernize*
%{python3_sitelib}/libmodernize*
%{python3_sitelib}/__pycache__/modernize*
%{_bindir}/python-modernize

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 0.7-1
- Update to 0.7. Fixes bug #1680393

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-5
- Rebuild for Python 3.6

* Sat Sep 17 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-4
- Obsoletes/Provide old python-modernize name to fix upgrades. Fixes bug #1375605

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Ralph Bean <rbean@redhat.com> - 0.5-2
- Switch over to a python3 package with modern python macros.

* Thu Feb 04 2016 Ralph Bean <rbean@redhat.com> - 0.5-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Ralph Bean <rbean@redhat.com> - 0.4-1
- new version

* Wed Aug 27 2014 Luke Macken <lmacken@redhat.com> - 0.3-1
- Update to 0.3 (#1130054)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-2
- BuildRequire python-setuptools; needed by setup.py
- Remove rpm constructs not needed in EPEL6+ or any current Fedora

* Mon Jul 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-1
- Initial Fedora build.

