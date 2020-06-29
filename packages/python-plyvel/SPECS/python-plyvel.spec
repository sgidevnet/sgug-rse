%global upstream_name plyvel
%global module_name plyvel

Name:           python-%{upstream_name}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Python interface to the LevelDB embedded database library
License:        BSD
URL:            https://github.com/wbolster/plyvel
Source0:        https://files.pythonhosted.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
Patch0:         0001-py.test.mark.skipif-wants-str-not-bool.patch
BuildRequires:  gcc-c++
BuildRequires:  leveldb-devel >= 1.20

%global __provides_exclude_from ^%{python3_sitearch}/.*\\.so$

%description
Plyvel is a fast and feature-rich Python interface to the LevelDB embedded 
database library. It has a rich feature set, high performance, and a friendly 
Pythonic API.

%package -n python3-%{upstream_name}
Summary:        Python 3 interface to the LevelDB embedded database library
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-Cython

%description -n python3-%{upstream_name}
Plyvel is a fast and feature-rich Python interface to the LevelDB embedded 
database library. It has a rich feature set, high performance, and a friendly 
Pythonic API.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0 -p1
rm -rf *.egg-info

%build
cython --cplus --fast-fail --annotate plyvel/_plyvel.pyx
%py3_build

%install
%py3_install

%check
rm -rf plyvel # so it picks the installed copy
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-3 -vv test/

%files -n python3-%{upstream_name}
%doc README.rst NEWS.rst
%license LICENSE.rst
%{python3_sitearch}/%{module_name}
%{python3_sitearch}/%{module_name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Dan Callaghan <djc@djc.id.au> - 1.2.0-1
- Update to 1.2.0 (RHBZ#1794162)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Dan Callaghan <djc@djc.id.au> - 1.1.0-1
- Update to 1.1.0 (RHBZ#1705471)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6
- Remove python2 subpackage (#1627302)

* Thu Aug 16 2018 Dan Callaghan <dcallagh@redhat.com> - 1.0.4-5
- Fixed Cython build (patch from Miro Hrončok <miro@hroncok.cz>)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Dan Callaghan <dcallagh@redhat.com> - 1.0.4-1
- Update to 1.0.4 (#1535264)

* Fri Jan 12 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (#1533687)

* Tue Jan 09 2018 Dan Callaghan <dcallagh@redhat.com> - 1.0.1-1
- Upstream release 1.0.1:
  https://plyvel.readthedocs.org/en/latest/news.html#plyvel-1-0-1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Dan Callaghan <dcallagh@redhat.com> - 0.9-9
- renamed python-plyvel to python2-plyvel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-7
- Rebuild for Python 3.6

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.9-6
- Rebuild for LevelDB 1.18

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Dan Callaghan <dcallagh@redhat.com> - 0.9-1
- upstream bug fix release 0.9:
  https://plyvel.readthedocs.org/en/latest/news.html#plyvel-0-9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Dec 19 2013 Dan Callaghan <dcallagh@redhat.com> - 0.8-1
- new upstream release 0.8

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Dan Callaghan <dcallagh@redhat.com> - 0.4-1
- new upstream release 0.4

* Tue Jun 04 2013 Dan Callaghan <dcallagh@redhat.com> - 0.3-1
- upstream bug fix release 0.3
- switch to upstream patch for test failure

* Sat May 25 2013 Dan Callaghan <dcallagh@redhat.com> - 0.2-1
- initial version
