%{?python_enable_dependency_generator}
%global realname parsedatetime

%bcond_without tests

Name:           python-%{realname}
Version:        2.5
Release:        3%{?dist}
Summary:        Parse human-readable date/time strings in Python

License:        ASL 2.0
URL:            https://github.com/bear/%{realname}
Source0:        https://github.com/bear/%{realname}/archive/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
parsedatetime is a python module that can parse human-readable date/time\
strings.


%package -n python3-%{realname}
Summary:        Parse human-readable date/time strings in Python
%{?python_provide:%python_provide python3-%{realname}}

%description -n python3-%{realname}
parsedatetime is a python module that can parse human-readable date/time
strings.

%prep
%autosetup -n %{realname}-%{version}


%build
%py3_build


%install
%py3_install
# It makes no sense to ship all these tests in the package
# just use them during the build
rm -rf %{buildroot}%{python3_sitelib}/%{realname}/tests

%check
%if %{with tests}
py.test-3 -x tests/*.py
%endif

%files -n python3-%{realname}
%license LICENSE.txt
%doc AUTHORS.txt CHANGES.txt README.rst
%{python3_sitelib}/%{realname}
%{python3_sitelib}/%{realname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 2.5-1
- update to new upstream version 2.5 (#1773846)

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 2.4-16
- add "tests" define to run tests manually without changing the spec file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-11
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-10
- Remove Python 2 subpackage and epydoc documentation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4-8
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4-7
- Fix BuildRequires to require the tox command and not the python2 module

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Eli Young <elyscape@gmail.com> - 2.4-5
- Declare missing dependency on python-future
- Update package on EPEL7

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.4-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4-3
- Python 2 binary package renamed to python2-parsedatetime
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Michele Baldessari <michele@acksyn.org> - 2.4-1
- New upstream release

* Mon Mar 13 2017 Michele Baldessari <michele@acksyn.org> - 2.3-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Michele Baldessari <michele@acksyn.org> - 2.2-2
- Disable %%check for the time being as not all requirements are packaged

* Tue Jan 24 2017 Michele Baldessari <michele@acksyn.org> - 2.2-1
- New upstream

* Tue Dec 27 2016 Michele Baldessari <michele@acksyn.org> - 2.1-4
- Fix python3.6 build

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 10 2016 Michele Baldessari <michele@acksyn.org> - 2.1-1
- New upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 02 2015 Michele Baldessari <michele@acksyn.org> - 1.5-1
- New upstream (BZ#1238670)
* Mon Jun 22 2015 Michele Baldessari <michele@acksyn.org> - 1.4-2
- Fix python --> python2 macros
* Thu Jun 04 2015 Michele Baldessari <michele@acksyn.org> - 1.4-1
- Initial packaging
