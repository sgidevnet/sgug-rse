%global srcname zodbpickle

Name:           python-%{srcname}
Version:        2.0.0
Release:        4%{?dist}
Summary:        Fork of Python 2 pickle module for ZODB

# Code taken from the python 3 sources is covered by the Python license.
# Additions to that code are covered by the ZPLv2.1 license.
License:        Python and ZPLv2.1
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

# Fix warnings about discarding the const qualifier
Patch0:         %{name}-const.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-test
BuildRequires:  %{py3_dist setuptools}

%global common_desc %{expand:
This package presents a uniform pickling interface for ZODB:
- Under Python2, this package forks both Python 2.7's pickle and cPickle
  modules, adding support for the protocol 3 opcodes.  It also provides
  a new subclass of bytes, zodbpickle.binary, which Python2 applications
  can use to pickle binary values such that they will be unpickled as
  bytes under Py3k.
- Under Py3k, this package forks the pickle module (and the supporting C
  extension) from Python 3.5, 3.6, 3.7, and 3.8.  The fork adds support
  for the noload operations used by ZODB.}

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        Fork of Python 3 pickle module for ZODB

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -p0 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}%{python3_sitearch}/%{srcname}/*.c
rm -f %{buildroot}%{python3_sitearch}/%{srcname}/pickle*_2.py
rm -fr %{buildroot}%{python3_sitearch}/%{srcname}/tests/*_2.py*
rm -fr %{buildroot}%{python3_sitearch}/%{srcname}/tests/__pycache__/*_2.cpy*
chmod 0755 %{buildroot}%{python3_sitearch}/%{srcname}/*.so

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%{python3_sitearch}/%{srcname}*

%changelog
* Tue Jun 23 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-4
- BR setuptools
- Drop unneeded nose BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 1.1-1
- Version 1.1
- Remove trailing whitespace from the description
- Add -const patch to eliminate gcc warnings

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- New upstream version

* Sat Nov 17 2018 Jerry James <loganjerry@gmail.com> - 1.0.2-2
- Drop python2 subpackage

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 23 2017 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 0.6.0-3
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- New upstream version
- Drop upstreamed -python34 patch

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.5.2-3
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Jerry James <loganjerry@gmail.com> - 0.5.2-1
- Initial RPM
