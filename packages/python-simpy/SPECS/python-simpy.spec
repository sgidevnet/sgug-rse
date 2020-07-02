%global srcname simpy
%global sum Python simulation framework

Name:       python-%{srcname}
Version:    3.0.9
Release:    16%{?dist}
Summary:    %{sum}
License:    LGPLv2+
URL:        https://simpy.readthedocs.io/
Source0:    https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:    noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%description
SimPy (= Simulation in Python) is an object-oriented, process-based
discrete-event simulation language based on standard Python. It
provides the modeler with components of a simulation model including
processes, for active components like customers, messages, and
vehicles, and resources, for passive components that form limited
capacity congestion points like servers, checkout counters, and
tunnels. It also provides monitor variables to aid in gathering
statistics. Random variates are provided by the standard Python random
module.


%package -n python3-%{srcname}
Summary:    %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
SimPy (= Simulation in Python3) is an object-oriented, process-based
discrete-event simulation language based on standard Python. It
provides the modeler with components of a simulation model including
processes, for active components like customers, messages, and
vehicles, and resources, for passive components that form limited
capacity congestion points like servers, checkout counters, and
tunnels. It also provides monitor variables to aid in gathering
statistics. Random variates are provided by the standard Python random
module.


%package doc
Summary:    Documentation for SimPy, the Python simulation framework

%description doc
SimPy (= Simulation in Python) is an object-oriented, process-based
discrete-event simulation language based on standard Python.  This
package contains the documentation including source code documentation.


%prep
%setup -q -n simpy-%{version}

%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%files -n python3-%{srcname}
%{python3_sitelib}/*
%doc CHANGES.txt AUTHORS.txt README.txt PKG-INFO
%license LICENSE.txt


%files doc
%doc docs/examples/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.9-10
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-8
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.9-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Dominika Krejci <dkrejci@redhat.com> - 3.0.9-1
- Update to 3.0.9
- Update URL and Source
- Add Python3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.1-6
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 22 2012 Sarantis Paskalis - 2.3.1-1
- Upgrade to 2.3.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Sarantis Paskalis <paskalis@di.uoa.gr> - 2.2-1
- Upgrade to 2.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jun 11 2010 Sarantis Paskalis <paskalis@di.uoa.gr> - 2.1.0-2
- Drop sitelib from the spec

* Sun Jun 06 2010 Sarantis Paskalis <paskalis@di.uoa.gr> - 2.1.0-1
- Upgrade to 2.1.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 2.0.1-1
- Upgrade to 2.0.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb  3 2009 Sarantis Paskalis <paskalis@di.uoa.gr> - 2.0-1
- Upgrade to 2.0

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.9.1-2
- Rebuild for Python 2.6

* Mon Mar 31 2008 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.9.1-1
- Upgrade to 1.9.1

* Thu Mar  6 2008 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.9-3
- Fix Source0 URL to downloads.sourceforge.net

* Wed Feb 20 2008 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.9-2
- Upgrade to 1.9
- Drop executable permissions for all files

* Thu Jan  3 2008 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.8-2
- Account for python eggs

* Mon Feb 12 2007 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.8-1
- Update to 1.8

* Mon Jan 22 2007 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.8-0.1.rc1
- Update to 1.8rc.

* Sat Dec  9 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7.1-5
- Rebuild for rawhide.

* Wed Sep  6 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7.1-4
- Un-ghost .pyo files. Thanks Christian Iseli (bug #205424).

* Tue Aug 29 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7.1-3
- Bump release for FC6 rebuild.

* Mon Jun 19 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7.1-2
- SimPy-1.7.1
- Bump release

* Fri Mar 24 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7-3
- Bump release to make tag for building.

* Fri Mar 24 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7-2
- Bump release

* Thu Mar 23 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.7-1
- SimPy-1.7
- Drop shebang removal patch.  Implement it with sed script.

* Mon Feb 20 2006 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.6.1-4
- Rebuild for FC5.

* Mon Dec 26 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.6.1-3
- Add dist in release. Bump release.

* Wed Dec 21 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.6.1-2
- Add source code documentation as a -doc package (John Mahowald).
- Add Requires: tkinter for SimGUI to work (John Mahowald).
 
* Fri Nov 25 2005 Sarantis Paskalis <paskalis@di.uoa.gr> - 1.6.1-1
- First packaging version for FE.
