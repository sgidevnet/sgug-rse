%global pkgname ttystatus

Name:           python-%{pkgname}
Version:        0.38
Release:        1%{?dist}
Summary:        Progress and status updates on terminals for Python

License:        GPLv3+
URL:            http://liw.fi/%{pkgname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch

%global _description\
ttystatus is a Python library for showing progress reporting and\
status updates on terminals, for (Unix) command line programs. Output\
is automatically adapted to the width of the terminal: truncated if it\
does not fit, and re-sized if the terminal size changes.\
\
Output is provided via widgets. Each widgets formats some data into a\
suitable form for output. It gets the data either via its initializer,\
or from key/value pairs maintained by the master object. The values\
are set by the user. Every time a value is updated, widgets get\
updated (although the terminal is only updated every so often to give\
user time to actually read the output).\


%description %_description

%package -n python2-%{pkgname}
Summary:        %summary
BuildRequires:  python2-devel
BuildRequires:  python2-coverage-test-runner
BuildRequires:  python2-pep8
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname} %_description


%package -n python3-%{pkgname}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-coverage-test-runner
BuildRequires:  python3-pep8
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname} %_description


%prep
%autosetup


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
%{__python2} -m CoverageTestRunner --ignore-missing-from=without-tests
rm -rf .coverage
%{__python3} -m CoverageTestRunner --ignore-missing-from=without-tests
rm -rf .coverage


%files -n python2-%{pkgname}
%license COPYING
%doc NEWS README
%{python2_sitelib}/*

%files -n python3-%{pkgname}
%license COPYING
%doc NEWS README
%{python3_sitelib}/*


%changelog
* Mon Jan 21 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.38-1
- Update to 0.38
- Also build for Python 3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.34-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.34-5
- Add a build-time dependency on python2-devel and modernize spec file

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.34-4
- Python 2 binary package renamed to python2-ttystatus
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.34-1
- Update to 0.34

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.32-1
- Update to 0.32

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct  6 2015 Michel Salim <salimma@fedoraproject.org> - 0.26-1
- Upgrade to 0.26

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul  4 2013 Michel Salim <salimma@fedoraproject.org> - 0.23-1
- Update to 0.23

* Fri Mar 15 2013 Michel Salim <salimma@fedoraproject.org> - 0.22-1
- Update to 0.22

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.21-1
- Update to 0.21

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 18 2012 Michel Salim <salimma@fedoraproject.org> - 0.19-1
- Update to 0.19

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun  7 2012 Michel Salim <salimma@fedoraproject.org> - 0.18-2
- Remove deprecated %%{python_sitelib} declaration
- Delete build directory before doing coverage tests; the coverage
  exclusion list does not include the built version of the excluded
  modules

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.18-1
- Initial package
