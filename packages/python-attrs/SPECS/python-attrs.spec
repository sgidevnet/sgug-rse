%global modname attrs

%if 0%{?rhel} && 0%{?rhel} <= 7
# Can't run tests on EPEL7 due to need for pytest >= 2.8
%bcond_with tests
%else
# Turn the tests off when bootstrapping Python, because pytest requires attrs
%bcond_with tests
%endif

Name:           python-attrs
Version:        19.1.0
Release:        2%{?dist}
Summary:        Python attributes without boilerplate

License:        MIT
URL:            http://www.attrs.org/
BuildArch:      noarch
Source0:        https://github.com/hynek/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz


BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-hypothesis
BuildRequires:  python2-six
BuildRequires:  python2-zope-interface
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-hypothesis
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-zope-interface
%endif

%description
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}

%description -n python2-%{modname}
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

%description -n python%{python3_pkgversion}-%{modname}
attrs is an MIT-licensed Python package with class decorators that
ease the chores of implementing the most common attribute-related
object protocols.

%prep
%setup -q -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
# Doesn't install anything to /usr/bin, so I don't think the order of
# installing python2 and python3 actually matters.
%py3_install
%py2_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}/%{python2_sitelib} py.test-2.7 -v
PYTHONPATH=%{buildroot}/%{python3_sitelib} py.test-3 -v
%endif

%files -n python2-%{modname}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitelib}/*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Eric Smith <brouhaha@fedoraproject.org> 19.1.0-1
- Updated to latest upstream.

* Mon Feb 25 2019 Eric Smith <brouhaha@fedoraproject.org> 18.2.0-1
- Updated to latest upstream.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 17.4.0-6
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 17.4.0-5
- Bootstrap for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.4.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Eric Smith <brouhaha@fedoraproject.org> 17.4.0-2
- Added BuildRequires for python<n>-six.

* Thu Jan 11 2018 Eric Smith <brouhaha@fedoraproject.org> 17.4.0-1
- Updated to latest upstream.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Eric Smith <brouhaha@fedoraproject.org> 16.3.0-1
- Updated to latest upstream.

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 16.1.0-3
- Enable tests

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 16.1.0-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Sat Sep 10 2016 Eric Smith <brouhaha@fedoraproject.org> 16.1.0-1
- Updated to latest upstream.
- Removed patch, no longer necessary.
- Removed "with python3" conditionals.

* Thu Aug 18 2016 Eric Smith <brouhaha@fedoraproject.org> 16.0.0-6
- Build for Python 3.4 in EPEL7.

* Thu Aug 18 2016 Eric Smith <brouhaha@fedoraproject.org> 16.0.0-5
- Updated based on Fedora package review (#1366878).
- Fix check section, though tests can not be run for EPEL7.
- Add patch to skip two tests with keyword collisions.

* Tue Aug 16 2016 Eric Smith <brouhaha@fedoraproject.org> 16.0.0-4
- Fix python2 BuildRequires.

* Mon Aug 15 2016 Eric Smith <brouhaha@fedoraproject.org> 16.0.0-3
- Updated based on Fedora package review (#1366878).

* Sun Aug 14 2016 Eric Smith <brouhaha@fedoraproject.org> 16.0.0-2
- Updated based on Fedora package review (#1366878).

* Sat Aug 13 2016 Eric Smith <brouhaha@fedoraproject.org> 16.0.0-1
- Initial version.
