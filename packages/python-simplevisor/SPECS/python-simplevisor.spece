
%global srcname simplevisor

Name:		python-simplevisor
Version:	1.2
Release:	20%{?dist}
Summary:	Python simple daemons supervisor
License:	ASL 2.0
URL:		https://github.com/cern-mig/%{name}
Source0:	https://pypi.python.org/packages/ef/a1/d3fef46a01312d8cb470503a476f813bd31abbc2136be37eb9fd1f537b73/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
%if 0%{?fedora} >= 24
BuildRequires:	perl-generators
%endif
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(No::Worries)
BuildRequires:	perl(No::Worries::Die)
BuildRequires:	perl(No::Worries::Log)
BuildRequires:	perl(No::Worries::PidFile)
BuildRequires:	perl(No::Worries::Proc)
BuildRequires:	perl(No::Worries::Syslog)
BuildRequires:	perl(No::Worries::Warn)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(sigtrap)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(warnings)

%global _description\
Simplevisor is a simple daemons supervisor, it is inspired by\
Erlang OTP and it can supervise hierarchies of services.

%description %_description

%package -n python3-simplevisor
Summary:	Python simple daemons supervisor

%description -n python3-simplevisor
Simplevisor is a simple daemons supervisor, it is inspired by
Erlang OTP and it can supervise hierarchies of services.

%prep
%setup -q -n %{srcname}-%{version}
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build 
%{__python3} setup.py build

%install
rm -fr $RPM_BUILD_ROOT
%{__python3} setup.py install --with-data-files --skip-build --root $RPM_BUILD_ROOT
install -D -m 644 man/%{srcname}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{srcname}.1;
install -D -m 644 man/%{srcname}-control.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{srcname}-control.1;
install -D -m 644 man/%{srcname}-loop.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{srcname}-loop.1;

%check
%{__python3} setup.py test
# And remove compiled documentation.
rm -f test/*.pyc

%files -n python3-simplevisor
%doc LICENSE README.rst CHANGES
%{_mandir}/man?/%{srcname}.1*
%{_mandir}/man?/%{srcname}-control.1*
%{_mandir}/man?/%{srcname}-loop.1*
%attr(755, root, root) /usr/bin/simplevisor
%attr(755, root, root) /usr/bin/simplevisor-control
%attr(755, root, root) /usr/bin/simplevisor-loop
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-20
- Rebuilt for Python 3.9

* Tue Mar 31 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-19
- Specify all perl dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Lionel Cons <lionel.cons@cern.ch> - 1.2-16
- Subpackage python2-simplevisor has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Lionel Cons <lionel.cons@cern.ch> - 1.2-12
- Fixed building using Python 2 (#1605914).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-10
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2-7
- Python 2 binary package renamed to python2-simplevisor
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul  4 2016 Lionel Cons <lionel.cons@cern.ch> - 1.2-2
- Corrected /usr/bin/simplevisor shebang in Rawhide

* Wed Jun 29 2016 Lionel Cons <lionel.cons@cern.ch> - 1.2-1
- Updated to upstream version (#1351066)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Adrien Devresse <adevress at cern.ch> - 1.1-2
 - Disable python3 for EPEL7

* Tue Mar 31 2015 Adrien Devresse <adevress at cern.ch> - 1.1-1
 - Update to upstream 1.1 version

* Thu Aug 14 2014 Adrien Devresse <adevress at cern.ch> - 1.0-1
 - Update to upstream 1.0 version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Mar 09 2014 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.9-1
- Updating to upstream version, rhbz #1071124.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.8-2
- Perl 5.18 rebuild

* Fri Apr 26 2013 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.8-1
- Updating to upstream 0.8.

* Mon Jan 28 2013 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.7-1
- Updating to upstream 0.7.

* Thu Jan 17 2013 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.6-1
- Updating to upstream 0.6.

* Fri Nov 30 2012 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.5-2
- Use macros consistently.

* Fri Sep 14 2012 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.5-1
- Updating to version 0.5.

* Thu Jul 05 2012 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.4-1
- Updating to version 0.4.

* Mon Jun 25 2012 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.3-1
- Updating to version 0.3.

* Wed Mar 14 2012 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.2-1
- Improvements.

* Sun Mar 11 2012 Massimo Paladin <Massimo.Paladin@gmail.com> - 0.1-1
- Initial packaging.
