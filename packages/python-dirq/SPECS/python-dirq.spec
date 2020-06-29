
%global srcname dirq

Name:           python-dirq
Version:        1.7.1
Release:        16%{?dist}
Summary:        Directory based queue
License:        ASL 2.0
URL:            https://github.com/cern-mig/%{name}
Source0:        http://pypi.python.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	python3-devel

%global _description\
The goal of this module is to offer a simple queue system using the\
underlying file system for storage, security and to prevent race\
conditions via atomic operations.  It focuses on simplicity,\
robustness and the ability to scale.\
\
The python module dirq is compatible with the Perl\
module Directory::Queue.

%description %_description

%package -n python3-dirq
Summary:	Directory based queue

%description -n python3-dirq
The goal of this module is to offer a simple queue system using the 
underlying file system for storage, security and to prevent race 
conditions via atomic operations.  It focuses on simplicity, 
robustness and the ability to scale.

The python module dirq is compatible with the Perl 
module Directory::Queue.

%prep
%setup -q -n %{srcname}-%{version}
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT

%check
%{__python3} setup.py test
# And remove compiled documentation.
rm -f test/*.pyc

%files -n python3-dirq
%doc README.rst CHANGES examples test
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-11
- Subpackage python2-dirq has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Lionel Cons <lionel.cons@cern.ch> - 1.7.1-9
- Fixed building using Python 2 (#1605656).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.1-5
- Python 2 binary package renamed to python2-dirq
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-2
- Rebuild for Python 3.6

* Tue Nov  1 2016 Lionel Cons <lionel.cons@cern.ch> - 1.7.1-1
- Update to upstream version, rhbz #1389920.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Lionel Cons <lionel.cons@cern.ch> - 1.7-1
- Update to upstream version, rhbz #1281769.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Feb 25 2014 Massimo Paladin <massimo.paladin@gmail.com> - 1.6.1-1
- Update to upstream version, rhbz #1069202.

* Sat Jan 11 2014 Massimo Paladin <massimo.paladin@gmail.com> - 1.5-1
- Update to upstream version, rhbz #1049761.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.4-1
- Update to upstream version, rhbz #976198.

* Wed May 29 2013 Massimo Paladin <massimo.paladin@gmail.com> - 1.3-1
- Update to upstream version, rhbz #967707.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.2-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.2.2-1
- Update to 1.2.2.

* Wed May 09 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.2.1-2
- Cleaning specfile and dependency error fixed on rhel5.

* Mon May 07 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.2.1-1
- Update to 1.2.1.

* Fri Mar 30 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.1.2-1
- Update to 1.1.2.

* Tue Mar 20 2012 Massimo Paladin <massimo.paladin@gmail.com> - 1.1.1-1
- Update to 1.1.1.

* Tue Feb 14 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.1-2
- Empty release for revision control error.

* Tue Feb 14 2012 Steve Traylen <steve.traylen@cern.ch> - 1.0.1-1
- Update to 1.0.1.
- Enable python3 support with patch dirq-1.0.1-dist-tag.patch.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 28 2010 Steve Traylen <steve.traylen@cern.ch> - 0.0.5-3
- Really disable python3 support.
- Change /usr/bin/env python to /usr/bin/python everywhere.

* Tue Jun 29 2010 Steve Traylen <steve.traylen@cern.ch> - 0.0.5-2
- Disable python3 support and add link to bug.

* Mon Jun 28 2010 Steve Traylen <steve.traylen@cern.ch> - 0.0.5-1
- Initial packaging.

