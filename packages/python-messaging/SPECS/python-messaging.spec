
%global srcname messaging

Name:		python-messaging
Version:	1.1
Release:	19%{?dist}
Summary:	Python abstraction of a "message"
License:	ASL 2.0
URL:		https://github.com/cern-mig/%{name}
Source0:	http://pypi.python.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
# For python < 2.6 python-simplejson is required

%global _description\
This module provides an abstraction of a "message", as used in Enterprise\
Messaging Systems.\
\
The modules include a transport independent message abstraction, a\
versatile message generator and several message queues/spools to\
locally store messages.\
\
The python module messaging is compatible with the Perl\
module Messaging::Message.

%description %_description

%package -n python3-messaging
Summary:	Python abstraction of a "message"

%description -n python3-messaging
This module provides an abstraction of a "message", as used in Enterprise
Messaging Systems.

The modules include a transport independent message abstraction, a
versatile message generator and several message queues/spools to
locally store messages.

The python module messaging is compatible with the Perl
module Messaging::Message.

%prep
%setup -q -n %{srcname}-%{version}
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%{__python3} setup.py build

%install
rm -fr $RPM_BUILD_ROOT
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT

%check
rm -f test/*.pyc
%{__python3} setup.py test
rm -f test/*.pyc

%files -n python3-messaging
%doc LICENSE README.rst CHANGES example test
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-13
- Subpackage python2-messaging has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jul 23 2018 Lionel Cons <lionel.cons@cern.ch> - 1.1-12
- Fixed building using Python 2 (#1605769).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1-9
- Fix condition for python-simplejson

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-7
- Python 2 binary package renamed to python2-messaging
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Lionel Cons <lionel.cons@cern.ch> - 1.1-1
- Updated to upstream version (#1296742)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 Steve Traylen <steve.traylen@cern.ch> - 1.0-5
- No python3 exists for epel7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.0-1
- Upgrading to upstream version 1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.10-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Massimo Paladin <massimo.paladin@gmail.com> - 0.10-1
- Upgrading to latest version 0.10

* Tue Jun 12 2012 Massimo Paladin <massimo.paladin@gmail.com> - 0.9-1
- Upgrading to latest version 0.9

* Mon May 07 2012 Massimo Paladin <massimo.paladin@gmail.com> - 0.8-1
- Upgrading to latest version 0.8

* Mon Apr 23 2012 Massimo Paladin <massimo.paladin@gmail.com> - 0.7-1
- Upgrading to latest version 0.7

* Tue Apr 17 2012 Massimo Paladin <massimo.paladin@gmail.com> - 0.6-1
- Upgrading to latest version 0.6

* Mon Feb 20 2012 Massimo Paladin <Massimo.Paladin@cern.ch> - 0.5-2
- Making it compliant with guidelines

* Mon Jan 23 2012 Massimo Paladin <Massimo.Paladin@cern.ch> - 0.5-1
- Initial packaging
