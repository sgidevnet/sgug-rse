%global pypiname trollius
Name:           python-trollius
Version:        2.1
Release:        16%{?dist}
Summary:        A port of the Tulip asyncio module to Python 2

License:        ASL 2.0
URL:            https://github.com/haypo/trollius
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypiname}/%{pypiname}-%{version}.tar.gz
# async is a keyword in python 3.7, thus cannot be a function name
Patch0:         %{name}-async.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description\
\
Trollius provides infrastructure for writing single-threaded\
concurrent code using coroutines, multiplexing I/O access over sockets\
and other resources, running network clients and servers, and other\
related primitives.\
\
Trollius is a portage of the asyncio project (PEP 3156) on Python\
2. Trollius works on Python 2.6-3.5. It has been tested on Windows,\
Linux, Mac OS X, FreeBSD and OpenIndiana.

%description %_description

%package -n python3-trollius
Summary: A port of the Tulip asyncio module

%description -n python3-trollius

Trollius provides infrastructure for writing single-threaded
concurrent code using coroutines, multiplexing I/O access over sockets
and other resources, running network clients and servers, and other
related primitives.

Trollius is a portage of the asyncio project (PEP 3156) on Python
2. Trollius works on Python 2.6-3.5. It has been tested on Windows,
Linux, Mac OS X, FreeBSD and OpenIndiana.

%prep
%setup -q -n %{pypiname}-%{version}
%patch0

%build
%py3_build

%install
%py3_install

%check
# these are currently causing koji builds to hang
#%{__python3} runtests.py -v1 -x test_subprocess_kill

%files -n python3-trollius
%defattr(-,root,root,-)
%doc README.rst
%dir %{python3_sitelib}/trollius
%{python3_sitelib}/trollius/*.py
%{python3_sitelib}/trollius/__pycache__
%{python3_sitelib}/%{pypiname}-%{version}-py3.?.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-11
- Subpackage python2-trollius has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Jerry James <loganjerry@gmail.com> - 2.1-9
- Add -async patch to fix FTBFS (bz 1593133)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1-9
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1-6
- Python 2 binary package renamed to python2-trollius
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb  7 2017 Ian Wienand <iwienand@redhat.com> - 2.1-4
- Add python-six dependency (rhbz#1402775)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Matthias Runge <mrunge@redhat.com> - 2.1-1
- update to 2.1 (rhbz#1101234)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 14 2015 Ian Wienand <iwienand@redhat.com> - 2.0-1
- update to 2.0 - rhbz#1101234

* Mon Jun 15 2015 Ian Wienand <iwienand@redhat.com> - 1.0.4-2
- add python3 - rhbz#1230868

* Wed Jan  7 2015 Ian Wienand <iwienand@redhat.com> - 1.0.4-1
- update to 1.0.4
- add python-mock as build dependency for tests

* Fri Aug 15 2014 Ian Wienand <iwienand@redhat.com> - 1.0.1-1
- update to 1.0.1

* Mon Jul  7 2014 Ian Wienand <iwienand@redhat.com> - 0.4-1
- update to 0.4
- 0.3 changed module name to trollius for python3.4 compatability
  (issue #8; see README)

* Wed Apr 16 2014 Ian Wienand <iwienand@redhat.com> - 0.2-2
- fix python-ordereddict dependency typo

* Mon Mar 24 2014 Ian Wienand <iwienand@fedora19> - 0.2-1
- update to 0.2

* Tue Mar  4 2014  <iwienand@redhat.com> - 0.1.5-3
- add python-futures as build-dep
- add __python2* macros; convert to them

* Thu Feb 20 2014  <iwienand@redhat.com> - 0.1.5-2
- change license to ASL 2.0
- add defattr (from rpmlint)
- add group tag (from rpmlint)

* Tue Feb 18 2014  <iwienand@redhat.com> - 0.1.5-1
- Initial release
