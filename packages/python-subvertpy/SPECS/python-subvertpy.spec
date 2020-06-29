%global srcname subvertpy

%filter_setup

Name:           python-%{srcname}
Version:        0.10.1
Release:        12%{?dist}
Summary:        Python bindings for Subversion

License:        LGPLv2+
URL:            https://jelmer.uk/code/subvertpy/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  subversion-devel

%description
Alternative Python bindings for Subversion, split out from bzr-svn.
The goal is to have complete, portable and "Pythonic" Python bindings.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Alternative Python bindings for Subversion, split out from bzr-svn.
The goal is to have complete, portable and "Pythonic" Python bindings.

%prep
%autosetup -n %{srcname}-%{version}
chmod -x examples/ra_*.py

%build
%py3_build

%install
%py3_install
 
#%check
#cd build/*/subvertpy/tests
#PYTHONPATH=.. nosetests test*.py

%files -n python3-%{srcname}
%doc AUTHORS NEWS TODO examples/
%license COPYING
%{_bindir}/subvertpy-fast-export
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}*.egg-info
%exclude %{python3_sitearch}/%{srcname}/tests

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-12
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.1-11
- Update source URL

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-8
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-7
- Subpackage python2-subvertpy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.1-1
- Update URLs
- Update to new upstream version 0.10.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.2-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-3
- Rebuilt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015  Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-1
- Cleanup and py3
- Update to new upstream release 0.9.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-3
- Update spec file

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to new upstream release 0.9.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to new upstream release 0.9.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 04 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.10-1
- Updated to new upstream release 0.8.10

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.9-1
- Update to new upstream release 0.8.9

* Mon Oct 10 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.8-1
- Update to new upstream release 0.8.8

* Mon Sep 19 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.7-1
- Update to new upstream release 0.8.7

* Sat Aug 20 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Update to new upstream release 0.8.4

* Wed Jun 22 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to new upstream release 0.8.2

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Exclude the tests directory
- Update to new upstream version 0.8.0

* Thu Nov 25 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-2
- Check section fixed

* Sat Nov 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.5-1
- Change the filtering stuff to get rid of private-shared-object-provides
- Add the tests (at the moment all failed)
- Rename the package

* Fri Aug 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.3-1
- Update to new upstream release 0.7.3

* Mon Jun 28 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-1
- Initial package
