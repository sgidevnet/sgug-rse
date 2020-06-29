%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%endif

%if 0%{?rhel} > 7
# Disable python2 build by default
%endif

# tests require internet connection
%global with_tests 0
Name:           python-ntplib
Version:        0.3.3
Release:        19%{?dist}
Summary:        Python module that offers a simple interface to query NTP servers

License:        MIT
URL:            http://pypi.python.org/pypi/ntplib/
Source0:        https://pypi.python.org/packages/source/n/ntplib/ntplib-%{?version}.tar.gz

BuildArch:      noarch

%description
The ntplib is a python module that offers a simple interface to query NTP
servers. It also provides utility functions to translate NTP fields' values to
text (mode, leap indicator...). Since it's pure Python, and only depends on core
modules, it should work on any platform with a Python implementation.



%package -n python3-ntplib
Summary:        Python 3 module that offers a simple interface to query NTP servers

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%{?python_provide:%python_provide python3-ntplib}

%description -n python3-ntplib
The ntplib is a python module that offers a simple interface to query NTP
servers. It also provides utility functions to translate NTP fields' values to
text (mode, leap indicator...). Since it's pure Python, and only depends on core
modules, it should work on any platform with a Python implementation.

Python 3 version.



%prep
%setup -q -n ntplib-%{?version}

%build

%py3_build

%install

%py3_install

%if 0%{?with_tests}

%{__python3} test_ntplib.py
%endif # with_tests


%files -n python3-ntplib
%doc CHANGELOG
%{python3_sitelib}/ntplib*
%{python3_sitelib}/__pycache__/*

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.3-13
- Subpackage python2-ntplib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-11
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.3.3-10
- Don't build Python 2 subpackage on EL > 7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.3-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.3.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.3.3-3
- Modernize spec
- Fix python3 package file ownership

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 0.3.3-2
- Rebuilt for Python3.5 rebuild

* Tue Jul 28 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.3.3-1
- New upstream version ntplib-0.3.3 (license change LGPLv2+ -> MIT)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 28 2014 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Introduced Python 3 subpackage
- Conditional %%check section

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Vratislav Podzimek <vpodzime@redhat.com> 0.3.2-1
- New upstream version ntplib-0.3.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Vratislav Podzimek <vpodzime@redhat.com> 0.3.1-1
- Initial release
