%global modname six

# tests are enabled by default, but on Fedora 32+, Python 2 tests are skipped
%bcond_without tests

# python2 is enabled by default, Fedora 32+ exception is for offlineimap
# https://pagure.io/fesco/issue/2274
# The exception applies to Fedora only and has no target release yet
%if 0%{?fedora}
%bcond_without python2
%else
%bcond_with python2
%endif

%global python_wheelname %{modname}-%{version}-py2.py3-none-any.whl

Name:           python-%{modname}
Version:        1.15.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            https://pypi.python.org/pypi/six
Source0:        %{pypi_source %{modname}}

BuildArch:      noarch

%global _description \
%%{name} provides simple utilities for wrapping over differences between\
Python 2 and Python 3.

%description %{_description}

%if %{with python2}
%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%if %{with tests} && 0%{?fedora} < 32
BuildRequires:  python2-pytest
BuildRequires:  python2-tkinter
%endif

%description -n python2-%{modname} %{_description}
Python 2 version.

%endif


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-tkinter
%endif

%description -n python3-%{modname} %{_description}
Python 3 version.


%prep
%autosetup -n %{modname}-%{version}


%build
%if %{with python2}
%py2_build
%endif

%py3_build_wheel


%install
%if %{with python2}
%py2_install
%endif

%py3_install_wheel %{python_wheelname}

%if %{with tests}
%check
%if %{with python2} && 0%{?fedora} < 32
PYTHONPATH=%{buildroot}%{python2_sitelib} pytest-2 -rfsxX test_six.py
%endif
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -rfsxX test_six.py
%endif


%if %{with python2}
%files -n python2-%{modname}
%license LICENSE
%doc README.rst documentation/index.rst
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}.py*
%endif

%files -n python3-%{modname}
%license LICENSE
%doc README.rst documentation/index.rst
%{python3_sitelib}/%{modname}-*.dist-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*


%changelog
* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.15.0-1
- Update to 1.15.0 (#1838702)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-4
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-3
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-1
- Update to 1.14.0 (#1768982) for Python 3.9 support (#1788494)
- Drop old obsoletes for platform-python-six

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-6
- Reduce Python 2 build dependencies

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-5
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-4
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Yatin Karel <ykarel@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-5
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-4
- Bootstrap for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Lumír Balhar <lbalhar@redhat.com> - 1.11.0-2
- Removed and obsoleted the platform-python subpackage

* Tue Sep 19 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Thu Aug 10 2017 Tomas Orsava <torsava@redhat.com> - 1.10.0-11
- Added the platform-python subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Petr Viktorin <pviktori@redhat.com> - 1.10.0-9
- Fix unversioned Python BuildRequires

* Mon Feb 13 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-8
- Rebuild as wheel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-6
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-5
- Rebuild for Python 3.6
- Disable python3 tests

* Tue Aug 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.10.0-4
- Modernize spec more
- Depend on system-python(abi)
- Cleanups

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-2
- Modernize spec
- Fix python3 package file ownership

* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.9.0-4
- Rebuilt for Python3.5 rebuild

* Mon Jul 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.9.0-3
- Added python2-six provide to python-six

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.9.0-1
- Upstream 1.9.0
- Packaging cleanups

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.8.0-1
- upgrade to 1.8.0 (rhbz#1105861)

* Sun Aug  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.7.3-2
- fix license handling

* Thu Jul 31 2014 Pádraig Brady <pbrady@redhat.com> - 1.7.3-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-2
- Rebuild for Python 3.4

* Tue Apr 29 2014 Matthias Runge <mrugne@redhat.com> - 1.6.1-1
- upgrade to 1.6.1 (rhbz#1076578)

* Fri Mar 07 2014 Matthias Runge <mrunge@redhat.com> - 1.5.2-1
- upgrade to 1.5.2 (rhbz#1048819)

* Mon Sep 16 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-1
- 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 David Malcolm <dmalcolm@redhat.com> - 1.3.0-1
- 1.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.0-1
- 1.2.0 (rhbz#852658)
- add %%check section

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Conditionalized python3-six, allowing an el6 build.

* Tue Feb  7 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-1
- 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial packaging


