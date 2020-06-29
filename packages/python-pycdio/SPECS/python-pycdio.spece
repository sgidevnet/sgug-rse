Name:		python-pycdio
Version:	2.1.0
Release:	2%{?dist}
Summary:	A Python interface to the CD Input and Control library

License:	GPLv3+
URL:		http://www.gnu.org/software/libcdio/
Source0:	%pypi_source pycdio

BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	libcdio-devel
BuildRequires:	swig

# For tests
BuildRequires:	python3-nose

%description
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%package -n python3-pycdio
Summary:	A Python interface to the CD Input and Control library
Obsoletes:	pycdio < 2.0.0-6
Provides:	pycdio = %{version}-%{release}
%{?python_provide:%python_provide python3-pycdio}

%description -n python3-pycdio
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%prep
%autosetup -n pycdio-%{version} -p1

%build
%py3_build

%install
%py3_install
chmod 755 %{buildroot}/%{python3_sitearch}/*.so

%check
%python3 setup.py nosetests

%files -n python3-pycdio
%license COPYING
%doc README.rst ChangeLog AUTHORS NEWS.md THANKS
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_pycdio*
%{python3_sitearch}/_pyiso9660*
%{python3_sitearch}/cdio.py
%{python3_sitearch}/iso9660.py
%{python3_sitearch}/pycdio.py
%{python3_sitearch}/pyiso9660.py
%{python3_sitearch}/pycdio-%{version}-py3*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Adrian Reber <adrian@lisas.de> - 2.1.0-1
- Updated to 2.1.0 for libcdio-2.1.0 update

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Kevin Fenzi <kevin@scrye.com> - 2.0.0-7
- Review fixes: drop python3 dep, Update obsoletes, add python_provide
- Review fixes: Use pypi_source, fixed files globbing. 

* Mon Nov 25 2019 Kevin Fenzi <kevin@scrye.com> - 2.0.0-6
- Rename pycdio to python3-pycdio, keeping release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 06 2018 Adrian Reber <adrian@lisas.de> - 2.0.0-1
- Updated to 2.0.0 for proper libcdio-2.0.0 support

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> - 0.21-1
- Rebuilt for libcdio-2.0.0
- Updated to latest upstream + patches from git

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Adrian Reber <adrian@lisas.de> - 0.20-4
- Rebuilt for libcdio-0.94

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov  3 2015 Adam Williamson <awilliam@redhat.com> - 0.20-1
- update to latest upstream (fixes #1269003)
- clean and modernize spec a little (note: no longer EPEL5 compatible)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> - 0.19-6
- Rebuilt for libcdio-0.93

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Adrian Reber <adrian@lisas.de> - 0.19-3
- Rebuilt for libcdio-0.92

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Adrian Reber <adrian@lisas.de> - 0.19-1
- Updated to 0.19 which actually works with libcdio-0.90

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Adrian Reber <adrian@lisas.de> - 0.18-1
- Updated to 0.18 (for for libcdio-0.90 rebuild)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> - 0.17-2
- Rebuilt for libcdio-0.83
* Fri Apr 22 2011 Jay Greguske <jgregusk@redhat.com> 0.17-1
- Fix source url
* Fri Apr 22 2011 Jay Greguske <jgregusk@redhat.com> 0.17-0
- Update to 0.17
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> - 0.16-2
- Rebuilt for libcdio-0.82
* Wed Oct 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.16-1
- Updated to version 0.16
* Mon Sep 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-4
- Off-by-one compensation in get_devices_* not needed anymore
* Tue Jul 28 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-3
- Added a patch to remove unnecessary shebangs
* Mon Jul 27 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-2
- Corrected the license field
* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 0.15-1
- Initial RPM release.
