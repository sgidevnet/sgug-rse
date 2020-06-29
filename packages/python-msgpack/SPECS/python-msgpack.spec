%global srcname msgpack
%global sum A Python MessagePack (de)serializer

Name:           python-%{srcname}
Version:        0.6.2
Release:        3%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://msgpack.org/
Source0:        %pypi_source

BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

# For backwards compatibility
Provides:       python3dist(%{srcname}-python) = %{version}
Provides:       python%{python3_version}dist(%{srcname}-python) = %{version}

%description -n python%{python3_pkgversion}-%{srcname}
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python %{python3_version} (de)serializer for MessagePack.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=$(pwd)
py.test-%{python3_version} -v test

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license COPYING
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Orion Poplawski <orion@nwra.com> - 0.6.2-1
- Update to 0.6.2

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-5
- Subpackage python2-msgpack has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Update to latest upstream release 0.6.1

* Fri Jan 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to latest upstream release 0.6.0

* Mon Sep 03 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.6-5
- Use msgpack from PyPI, not msgpack-python (deprecated)

* Fri Aug 10 2018 Felix Schwarz <fschwarz@fedoraproject.org> - 0.5.6-4
- Require gcc-c++, avoid FTBFS in rawhide (#1605779)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.6-2
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.6-1
- Update to latest upstream release 0.5.6 (rhbz#1548215)

* Fri Feb 23 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.5-1
- Update to latest upstream release 0.5.5 (rhbz#1548215)

* Fri Feb 09 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.4-1
- Update to latest upstream release 0.5.4 (rhbz#1541377)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Jan 20 2018 Denis Fateyev <denis@fateyev.com> - 0.5.1-1
- Update to 0.5.1 version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.8-2
- Rebuild for Python 3.6

* Fri Aug 05 2016 Denis Fateyev <denis@fateyev.com> - 0.4.8-1
- Update to 0.4.8 version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 16 2016 Denis Fateyev <denis@fateyev.com> - 0.4.7-3
- Added EPEL compatibility (RHBZ #1290393)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.7-1
- Update spec file
- Update to latest upstream version 0.4.7

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 0.4.6-5
- Drop py3dir
- Provide python2-msgpack

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.4.6-4
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 13 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.6-1
- Update to latest upstream version 0.4.6 (RHBZ #1201568)

* Fri Jan 30 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.5-2
- Correct python3 subpackage Summary

* Sun Jan 25 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.5-1
- Update to latest upstream version 0.4.5

* Fri Jan 23 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.4-2
- Patch test suite for EL6 and EL7 compatibility (RHBZ #1182808)
- Add python2 macros for EL6 compatibility (RHBZ #1182808)

* Thu Jan 15 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.4-1
- Update to latest upstream version 0.4.4 (RHBZ #1180507)
- Add tests in %%check

* Wed Sep 10 2014 Nejc Saje <nsaje@redhat.com> - 0.4.2-4
- Introduce python3- subpackage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream version 0.4.2

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Update to latest upstream version 0.4.1

* Tue Jan 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Update to latest upstream version 0.4.0

* Mon Jan 06 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.13-5
- Update spec file and python macros

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.13-1
- Update to new upstream version 0.1.13

* Tue Jan 31 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.12-1
- Update to new upstream version 0.1.12

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.10-1
- Updated to new upstream version 0.1.10
- README is gone

* Tue Jul 12 2011 Dan Horák <dan[at]danny.cz> - 0.1.9-3
- Fix build on big endian arches

* Fri Jun 24 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.9-2
- Tests are failing, they are not active at the moment
- Filtering added

* Sat Mar 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.9-1
- Initial package
