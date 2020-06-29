%global srcname sh

%global common_description %{expand:
sh is a full-fledged subprocess replacement for Python that allows you to call
any program as if it were a function.  sh is not a collection of system
commands implemented in Python.}

Name:           python-%{srcname}
License:        MIT
Summary:        Python subprocess replacement
Version:        1.13.1
Release:        1%{?dist}
URL:            https://github.com/amoffat/sh
Source0:        %pypi_source
Patch1:         no-coverage.patch
# test_timeout expects the sleep binary to reside in /bin/
# so we change it to the appropriate path for Fedora.
Patch2:         fix-test_timeout.patch
BuildArch:      noarch
BuildRequires:  lsof


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
%{__python3} sh.py travis


%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGELOG.md README.rst
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.cpython-%{python3_version_nodots}.*
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jun 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.13.1-1
- Update to 1.13.1 (#1828679)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.14-17
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Carl George <carl@george.computer> - 1.12.14-16
- Always apply patch3 (el8 fix)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.14-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.14-13
- Subpackage python2-sh has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.14-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Carl George <carl@george.computer> - 1.12.14-10
- Refresh patch4, which also obsoletes patch5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.12.14-8
- Fix tests for the drop of the unversioned python interpreter

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Carl George <carl@george.computer> - 1.12.14-6
- Add patch4 to always use fully versioned python command in tests

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.14-5
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Carl George <carl@george.computer> - 1.12.14-4
- Use common license and documentation directory
- Enable EPEL python3 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Carl George <carl.george@rackspace.com> - 1.12.14-1
- Latest upstream
- Update patch0 to account for changes in PEP-0538

* Sun Apr 16 2017 Carl George <carl.george@rackspace.com> - 1.12.13-2
- Add patch2 to remove coverage (too old in EL6/7, doesn't add any value for packaging)
- Add patch3 to fix tests to work with PEP-0538 changes in F26+ (obsoletes patch1)
- Run tests via `sh.py travis` to only test with the called python version
- Properly install license
- Switch to PyPI tarball
- Update summary and description

* Sat Apr 15 2017 Kevin Fenzi <kevin@scrye.com> - 1.12.13-1
- Update to 1.12.13. Fixes bug #1442462
- Update to current python guidelines. Fixes bug #1442465

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.11-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Javier Peña <jpena@redhat.com> - 1.11-1
- Updated to upstream version 1.11
- Kill the entire process group when a command times out (bz#1306405)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Ralph Bean <rbean@redhat.com> - 1.08-1
- Latest upstream version.
- More explicit directory ownership in files section.
- Added python3-sh subpackage.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Andy Grover <agrover@redhat.com> - 1.02-2
- Re-add check

* Mon Sep 17 2012 Andy Grover <agrover@redhat.com> - 1.02-1
- New upstream release
- New upstream download location
- Remove check, upstream unittest has been removed

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 0.107-1
- New upstream release

* Fri May 4 2012 Andy Grover <agrover@redhat.com> - 0.105-1
- New upstream release

* Thu Mar 22 2012 Andy Grover <agrover@redhat.com> - 0.95-2
- Initial packaging
